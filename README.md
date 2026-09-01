# Flourish! — Artisan Craft Bakery · Islamabad 🥐✨

[![Deploy to GitHub Pages](https://github.com/maanjk/flourish-craft-bakery/actions/workflows/deploy.yml/badge.svg)](https://github.com/maanjk/flourish-craft-bakery/actions/workflows/deploy.yml)
[![Live Demo](https://img.shields.io/badge/Live_Demo-Visit_Bakery-FF5E7A?style=flat&logo=safari&logoColor=white)](https://maanjk.github.io/flourish-craft-bakery/)
[![License: MIT](https://img.shields.io/badge/License-MIT-F7B733.svg)](LICENSE)

> Handcrafted sourdough, 27-layer French butter croissants, bespoke celebration cakes & artisanal cookies — slow-fermented and baked fresh every morning in **I-16 Markaz, Islamabad**.

---

## 🌟 Highlights & Features

### 🛒 Interactive Shopping Bag & Direct WhatsApp Ordering
- **Real-Time Bag Drawer**: Slide-out cart drawer with live badge counter, itemized summary, and persistent storage.
- **Item Adjustments**: Add items via `+` buttons on any dish, adjust quantities, or remove items.
- **Fulfillment Selector**: Toggle between **Store Pickup (I-16 Markaz)** and **Express Delivery (Islamabad & Rawalpindi)** with automated subtotal and delivery fee calculations.
- **1-Click WhatsApp Checkout**: Auto-generates a structured order with timestamps, quantities, items, and total in PKR (Rs.) sent directly to the bakery's WhatsApp.

### 🔍 Menu Instant Search & Dietary Filtering
- **Live Search**: Instant debounced search filtering by bake name, ingredients, or description.
- **Dietary Filter Chips**: One-click filters for **All Items**, **⭐ Bestsellers**, **🌱 Vegetarian/Vegan**, and **✨ New In**.
- **Category Tabs**: Switch between Breads, Pastries, Cakes, and Cookies with smooth transition animations.

### 🖼️ Photo Lightbox & Bakery Showcase
- **Click-to-Zoom Lightbox**: High-resolution gallery modal with captions and keyboard/touch dismissal.
- **Floating Product Cutouts**: Optimized, defringed PNG assets floating over animated marquee banners.

### 🥖 Bakery FAQs & Bread Care Guide
- **Care & Reheat Instructions**: How to preserve and revive artisan stone-baked sourdough crusts.
- **Custom Cake Timelines**: Ordering guidance for tiered celebration and wedding cakes.
- **Delivery & Payment Info**: Coverage zones across Islamabad/Rawalpindi and supported payment methods (COD, Raast, JazzCash, EasyPaisa, Bank Transfer).

### 🚀 SEO & Performance Engineered
- **Schema.org JSON-LD**: Comprehensive `Bakery` schema markup for local search discovery.
- **Social Sharing Previews**: Complete Open Graph and Twitter Card tags.
- **Zero Heavy Frameworks**: Pure vanilla HTML5, CSS3, and modern JavaScript for blazing-fast 100/100 Lighthouse performance.

---

## 📂 Project Structure

```text
ba/
├── .github/
│   └── workflows/
│       └── deploy.yml        # Automated GitHub Pages deployment
├── images/
│   ├── cutout/               # Transparent defringed product cutouts
│   │   ├── float-cinnamon.png
│   │   ├── float-cookie.png
│   │   ├── float-croissant.png
│   │   ├── float-cupcake.png
│   │   └── float-sourdough.png
│   ├── cake-signature.jpg
│   ├── cinnamon-rolls.jpg
│   ├── cookies.jpg
│   ├── croissant.jpg
│   ├── interior.webp
│   ├── pastries.jpg
│   └── sourdough.jpg
├── .gitignore                # Git ignore rules
├── cutout.py                 # Background removal & asset processing script
├── index.html                # Single-page web application
└── README.md                 # Project documentation
```

---

## 💻 Local Development Setup

No complex build tools or `npm install` needed! You can run and test the website locally using any static web server:

### Python 3
```bash
python -m http.server 8000
```
Open `http://localhost:8000` in your web browser.

### Node.js (npx serve)
```bash
npx serve .
```

### VS Code Live Server
Right-click `index.html` and click **"Open with Live Server"**.

---

## 🌐 Hosting on GitHub & GitHub Pages

To host this website for free on **GitHub Pages**:

### 1. Initialize Git & Commit
```bash
git init
git add .
git commit -m "feat: complete Flourish Artisan Bakery website"
```

### 2. Create a GitHub Repository & Push
1. Go to [GitHub New Repository](https://github.com/new).
2. Name your repository (e.g., `flourish-craft-bakery`).
3. Push your local code:
```bash
git remote add origin https://github.com/<YOUR_USERNAME>/<YOUR_REPO_NAME>.git
git branch -M main
git push -u origin main
```

### 3. Enable GitHub Pages
1. In your GitHub repository, navigate to **Settings** > **Pages**.
2. Under **Build and deployment** > **Source**, select **GitHub Actions** (or select **Deploy from a branch** -> `main` / `/ (root)`).
3. Your website will be live at `https://<YOUR_USERNAME>.github.io/<YOUR_REPO_NAME>/`! 🎉

---

## 📍 Bakery Location & Contact

- **Location:** Shop No 18 & 19, Deans Arcade, I-16 Markaz (East), Islamabad, Pakistan
- **Phone / WhatsApp:** +92 346 55556677
- **Hours:** Mon–Fri: 8:00 AM – 10:00 PM | Sat–Sun: 9:00 AM – 11:00 PM
- **Instagram / Socials:** `@flourishbakery.pk`

---

## 📄 License
This project is open source and available under the [MIT License](LICENSE).
