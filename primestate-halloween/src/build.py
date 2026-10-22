"""Slice a design canvas into an email.
usage: python3 build.py <design.html> <out_email.html> <slice_prefix> <title> <preheader> <outer_bg>
"""
import json, os, re, subprocess, sys, tempfile, html as H
from PIL import Image

CHROME = os.environ.get("CHROME", "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome")
design, out_email, prefix, title, preheader, outer = sys.argv[1:7]
ROOT = os.path.dirname(os.path.abspath(out_email))
SL = os.path.join(ROOT, "images", "slices")
os.makedirs(SL, exist_ok=True)

def chrome(args, timeout=90):
    prof = tempfile.mkdtemp(prefix="sliceprof")
    base = [CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", f"--user-data-dir={prof}", "--no-first-run",
            "--allow-file-access-from-files", "--virtual-time-budget=6000"]
    for _ in range(3):
        try:
            return subprocess.run(base + args, capture_output=True, text=True, timeout=timeout).stdout
        except subprocess.TimeoutExpired:
            continue
    raise SystemExit("chrome timed out")

dom = chrome(["--window-size=600,1000", "--dump-dom", f"file://{design}#dump"])
m = re.search(r'<pre id="__out">(.*?)</pre>', dom, re.S)
if not m: raise SystemExit("no dump output")
data = json.loads(H.unescape(m.group(1)))
total = int(round(data["total"]))
shot = os.path.join(tempfile.mkdtemp(), "full.png")
chrome(["--force-device-scale-factor=2", f"--window-size=600,{total}", f"--screenshot={shot}", f"file://{design}"])
full = Image.open(shot).convert("RGB")

FONT = "'Montserrat',Helvetica,Arial,sans-serif"
rows = []
n = 0
for it in data["items"]:
    if it["h"] < 1: continue
    if it["type"] == "img":
        y0, y1 = int(round(it["y"] * 2)), int(round((it["y"] + it["h"]) * 2))
        crop = full.crop((0, y0, 1200, min(y1, full.height)))
        n += 1
        fn = f"{prefix}-{n:02d}-{it['name']}.jpg"
        crop.save(os.path.join(SL, fn), quality=84, optimize=True, progressive=True)
        h = round(crop.height / 2)
        tag = f'<img class="full" src="images/slices/{fn}" width="600" height="{h}" alt="{H.escape(it["alt"])}" style="width:600px;height:auto;display:block;border:0;">'
        if it["href"]: tag = f'<a href="{H.escape(it["href"])}" target="_blank">{tag}</a>'
        bg = it["bg"] or "#FFFFFF"
        rows.append(f'  <tr><td style="background:{bg};font-size:0;line-height:0;">{tag}</td></tr>')
    elif it["kind"] == "button":
        bb = it["btnbg"] or "#BD2629"; bc = it["btncolor"] or "#FFFFFF"; lab = it["label"]; href = H.escape(it["href"])
        note = (f'<p style="margin:14px 0 0;font-family:{FONT};font-size:13px;line-height:18px;color:{it["notecolor"] or "#8A857E"};">{it["note"]}</p>' if it["note"] else "")
        rows.append(f'''  <tr><td align="center" style="background:{it["bg"]};padding:{it["pad"]};">
    <table role="presentation" align="center" cellpadding="0" cellspacing="0" border="0" style="border-collapse:separate;"><tr><td align="center" bgcolor="{bb}" style="border-radius:999px;background:{bb};">
      <!--[if mso]><v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" href="{href}" style="height:56px;v-text-anchor:middle;width:270px;" arcsize="50%" stroke="f" fillcolor="{bb}"><w:anchorlock/><center style="color:{bc};font-family:Arial,sans-serif;font-size:17px;font-weight:bold;">{lab} &rarr;</center></v:roundrect><![endif]-->
      <!--[if !mso]><!--><a href="{href}" target="_blank" style="display:inline-block;padding:18px 40px;font-family:{FONT};font-size:17px;line-height:20px;font-weight:700;color:{bc};border-radius:999px;text-decoration:none;">{lab} &nbsp;&rarr;</a><!--<![endif]-->
    </td></tr></table>{note}
  </td></tr>''')
    else:  # live text
        rows.append(f'  <tr><td class="px" style="background:{it["bg"]};padding:{it["pad"]};">{it["html"]}</td></tr>')

doc = f'''<!DOCTYPE html>
<html lang="en" xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="x-apple-disable-message-reformatting">
<meta name="format-detection" content="telephone=no, date=no, address=no, email=no">
<meta name="color-scheme" content="light">
<meta name="supported-color-schemes" content="light">
<title>{H.escape(title)}</title>
<!--[if mso]><noscript><xml><o:OfficeDocumentSettings><o:PixelsPerInch>96</o:PixelsPerInch></o:OfficeDocumentSettings></xml></noscript><![endif]-->
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
  body{{margin:0!important;padding:0!important;width:100%!important;background:{outer}}}
  table{{border-collapse:collapse;mso-table-lspace:0;mso-table-rspace:0}}
  img{{border:0;outline:none;text-decoration:none;-ms-interpolation-mode:bicubic;display:block}}
  a{{text-decoration:none}}
  @media screen and (max-width:620px){{ .wrap{{width:100%!important}} .full{{width:100%!important;height:auto!important}} .px{{padding-left:20px!important;padding-right:20px!important}} }}
</style>
</head>
<body style="margin:0;padding:0;background:{outer};">
<div style="display:none;max-height:0;overflow:hidden;mso-hide:all;font-size:1px;line-height:1px;color:{outer};">{H.escape(preheader)}{"&#8199;&#847;" * 18}</div>
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background:{outer};"><tr><td align="center" style="padding:24px 0;">
<!--[if mso]><table role="presentation" width="600" cellpadding="0" cellspacing="0" border="0"><tr><td><![endif]-->
<table role="presentation" class="wrap" width="600" cellpadding="0" cellspacing="0" border="0" style="width:600px;max-width:600px;">
{chr(10).join(rows)}
</table>
<!--[if mso]></td></tr></table><![endif]-->
</td></tr></table>
</body>
</html>
'''
open(out_email, "w").write(doc)
print("slices:", n, "rows:", len(rows), "height:", total)
