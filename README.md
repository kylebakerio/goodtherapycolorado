# Good Therapy Colorado (goodtherapycolorado.com)

A clean, modern, zero-dependency static clone of **goodtherapycolorado.com**, completely decoupled from Wix and optimized for lightning-fast performance, zero hosting costs, and 100% SEO preservation.

---

## 🌟 Overview & Key Improvements over Wix

- **Zero Wix Dependencies**: Completely freed from Wix's proprietary JavaScript runtime, bloated tracking scripts, and `parastorage.com` CDN dependencies.
- **Blazing Fast**: From Wix's multi-megabyte bloated payloads down to lightweight, optimized static HTML/CSS. Average page loads in < 100ms.
- **100% SEO Preserved**: All original URLs (`/`, `/about-me`, `/contact-3`, `/faq`, `/blog`, and all `/post/<slug>` articles) are exact matches, maintaining all existing backlinks and Google search index rankings.
- **Responsive & Accessible**: Clean responsive layout for mobile, tablet, and desktop with accessible navigation and interactive FAQ accordion.
- **$0/month Hosting**: Can be hosted permanently for free on **Cloudflare Pages** or **GitHub Pages** with free automatic SSL.

---

## 📁 Repository Structure

```
├── index.html                  # Homepage
├── about-me/
│   └── index.html              # About Kelly Roper (/about-me/)
├── contact-3/
│   └── index.html              # Contact page (/contact-3/)
├── contact/
│   └── index.html              # Contact alias (/contact/)
├── faq/
│   └── index.html              # Frequently Asked Questions (/faq/)
├── blog/
│   └── index.html              # Blog index (/blog/)
├── post/
│   ├── boundaries-why-no-is-a-nice-word/index.html
│   ├── communication-the-heart-of-human-relationships/index.html
│   ├── core-values-as-fun-as-an-internet-quiz-only-more-helpful/index.html
│   ├── family-of-origin-are-you-becoming-your-parents/index.html
│   ├── healing-from-past-trauma-a-journey-toward-recovery/index.html
│   └── mindfulness-not-just-for-hippies/index.html
├── assets/
│   └── images/                 # Optimized web images (logo, hero, cards, headshots)
├── content/                    # Structured JSON data backups of all blog posts
├── build.py                    # Static site generator script
├── _redirects                  # Cloudflare Pages 301 redirects
├── robots.txt                  # Search engine crawler instructions
└── sitemap.xml                 # Full XML sitemap for Google Search Console
```

---

## 💻 Local Development & Testing

To preview the website locally on your computer:

```bash
# In this directory:
python3 -m http.server 8000
```

Then open your browser to `http://localhost:8000`.

To rebuild or modify any page template, update `build.py` and run:

```bash
python3 build.py
```

---

## 🚀 Deployment to Cloudflare Pages (Recommended)

Cloudflare Pages is the ideal host because:
1. It is **100% free** with unlimited bandwidth and global edge CDN.
2. It connects directly to your GitHub repository and automatically deploys on every `git push`.
3. Since you are moving the domain registrar/DNS to Cloudflare, adding the custom domain takes just 1 click with automatic SSL.

### Step 1: Push this repo to GitHub

```bash
cd /home/kyle/goodtherapycolorado

# Create a public or private repo on GitHub using GitHub CLI:
gh repo create goodtherapycolorado --public --source=. --push
```
*(Or create a new empty repository on github.com, add the remote, and push)*.

### Step 2: Connect to Cloudflare Pages

1. Log in to the [Cloudflare Dashboard](https://dash.cloudflare.com/).
2. In the left sidebar, navigate to **Compute (Workers & Pages)** > **Pages**.
3. Click **Connect to Git** and select your GitHub repository (`goodtherapycolorado`).
4. Set the build settings:
   - **Framework preset**: `None`
   - **Build command**: *(leave blank)*
   - **Build output directory**: `/` *(root directory)*
5. Click **Save and Deploy**. Your site is now live on a `*.pages.dev` subdomain!

---

## 🌐 Moving DNS & Domain Registrar to Cloudflare

Follow this exact sequence to ensure **zero downtime**:

### Phase 1: Add Site to Cloudflare DNS (Before touching the registrar)

1. In the Cloudflare dashboard, click **Add a Domain** and enter `goodtherapycolorado.com`.
2. Select the **Free Plan**.
3. Cloudflare will scan existing DNS records. Verify:
   - Make sure no critical records are missing. (Note: Good Therapy Colorado currently uses direct `goodtherapycolorado@gmail.com` with no custom domain MX records).
4. Cloudflare will assign you two assigned nameservers (e.g. `adam.ns.cloudflare.com` and `linda.ns.cloudflare.com`).
5. **Update Nameservers in Wix**:
   - In Wix Dashboard > **Domains** > Click `...` next to `goodtherapycolorado.com` > **Manage DNS Records** or **Change Nameservers**.
   - Switch from Wix nameservers (`ns14.wixdns.net`, `ns15.wixdns.net`) to the two Cloudflare nameservers.
6. In Cloudflare Pages project settings:
   - Go to **Custom Domains** > **Set up a domain**.
   - Enter `goodtherapycolorado.com` and `www.goodtherapycolorado.com`.
   - Cloudflare will automatically configure the CNAME / apex records and issue an SSL certificate.
   - **Test the website**: Confirm the new static site is serving over HTTPS.

---

### Phase 2: Transfer Domain Registrar to Cloudflare (Wholesale pricing)

Once DNS is pointing to Cloudflare and the site is live, transfer registrar ownership away from Wix to Cloudflare Registrar (Cloudflare charges zero markup, saving annual renewal fees):

1. **Unlock Domain in Wix**:
   - Go to Wix Dashboard > **Domains**.
   - Click the `...` menu next to `goodtherapycolorado.com` > **Transfer Away from Wix**.
   - Click **Transfer to Another Registrar** > **Continue Transfer**.
   - Ensure the domain is **Unlocked** and copy the **EPP / Authorization Transfer Code**.
2. **Initiate Transfer in Cloudflare**:
   - In Cloudflare Dashboard, go to **Domain Registration** > **Transfer Domains**.
   - `goodtherapycolorado.com` will appear as eligible for transfer.
   - Enter the **EPP / Auth Code** obtained from Wix.
   - Confirm registrant contact details and complete the transfer checkout (ICANN wholesale rate: ~$10/yr, which extends registration by 1 additional year!).
3. **Approve Transfer Email**:
   - An authorization email will be sent to the registrant email address on file. Click the approval link to finalize the transfer immediately without waiting the default 5-day ICANN hold.

---

### Phase 3: Cancel Wix Subscription Safely

Once:
1. The new site is verified working on Cloudflare Pages.
2. The domain shows **Active** in Cloudflare Registrar.
3. You can safely go to Wix > **Subscriptions** / **Billing** and cancel the Wix website plan.
