# Harbor

A website for families facing cancer, dedicated to the memory of Elyse Spurgeon.

The site is one page, `index.html`, with no build step. Alongside it:

- `favicon.svg`: the browser-tab icon
- `og-image.png`: the 1200×630 preview shown when the link is shared on social media or in messages
- `sitemap.xml` and `robots.txt`: help search engines find the page

## SEO built in

- Descriptive title, meta description and canonical URL
- Open Graph and Twitter card tags for link previews
- Structured data (JSON-LD) describing the organisation, the website and the FAQ, so search results can show FAQ answers
- One `h1`, ordered headings, landmarks, skip link and labelled forms
- Fonts preconnected and loaded with `display=swap`; no images to slow the first paint

If Harbor gets its own domain, update the canonical, `og:url`, `og:image` and JSON-LD URLs in `index.html` and the URL in `sitemap.xml`, and move `robots.txt` to the domain root. Then submit the sitemap in Google Search Console.

## Before launch

- Replace every `[PLACEHOLDER]` in square brackets (helpline number, hours, support email, group times and venues, Elyse's years and a few words about her).
- Connect the "Save a seat" form to a form service (for example Formspree or Google Forms). Today it only shows a thank-you message and sends nothing.

## Hosting

Turn on GitHub Pages for this repository (Settings → Pages → Source: Deploy from a branch → pick the branch that holds this folder, folder `/ (root)`). The site is then at `https://dookdog.github.io/tare/harbor/`.
