#!/bin/bash
# Install the Finance Guide bot as a macOS LaunchAgent.
#
# Why: `nohup python3 finance_guide.py &` dies on reboot, logout, or when
# the terminal that launched it goes away, and nothing restarts it.
# launchd starts the bot at login and restarts it within a minute if it
# ever exits or crashes.
#
#   bash install_launchd.sh            # install (or reinstall) and start
#   bash install_launchd.sh --remove   # stop and uninstall
#
# Afterwards:
#   python3 finance_guide.py --status                          # is it alive?
#   tail -f bot.log                                            # watch it work
#   launchctl kickstart -k gui/$(id -u)/com.a.financeguide     # force restart
#
# The Mac must be awake for a check to happen. If it sleeps through a
# 6-hour mark the check runs as soon as it wakes.
set -euo pipefail

DIR="$(cd "$(dirname "$0")" && pwd)"
LABEL="com.a.financeguide"
PLIST="$HOME/Library/LaunchAgents/$LABEL.plist"
DOMAIN="gui/$(id -u)"

if [[ "${1:-}" == "--remove" ]]; then
  launchctl bootout "$DOMAIN/$LABEL" 2>/dev/null || true
  rm -f "$PLIST"
  echo "Removed $LABEL"
  exit 0
fi

# Real interpreter (not a pyenv/asdf shim) — the one that has
# youtube_transcript_api installed, since that's the python3 you use.
PY="$(python3 -c 'import sys; print(sys.executable)')"

# Build a PATH that includes wherever claude and yt-dlp actually live.
# launchd does NOT load your shell profile, so a bare PATH would miss them.
EXTRA=""
for tool in claude yt-dlp git; do
  if loc="$(command -v "$tool" 2>/dev/null)"; then
    EXTRA="$EXTRA:$(dirname "$loc")"
  else
    echo "WARNING: '$tool' not found on your PATH — the bot needs it." >&2
  fi
done
BOT_PATH="/opt/homebrew/bin:/usr/local/bin:$HOME/.local/bin$EXTRA:/usr/bin:/bin"

# Stop any hand-started copy so it can't hold the lock.
pkill -f "finance_guide.py" 2>/dev/null && echo "Stopped a running nohup copy" || true
sleep 1

mkdir -p "$HOME/Library/LaunchAgents"
cat > "$PLIST" <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key>
  <string>$LABEL</string>

  <key>ProgramArguments</key>
  <array>
    <string>$PY</string>
    <string>$DIR/finance_guide.py</string>
  </array>

  <key>WorkingDirectory</key>
  <string>$DIR</string>

  <key>EnvironmentVariables</key>
  <dict>
    <key>PATH</key>
    <string>$BOT_PATH</string>
    <key>HOME</key>
    <string>$HOME</string>
    <key>PYTHONUNBUFFERED</key>
    <string>1</string>
  </dict>

  <!-- start at login -->
  <key>RunAtLoad</key>
  <true/>

  <!-- restart if it ever exits, for any reason -->
  <key>KeepAlive</key>
  <true/>

  <!-- but never faster than once a minute (avoids a crash loop) -->
  <key>ThrottleInterval</key>
  <integer>60</integer>

  <!-- anything the script prints that isn't in bot.log lands here -->
  <key>StandardOutPath</key>
  <string>$DIR/launchd.out.log</string>
  <key>StandardErrorPath</key>
  <string>$DIR/launchd.err.log</string>
</dict>
</plist>
EOF

launchctl bootout "$DOMAIN/$LABEL" 2>/dev/null || true
launchctl bootstrap "$DOMAIN" "$PLIST"

echo "Installed $PLIST"
echo "  python: $PY"
echo "  script: $DIR/finance_guide.py"
echo
sleep 4
"$PY" "$DIR/finance_guide.py" --status
