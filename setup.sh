#!/data/data/com.termux/files/usr/bin/bash
# Jalankan sekali: bash setup.sh
cd "$(dirname "$0")"
pkg install -y python curl >/dev/null 2>&1
if [ ! -s three.min.js ]; then
  echo "Mengunduh three.js (sekali saja)..."
  curl -L -o three.min.js https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js || { echo "Gagal unduh, cek internet"; exit 1; }
fi
echo "Siap! Buka di Chrome: http://localhost:8080"
python -m http.server 8080
