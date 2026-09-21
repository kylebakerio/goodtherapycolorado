# Good Therapy Colorado — Website Migration Guide

A clean, modern, zero-dependency static reconstruction of **[goodtherapycolorado.com](https://www.goodtherapycolorado.com)**, completely decoupled from Wix and prepared for $0/month edge hosting on Cloudflare.

---

## 📊 Current State of the Project

### 1. Cloned Content & Structure
- **Pages Rebuilt**:
  - Homepage (`/index.html`)
  - About Me (`/about-me/index.html` and `/about-me.html`)
  - Contact (`/contact-3/index.html`, `/contact/index.html`, and `/contact-3.html`)
  - Frequently Asked Questions (`/faq/index.html` and `/faq.html`)
  - Blog Index (`/blog/index.html` and `/blog.html`)
- **All 6 Blog Articles Preserved**:
  - `post/boundaries-why-no-is-a-nice-word/`
  - `post/family-of-origin-are-you-becoming-your-parents/`
  - `post/communication-the-heart-of-human-relationships/`
  - `post/mindfulness-not-just-for-hippies/`
  - `post/healing-from-past-trauma-a-journey-toward-recovery/`
  - `post/core-values-as-fun-as-an-internet-quiz-only-more-helpful/`
- **100% SEO Preservation**: All URL paths and slugs exactly mirror the original Wix site so Google rankings, indexed pages, and external backlinks remain intact.
- **Structured Data & SEO**: Included OpenGraph tags, Twitter cards, canonical tags, `robots.txt`, `sitemap.xml`, and JSON-LD `MedicalBusiness` schema.

---

### 2. Media & Performance
- **Original Photo Assets**: All 24 original images downloaded at raw camera resolution and preserved in `assets/originals/` (136 MB).
- **Web-Optimized Assets**: Optimized production images saved to `assets/images/` (total site weight reduced from 136 MB to ~4.3 MB for <100ms load times).
- **Hero Background Video**:
  - Desktop 720p: [`assets/video/hero-mountains.mp4`](assets/video/hero-mountains.mp4) (7.4 MB)
  - Mobile 480p: [`assets/video/hero-mountains-mobile.mp4`](assets/video/hero-mountains-mobile.mp4) (3.0 MB)
- **Intelligent Lazy-Loading**:
  - **Instant Paint**: High-resolution mountain poster image displays immediately with zero layout shift.
  - **Connection Aware**: Inspects `navigator.connection` (`saveData` or slow 2G) and skips video download on metered or poor connections.
  - **Motion Aware**: Respects `prefers-reduced-motion: reduce`.
  - **Smooth Fade**: Uses `requestIdleCallback` to defer loading and smoothly fades the video in over 1 second once playback starts.

---

### 3. Forms & Mailing List
- **Why Wix APIs Cannot Be Used Off-Site**: Wix form endpoints (`/_api/wix-forms/...`) require active session cookies, CSRF tokens, and origin validation. Once the domain moves off Wix and the Wix subscription is canceled, those endpoints stop accepting data.
- **Client-Side Form Handlers**:
  - **Mailing List (Footer)**: Submits asynchronously to `/api/subscribe` with loading state, success message, and automatic backup into the visitor's `localStorage` (`gtc_subscribers`).
  - **Contact Form (`/contact-3/`)**: Submits asynchronously to `/api/contact` with loading state, confirmation message, and a pre-filled `mailto:goodtherapycolorado@gmail.com` fallback button.
- **Cloudflare Backend Functions Provided**:
  - [`functions/api/subscribe.js`](functions/api/subscribe.js) (Cloudflare Pages)
  - [`functions/api/contact.js`](functions/api/contact.js) (Cloudflare Pages)
  - [`_worker.js`](_worker.js) (Cloudflare Workers Static Assets router)
  - Ready to log submissions, store them in Cloudflare KV / D1, or forward them via webhooks/email.

---

### 4. Git & Deployment Status
- **Local Repo**: `/home/kyle/goodtherapycolorado` on branch `main`.
- **Remote Repo**: `git@github.com:kylebakerio/goodtherapycolorado.git`.
- **Live Preview URL**: [goodtherapycolorado.finesttype4325.workers.dev](https://goodtherapycolorado.finesttype4325.workers.dev/).

---

## 🗺️ Next Steps: Migration Roadmap

Follow this step-by-step checklist to finalize the migration and move the domain to Cloudflare:

### Phase 1: Deploy Video & API Backend to Cloudflare
Commit `3a3ffb9` added the video files and API handlers to Git. Ensure your Cloudflare Worker / Pages deployment has deployed the latest assets:

- If deploying via **Wrangler CLI**:
  ```bash
  cd /home/kyle/goodtherapycolorado
  npx wrangler deploy
  ```
- If deploying via **Cloudflare Pages (Git integration)**:
  - Any push to `main` automatically rebuilds and deploys the latest version.
  - Verify that `https://goodtherapycolorado.finesttype4325.workers.dev/assets/video/hero-mountains.mp4` returns HTTP 200.

---

### Phase 2: Form & Email Forwarding Setup
Decide where Kelly wants contact form submissions and mailing list signups to go:

#### Option A: Free Form Forwarding (Recommended — Zero Code)
Use **Web3Forms** or **Formspree** to forward submissions directly to `goodtherapycolorado@gmail.com`:
1. Get a free access key at [web3forms.com](https://web3forms.com/) (no account required).
2. Add your key to the form in `contact-3/index.html` or set it in the Cloudflare Worker.
3. Submissions will arrive directly in Kelly's Gmail inbox with spam filtering included.

#### Option B: Cloudflare KV Storage
Store subscribers in Cloudflare's free edge database:
1. In Cloudflare Dashboard > **Workers & Pages** > **KV** > Create namespace `GTC_DATA`.
2. Bind the namespace to your Worker/Pages project as `GTC_DATA`.
3. The `/api/subscribe` and `/api/contact` functions in `_worker.js` will automatically save entries.

#### Option C: Newsletter Tool
If Kelly actively sends email newsletters, plug in a free tool like **MailerLite** or **Mailchimp** (free for up to 500–1,000 subscribers) to manage the mailing list.

---

### Phase 3: Move DNS to Cloudflare (Zero Downtime)

> [!IMPORTANT]
> **Email Safety Confirmed**: An authoritative DNS audit confirmed that `goodtherapycolorado.com` has **no MX records** (the practice uses `goodtherapycolorado@gmail.com` directly). Changing DNS will **not interrupt email service**.

1. **Add Domain to Cloudflare**:
   - In [dash.cloudflare.com](https://dash.cloudflare.com/), click **Add a Domain**.
   - Enter `goodtherapycolorado.com` and select the **Free Plan**.
   - Cloudflare will scan existing DNS records. Verify all records match.
   - Cloudflare will assign two nameservers (e.g. `adam.ns.cloudflare.com` and `linda.ns.cloudflare.com`).
2. **Update Nameservers in Wix**:
   - Log into Wix > **Domains** > click `...` next to `goodtherapycolorado.com` > **Manage DNS** > **Change Nameservers**.
   - Select **Use other nameservers** and enter the two Cloudflare nameservers.
3. **Attach Domain in Cloudflare**:
   - Go to your Worker / Pages project > **Custom Domains** > **Set up a domain**.
   - Add `goodtherapycolorado.com` and `www.goodtherapycolorado.com`.
   - Cloudflare will automatically provision a free SSL certificate.
4. **Verify**:
   - Visit `https://goodtherapycolorado.com` to verify the new static site is serving securely.

---

### Phase 4: Transfer Domain Registrar to Cloudflare

After DNS is pointing to Cloudflare and the site is confirmed working:

1. **Unlock Domain in Wix**:
   - Wix Dashboard > **Domains** > click `...` next to `goodtherapycolorado.com` > **Transfer Away from Wix**.
   - Ensure the domain lock is set to **Unlocked**.
   - Copy the **EPP / Authorization Transfer Code**.
2. **Initiate Transfer in Cloudflare**:
   - In Cloudflare Dashboard, go to **Domain Registration** > **Transfer Domains**.
   - Select `goodtherapycolorado.com`.
   - Enter the EPP / Auth code and confirm registrant details.
   - Pay the ICANN wholesale transfer fee (~$10/year vs Wix's $25+/year). This extends registration by 1 full year.
3. **Confirm Transfer**:
   - Check the registrant email account for a transfer authorization email and click **Approve**.

---

### Phase 5: Cancel Wix Subscription
Once:
1. `goodtherapycolorado.com` is verified live on Cloudflare.
2. The domain shows as **Active** under Cloudflare Registrar.
3. Go to Wix > **Subscriptions & Billing** and cancel the Wix website hosting plan.

---

## 💻 Local Development & Maintenance

### Preview Locally
```bash
cd /home/kyle/goodtherapycolorado
python3 -m http.server 8000
```
Open `http://localhost:8000` in your browser.

### Modify Content or Blog Posts
- Blog post data and structure are stored in [`content/posts_detailed.json`](content/posts_detailed.json).
- Page templates and generators are located in [`build.py`](build.py).
- To regenerate all static files after making changes:
  ```bash
  python3 build.py
  ```
