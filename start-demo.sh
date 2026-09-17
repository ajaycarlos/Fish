#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"

echo "Starting Flask..."
if [ -f "venv/bin/activate" ]; then
    source venv/bin/activate
fi

python app.py &
FLASK_PID=$!

cleanup() {
    echo
    echo "Stopping demo..."
    kill "$FLASK_PID" 2>/dev/null || true
}
trap cleanup INT TERM

sleep 1

echo
echo "Starting Cloudflare Quick Tunnel..."
echo "Keep this terminal open while the demo is running."
echo

cloudflared tunnel --url http://127.0.0.1:5000
