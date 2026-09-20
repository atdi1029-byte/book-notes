# Sourced by the book tooling: pick a python3 that actually runs here.
# On an Apple Silicon Mac an Intel-only python3 earlier in PATH fails with
# "Bad CPU type in executable". Set PYTHON=/path/to/python3 to force one.
if [ -z "${PYTHON:-}" ] || ! "$PYTHON" -c 'import sys' >/dev/null 2>&1; then
  PYTHON=""
  for _py in /opt/homebrew/bin/python3 /usr/bin/python3 python3; do
    if "$_py" -c 'import sys' >/dev/null 2>&1; then PYTHON="$_py"; break; fi
  done
  [ -n "$PYTHON" ] || PYTHON=python3
fi
export PYTHON
python3() { "$PYTHON" "$@"; }
export -f python3 2>/dev/null
