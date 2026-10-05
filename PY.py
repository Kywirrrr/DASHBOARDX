from pathlib import Path
import base64, html

img_path = Path("banner")
data = img_path.read_bytes()
b64 = base64.b64encode(data).decode("ascii")

html_content = f"""<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>ExamBrowser</title>
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
body{{font-family:Arial,Helvetica,sans-serif;background:#f7f9ff;color:#444;min-height:100vh}}
.app{{min-height:100vh;background:#f8faff;overflow:hidden}}
.header{{
  min-height:520px;position:relative;padding:55px 7% 45px;color:#fff;
  background:linear-gradient(145deg,#858bef,#737de8);overflow:hidden
}}
.header:before{{
  content:"";position:absolute;width:480px;height:480px;border-radius:50%;
  background:rgba(255,255,255,.045);right:-190px;top:-270px
}}
.header:after{{
  content:"";position:absolute;width:280px;height:280px;border-radius:50%;
  background:rgba(255,255,255,.035);left:-160px;bottom:-200px
}}
.top{{position:relative;z-index:3;display:flex;align-items:center;gap:15px}}
.time{{font-size:13px;opacity:.92}}
.greeting{{position:relative;z-index:3;margin-top:20px}}
.greeting h1{{font-size:30px;font-weight:800;margin-bottom:10px}}
.greeting p{{font-size:12px;line-height:1.6;font-style:italic;max-width:360px}}
.side-image{{
  position:absolute;z-index:4;right:7%;top:68px;width:78px;height:78px;
  object-fit:contain;cursor:pointer;display:none
}}
.side-image.show{{display:block}}
.side-symbol{{
  position:absolute;z-index:4;right:7%;top:65px;width:78px;height:78px;
  display:flex;align-items:center;justify-content:center;font-size:58px;cursor:pointer
}}
.side-symbol.hidden{{display:none}}
.banner{{
  position:relative;z-index:6;margin:40px auto 0;width:min(100%,1050px);
  border-radius:18px;overflow:hidden;background:#dff8ff;
  box-shadow:0 14px 30px rgba(40,80,150,.20);
  animation:bannerIn .8s ease both
}}
.banner img{{display:block;width:100%;height:auto;max-height:330px;object-fit:cover}}
.banner-overlay{{
  position:absolute;inset:auto 0 0 0;height:34px;
  background:linear-gradient(transparent,rgba(0,0,0,.18));pointer-events:none
}}
.main{{min-height:calc(100vh - 520px);padding:70px 7% 120px;background:#f8faff}}
.menu{{
  max-width:680px;margin:0 auto;display:grid;grid-template-columns:repeat(3,1fr);
  gap:65px;animation:fadeUp .8s .2s both
}}
.menu-item{{text-align:center;cursor:pointer;transition:transform .25s}}
.menu-item:hover{{transform:translateY(-7px)}}
.menu-icon{{
  width:86px;height:86px;margin:auto;border-radius:19px;display:flex;
  align-items:center;justify-content:center;font-size:35px;transition:.25s
}}
.menu-item:nth-child(1) .menu-icon{{background:#eadcff;color:#a855e8}}
.menu-item:nth-child(2) .menu-icon{{background:#eedaff;color:#a943d7}}
.menu-item:nth-child(3) .menu-icon{{background:#ffdce6;color:#f2678d}}
.menu-item:hover .menu-icon{{transform:scale(1.07);box-shadow:0 12px 25px rgba(100,110,220,.18)}}
.menu-title{{margin-top:12px;font-size:11px;font-weight:700;color:#555}}
.floating{{
  position:fixed;right:28px;bottom:92px;width:60px;height:60px;border-radius:50%;
  background:#8189ed;color:#fff;display:flex;align-items:center;justify-content:center;
  font-size:24px;box-shadow:0 8px 20px rgba(100,110,220,.3);cursor:pointer;z-index:50
}}
.bottom-nav{{
  position:fixed;left:0;right:0;bottom:0;height:75px;background:rgba(255,255,255,.98);
  border-top:1px solid #ececf1;box-shadow:0 -4px 20px rgba(50,60,100,.04);
  display:flex;justify-content:center;align-items:center;gap:7%;z-index:40
}}
.nav-item{{width:50px;text-align:center;color:#aaa;cursor:pointer;transition:.2s}}
.nav-item:hover{{color:#777;transform:translateY(-3px)}}
.nav-icon{{font-size:22px}}
.nav-label{{display:block;margin-top:4px;font-size:8px}}
.active-circle{{
  width:48px;height:48px;margin:auto;border-radius:50%;background:#8189ed;color:#fff;
  display:flex;align-items:center;justify-content:center;font-size:20px;
  box-shadow:0 7px 18px rgba(110,120,230,.25)
}}
.toast{{
  position:fixed;left:50%;bottom:100px;transform:translate(-50%,20px);
  padding:11px 22px;background:#333;color:#fff;border-radius:30px;font-size:12px;
  opacity:0;pointer-events:none;z-index:100;transition:.3s
}}
.toast.show{{opacity:1;transform:translate(-50%,0)}}
.upload-hint{{
  position:absolute;right:6.7%;top:145px;z-index:5;font-size:9px;color:rgba(255,255,255,.75);
  display:none
}}
@keyframes bannerIn{{from{{opacity:0;transform:translateY(18px)}}to{{opacity:1;transform:translateY(0)}}}}
@keyframes fadeUp{{from{{opacity:0;transform:translateY(20px)}}to{{opacity:1;transform:translateY(0)}}}}
@media(max-width:700px){{
  .header{{min-height:390px;padding:42px 20px 30px}}
  .greeting h1{{font-size:22px}}
  .side-symbol,.side-image{{right:20px;top:60px;width:58px;height:58px}}
  .side-symbol{{font-size:43px}}
  .banner{{margin-top:30px;border-radius:12px}}
  .main{{padding:60px 20px 110px}}
  .menu{{gap:18px}}
  .menu-icon{{width:65px;height:65px;font-size:28px}}
  .menu-title{{font-size:9px}}
  .bottom-nav{{gap:3%}}
  .floating{{right:18px;bottom:90px}}
}}
</style>
</head>
<body>
<div class="app">

<header class="header">
  <div class="top">
    <div class="time" id="time">00:00:00</div>
  </div>

  <div class="greeting">
    <h1 id="greeting">Hallo, Selamat Malam!</h1>
    <p>"Ilmu bukanlah apa yang dihafal, akan tetapi yang bermanfaat."</p>
  </div>

  <!--
    Klik ikon di kanan atas untuk mengganti dengan foto/gambar sendiri.
    Foto hanya tersimpan di browser saat halaman sedang dibuka.
  -->
  <div class="side-symbol" id="sideSymbol" title="Klik untuk mengganti foto">🌙</div>
  <img class="side-image" id="sideImage" alt="Foto pilihan">

  <input id="imagePicker" type="file" accept="image/*" hidden>

  <!-- Banner dari gambar yang kamu kirim -->
  <div class="banner">
    <img src="data:image/png;base64,{b64}" alt="Banner Keep Calm and Study Hard">
    <div class="banner-overlay"></div>
  </div>
</header>

<main class="main">
  <div class="menu">
    <div class="menu-item" onclick="showToast('Scan QRCode')">
      <div class="menu-icon">▦</div>
      <div class="menu-title">SCAN QRCODE</div>
    </div>

    <div class="menu-item" onclick="showToast('Masuk URL')">
      <div class="menu-icon">▤</div>
      <div class="menu-title">MASUK URL</div>
    </div>

    <div class="menu-item" onclick="showToast('E-Ujian')">
      <div class="menu-icon">▣</div>
      <div class="menu-title">E-UJIAN</div>
    </div>
  </div>
</main>

<div class="floating" onclick="showToast('Dashboard')">◇</div>

<nav class="bottom-nav">
  <div class="nav-item" onclick="showToast('Profile')">
    <div class="nav-icon">◎</div><span class="nav-label">Profile</span>
  </div>
  <div class="nav-item" onclick="showToast('Dokumen')">
    <div class="nav-icon">▱</div><span class="nav-label">Dokumen</span>
  </div>
  <div class="nav-item">
    <div class="active-circle">◇</div><span class="nav-label">Dashboard</span>
  </div>
  <div class="nav-item" onclick="showToast('Setting')">
    <div class="nav-icon">⚙</div><span class="nav-label">Setting</span>
  </div>
  <div class="nav-item" onclick="showToast('Exit')">
    <div class="nav-icon">⇥</div><span class="nav-label">Exit</span>
  </div>
</nav>

<div class="toast" id="toast"></div>
</div>

<script>
const timeEl = document.getElementById("time");
const greetingEl = document.getElementById("greeting");
const sideSymbol = document.getElementById("sideSymbol");
const sideImage = document.getElementById("sideImage");
const imagePicker = document.getElementById("imagePicker");

function updateThemeByTime() {{
  const now = new Date();
  const hour = now.getHours();

  timeEl.textContent =
    String(hour).padStart(2,"0") + ":" +
    String(now.getMinutes()).padStart(2,"0") + ":" +
    String(now.getSeconds()).padStart(2,"0");

  if (hour >= 5 && hour < 11) {{
    greetingEl.textContent = "Hallo, Selamat Pagi!";
    if (!sideImage.classList.contains("show")) sideSymbol.textContent = "☀️";
  }} else if (hour >= 11 && hour < 15) {{
    greetingEl.textContent = "Hallo, Selamat Siang!";
    if (!sideImage.classList.contains("show")) sideSymbol.textContent = "☀️";
  }} else if (hour >= 15 && hour < 18) {{
    greetingEl.textContent = "Hallo, Selamat Sore!";
    if (!sideImage.classList.contains("show")) sideSymbol.textContent = "🌤️";
  }} else {{
    greetingEl.textContent = "Hallo, Selamat Malam!";
    if (!sideImage.classList.contains("show")) sideSymbol.textContent = "🌙";
  }}
}}

updateThemeByTime();
setInterval(updateThemeByTime, 1000);

/* Klik gambar bulan/matahari untuk memilih foto/gambar sendiri */
sideSymbol.addEventListener("click", () => imagePicker.click());
sideImage.addEventListener("click", () => imagePicker.click());

imagePicker.addEventListener("change", (event) => {{
  const file = event.target.files[0];
  if (!file) return;

  const reader = new FileReader();

  reader.onload = (e) => {{
    sideImage.src = e.target.result;
    sideImage.classList.add("show");
    sideSymbol.classList.add("hidden");
  }};

  reader.readAsDataURL(file);
}});

let toastTimer;

function showToast(message) {{
  const toast = document.getElementById("toast");
  toast.textContent = message;
  toast.classList.add("show");

  clearTimeout(toastTimer);
  toastTimer = setTimeout(() => {{
    toast.classList.remove("show");
  }}, 1300);
}}
</script>

</body>
</html>
"""

out = Path("/mnt/data/DASHBOARD.html")
out.write_text(html_content, encoding="utf-8")
print(out)
