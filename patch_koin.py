import os, sys, shutil

F = 'index.html'
s = open(F, encoding='utf-8').read()

if 'Tes: tambah koin' in s:
    print('Sudah pernah dipatch, tidak ada yang diubah.')
    sys.exit()

old = "['Mulai ulang (hapus progres)'"
n = s.count(old)
if n != 1:
    print('GAGAL: bagian menu ditemukan %d kali (harus 1). Tidak ada yang diubah.' % n)
    print('Kirim screenshot ini ke Claude.')
    sys.exit(1)

new = (
    "['Tes: tambah koin +$1000',()=>{coins+=1000;$('cn').textContent=Math.floor(coins);"
    "try{save()}catch(e){};toast('Koin +$1000');closeSheet()},true,ICO.cam],"
    "['Tes: tambah koin +$10000',()=>{coins+=10000;$('cn').textContent=Math.floor(coins);"
    "try{save()}catch(e){};toast('Koin +$10000');closeSheet()},true,ICO.cam],"
) + old

s = s.replace(old, new)

i = 1
while os.path.exists('index.html.koin%d' % i):
    i += 1
bak = 'index.html.koin%d' % i
shutil.copy(F, bak)
open(F, 'w', encoding='utf-8').write(s)
print('2 tombol tambah koin ditambahkan ke menu.')
print('SELESAI. Backup: ' + bak)
