# Socialorbit Technologies — static site

A pure HTML/CSS/JS build of the approved homepage design (Electric Violet / Modern SaaS). No build step and no framework. Open `index.html` directly or serve the folder from any static host.

## Structure

```
index.html        Homepage
css/site.css      Shared stylesheet (every page links it). Brand tokens are in :root
js/site.js        Shared script: mobile menu, active nav, scroll reveal, placeholder forms
img/favicon.svg   Placeholder logo mark
bust-cache.py     Content-hash cache-busting (run after editing CSS/JS)
```

## Adding a page

1. Copy `index.html` and rename it, e.g. `services.html`.
2. Keep the `<header>` and `<footer>` blocks as they are.
3. Set `<body data-page="services">`. The nav link with the matching `data-nav` gets `aria-current="page"` automatically. Values: `services`, `solutions`, `audit`, `about`, `contact`.
4. Replace the `<main>` content. Interior pages should use a breadcrumb plus a title band, not the homepage hero.
5. When the page exists locally, change that nav/footer link from `https://socialorbit.net/...` to the local file **in every page**.
6. Run `python3 bust-cache.py`.

### Nav & footer

They are **duplicated per page**, which suits a small `file://`-safe static site. If the site grows past about 8 pages, switch to partials with a build script. Use one approach for the whole site, not both.

## Before launch: checklist

- [ ] **Forms are placeholders.** The audit form validates and shows a success message, but **nothing is sent**. Wire it to a real endpoint (CRM or form service) that delivers to **support@socialorbit.net**. See the `PLACEHOLDER` comment in `js/site.js`.
- [ ] **Remove `<meta name="robots" content="noindex, nofollow">`** from every page.
- [ ] Search the repo for `[PH]` and `PLACEHOLDER`, then confirm or replace each item:
  - Logo mark (SVG placeholder in the header, footer and favicon): swap in the real logo.
  - "sent within two business days" promise on the audit form.
  - The "Ace Roofing" chat demo. It is fictional and labelled "Example conversation" on the page.
  - "Full system" tag, plus the Growth Engine and Revenue Recovery bullet points (draft wording).
- [ ] The links to pages not built yet point to the live WordPress site. Check that `/privacy-policy/` is the correct privacy URL.
- [ ] Fonts load from Google Fonts (DM Sans and Outfit). Self-host them in `/fonts` if you want no outside dependencies.
- [ ] HTML caching: use `no-cache, must-revalidate` for HTML; the hashed CSS/JS can be cached long-term (`immutable`).

## Notes

- Copy comes from the current socialorbit.net. Nothing in it is invented proof such as stats, testimonials or client logos. The tools strip lists integrations, not clients.
- Every animation respects `prefers-reduced-motion`.
- Tested at 1440px, 900px and 390px. No horizontal overflow and no console errors.

## Staging deploy

Every push to `main` deploys to **https://socialorbit.net/staging/** via `.github/workflows/deploy-staging.yml` (FTPS to the WordPress host).

One-time setup in GitHub → Settings → Secrets and variables → Actions:

- Secrets: `FTP_SERVER` (e.g. `ftp.socialorbit.net`), `FTP_USERNAME`, `FTP_PASSWORD` (from the hosting cPanel → FTP Accounts)
- Variable (optional): `FTP_SERVER_DIR`, default `public_html/staging/`. If the FTP account is already rooted at `public_html`, set it to `staging/`.

Keep the `noindex` meta on staging pages.
