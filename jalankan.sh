#!/data/data/com.termux/files/usr/bin/bash
cd "$(dirname "$0")"
echo "Buka di Chrome: http://localhost:8080  (Ctrl+C untuk berhenti)"
python -m http.server 8080
