# balduin.me — Portfolio

A static portfolio site for [Balduin Allroggen](https://balduin.me) — game designer, solo developer, and 3D/2D artist.

Built with [Eleventy](https://www.11ty.dev/) (a static site generator), deployed free to [GitHub Pages](https://pages.github.com/) via GitHub Actions.

## Local development

```bash
# Install dependencies
npm install

# Start dev server with hot reload → http://localhost:8080
npm start

# Build production output → _site/
npm run build
```

No build watchers, no bundlers, no surprises. Just edit a `.md` file in `src/`, save, and the dev server refreshes.

## Project structure

```
.
├── src/                          # ← everything you edit lives here
│   ├── _data/
│   │   └── site.js              # site title, social links, nav order
│   ├── _includes/
│   │   ├── base.njk             # HTML shell (head, header, footer)
│   │   ├── header.njk           # site nav
│   │   ├── footer.njk           # email + socials
│   │   └── project.njk          # project page layout
│   ├── assets/
│   │   ├── css/style.css        # all styles
│   │   ├── favicon.png          # browser tab icon
│   │   └── images/              # all portfolio images
│   ├── projects/
│   │   ├── endstation.md
│   │   ├── next-level-pioneers.md
│   │   ├── a-planet-on-fire.md
│   │   └── romanesco.md
│   ├── index.md                  # homepage
│   ├── robots.txt                # search engine rules
│   └── sitemap.xml.njk           # sitemap
├── .eleventy.js                  # Eleventy config
├── .github/workflows/deploy.yml  # auto-deploy on push to main
├── package.json
└── README.md
```

## How to add a new project

Two places to edit — that's it.

**1. Add a Markdown file in `src/projects/`:**

```bash
cp src/projects/endstation.md src/projects/my-new-game.md
```

Edit the frontmatter:

```yaml
---
layout: project
title: My New Game
permalink: /projects/my-new-game/index.html
tagline: "One-line pitch — appears under the title in big text."
description: "Longer one-paragraph description — appears under the cover image."
hero: /assets/images/my-new-game-cover.png    # REQUIRED: the cover image
role: Solo Developer
year: 2026
status: In development
engine: Godot 4.4
platform: PC (Steam)
cta:
  - { label: "Play on Steam", url: "https://store.steampowered.com/app/..." }
  - { label: "Devlog",       url: "https://bsky.app/profile/..." }
gallery:
  - { src: /assets/images/my-new-game-screenshot-1.png, alt: "Gameplay shot 1" }
  - { src: /assets/images/my-new-game-screenshot-2.png, alt: "Gameplay shot 2" }
---

## Game Design

Your text here, in Markdown. Each `## H2` becomes a section in the project page.

## Game Art

More text.

## Project

Wrap-up text.
```

**2. Add a nav entry in `src/_data/site.js`:**

```js
navProjects: [
  { url: "/projects/endstation/",     label: "ENDSTATION",         slug: "endstation" },
  { url: "/projects/my-new-game/",     label: "My New Game",        slug: "my-new-game" },  // ← add this
  { url: "/projects/next-level-pioneers/", label: "Next Level Pioneers", slug: "nlp" },
  // ...
]
```

**3. Drop your images into `src/assets/images/`** (any name, jpg/png/webp).

**4. Commit and push:**

```bash
git add .
git commit -m "feat: add My New Game project"
git push
```

The GitHub Actions workflow will build and deploy to balduin.me in about 30 seconds.

## How to edit an existing project

Open the `.md` file in `src/projects/`, change the text, save. The dev server (`npm start`) will hot-reload. When you're happy:

```bash
git commit -am "Update ENDSTATION description"
git push
```

## How to edit the homepage

Open `src/index.md`. It's hand-coded HTML (game cards, sections) — edit the cards or text in place. For new sections, follow the existing pattern (`.section-title` + content).

## How to update your social links

Edit `src/_data/site.js`. The `social` object controls the footer. Update the email there too.

## Deployment

GitHub Actions automatically builds and deploys on every push to `main`. Check the **Actions** tab in the GitHub repo to see deploy status.

If you need to deploy manually, you can trigger the workflow from the Actions tab → "Run workflow".

### One-time setup (if forking or starting fresh)

In GitHub repo settings:
1. **Settings → Pages → Source → GitHub Actions**
2. Push to `main` to trigger the first deploy

## Tech

- **Eleventy 3.x** — static site generator
- **Nunjucks** — templating
- **Markdown** — content
- **Plain CSS** — styles (no framework, no preprocessor)
- **Space Grotesk** + **Inter** — Google Fonts (replacing the old Adobe Typekit)
- **GitHub Pages** — free hosting
- **GitHub Actions** — CI/CD

## License

Personal portfolio. All rights reserved by Balduin Allroggen.
