# TOMA — Paid Ads Email Designs (Options F & G)

Two B2B emails selling TOMA's paid-acquisition service to peptide brands, each in two design directions.

| | Option F — Red Signal (dark) | Option G — Silver Light |
|---|---|---|
| **Email 1** — Growth Beyond Affiliates | [HTML](emails/email-1-growth-beyond-affiliates-option-f.html) · [preview](previews/email-1f-preview.png) | [HTML](emails/email-1-growth-beyond-affiliates-option-g.html) · [preview](previews/email-1g-preview.png) |
| **Email 2** — Keep More of the Sale | [HTML](emails/email-2-keep-more-of-the-sale-option-f.html) · [preview](previews/email-2f-preview.png) | [HTML](emails/email-2-keep-more-of-the-sale-option-g.html) · [preview](previews/email-2g-preview.png) |

- **Email 1** subject: *Your next customer shouldn’t depend on an influencer posting.*
- **Email 2** subject: *More revenue. But how much are you keeping?*

Copy follows the TOMA-B1-01 and TOMA-B1-02 briefs word for word. Typeface: DM Sans (TOMA brand). Email 1 and Email 2 use separate asset sets (only the logo is shared).

## Structure

```
emails/                 Ready-to-send HTML (600px, table-based, Outlook-safe)
  images/slices/        Image slices each email is built from
  images/cut/ gen/ ...  Source assets (transparent cutouts, textures, icons, logos)
src/designs/            Design canvases (one long 600px page per email) + slicer
previews/               Full-page PNG previews
figma-import/           All four emails on one board, for html.to.design / Figma import
```

## How the emails are built

Each email is designed as a single continuous canvas in `src/designs/*.html`, so glows, gradients and products can flow across section edges. `build.py` renders the canvas at 2x in headless Chrome, cuts it into slices at the section boundaries, and writes the email HTML. Buttons are linked image slices; the footer (contact, policy links, unsubscribe) stays live HTML.

Rebuild one email after editing its canvas:

```bash
cd src/designs
python3 build.py "$PWD/e1-f.html" "$PWD/../../emails/email-1-growth-beyond-affiliates-option-f.html" e1f "Your next customer shouldn’t depend on an influencer posting." "Less affiliate dependence. Compliance-led creative. Measurable returns." "#0A0909"
```

Requires Python 3 with Pillow and Google Chrome (set `CHROME=/path/to/chrome` if it isn’t in the default macOS location).

## Before sending

- Replace footer placeholders: `[Business address]`, `[ABN]`, `{{privacy_policy_url}}`, `{{preferences_url}}`, `{{unsubscribe_url}}`.
- Host `emails/images/` on your ESP or CDN and update image paths to absolute URLs.
- ROAS “3–6x” is shown as an illustrative target range with a caveat line; vial packaging is fictional “YOUR BRAND” artwork, not client work or a Meta approval.
- Links point to `tomaau.com` with UTM tags (`toma_b1_01_f`, `toma_b1_02_g`, …).

## Figma

Open `figma-import/toma-email-board.html` in Chrome and import it with the html.to.design extension (or plugin) to get editable layers.
