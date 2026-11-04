# python3 shoot.py site/index.html out/d 1440 900 "top,how:0.2,how:0.8,live,fees,token,faq,footer"
# Section ids, "id:frac" for pinned sections (0..1 through the pin), "top" and "footer". Fonts load from ./node_modules.
import sys, pathlib
from playwright.sync_api import sync_playwright
page, pre, w, h, shots = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), sys.argv[5].split(",")
nm = (pathlib.Path(__file__).resolve().parent / "node_modules/@fontsource").as_uri()
fonts = "".join(f'@font-face{{font-family:"JetBrains Mono";font-weight:{wt};src:url({nm}/jetbrains-mono/files/jetbrains-mono-latin-{wt}-normal.woff2)}}' for wt in (400,500,600,700))
fonts += f'@font-face{{font-family:"Silkscreen";src:url({nm}/silkscreen/files/silkscreen-latin-400-normal.woff2)}}'
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={"width": w, "height": h}); errs = []
    pg.on("pageerror", lambda e: errs.append(str(e)))
    pg.goto(pathlib.Path(page).resolve().as_uri()); pg.add_style_tag(content=fonts + "html{scroll-behavior:auto!important}")
    pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(1500); pg.evaluate("dispatchEvent(new Event('resize'))")
    for sh in shots:
        sec, frac = (sh.split(":") + ["0"])[:2]
        if sec == "top": pg.evaluate("scrollTo(0,0)")
        elif sec == "footer": pg.evaluate("scrollTo(0,document.body.scrollHeight)")
        else: pg.evaluate(f"(()=>{{const r=document.getElementById('{sec}').getBoundingClientRect();const span=Math.max(0,r.height-innerHeight);scrollTo(0,r.top+scrollY+span*{frac}-(span?0:20))}})()")
        pg.wait_for_timeout(900); pg.screenshot(path=f"{pre}_{sec}_{frac}.png")
    print("errors:", errs, "scrollWidth:", pg.evaluate("document.documentElement.scrollWidth"), "w:", w)
    b.close()
