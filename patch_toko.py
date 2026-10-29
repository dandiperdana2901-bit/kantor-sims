import re, shutil, sys

F = 'index.html'
s = open(F, encoding='utf-8').read()

if 'TOKOPLUS' in s:
    print('Sudah pernah dipatch. Batal.'); sys.exit()

shutil.copy(F, 'index.html.bak13')

INJECT = r"""/* ===== TOKOPLUS: dinding & lantai + kategori Home Store ===== */
const TPW=[["White Simple Tile",10,"#e8e8e8"],["Red Paint",11,"#8a3b36"],["Green Paint",11,"#4a6b45"],["Eggshell Paint",11,"#e0d3b8"],["White Paint",11,"#e6e6e2"],["Brown Paint",11,"#6b4636"],["Purple Paint",11,"#6a4f86"],["Pink Wall",11,"#d97fc0"],["Creme Paint",11,"#d9c9a3"],["Blue Paint",11,"#4a6078"],["Offwhite Paint",11,"#b9b8ae"],["Unpainted Wall",5,"#e9dfc9"]];
const TPF=[["Plain Pine Floorboards",15,"#d9b27c"],["Rustic Plank",10,"#4a3a33"],["Blue Terrazzo",10,"#9aa0a0"],["Red Shag",10,"#5a0a0e"],["Blue Checkered Lino",15,"#a8cdd6"],["White Terrazzo",10,"#b8aea0"],["Yellow Shag",10,"#c99a0a"],["Sky Blue Carpet",5,"#4f8fc0"],["Old Brown Carpet",15,"#a79a7e"],["Red Terrazzo",10,"#5c2a20"],["Blue Shag",10,"#8a9aa8"],["Purple Carpet",5,"#5a2a70"]];
const TPOPEN=[["bedroom","Bedroom","🛏️"],["living","Living Room","🛋️"],["rugs","Rugs","🟫"],["outdoor","Outdoor Furniture","⛱️"],["bathroom","Bathroom","🚽"],["kitchen","Kitchen","🍳"],["dining","Dining Room","🍽️"],["lighting","Lighting","💡"],["electronics","Electronics","📺"],["counter","Counter Tops","🗄️"],["decor","Decorations","🗿"],["plants","Plants & Gardens","🌳"],["roofing","Roofing","🏚️"],["windows","Windows","🪟"],["outdoor_decor","Outdoor Decorations","🦩"],["doors","Doors","🚪"],["ext_walls","Exterior Walls","🧱"],["fireplaces","Fireplaces","🔥"],["chimneys","Chimneys","🏭"]];
const TPLOCK=[["support_posts","Support Posts"],["railings","Railings"],["balcony_paving","Balcony Paving"],["patio_paving","Patio Paving"],["patio_gates","Patio Gates"],["stairs","Stairs"],["pets","Pets"],["toddler","Toddler"],["preteen","Preteen"],["teen","Teen"],["pool_items","Pool Items"],["pool_interior","Pool Interior"],["pool_paving","Pool Paving"],["roof_items","Roof Items"]];
const TPS={stage:'mat',mat:null,room:-1,old:null,cost:0,isW:false,inited:false};
function tpxShade(h,d){const n=parseInt(h.slice(1),16),c=v=>Math.max(0,Math.min(255,v));return '#'+((1<<24)+(c((n>>16)+d)<<16)+(c(((n>>8)&255)+d)<<8)+c((n&255)+d)).toString(16).slice(1)}
function tpxLoad(){try{return JSON.parse(localStorage.getItem('tp_mat')||'{}')}catch(e){return {}}}
function tpxSave(i){try{const M=tpxLoad(),r=rooms[i];M[r.id]={t:r.t,wc:r.wc};localStorage.setItem('tp_mat',JSON.stringify(M))}catch(e){}}
function tpxSetFloor(i){const f=floors[i];if(!f)return;f.material.map=tex(...rooms[i].t);f.material.needsUpdate=true;applyExt()}
function tpxRevert(){if(TPS.room<0)return;const i=TPS.room,r=rooms[i];if(TPS.isW){r.wc=TPS.old;buildWalls()}else{r.t=TPS.old;tpxSetFloor(i)}TPS.room=-1;$('tpbar').style.display='none'}
function tpxPreview(i,cost,isW){tpxRevert();shut();TPS.room=i;TPS.cost=cost;TPS.isW=isW;const r=rooms[i];
 if(isW){TPS.old=r.wc;r.wc=parseInt(TPS.mat.v.slice(1),16);buildWalls()}
 else{TPS.old=r.t.slice();r.t=[TPS.mat.v,tpxShade(TPS.mat.v,-14)];tpxSetFloor(i)}
 $('tpbar').style.display='flex';$('tpcost').textContent='$'+cost}
function tpxOk(){if(TPS.room<0)return;if(coins<TPS.cost){toast('Koin kurang');tpxRevert();return}
 coins-=TPS.cost;tpxSave(TPS.room);TPS.room=-1;$('tpbar').style.display='none';$('cn').textContent=Math.floor(coins);try{save()}catch(e){}toast('Berhasil diganti!')}
function tpxInit(){if(TPS.inited)return;TPS.inited=true;
 FCAT.push(['h_walls','Walls','🧱']);FCAT.push(['h_floors','Floors','🟦']);
 TPOPEN.forEach(c=>FCAT.push(['h_'+c[0],c[1],c[2]]));
 TPLOCK.forEach(c=>FCAT.push(['h_'+c[0],c[1],'🔒']));
 const b=document.createElement('div');b.id='tpbar';
 b.style.cssText='position:fixed;left:50%;bottom:90px;transform:translateX(-50%);display:none;align-items:center;gap:12px;z-index:99;background:#000b;padding:8px 14px;border-radius:30px;color:#fff;font-weight:bold';
 b.innerHTML='<button id="tpno" style="width:46px;height:46px;border-radius:50%;border:0;background:#e53935;color:#fff;font-size:22px">✕</button><span id="tpcost"></span><button id="tpok" style="width:46px;height:46px;border-radius:50%;border:0;background:#2e9e3a;color:#fff;font-size:22px">✓</button>';
 document.body.appendChild(b);$('tpno').onclick=tpxRevert;$('tpok').onclick=tpxOk;
 new MutationObserver(()=>{[...$('shg').children].forEach(d=>{if(d.textContent.indexOf('🔒')>=0&&!d.classList.contains('lk'))d.classList.add('lk')})}).observe($('shg'),{childList:true})}
function tpxDraw(){
 if(view=='cat'){TPS.stage='mat';return false}
 if(view!='it'||!cat)return false;
 const id=cat[0];
 if(TPLOCK.some(c=>'h_'+c[0]==id)){view='cat';draw();toast('Terkunci 🔒');return true}
 if(id!='h_walls'&&id!='h_floors')return false;
 const isW=id=='h_walls',g=$('shg');g.innerHTML='';$('shb').innerHTML=ICO.back;$('sht').textContent=cat[1];
 if(TPS.stage=='mat'){
  (isW?TPW:TPF).forEach(m=>{const d=document.createElement('div');d.className='fcd';
   d.innerHTML='<i style="display:block;width:46px;height:34px;margin:0 auto 4px;border:1px solid #000;border-radius:4px;background:'+m[2]+'"></i>'+m[0]+'<u class="v">$'+m[1]+'</u>';
   d.onclick=()=>{TPS.mat={n:m[0],p:m[1],v:m[2]};TPS.stage='room';draw();toast('Pilih ruangan untuk '+m[0])};g.appendChild(d)});
 }else{
  rooms.forEach((r,i)=>{if(!owned[i])return;const [x0,x1,z0,z1]=RR(i),W=x1-x0,D=z1-z0,n=isW?Math.ceil((W+D)/2):Math.ceil(W*D/4),cost=TPS.mat.p*n;
   const d=document.createElement('div');d.className='fcd';
   d.innerHTML='<i>'+(isW?'🧱':'🟦')+'</i>'+r.n+'<u class="v">$'+cost+'</u>';
   d.onclick=()=>tpxPreview(i,cost,isW);g.appendChild(d)});
 }
 return true}
setTimeout(()=>{try{const M=tpxLoad();rooms.forEach((r,i)=>{const s=M[r.id];if(!s)return;if(s.t&&floors[i]){r.t=s.t;floors[i].material.map=tex(...s.t);floors[i].material.needsUpdate=true}if(s.wc!=null)r.wc=s.wc});applyExt();buildWalls()}catch(e){console.log('tp load',e)}},1500);
/* ===== END TOKOPLUS ===== */
"""

# 1. sisipkan blok sebelum deklarasi view toko
k = "let view='cat',cat=null;"
if k not in s:
    print('GAGAL: baris', k, 'tidak ketemu'); sys.exit()
s = s.replace(k, INJECT + k, 1)

# 2. hook di draw()
h = "function draw(){const g=$('shg');"
if h not in s:
    print('GAGAL: function draw tidak ketemu'); sys.exit()
s = s.replace(h, "function draw(){tpxInit();if(tpxDraw())return;const g=$('shg');", 1)

# 3. warna dinding per ruangan di buildWalls
a = s.find('function buildWalls(){')
e = s.find('function mkDesk', a)
if a < 0 or e < 0:
    print('PERINGATAN: buildWalls tidak ketemu, warna dinding tidak aktif')
else:
    body = s[a:e]
    body2, n = re.subn(r'0xf6ecdc', '(rooms[i].wc||0xf6ecdc)', body, flags=re.I)
    s = s[:a] + body2 + s[e:]
    print('Warna dinding diganti di', n, 'tempat')

# 4. reset progres juga hapus material
s = s.replace("localStorage.removeItem('sims2')", "localStorage.removeItem('sims2');localStorage.removeItem('tp_mat')")

open(F, 'w', encoding='utf-8').write(s)
print('SELESAI. Backup: index.html.bak13')
