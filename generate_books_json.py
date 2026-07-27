#!/usr/bin/env python3
"""
Generate canonical books.json by scanning book directories
and merging with existing shelf/toread HTML metadata.

Usage:
    python3 generate_books_json.py

Outputs:
    books.json — single source of truth for the entire library
"""

import json
import os
import re
import sys
from datetime import datetime
from html import unescape

BOOKS_DIR = os.path.dirname(os.path.abspath(__file__))
SHELF_PATH = os.path.join(BOOKS_DIR, 'index.html')
OUT_PATH = os.path.join(BOOKS_DIR, 'books.json')

# Directories to skip (not books)
SKIP_DIRS = {
    'metadata', 'reports', '.git', 'node_modules',
    '__pycache__', 'CourseAI-SMC',
    'Franklin_Article_Temp',  # temp article, not a book
    'Thinking_Fast_and_Slow',  # dupe of thinking-fast-and-slow
}

# Category assignments for books not in the shelf HTML.
# Key = directory name, value = category.
# This covers orphan books that need manual assignment.
CATEGORY_OVERRIDES = {
    # Economics Fundamentals
    'A_Primer_On_Money': 'Economics Fundamentals',
    'Basic_Economics': 'Economics Fundamentals',
    'Capital_Twenty_First_Century': 'Economics Fundamentals',
    'Economics_101': 'Economics Fundamentals',
    'How_An_Economy_Grows': 'Economics Fundamentals',
    'Principles_Of_Economics': 'Economics Fundamentals',
    'The_Worldly_Philosophers': 'Economics Fundamentals',
    'Seven_Deadly_Innocent_Frauds':
        'Free Markets & Political Economy',
    'Capitalism_and_Freedom':
        'Free Markets & Political Economy',
    'The_General_Theory': 'Economics Fundamentals',

    # Economic History & Financial Crises
    'Debt_The_First_5000_Years':
        'Economic History & Financial Crises',
    'When_Money_Dies':
        'Economic History & Financial Crises',
    'Manias_Panics_And_Crashes':
        'Economic History & Financial Crises',
    'Rise_And_Fall_Of_American_Growth':
        'Economic History & Financial Crises',
    'The_Ascent_of_Money':
        'Economic History & Financial Crises',
    'How_Countries_Go_Broke':
        'Economic History & Financial Crises',
    'Crash_Proof_2':
        'Economic History & Financial Crises',

    # Monetary Policy & Central Banking
    'The_Creature_From_Jekyll_Island':
        'Monetary Policy & Central Banking',
    'Primer_on_Money_Banking_and_Gold':
        'Monetary Policy & Central Banking',
    'The_Theory_Of_Money_And_Credit':
        'Monetary Policy & Central Banking',
    'A_History_of_Interest_Rates':
        'Fixed Income & Bonds',

    # Behavioral Finance & Psychology
    'Fooled_By_Randomness':
        'Behavioral Finance & Psychology',
    'The_Black_Swan':
        'Behavioral Finance & Psychology',
    'Skin_In_The_Game':
        'Behavioral Finance & Psychology',
    'Antifragile': 'Behavioral Finance & Psychology',
    'How_Not_To_Be_Wrong':
        'Behavioral Finance & Psychology',
    'Superforecasting':
        'Behavioral Finance & Psychology',
    'The_Hour_Between_Dog_And_Wolf':
        'Behavioral Finance & Psychology',
    'The_Psychology_Of_Money':
        'Behavioral Finance & Psychology',
    'Against_The_Gods': 'Behavioral Finance & Psychology',
    'thinking-fast-and-slow':
        'Behavioral Finance & Psychology',

    # Portfolio Management & Asset Allocation
    'All_About_Asset_Allocation':
        'Portfolio Management & Asset Allocation',
    'Pioneering_Portfolio_Management':
        'Portfolio Management & Asset Allocation',
    'Expected_Returns':
        'Portfolio Management & Asset Allocation',
    'Asset_Allocation':
        'Portfolio Management & Asset Allocation',
    'The_Four_Pillars_Of_Investing':
        'Investing Fundamentals',
    'The_Most_Important_Thing': 'Investing Fundamentals',
    'intelligent-asset-allocator': 'Investing Fundamentals',
    'stocks-for-the-long-run': 'Investing Fundamentals',
    'The_Bogleheads_Guide_To_Investing':
        'Investing Fundamentals',

    # Fixed Income & Bonds
    'Bond_Markets_Analysis_and_Strategies':
        'Fixed Income & Bonds',
    'The_Bond_Book': 'Fixed Income & Bonds',
    'The_Principles_Of_Banking': 'Fixed Income & Bonds',

    # Options & Derivatives
    'Options_As_Strategic_Investment':
        'Options & Derivatives',
    'Options_Playbook': 'Options & Derivatives',
    'Trading_Options_Greeks': 'Options & Derivatives',
    'Options_Made_Easy': 'Options & Derivatives',
    'Trading_Options_for_Dummies': 'Options & Derivatives',

    # Risk Management & Position Sizing
    'position-sizing': 'Risk Management & Position Sizing',
    'red-blooded-risk': 'Risk Management & Position Sizing',
    'way-of-the-turtle':
        'Risk Management & Position Sizing',
    'The_Zurich_Axioms':
        'Risk Management & Position Sizing',
    'Trade_Your_Way_To_Financial_Freedom':
        'Risk Management & Position Sizing',
    'Kelly_Capital_Growth':
        'Risk Management & Position Sizing',
    'The_Mathematics_Of_Money_Management':
        'Risk Management & Position Sizing',
    'beat-the-market':
        'Risk Management & Position Sizing',

    # Cycles & Market Timing
    'Bressert_Cycle_Trading': 'Cycles & Market Timing',
    'Elliott_Wave_Principle': 'Cycles & Market Timing',
    'The_Taylor_Trading_Technique':
        'Cycles & Market Timing',
    'Secular_Cycles': 'Cycles & Market Timing',
    'anatomy-of-the-bear': 'Cycles & Market Timing',
    'The_Long_Good_Buy': 'Cycles & Market Timing',

    # Technical Analysis
    'Trading_With_Intermarket_Analysis':
        'Technical Analysis',

    # Macro Investing & Geopolitics
    'Capital_Returns': 'Macro Investing & Geopolitics',
    'Trade_Wars_Are_Class_Wars':
        'Macro Investing & Geopolitics',
    'The_Changing_World_Order':
        'Macro Investing & Geopolitics',
    'Capital_Wars': 'Macro Investing & Geopolitics',
    'The_Price_Of_Time': 'Macro Investing & Geopolitics',

    # Wall Street Stories & Biographies
    'The_House_Of_Rothschild':
        'Wall Street Stories & Biographies',
    'House_Of_Rothschild_Vol2':
        'Wall Street Stories & Biographies',
    'The_Life_Of_John_D_Rockefeller':
        'Wall Street Stories & Biographies',
    'more-money-than-god':
        'Wall Street Stories & Biographies',
    'the-quants': 'Wall Street Stories & Biographies',
    'marketwizards': 'Wall Street Stories & Biographies',
    'Unknown_Market_Wizards':
        'Wall Street Stories & Biographies',
    'Hedge_Fund_Market_Wizards':
        'Wall Street Stories & Biographies',
    'the-man-who-solved-the-market':
        'Wall Street Stories & Biographies',
    'a-man-for-all-markets':
        'Wall Street Stories & Biographies',
    'fortunes-formula':
        'Wall Street Stories & Biographies',
    'beat-the-dealer':
        'Wall Street Stories & Biographies',
    'The_Prize':
        'Wall Street Stories & Biographies',

    # Geopolitics, Sociology & Power
    'the-road-to-serfdom':
        'Geopolitics, Sociology & Power',
    'Bowling_Alone': 'Geopolitics, Sociology & Power',
    'The_Middle_East': 'Geopolitics, Sociology & Power',
    'fate-of-empires': 'Geopolitics, Sociology & Power',
    'Historical_Dynamics':
        'Geopolitics, Sociology & Power',
    'Why_Nations_Fail': 'Geopolitics, Sociology & Power',
    'fourthturning': 'Geopolitics, Sociology & Power',
    'The_Rise_and_Fall_of_Great_Powers':
        'Geopolitics, Sociology & Power',
    'The_Lessons_Of_History':
        'Geopolitics, Sociology & Power',

    # Personal Finance Basics
    'How_to_Retire_on_Dividends':
        'Personal Finance Basics',
    'Poor_Richards_Almanack': 'Personal Finance Basics',
    'The_Small_Business_Bible': 'Personal Finance Basics',
    'Your_Money_Or_Your_Life': 'Personal Finance Basics',
    'Personal_Finance_For_Dummies':
        'Personal Finance Basics',
    'I_Will_Teach_You_To_Be_Rich':
        'Personal Finance Basics',
    'millionaire-teacher': 'Personal Finance Basics',
    'The_Millionaire_Mind': 'Personal Finance Basics',
    'The_Simple_Path_to_Wealth': 'Personal Finance Basics',

    # Self-Development & Mindset
    'The_Power_Of_Habit': 'Self-Development & Mindset',
    'Grit': 'Self-Development & Mindset',
    'How_To_Win_Friends_And_Influence_People':
        'Self-Development & Mindset',
    'Principles': 'Self-Development & Mindset',

    # Commodities & Energy
    'Investing_in_Commodities_For_Dummies':
        'Commodities & Energy',
    'The_Golden_Constant': 'Commodities & Energy',
    'the-power-of-gold': 'Commodities & Energy',
    'Hot_Commodities': 'Commodities & Energy',

    # Forex & Currencies
    'King_Dollar': 'Forex & Currencies',

    # Training & Nutrition
    'Muscle_And_Strength_Pyramid_Training':
        'Training & Nutrition',

    # Guides
    'advanced-claude': 'Guides',
    'code-101': 'Guides',
    'llm-guide': 'Guides',
    'terminal-101': 'Guides',
    'rsi-guide': 'Guides',
    'spanish-guide': 'Language Guides',
    'italian-guide': 'Language Guides',
    'property-scout': 'Guides',
    'Systematic_Trading': 'Risk Management & Position Sizing',
}

# Book type classifications
BOOK_TYPES = {
    # Textbooks
    'Principles_Of_Economics': 'textbook',
    'Economics_101': 'textbook',
    'Bond_Markets_Analysis_and_Strategies': 'textbook',
    'Options_As_Strategic_Investment': 'textbook',
    'The_Principles_Of_Banking': 'textbook',
    'Basic_Economics': 'textbook',
    'The_Mathematics_Of_Money_Management': 'textbook',
    'Muscle_And_Strength_Pyramid_Training': 'textbook',

    # Technical / Quantitative
    'Expected_Returns': 'technical',
    'Systematic_Trading': 'technical',
    'Bressert_Cycle_Trading': 'technical',
    'Elliott_Wave_Principle': 'technical',
    'The_Taylor_Trading_Technique': 'technical',
    'Trading_With_Intermarket_Analysis': 'technical',
    'Trading_Options_Greeks': 'technical',
    'position-sizing': 'technical',
    'Kelly_Capital_Growth': 'technical',

    # Practical Finance
    'Personal_Finance_For_Dummies': 'practical',
    'I_Will_Teach_You_To_Be_Rich': 'practical',
    'The_Bogleheads_Guide_To_Investing': 'practical',
    'How_to_Retire_on_Dividends': 'practical',
    'Options_Made_Easy': 'practical',
    'Trading_Options_for_Dummies': 'practical',
    'Options_Playbook': 'practical',
    'All_About_Asset_Allocation': 'practical',
    'The_Simple_Path_to_Wealth': 'practical',
    'Your_Money_Or_Your_Life': 'practical',
    'The_Small_Business_Bible': 'practical',
    'Investing_in_Commodities_For_Dummies': 'practical',
    'Asset_Allocation': 'practical',
    'The_Four_Pillars_Of_Investing': 'practical',
    'intelligent-asset-allocator': 'practical',

    # Narrative
    'The_House_Of_Rothschild': 'narrative',
    'House_Of_Rothschild_Vol2': 'narrative',
    'The_Life_Of_John_D_Rockefeller': 'narrative',
    'more-money-than-god': 'narrative',
    'the-quants': 'narrative',
    'the-man-who-solved-the-market': 'narrative',
    'a-man-for-all-markets': 'narrative',
    'fortunes-formula': 'narrative',
    'The_Ascent_of_Money': 'narrative',
    'The_Prize': 'narrative',
    'When_Money_Dies': 'narrative',
    'beat-the-dealer': 'narrative',
    'marketwizards': 'narrative',
    'Hedge_Fund_Market_Wizards': 'narrative',
    'Unknown_Market_Wizards': 'narrative',

    # Conversational
    'Talking_To_My_Daughter_About_The_Economy':
        'conversational',
    'How_An_Economy_Grows': 'conversational',
    'Skin_In_The_Game': 'conversational',
    'Antifragile': 'conversational',
    'Fooled_By_Randomness': 'conversational',
    'The_Black_Swan': 'conversational',
    'The_Psychology_Of_Money': 'conversational',
    'The_Zurich_Axioms': 'conversational',
    'The_Lessons_Of_History': 'conversational',
    'Poor_Richards_Almanack': 'conversational',

    # Analytical (default for most non-fiction)
    'Big_Debt_Crises': 'analytical',
    'The_Changing_World_Order': 'analytical',
    'Capital_Wars': 'analytical',
    'Trade_Wars_Are_Class_Wars': 'analytical',
    'Capital_Returns': 'analytical',
    'The_General_Theory': 'analytical',
    'The_Wealth_Of_Nations': 'analytical',
    'The_Creature_From_Jekyll_Island': 'analytical',
    'Against_The_Gods': 'analytical',
    'Pioneering_Portfolio_Management': 'analytical',
    'stocks-for-the-long-run': 'analytical',
    'The_Most_Important_Thing': 'analytical',
    'The_Rise_and_Fall_of_Great_Powers': 'analytical',
    'Bowling_Alone': 'analytical',
    'Why_Nations_Fail': 'analytical',
    'Historical_Dynamics': 'analytical',
    'Secular_Cycles': 'analytical',
    'Debt_The_First_5000_Years': 'analytical',
    'Manias_Panics_And_Crashes': 'analytical',
    'Rise_And_Fall_Of_American_Growth': 'analytical',
    'Crash_Proof_2': 'analytical',
    'How_Countries_Go_Broke': 'analytical',
    'The_Theory_Of_Money_And_Credit': 'analytical',
    'Capitalism_and_Freedom': 'analytical',
    'A_History_of_Interest_Rates': 'analytical',
    'The_Bond_Book': 'analytical',
    'The_Price_Of_Time': 'analytical',
    'anatomy-of-the-bear': 'analytical',
    'The_Long_Good_Buy': 'analytical',
    'Superforecasting': 'analytical',
    'How_Not_To_Be_Wrong': 'analytical',
    'thinking-fast-and-slow': 'analytical',
    'The_Hour_Between_Dog_And_Wolf': 'analytical',
    'red-blooded-risk': 'analytical',
    'way-of-the-turtle': 'analytical',
    'A_History_Of_Money_And_Banking_In_The_United_States':
        'analytical',
    'A_Primer_On_Money': 'analytical',
    'Primer_on_Money_Banking_and_Gold': 'analytical',
    'The_Golden_Constant': 'analytical',
    'King_Dollar': 'analytical',
    'Capital_Twenty_First_Century': 'analytical',
    'Seven_Deadly_Innocent_Frauds': 'analytical',
    'The_Worldly_Philosophers': 'analytical',
    'The_Middle_East': 'analytical',
    'fate-of-empires': 'analytical',
    'the-road-to-serfdom': 'analytical',
    'fourthturning': 'analytical',
    'beat-the-market': 'analytical',
    'the-power-of-gold': 'narrative',
    'Hot_Commodities': 'conversational',
    'Trade_Your_Way_To_Financial_Freedom': 'practical',
    'Systematic_Trading': 'technical',

    # Self-Development
    'Grit': 'conversational',
    'The_Power_Of_Habit': 'conversational',
    'How_To_Win_Friends_And_Influence_People': 'practical',
    'Principles': 'conversational',
    'The_Millionaire_Mind': 'analytical',
    'millionaire-teacher': 'practical',

    # Fitness
    'Muscle_And_Strength_Pyramid_Training': 'fitness',
}

# Queue tiers for To Read books
QUEUE_TIERS = {
    # Now — builds directly on books already read
    'The_Worldly_Philosophers': 'now',
    'Basic_Economics': 'now',
    'How_Not_To_Be_Wrong': 'now',
    'Fooled_By_Randomness': 'now',
    'The_Black_Swan': 'now',
    'Skin_In_The_Game': 'now',
    'Antifragile': 'now',
    'The_Zurich_Axioms': 'now',
    'red-blooded-risk': 'now',
    'way-of-the-turtle': 'now',
    'more-money-than-god': 'now',
    'The_Life_Of_John_D_Rockefeller': 'now',
    'the-quants': 'now',
    'marketwizards': 'now',
    'The_House_Of_Rothschild': 'now',
    'House_Of_Rothschild_Vol2': 'now',
    'the-road-to-serfdom': 'now',
    'Bowling_Alone': 'now',
    'The_Middle_East': 'now',
    'fate-of-empires': 'now',
    'The_Creature_From_Jekyll_Island': 'now',
    'Primer_on_Money_Banking_and_Gold': 'now',
    'The_Theory_Of_Money_And_Credit': 'now',
    'All_About_Asset_Allocation': 'now',
    'A_History_of_Interest_Rates': 'now',
    'How_to_Retire_on_Dividends': 'now',
    'Poor_Richards_Almanack': 'now',
    'The_Small_Business_Bible': 'now',
    'Your_Money_Or_Your_Life': 'now',
    'spanish-guide': 'now',
    'italian-guide': 'now',
    'The_Power_Of_Habit': 'now',
    'Grit': 'now',
    'How_To_Win_Friends_And_Influence_People': 'now',
    'Investing_in_Commodities_For_Dummies': 'now',
    'Debt_The_First_5000_Years': 'now',
    'When_Money_Dies': 'now',
    'Manias_Panics_And_Crashes': 'now',
    'The_Ascent_of_Money': 'now',
    'Capital_Returns': 'now',
    'Trade_Wars_Are_Class_Wars': 'now',

    # Soon — core reads, solid foundation needed
    'Capital_Twenty_First_Century': 'soon',
    'position-sizing': 'soon',
    'Trade_Your_Way_To_Financial_Freedom': 'soon',
    'Systematic_Trading': 'soon',
    'fourthturning': 'soon',
    'Bressert_Cycle_Trading': 'soon',
    'The_Changing_World_Order': 'soon',
    'Rise_And_Fall_Of_American_Growth': 'soon',
    'The_Taylor_Trading_Technique': 'soon',
    'Bond_Markets_Analysis_and_Strategies': 'soon',
    'The_Principles_Of_Banking': 'soon',
    'Pioneering_Portfolio_Management': 'soon',
    'Expected_Returns': 'soon',
    'Options_As_Strategic_Investment': 'soon',
    'Options_Playbook': 'soon',
    'Trading_Options_Greeks': 'soon',
    'thinking-fast-and-slow': 'soon',
    'Superforecasting': 'soon',
    'The_Hour_Between_Dog_And_Wolf': 'soon',
    'Historical_Dynamics': 'soon',
    'Why_Nations_Fail': 'soon',
    'Unknown_Market_Wizards': 'soon',
    'Muscle_And_Strength_Pyramid_Training': 'soon',

    # Later — worth it, no urgency
    'property-scout': 'later',
    'Kelly_Capital_Growth': 'later',
    'Elliott_Wave_Principle': 'later',
}

# Author overrides for guides and books where extraction fails
AUTHOR_OVERRIDES = {
    'advanced-claude': 'Alex Barnett & Claude',
    'code-101': 'Alex Barnett & Claude',
    'llm-guide': 'Alex Barnett & Claude',
    'terminal-101': 'Alex Barnett & Claude',
    'rsi-guide': 'Alex Barnett & Claude',
    'spanish-guide': 'Alex Barnett & Claude',
    'italian-guide': 'Alex Barnett & Claude',
    'property-scout': 'Alex Barnett & Claude',
    'All_About_Asset_Allocation': 'Richard A. Ferri',
    'I_Will_Teach_You_To_Be_Rich': 'Ramit Sethi',
    'Basic_Economics': 'Thomas Sowell',
    'stocks-for-the-long-run': 'Jeremy Siegel',
    'The_Theory_Of_Money_And_Credit': 'Ludwig von Mises',
    'The_Black_Swan': 'Nassim Nicholas Taleb',
    'Expected_Returns': 'Antti Ilmanen',
    'Pioneering_Portfolio_Management': 'David F. Swensen',
    'Bressert_Cycle_Trading': 'Walter Bressert',
    'Options_Made_Easy': 'Guy Cohen',
    'Trading_Options_for_Dummies': 'Joe Duarte',
    'Capital_Returns': 'Edward Chancellor',
    'Atomic_Habits': 'James Clear',
    'The_Worldly_Philosophers': 'Robert L. Heilbroner',
    'The_Most_Important_Thing': 'Howard Marks',
    'Crash_Proof_2': 'Peter D. Schiff',
    'Rise_And_Fall_Of_American_Growth': 'Robert J. Gordon',
    'Skin_In_The_Game': 'Nassim Nicholas Taleb',
    'The_Hour_Between_Dog_And_Wolf': 'John Coates',
    'Asset_Allocation': 'Roger C. Gibson',
    'The_Long_Good_Buy': 'Peter C. Oppenheimer',
    'beat-the-market': 'Edward O. Thorp & Sheen T. Kassouf',
    'Systematic_Trading': 'Robert Carver',
    'The_Mathematics_Of_Money_Management': 'Ralph Vince',
    'The_Zurich_Axioms': 'Max Gunther',
    'marketwizards': 'Jack D. Schwager',
    'The_Prize': 'Daniel Yergin',
    'Options_Playbook': 'Brian Overby',
    'Personal_Finance_For_Dummies': 'Eric Tyson',
    'Manias_Panics_And_Crashes':
        'Charles P. Kindleberger & Robert Z. Aliber',
    'Principles_Of_Economics': 'N. Gregory Mankiw',
    'The_Taylor_Trading_Technique': 'George Douglass Taylor',
    'Options_As_Strategic_Investment': 'Lawrence G. McMillan',
    'Muscle_And_Strength_Pyramid_Training':
        'Eric Helms, Andy Morgan & Andrea Valdez',
    'Fooled_By_Randomness': 'Nassim Nicholas Taleb',
    'Antifragile': 'Nassim Nicholas Taleb',
    'The_Golden_Constant': 'Roy W. Jastram',
    'King_Dollar': 'Paul Blustein',
    'anatomy-of-the-bear': 'Russell Napier',
    'Cycles_The_Science_Of_Prediction':
        'Edward R. Dewey & Edwin F. Dakin',
    'Talking_To_My_Daughter_About_The_Economy':
        'Yanis Varoufakis',
    'The_Wealth_Of_Nations': 'Adam Smith',
    'A_History_Of_Money_And_Banking_In_The_United_States':
        'Murray N. Rothbard',
    'When_Money_Dies': 'Adam Fergusson',
    'Trading_Options_Greeks': 'Dan Passarelli',
    'red-blooded-risk': 'Aaron Brown',
    'fourthturning': 'William Strauss & Neil Howe',
    'Bond_Markets_Analysis_and_Strategies':
        'Frank J. Fabozzi',
    'The_Principles_Of_Banking': 'Moorad Choudhry',
    'A_History_of_Interest_Rates':
        'Sidney Homer & Richard Sylla',
}

# Canonical category display order
CATEGORY_ORDER = [
    'Personal Finance Basics',
    'Economics Fundamentals',
    'Investing Fundamentals',
    'Free Markets & Political Economy',
    'Monetary Policy & Central Banking',
    'Economic History & Financial Crises',
    'Behavioral Finance & Psychology',
    'Portfolio Management & Asset Allocation',
    'Fixed Income & Bonds',
    'Commodities & Energy',
    'Forex & Currencies',
    'Cycles & Market Timing',
    'Technical Analysis',
    'Options & Derivatives',
    'Risk Management & Position Sizing',
    'Macro Investing & Geopolitics',
    'Wall Street Stories & Biographies',
    'Geopolitics, Sociology & Power',
    'Self-Development & Mindset',
    'Training & Nutrition',
    'Language Guides',
    'Guides',
]


def normalize_id(folder):
    """Generate a stable, URL-safe ID from folder name."""
    s = folder.lower()
    s = re.sub(r'[^a-z0-9]+', '-', s)
    s = s.strip('-')
    return s


def extract_title_author(book_dir):
    """Extract title and author from a book's index.html."""
    idx = os.path.join(BOOKS_DIR, book_dir, 'index.html')
    if not os.path.isfile(idx):
        return None, None

    with open(idx, 'r', errors='replace') as f:
        content = f.read(8000)

    # Title from <title> tag
    title = None
    m = re.search(r'<title>([^<]+)</title>', content)
    if m:
        title = unescape(m.group(1).strip())
    if not title or title == 'Book Notes':
        m = re.search(r'<h1[^>]*>([^<]+)</h1>', content)
        if m:
            title = unescape(m.group(1).strip())

    # Clean up title — remove " — Author" suffix
    if title and ' — ' in title:
        title = title.split(' — ')[0].strip()
    if title and ' - ' in title:
        # Only split on " - " if it looks like a title-author
        parts = title.split(' - ')
        if len(parts) == 2 and len(parts[1]) < 40:
            title = parts[0].strip()

    # Author extraction
    author = AUTHOR_OVERRIDES.get(book_dir)
    if not author:
        # Try subtitle class
        m = re.search(
            r'class="subtitle"[^>]*>([^<]+)<', content
        )
        if m:
            author = unescape(m.group(1).strip())
    if not author:
        # Try author class
        m = re.search(
            r'class="author"[^>]*>([^<]+)<', content
        )
        if m:
            author = unescape(m.group(1).strip())
    if not author:
        # Try "by Author" pattern
        m = re.search(
            r'>\s*(?:by|By)\s+([A-Z][^<]{2,50})<', content
        )
        if m:
            author = unescape(m.group(1).strip())

    # Clean up author — remove page counts, editions, etc.
    if author:
        # Remove "By " prefix
        author = re.sub(r'^(?:By|by)\s+', '', author)
        # Remove "Nth Edition — " prefix
        author = re.sub(
            r'^(?:\d+(?:st|nd|rd|th)\s+)?Edition\s*[—\-]\s*',
            '', author, flags=re.I
        )
        # Remove everything after " — " (usually subtitle)
        author = re.sub(r'\s*—\s+.*$', '', author)
        # Remove everything from first " · " onward
        # (year, publisher, page count, edition — all junk)
        author = re.sub(r'\s*\u00b7\s.*$', '', author)
        # Also handle bullet "•"
        author = re.sub(r'\s*\u2022\s.*$', '', author)
        # Remove "(Nth ed. YEAR)" patterns
        author = re.sub(
            r'\s*\((?:\d+(?:st|nd|rd|th)\s+)?'
            r'(?:ed|edition|updated|revised)\.?\s*'
            r'(?:\d{4})?\).*$', '', author, flags=re.I
        )
        # Remove "· N pages" patterns
        author = re.sub(r'\s*·\s*~?\d+\s*pages.*$', '', author)
        # Remove "· N Chapters/Books/Parts ..." patterns
        author = re.sub(
            r'\s*·\s*\d+\s*(?:Chapter|Book|Part|Major|Minor).*$',
            '', author, flags=re.I
        )
        # Remove trailing year in parens
        author = re.sub(r'\s*\(\d{4}\)$', '', author)
        # Remove "· Illustrated by ..."
        author = re.sub(r'\s*·\s*Illustrated.*$', '', author, flags=re.I)
        # Remove CFA/CFP designations
        author = re.sub(r',?\s*(?:CFA|CFP)\b', '', author)
        # Remove "· ~NNN pages" at end
        author = re.sub(r'\s*·\s*~?\d+\s*pages?\s*·?$', '', author, flags=re.I)
        # Remove "(ed.)" for editors
        author = re.sub(r'\s*\(ed\.?\)\s*', ' ', author)
        # Remove "Translated by ..." suffix
        author = re.sub(r'\s*·?\s*Translated\s+by.*$', '', author, flags=re.I)
        # Final cleanup
        author = author.strip(' ·,')
        author = ' '.join(author.split())

    return title, author


def extract_existing_ids():
    """Extract existing data-book and bmkey from shelf HTML
    so we preserve read state and bookmarks."""
    if not os.path.isfile(SHELF_PATH):
        return {}
    with open(SHELF_PATH) as f:
        html = f.read()
    existing = {}
    for m in re.finditer(
        r'href="([^"]+)/(index|plain)\.html"[^>]*'
        r'data-book="([^"]+)"[^>]*'
        r'data-bmkey="([^"]+)"',
        html
    ):
        folder = m.group(1)
        fmt = m.group(2)  # 'index' or 'plain'
        data_book = m.group(3)
        bmkey = m.group(4)
        if folder not in existing:
            existing[folder] = {}
        existing[folder][fmt] = {
            'id': data_book, 'bmkey': bmkey
        }
    return existing


def extract_shelf_data():
    """Parse the existing shelf HTML for category + author data
    to use as fallback/override."""
    if not os.path.isfile(SHELF_PATH):
        return {}, {}

    with open(SHELF_PATH) as f:
        html = f.read()

    book_to_category = {}
    book_to_author = {}

    # Find section titles and their positions
    sections = []
    for m in re.finditer(
        r'<h2\s+class="section-title"[^>]*>(.*?)</h2>',
        html, re.DOTALL
    ):
        cat = re.sub(r'<[^>]+>', '', m.group(1)).strip()
        cat = unescape(cat)
        sections.append((m.start(), cat))

    def get_cat(pos):
        cat = ''
        for s_pos, s_cat in sections:
            if s_pos <= pos:
                cat = s_cat
            else:
                break
        return cat

    # Find all book entries
    for m in re.finditer(
        r'<a\s+class="book"\s+href="([^"]+)".*?'
        r'<div\s+class="book-author">(.*?)</div>',
        html, re.DOTALL
    ):
        href = m.group(1)
        author_raw = re.sub(r'<[^>]+>', '', m.group(2))
        author = unescape(author_raw.strip())
        folder = href.split('/')[0] if '/' in href else href
        cat = get_cat(m.start())
        if cat and cat not in (
            'To Read', 'Recently Added from To Read', ''
        ):
            book_to_category[folder] = cat
        if author:
            book_to_author[folder] = author

    return book_to_category, book_to_author


def generate():
    """Main generation logic."""
    shelf_cats, shelf_authors = extract_shelf_data()
    existing_ids = extract_existing_ids()

    books = []
    seen_ids = set()

    for d in sorted(os.listdir(BOOKS_DIR)):
        full = os.path.join(BOOKS_DIR, d)
        if not os.path.isdir(full):
            continue
        if d in SKIP_DIRS:
            continue

        has_index = os.path.isfile(
            os.path.join(full, 'index.html')
        )
        has_plain = os.path.isfile(
            os.path.join(full, 'plain.html')
        )
        has_notes = os.path.isfile(
            os.path.join(full, 'notes.md')
        )
        has_thumb = os.path.isfile(
            os.path.join(full, 'thumb.jpg')
        )
        has_cover = os.path.isfile(
            os.path.join(full, 'cover.jpg')
        )

        if not has_index and not has_notes:
            continue  # Skip empty directories

        title, author = extract_title_author(d)

        # Use shelf HTML author as fallback
        if not author and d in shelf_authors:
            author = shelf_authors[d]

        # Determine category
        category = CATEGORY_OVERRIDES.get(
            d, shelf_cats.get(d, 'Uncategorized')
        )

        # Determine book type
        book_type = BOOK_TYPES.get(d, 'analytical')

        # Use existing ID from shelf HTML to preserve
        # read state and bookmarks
        ex = existing_ids.get(d, {})
        if 'index' in ex:
            book_id = ex['index']['id']
            bmkey = ex['index']['bmkey']
        else:
            book_id = normalize_id(d)
            bmkey = 'bm_' + book_id.replace('-', '_')
        # Ensure uniqueness
        if book_id in seen_ids:
            book_id = book_id + '-2'
        seen_ids.add(book_id)

        # Build formats with bmkeys
        formats = {}
        if has_index:
            formats['full'] = {
                'file': 'index.html',
                'bmkey': bmkey,
            }
        if has_plain:
            plain_ex = ex.get('plain', {})
            plain_id = plain_ex.get('id', book_id + '-plain')
            plain_bmkey = plain_ex.get(
                'bmkey', bmkey + '_plain'
            )
            formats['plain'] = {
                'file': 'plain.html',
                'id': plain_id,
                'bmkey': plain_bmkey,
            }

        # Queue info
        queue = None
        if d in QUEUE_TIERS:
            queue = {'tier': QUEUE_TIERS[d]}

        # Content version from file modification time
        content_version = None
        if has_index:
            mtime = os.path.getmtime(
                os.path.join(full, 'index.html')
            )
            content_version = datetime.fromtimestamp(
                mtime
            ).strftime('%Y-%m-%d')

        book = {
            'id': book_id,
            'folder': d,
            'title': title or d,
            'author': author or 'Unknown',
            'category': category,
            'type': book_type,
            'formats': formats,
            'bmkey': bmkey,
            'cover': 'thumb.jpg' if has_thumb else (
                'cover.jpg' if has_cover else None
            ),
            'built': has_index,
            'contentVersion': content_version,
        }

        if queue:
            book['queue'] = queue

        books.append(book)

    # Sort by category order, then title
    cat_order = {c: i for i, c in enumerate(CATEGORY_ORDER)}

    def sort_key(b):
        return (
            cat_order.get(b['category'], 999),
            b['title'].lower()
        )

    books.sort(key=sort_key)

    manifest = {
        'schemaVersion': 1,
        'generated': datetime.now().strftime(
            '%Y-%m-%dT%H:%M:%S'
        ),
        'categories': CATEGORY_ORDER,
        'books': books,
    }

    with open(OUT_PATH, 'w') as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)

    # Print summary
    built = sum(1 for b in books if b['built'])
    queued = sum(1 for b in books if b.get('queue'))
    cats = len(set(b['category'] for b in books))
    uncat = sum(
        1 for b in books if b['category'] == 'Uncategorized'
    )

    print(f'Generated {OUT_PATH}')
    print(f'  Total books: {len(books)}')
    print(f'  Built: {built}')
    print(f'  In queue (To Read): {queued}')
    print(f'  Categories: {cats}')
    if uncat:
        print(f'  WARNING: {uncat} uncategorized books:')
        for b in books:
            if b['category'] == 'Uncategorized':
                print(f'    - {b["folder"]}')

    return manifest


if __name__ == '__main__':
    generate()
