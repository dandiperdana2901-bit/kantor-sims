import os, sys, shutil

F = 'index.html'
s = open(F, encoding='utf-8').read()

if 'texImg' in s:
    print('Sudah pernah dipatch, tidak ada yang diubah.')
    sys.exit()

def rep(old, new):
    global s
    n = s.count(old)
    if n != 1:
        print('GAGAL: bagian kode ditemukan %d kali (harus 1):' % n)
        print('  ' + old[:70])
        print('Tidak ada yang diubah. Kirim screenshot ini ke Claude.')
        sys.exit(1)
    s = s.replace(old, new)

# 1. tex() bisa memuat gambar kalau isinya diawali "img:"
rep('function tex(a,b){', """const TEXC={};
function texImg(u){if(TEXC[u])return TEXC[u];const t=new THREE.TextureLoader().load(u);t.wrapS=t.wrapT=THREE.RepeatWrapping;t.repeat.set(3,2);if(THREE.SRGBColorSpace)t.colorSpace=THREE.SRGBColorSpace;else if(THREE.sRGBEncoding)t.encoding=THREE.sRGBEncoding;t.anisotropy=4;TEXC[u]=t;return t}
function tex(a,b){if(typeof a==='string'&&a.indexOf('img:')==0)return texImg(a.slice(4));""")

# 2. tambah 4 motif ke daftar lantai toko
rep('const TPOPEN=', """TPF.push(["Japanese Cedar Planks",25,"img:LANTAI/textures/japanese_cedar_planks_diff_2k.jpg"],["Lacquered Cherry Wood",30,"img:LANTAI/textures/lacquered_cherry_wood_diff_4k.jpg"],["Oak Veneer",25,"img:LANTAI/textures/oak_veneer_05_diff_2k.jpg"],["Plank Flooring",25,"img:LANTAI/textures/plank_flooring_04_diff_2k.jpg"]);
const TPOPEN=""")

# 3. kartu di toko menampilkan gambar motif
rep("""background:'+m[2]+'"></i>'""",
    """background:'+(m[2].indexOf('img:')==0?'url('+m[2].slice(4)+') center/cover':m[2])+'"></i>'""")

# 4. preview lantai: jangan hitung warna gelap untuk motif gambar
rep("r.t=[TPS.mat.v,tpxShade(TPS.mat.v,-14)];tpxSetFloor(i)",
    "r.t=[TPS.mat.v,TPS.mat.v.indexOf('img:')==0?TPS.mat.v:tpxShade(TPS.mat.v,-14)];tpxSetFloor(i)")

# semua berhasil -> backup lalu tulis
i = 1
while os.path.exists('index.html.lantai%d' % i):
    i += 1
bak = 'index.html.lantai%d' % i
shutil.copy(F, bak)
open(F, 'w', encoding='utf-8').write(s)
print('4 motif lantai ditambahkan ke toko (tab Floors).')
print('SELESAI. Backup: ' + bak)
