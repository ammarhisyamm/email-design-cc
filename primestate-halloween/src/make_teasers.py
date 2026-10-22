"""Generate the two Prime State Halloween teaser design canvases (Singles/White and Bulk/Black).
Copy is taken verbatim from the Prime-State-Halloween-Designer-Briefs PDF, with the brand name set to Prime State.
Run: python3 make_teasers.py  -> writes teaser-white.html and teaser-black.html next to this file.
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
K = "../emails/images/kit"      # generated scene kit
I = "../emails/images"
SITE = "https://primestateaus.com"
FONT = "'Montserrat',Helvetica,Arial,sans-serif"


def utm(camp, content, path="/"):
    return f"{SITE}{path}?utm_source=omnisend&amp;utm_medium=email&amp;utm_campaign={camp}&amp;utm_content={content}"


def live(bg, pad, html):
    return f'<div class="live" data-kind="text" data-bg="{bg}" data-pad="{pad}">{html}</div>\n'


def p(t, size=17, lh=27, color="#E9E2C8", weight=500, mt=16, align="left", extra=""):
    return (f'<p style="margin:{mt}px 0 0;font-family:{FONT};font-size:{size}px;line-height:{lh}px;'
            f'font-weight:{weight};color:{color};text-align:{align};{extra}">{t}</p>')


def footer(camp):
    a = "color:#FF7A1A;text-decoration:underline;"
    return live("#000000", "40px 32px 44px", f"""
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td align="center" style="text-align:center;">
   <a href="{utm(camp,'footer_logo')}" target="_blank"><img src="images/logo-white.png" width="130" alt="Prime State" style="width:130px;height:auto;margin:0 auto;display:block;border:0;"></a>
   {p(f'Questions? <a href="mailto:primestatebusiness@gmail.com" style="color:#FF7A1A;font-weight:700;text-decoration:none;">primestatebusiness@gmail.com</a>', 13, 20, '#C9BFAE', 500, 18, 'center')}
   {p(f'<a href="{SITE}/policies/privacy-policy" style="{a}">Privacy Policy</a> &nbsp;|&nbsp; <a href="{SITE}/policies/shipping-policy" style="{a}">Shipping Policy</a> &nbsp;|&nbsp; <a href="{SITE}/policies/terms-of-service" style="{a}">Terms of Service</a>', 12, 19, '#8C8496', 500, 16, 'center')}
   {p('Research-grade peptides. Not for human or animal use.', 11.5, 17, '#8C8496', 500, 14, 'center')}
   {p(f'&copy;2026 Prime State. <a href="{{{{unsubscribe_url}}}}" style="{a}">Unsubscribe</a>', 11.5, 17, '#8C8496', 500, 6, 'center')}
  </td></tr></table>""")


def canvas(v):
    camp = v["camp"]
    cobwebs = (f'<img class="cw" src="{K}/ph-cobweb.png" style="left:-4px;top:-4px">'
               f'<img class="cw" src="{K}/ph-cobweb.png" style="right:-4px;top:-4px;transform:scaleX(-1)">')
    body = "".join(p(t, mt=(0 if i == 0 else 16)) for i, t in enumerate(v["body"]))
    badges = "".join(f'<div class="badge"><img src="{K}/badge{i+1}.png"><b>{t}</b></div>' for i, t in enumerate(
        ["Cold chain shipping", "Third party tested", "Research grade", "Secure &amp; discreet"]))
    return f"""<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="hw.css"></head><body><div id="email">
{live('#0E0718', '13px 20px', p(v['banner'], 12, 16, '#FF7A1A', 800, 0, 'center', 'letter-spacing:2.6px;text-transform:uppercase;'))}
 <div class="s" data-name="header" data-bg="#150B24" data-href="{utm(camp,'logo')}" data-alt="Prime State" style="height:150px;background:linear-gradient(#0E0718,#150B24)">
   <img class="abs" src="{I}/logo-bone.png" style="left:245px;top:12px;width:110px;z-index:4">
   <img class="abs" src="{K}/ph-candy.png" style="left:-10px;top:84px;width:620px;z-index:2">
 </div>
 <div class="s" data-name="headline" data-bg="#150B24" data-alt="{v['headline_alt']}" style="padding:30px 36px 10px;background:linear-gradient(#150B24,{v['sky']})">
   {cobwebs}
   <img class="abs" src="{K}/ph-bats.png" style="left:{v['bats_x']}px;top:6px;width:{v['bats_w']}px;opacity:{v['bats_o']};z-index:2">
   <div class="headline in" style="font-size:{v['hl_size']}px;line-height:{v['hl_lh']}px">{v['headline']}</div>
 </div>
 <div class="s" data-name="hero" data-bg="{v['sky']}" data-alt="{v['hero_alt']}" style="height:{v['hero_h']}px;background:{v['sky']} url({K}/{v['hero']}.jpg) center {v['hero_pos']}/600px auto no-repeat">
   <div class="abs" style="left:0;right:0;top:0;height:90px;background:linear-gradient({v['sky']},rgba(0,0,0,0))"></div>
   <div class="abs" style="left:0;right:0;bottom:0;height:120px;background:linear-gradient(rgba(21,11,36,0),#150B24)"></div>
 </div>
{live('#150B24', '30px 40px 10px', body)}
 <div class="s c" data-name="sign" data-bg="#150B24" data-alt="Hand-painted wooden sign: {v['sign_alt']}" style="height:360px">
   <div class="blob" style="left:180px;top:150px;width:240px;height:180px;background:#FF7A1A;opacity:.22"></div>
   <img class="abs" src="{K}/ph-sign.png" style="left:130px;top:0;width:340px;z-index:3">
   <div class="sign-txt" style="top:{v['sign_y']}px;font-size:{v['sign_size']}px;z-index:4">{v['sign']}</div>
 </div>
 <div class="s c" data-name="countdown" data-bg="#150B24" data-alt="Countdown {v['caption']}" style="height:373px">
   <img class="abs" src="{K}/ph-arch.jpg" style="left:20px;top:0;width:560px;border-radius:18px">
   <div class="abs" style="left:0;right:0;top:{v['digits_y']}px;z-index:4">
     <div class="digits"><div class="digit"><b>02</b><small>DAYS</small></div><div class="colon">:</div><div class="digit"><b>18</b><small>HRS</small></div><div class="colon">:</div><div class="digit"><b>36</b><small>MIN</small></div></div>
   </div>
 </div>
{live('#150B24', '4px 32px 0', p(v['caption'], 15, 20, '#F5EFE6', 700, 0, 'center', 'letter-spacing:2px;text-transform:uppercase;'))}
{live('#150B24', '28px 44px 8px', p(v['contacts'], 15, 23, '#C9BFAE', 500, 0, 'center'))}
 <div class="s" data-name="badges" data-bg="#150B24" data-alt="Cold chain shipping. Third party tested. Research grade. Secure and discreet." style="padding:30px 24px 30px">
   <div class="cc in" style="margin:0 8px 26px;border-radius:6px;background:linear-gradient(90deg,#FFF4E0 0 33%,#FF7A1A 33% 66%,#F5D547 66%);-webkit-mask:repeating-linear-gradient(90deg,#000 0 18px,transparent 18px 26px);height:10px"></div>
   <div class="badges in">{badges}</div>
 </div>
{live('#150B24', '18px 40px 44px', p(v['signoff'], 16, 25, '#E9E2C8', 500, 0) + p(v['ps'], 15, 23, '#FF7A1A', 600, 18))}
{footer(camp)}
</div><script src="kit.js"></script></body></html>
"""


WHITE = dict(
    camp="ps_halloween_teaser_singles",
    banner="Something is stirring &middot; Opens Monday",
    headline="Something is <em>stirring</em><br>in the castle.",
    headline_alt="SOMETHING IS STIRRING IN THE CASTLE.",
    hl_size=58, hl_lh=60, sky="#1B0F33", bats_x=330, bats_w=280, bats_o=.9,
    hero="ph-hero-gates", hero_h=840, hero_pos="bottom",
    hero_alt="Locked black iron castle gates chained shut on a moonlit hill, one tower window glowing orange, bats leaving the tower across a huge full moon, jack-o-lanterns either side of the gate and fog on the path.",
    body=["Hey {{first_name}},",
          "A Halloween sale opens on Monday. It is a limited-time sale and it ends on Halloween night.",
          "You are on the list, so you get the first look. Keep an eye on your inbox on Monday morning.",
          "First in, best dressed. Popular products tend to go first once a sale is live."],
    sign="Knock if you dare.<br>Opens Monday.", sign_alt="Knock if you dare. Opens Monday.", sign_y=104, sign_size=31,
    caption="until the gates open", digits_y=132,
    contacts="Add Prime State to your contacts so Monday&rsquo;s email lands in your inbox.",
    signoff="Happy Halloween,<br>Tiana from Prime State",
    ps="P.S. Costume optional. Code arrives Monday.",
)
BLACK = dict(
    camp="ps_halloween_teaser_bulk",
    banner="The cellar opens Monday &middot; Bulk Halloween sale",
    headline="The cellar opens<br><em>Monday.</em>",
    headline_alt="THE CELLAR OPENS MONDAY.",
    hl_size=62, hl_lh=62, sky="#170C2B", bats_x=420, bats_w=170, bats_o=.75,
    hero="ph-hero-cellar", hero_h=840, hero_pos="bottom",
    hero_alt="Heavy iron-bound oak cellar doors chained shut at the base of a gothic castle, cartons and vials visible as dark silhouettes behind the bars, orange glow leaking through the cracks, a jack-o-lantern either side and a full moon above.",
    body=["Hi {{first_name}},",
          "A Halloween sale for bulk orders opens on Monday. It is limited time and ends on Halloween night.",
          "If you are planning a restock this month, Monday is worth waiting for. You are on the list, so you see it first.",
          "Same tested batches and consistent supply, with a COA on every product page."],
    sign="Restock night.<br>Opens Monday.", sign_alt="Restock night. Opens Monday.", sign_y=104, sign_size=31,
    caption="until the cellar opens", digits_y=132,
    contacts="Need a custom quantity ready to go? Reply and I will set it up for Monday.",
    signoff="Happy Halloween,<br>Tiana from Prime State",
    ps="P.S. Costume optional. Code arrives Monday.",
)

if __name__ == "__main__":
    for name, v in [("teaser-white.html", WHITE), ("teaser-black.html", BLACK)]:
        open(os.path.join(HERE, name), "w").write(canvas(v))
        print("wrote", name)
