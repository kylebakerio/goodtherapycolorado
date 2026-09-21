#!/usr/bin/env python3
"""
Static Site Generator for Good Therapy Colorado (goodtherapycolorado.com)
Generates clean, modern, zero-dependency static HTML files ready for Cloudflare Pages / GitHub Pages.
"""

import os
import json
import shutil

SITE_DIR = os.path.dirname(os.path.abspath(__file__))
POSTS_FILE = os.path.join(SITE_DIR, 'content', 'posts_detailed.json')

# Load blog posts data
with open(POSTS_FILE) as f:
    BLOG_POSTS = json.load(f)

# Post metadata enrichments (excerpts, read time, category)
POST_META = {
    'boundaries-why-no-is-a-nice-word': {
        'read_time': '4 min read',
        'date': 'Nov 1, 2024',
        'category': 'Boundaries & Relationships',
        'cover': '/assets/images/boundaries-card.jpg',
        'excerpt': 'Boundaries are essential for maintaining healthy relationships and protecting our mental and emotional well-being. Discover why saying "no" can be one of the kindest things you can do.'
    },
    'family-of-origin-are-you-becoming-your-parents': {
        'read_time': '4 min read',
        'date': 'Nov 1, 2024',
        'category': 'Family Dynamics',
        'cover': '/assets/images/family-of-origin-card.jpg',
        'excerpt': 'Your family of origin plays a significant role in shaping who you are. Understanding these early dynamics can help you break unwanted patterns and choose who you want to become.'
    },
    'communication-the-heart-of-human-relationships': {
        'read_time': '3 min read',
        'date': 'Nov 1, 2024',
        'category': 'Communication',
        'cover': '/assets/images/communication-card.jpg',
        'excerpt': 'Communication is the cornerstone of all relationships. Learn practical strategies for expressing thoughts, active listening, and resolving misunderstandings with loved ones.'
    },
    'mindfulness-not-just-for-hippies': {
        'read_time': '3 min read',
        'date': 'Nov 1, 2024',
        'category': 'Mindfulness & CBT',
        'cover': '/assets/images/mindfulness-card.jpg',
        'excerpt': 'Mindfulness offers a simple yet scientifically proven way to find calm amidst chaos, reduce anxiety, and improve emotional regulation in modern life.'
    },
    'healing-from-past-trauma-a-journey-toward-recovery': {
        'read_time': '4 min read',
        'date': 'Nov 1, 2024',
        'category': 'Trauma Recovery',
        'cover': '/assets/images/past-trauma-card.jpg',
        'excerpt': 'The past doesn’t always stay in the past. Discover how understanding and gently addressing past traumas can pave the way toward authentic healing and emotional freedom.'
    },
    'core-values-as-fun-as-an-internet-quiz-only-more-helpful': {
        'read_time': '4 min read',
        'date': 'Nov 1, 2024',
        'category': 'Personal Growth',
        'cover': '/assets/images/core-values-card.jpg',
        'excerpt': 'At the heart of who we are lies our core values. Learn how identifying your unique values brings clarity to your decisions, relationships, and emotional well-being.'
    }
}

for p in BLOG_POSTS:
    slug = p['slug']
    if slug in POST_META:
        p.update(POST_META[slug])

def get_head(title, description, canonical_url, og_image="/assets/images/hero-mountains.jpg"):
    return f"""<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <link rel="canonical" href="https://www.goodtherapycolorado.com{canonical_url}">
  
  <!-- Open Graph / Facebook -->
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://www.goodtherapycolorado.com{canonical_url}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:image" content="https://www.goodtherapycolorado.com{og_image}">

  <!-- Twitter -->
  <meta property="twitter:card" content="summary_large_image">
  <meta property="twitter:url" content="https://www.goodtherapycolorado.com{canonical_url}">
  <meta property="twitter:title" content="{title}">
  <meta property="twitter:description" content="{description}">
  <meta property="twitter:image" content="https://www.goodtherapycolorado.com{og_image}">

  <!-- Favicon -->
  <link rel="icon" type="image/png" href="/assets/images/logo.png">

  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {{
      theme: {{
        extend: {{
          colors: {{
            brand: {{
              50: '#fef8f0',
              100: '#fef3e5',
              200: '#fbe3c7',
              300: '#f5c697',
              600: '#23374d',
              700: '#1b2a3b',
              800: '#15212f',
              900: '#0e1722',
              navy: '#1B365D',
              cream: '#FEF3E5',
              warm: '#F7EFE5'
            }}
          }},
          fontFamily: {{
            sans: ['Inter', 'system-ui', '-apple-system', 'BlinkMacSystemFont', 'Segoe UI', 'Roboto', 'sans-serif'],
            serif: ['Georgia', 'Cambria', 'Times New Roman', 'serif']
          }}
        }}
      }}
    }}
  </script>
  
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
  
  <style>
    body {{
      font-family: 'Inter', sans-serif;
      color: #2D3748;
    }}
    .hero-bg {{
      background-image: linear-gradient(rgba(14, 23, 34, 0.65), rgba(14, 23, 34, 0.70)), url('/assets/images/hero-mountains.jpg');
      background-size: cover;
      background-position: center;
    }}
  </style>

  <!-- Schema.org LocalBusiness -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "MedicalBusiness",
    "name": "Good Therapy Colorado",
    "image": "https://www.goodtherapycolorado.com/assets/images/logo.png",
    "@id": "https://www.goodtherapycolorado.com",
    "url": "https://www.goodtherapycolorado.com",
    "telephone": "(405) 210-6683",
    "email": "goodtherapycolorado@gmail.com",
    "address": {{
      "@type": "PostalAddress",
      "streetAddress": "1586 S. 21st Suite 20",
      "addressLocality": "Colorado Springs",
      "addressRegion": "CO",
      "postalCode": "80904",
      "addressCountry": "US"
    }},
    "description": "Colorado-based therapy practice for individuals and families providing CBT, mindfulness, and personalized counseling. In-person Colorado Springs and telehealth in Colorado and Oklahoma."
  }}
  </script>
</head>
<body class="bg-[#FFFDFB] text-slate-800 antialiased flex flex-col min-h-screen">
"""

def get_nav(current_page=""):
    def link_class(page):
        if page == current_page:
            return "text-brand-navy font-bold border-b-2 border-brand-navy pb-1"
        return "text-slate-700 hover:text-brand-navy font-medium transition-colors"

    def mobile_link_class(page):
        if page == current_page:
            return "block py-2 px-3 text-brand-navy font-bold bg-brand-100 rounded-lg"
        return "block py-2 px-3 text-slate-700 hover:text-brand-navy font-medium rounded-lg hover:bg-slate-100"

    return f"""
  <!-- Top Bar / Announcement -->
  <div class="bg-brand-cream text-brand-900 border-b border-orange-100 text-xs sm:text-sm py-2 px-4 text-center font-medium">
    Offering Telehealth throughout Colorado & Oklahoma · In-person sessions in Colorado Springs
  </div>

  <!-- Navigation Header -->
  <header class="bg-white/95 backdrop-blur sticky top-0 z-50 border-b border-slate-100 shadow-sm">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex justify-between items-center h-20">
        
        <!-- Logo & Brand Name -->
        <a href="/" class="flex items-center gap-3 group">
          <img src="/assets/images/logo.png" alt="Good Therapy Colorado Logo" class="h-12 w-auto object-contain transition-transform group-hover:scale-105">
          <div class="flex flex-col">
            <span class="text-xl sm:text-2xl font-bold tracking-tight text-brand-navy">GOOD THERAPY</span>
            <span class="text-xs uppercase tracking-widest text-slate-500 font-semibold">Colorado</span>
          </div>
        </a>

        <!-- Desktop Navigation -->
        <nav class="hidden md:flex items-center gap-8 text-sm">
          <a href="/" class="{link_class('home')}">HOME</a>
          <a href="/about-me/" class="{link_class('about')}">ABOUT ME</a>
          <a href="/contact-3/" class="{link_class('contact')}">CONTACT</a>
          <a href="/faq/" class="{link_class('faq')}">FAQ</a>
          <a href="/blog/" class="{link_class('blog')}">BLOG</a>
        </nav>

        <!-- Phone Button -->
        <div class="hidden lg:flex items-center gap-4">
          <a href="tel:4052106683" class="inline-flex items-center gap-2 text-sm font-semibold text-brand-navy bg-brand-100 hover:bg-brand-200 px-4 py-2.5 rounded-full transition-all border border-brand-200">
            <svg class="w-4 h-4 text-brand-navy" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"></path>
            </svg>
            (405) 210-6683
          </a>
        </div>

        <!-- Mobile Menu Hamburger Button -->
        <div class="md:hidden flex items-center">
          <button id="mobile-menu-button" type="button" aria-label="Toggle navigation menu" class="p-2 rounded-lg text-slate-600 hover:text-slate-900 hover:bg-slate-100 focus:outline-none">
            <svg id="menu-open-icon" class="w-7 h-7" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>
            </svg>
            <svg id="menu-close-icon" class="w-7 h-7 hidden" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
            </svg>
          </button>
        </div>

      </div>
    </div>

    <!-- Mobile Dropdown Menu -->
    <div id="mobile-menu" class="hidden md:hidden border-t border-slate-200 bg-white px-4 pt-3 pb-6 space-y-2 shadow-xl">
      <a href="/" class="{mobile_link_class('home')}">HOME</a>
      <a href="/about-me/" class="{mobile_link_class('about')}">ABOUT ME</a>
      <a href="/contact-3/" class="{mobile_link_class('contact')}">CONTACT</a>
      <a href="/faq/" class="{mobile_link_class('faq')}">FAQ</a>
      <a href="/blog/" class="{mobile_link_class('blog')}">BLOG</a>
      <div class="pt-3 border-t border-slate-100">
        <a href="tel:4052106683" class="flex items-center justify-center gap-2 w-full py-3 bg-brand-navy text-white rounded-lg font-semibold text-center shadow-sm">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"></path>
          </svg>
          Call (405) 210-6683
        </a>
      </div>
    </div>
  </header>
"""

def get_footer():
    return """
  <!-- Pre-Footer Banner -->
  <section class="bg-brand-cream border-t border-orange-100 py-10 px-4 text-center">
    <div class="max-w-4xl mx-auto">
      <p class="text-xl sm:text-2xl font-bold text-brand-navy mb-2">
        Offering telehealth in Colorado and Oklahoma.
      </p>
      <p class="text-slate-600 text-base sm:text-lg">
        In-person appointments available at our Colorado Springs office.
      </p>
    </div>
  </section>

  <!-- Main Footer -->
  <footer class="bg-slate-900 text-slate-300 pt-16 pb-12 mt-auto">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-10">
        
        <!-- Col 1: Brand Info -->
        <div class="space-y-4">
          <div class="flex items-center gap-3">
            <img src="/assets/images/logo.png" alt="Good Therapy Colorado" class="h-10 w-auto brightness-0 invert">
            <span class="text-xl font-bold tracking-tight text-white">GOOD THERAPY</span>
          </div>
          <p class="text-sm text-slate-400 leading-relaxed">
            A Colorado-based therapy practice dedicated to helping individuals and families navigate life’s ups and downs with warmth, evidence-based care, and practical tools.
          </p>
          <div class="pt-2 text-xs text-amber-300/80 font-medium">
            * Social media coming soon!
          </div>
        </div>

        <!-- Col 2: Contact -->
        <div>
          <h3 class="text-white text-sm font-semibold tracking-wider uppercase mb-4">Contact</h3>
          <ul class="space-y-3 text-sm text-slate-400">
            <li class="flex items-start gap-3">
              <svg class="w-5 h-5 text-amber-400 flex-shrink-0 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"></path>
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"></path>
              </svg>
              <span>1586 S. 21st Suite 20<br>Colorado Springs, CO 80904</span>
            </li>
            <li class="flex items-center gap-3">
              <svg class="w-5 h-5 text-amber-400 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path>
              </svg>
              <a href="mailto:goodtherapycolorado@gmail.com" class="hover:text-white transition-colors">goodtherapycolorado@gmail.com</a>
            </li>
            <li class="flex items-center gap-3">
              <svg class="w-5 h-5 text-amber-400 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"></path>
              </svg>
              <a href="tel:4052106683" class="hover:text-white transition-colors">(405) 210-6683</a>
            </li>
          </ul>
        </div>

        <!-- Col 3: Quick Links -->
        <div>
          <h3 class="text-white text-sm font-semibold tracking-wider uppercase mb-4">Information</h3>
          <ul class="space-y-2 text-sm text-slate-400">
            <li><a href="/" class="hover:text-white transition-colors">Home</a></li>
            <li><a href="/about-me/" class="hover:text-white transition-colors">About Me</a></li>
            <li><a href="/contact-3/" class="hover:text-white transition-colors">Contact</a></li>
            <li><a href="/faq/" class="hover:text-white transition-colors">Frequently Asked Questions</a></li>
            <li><a href="/blog/" class="hover:text-white transition-colors">Blog</a></li>
          </ul>
        </div>

        <!-- Col 4: Newsletter -->
        <div>
          <h3 class="text-white text-sm font-semibold tracking-wider uppercase mb-4">Stay Connected</h3>
          <p class="text-sm text-slate-400 mb-3 leading-relaxed">
            Subscribe to receive updates, insights, and mental wellness resources.
          </p>
          <form onsubmit="event.preventDefault(); alert('Thank you for subscribing!'); this.reset();" class="space-y-2">
            <input type="email" required placeholder="Your email address" class="w-full px-3.5 py-2.5 rounded-lg bg-slate-800 border border-slate-700 text-white placeholder-slate-500 text-sm focus:outline-none focus:ring-2 focus:ring-amber-400">
            <button type="submit" class="w-full bg-brand-navy hover:bg-brand-700 text-white font-medium px-4 py-2.5 rounded-lg text-sm transition-colors border border-slate-700">
              Join Our Mailing List
            </button>
          </form>
        </div>

      </div>

      <!-- Copyright -->
      <div class="pt-12 mt-12 border-t border-slate-800 flex flex-col sm:flex-row items-center justify-between gap-4 text-xs text-slate-500">
        <p>&copy; 2026 Good Therapy Colorado. All rights reserved.</p>
        <p>Colorado Springs, CO · Telehealth in CO &amp; OK</p>
      </div>
    </div>
  </footer>

  <!-- Script for Mobile Menu -->
  <script>
    const menuBtn = document.getElementById('mobile-menu-button');
    const mobileMenu = document.getElementById('mobile-menu');
    const openIcon = document.getElementById('menu-open-icon');
    const closeIcon = document.getElementById('menu-close-icon');

    if (menuBtn && mobileMenu) {
      menuBtn.addEventListener('click', () => {
        const isHidden = mobileMenu.classList.contains('hidden');
        if (isHidden) {
          mobileMenu.classList.remove('hidden');
          openIcon.classList.add('hidden');
          closeIcon.classList.remove('hidden');
        } else {
          mobileMenu.classList.add('hidden');
          openIcon.classList.remove('hidden');
          closeIcon.classList.add('hidden');
        }
      });
    }
  </script>
</body>
</html>
"""

def generate_home():
    head = get_head(
        title="HOME | Good Therapy",
        description="Good Therapy is a Colorado based therapy practice for individuals and families looking for real help! Telehealth and in-person in Colorado Springs.",
        canonical_url="/"
    )
    nav = get_nav("home")
    
    content = """
  <!-- Hero Section -->
  <section class="hero-bg py-24 sm:py-32 md:py-40 px-4 text-white text-center relative flex items-center justify-center">
    <div class="max-w-4xl mx-auto space-y-6">
      <div class="inline-block px-4 py-1.5 rounded-full bg-white/10 backdrop-blur border border-white/20 text-xs sm:text-sm uppercase tracking-widest font-semibold text-amber-200">
        Compassionate Therapy in Colorado & Oklahoma
      </div>
      <h1 class="text-3xl sm:text-5xl md:text-6xl font-extrabold tracking-tight leading-tight uppercase max-w-3xl mx-auto">
        GOOD THERAPY HELPS PEOPLE TURN MOUNTAINS INTO MOLEHILLS
      </h1>
      <p class="text-lg sm:text-2xl text-slate-200 font-light italic max-w-2xl mx-auto">
        "Small steps lead to big changes"
      </p>
      <div class="pt-6 flex flex-wrap justify-center gap-4">
        <a href="/contact-3/" class="bg-amber-500 hover:bg-amber-400 text-slate-900 font-bold px-8 py-3.5 rounded-full text-base sm:text-lg transition-all shadow-lg hover:shadow-xl transform hover:-translate-y-0.5">
          Let's Chat!
        </a>
        <a href="#approach" class="bg-white/15 hover:bg-white/25 text-white font-semibold px-8 py-3.5 rounded-full text-base sm:text-lg transition-all border border-white/30 backdrop-blur">
          Our Approach
        </a>
      </div>
    </div>
  </section>

  <!-- Section 1: Intro / Mission -->
  <section class="py-20 px-4 sm:px-6 lg:px-8 max-w-7xl mx-auto">
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
      
      <div class="lg:col-span-5 order-2 lg:order-1">
        <div class="relative">
          <div class="absolute -top-4 -left-4 w-full h-full bg-brand-cream rounded-2xl -z-10 transform rotate-1"></div>
          <img src="/assets/images/family-mountaintop.jpg" alt="Family with backpacks on a mountain top" class="rounded-2xl shadow-xl w-full h-[380px] sm:h-[460px] object-cover">
        </div>
      </div>

      <div class="lg:col-span-7 order-1 lg:order-2 space-y-6">
        <div class="inline-block text-xs uppercase tracking-widest text-brand-navy font-bold bg-brand-100 px-3 py-1 rounded-md">
          Welcome to Good Therapy
        </div>
        <h2 class="text-3xl sm:text-4xl font-extrabold text-brand-navy tracking-tight leading-tight">
          "Small steps lead to big changes"
        </h2>
        <p class="text-slate-700 text-lg leading-relaxed">
          People seek therapy for a multitude of reasons; some are driven by the desire for support, understanding, and growth; others to find help through challenging life events such as grief, trauma, or relationship issues. Some may struggle with mental health conditions like anxiety, depression, or chronic stress.
        </p>
        <p class="text-slate-700 text-lg leading-relaxed">
          Good Therapy provides a supportive environment where people can explore their thoughts and feelings, improve relationships, learn new skills, and work towards a more fulfilling and balanced life.
        </p>
        <div class="pt-2">
          <a href="/about-me/" class="inline-flex items-center gap-2 font-bold text-brand-navy hover:text-blue-800 text-base group">
            Learn more about Kelly Roper
            <svg class="w-5 h-5 transform group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"></path>
            </svg>
          </a>
        </div>
      </div>

    </div>
  </section>

  <!-- Section 2: Our Approach -->
  <section id="approach" class="py-20 bg-brand-50 border-y border-orange-100/60 px-4 sm:px-6 lg:px-8">
    <div class="max-w-7xl mx-auto">
      
      <div class="text-center max-w-3xl mx-auto mb-16 space-y-4">
        <h2 class="text-xs uppercase tracking-widest text-brand-navy font-bold bg-brand-cream inline-block px-3 py-1 rounded-md border border-orange-200">
          How We Help
        </h2>
        <h3 class="text-3xl sm:text-4xl font-extrabold text-brand-navy tracking-tight">
          OUR APPROACH
        </h3>
        <p class="text-slate-700 text-base sm:text-lg leading-relaxed">
          At Good Therapy we believe that mental health isn’t just in your head. Good mental health encompasses thoughts, emotions, relationships, actions and much more. Each plays an important role in helping you build the life you want. Because of this, we utilize several different therapeutic modalities including cognitive-behavioral, strength-based and person-centered therapy. Each person needs something a little different. Learn about some of the ways we help below.
        </p>
      </div>

      <!-- 6 Modality Cards Grid -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        
        <!-- 1. Mindfulness -->
        <div class="bg-white rounded-2xl shadow-sm hover:shadow-md transition-shadow border border-slate-200/80 overflow-hidden flex flex-col">
          <div class="h-56 overflow-hidden">
            <img src="/assets/images/mindfulness-card.jpg" alt="Mindfulness" class="w-full h-full object-cover hover:scale-105 transition-transform duration-500">
          </div>
          <div class="p-6 flex-1 flex flex-col justify-between space-y-4">
            <div>
              <h4 class="text-xl font-bold text-brand-navy mb-2">Mindfulness</h4>
              <p class="text-slate-600 text-sm leading-relaxed">
                is the practice of being fully present in the moment without judgement. It allows people to deepen their own understanding, increase emotional regulation and reduce stress.
              </p>
            </div>
            <a href="/post/mindfulness-not-just-for-hippies/" class="inline-flex items-center text-sm font-semibold text-brand-navy hover:text-amber-600 transition-colors pt-2">
              Learn More →
            </a>
          </div>
        </div>

        <!-- 2. Communication -->
        <div class="bg-white rounded-2xl shadow-sm hover:shadow-md transition-shadow border border-slate-200/80 overflow-hidden flex flex-col">
          <div class="h-56 overflow-hidden">
            <img src="/assets/images/communication-card.jpg" alt="Communication" class="w-full h-full object-cover hover:scale-105 transition-transform duration-500">
          </div>
          <div class="p-6 flex-1 flex flex-col justify-between space-y-4">
            <div>
              <h4 class="text-xl font-bold text-brand-navy mb-2">Communication</h4>
              <p class="text-slate-600 text-sm leading-relaxed">
                is the ability to effectively convey, receive, and interpret messages both verbally and non-verbally. While this may seem simple, relationships and family dynamics can sometimes make this feel impossible.
              </p>
            </div>
            <a href="/post/communication-the-heart-of-human-relationships/" class="inline-flex items-center text-sm font-semibold text-brand-navy hover:text-amber-600 transition-colors pt-2">
              Learn More →
            </a>
          </div>
        </div>

        <!-- 3. Boundary Setting -->
        <div class="bg-white rounded-2xl shadow-sm hover:shadow-md transition-shadow border border-slate-200/80 overflow-hidden flex flex-col">
          <div class="h-56 overflow-hidden">
            <img src="/assets/images/boundaries-card.jpg" alt="Boundary Setting" class="w-full h-full object-cover hover:scale-105 transition-transform duration-500">
          </div>
          <div class="p-6 flex-1 flex flex-col justify-between space-y-4">
            <div>
              <h4 class="text-xl font-bold text-brand-navy mb-2">Boundary Setting</h4>
              <p class="text-slate-600 text-sm leading-relaxed">
                is the ability to maintain clear, healthy limits that protect one's emotional, mental, and physical well-being. This skill involves understanding personal needs and limits, communicating them assertively, and respecting both one's own boundaries and those of others.
              </p>
            </div>
            <a href="/post/boundaries-why-no-is-a-nice-word/" class="inline-flex items-center text-sm font-semibold text-brand-navy hover:text-amber-600 transition-colors pt-2">
              Learn More →
            </a>
          </div>
        </div>

        <!-- 4. Core Values -->
        <div class="bg-white rounded-2xl shadow-sm hover:shadow-md transition-shadow border border-slate-200/80 overflow-hidden flex flex-col">
          <div class="h-56 overflow-hidden">
            <img src="/assets/images/core-values-card.jpg" alt="Core Values" class="w-full h-full object-cover hover:scale-105 transition-transform duration-500">
          </div>
          <div class="p-6 flex-1 flex flex-col justify-between space-y-4">
            <div>
              <h4 class="text-xl font-bold text-brand-navy mb-2">Core Values</h4>
              <p class="text-slate-600 text-sm leading-relaxed">
                each person has their own unique set of core values. These values shape both our internal emotions and our external outlook. Identifying and understanding your core values can be extremely helpful in understanding emotions and relationships.
              </p>
            </div>
            <a href="/post/core-values-as-fun-as-an-internet-quiz-only-more-helpful/" class="inline-flex items-center text-sm font-semibold text-brand-navy hover:text-amber-600 transition-colors pt-2">
              Learn More →
            </a>
          </div>
        </div>

        <!-- 5. Family of Origin -->
        <div class="bg-white rounded-2xl shadow-sm hover:shadow-md transition-shadow border border-slate-200/80 overflow-hidden flex flex-col">
          <div class="h-56 overflow-hidden">
            <img src="/assets/images/family-of-origin-card.jpg" alt="Family of Origin" class="w-full h-full object-cover hover:scale-105 transition-transform duration-500">
          </div>
          <div class="p-6 flex-1 flex flex-col justify-between space-y-4">
            <div>
              <h4 class="text-xl font-bold text-brand-navy mb-2">Family of Origin</h4>
              <p class="text-slate-600 text-sm leading-relaxed">
                refers to the family in which you were raised specifically during your early formative years. Understanding these early relationships, dynamics, and patterns of behavior can be extremely helpful in understanding yourself in the present.
              </p>
            </div>
            <a href="/post/family-of-origin-are-you-becoming-your-parents/" class="inline-flex items-center text-sm font-semibold text-brand-navy hover:text-amber-600 transition-colors pt-2">
              Learn More →
            </a>
          </div>
        </div>

        <!-- 6. Past Trauma -->
        <div class="bg-white rounded-2xl shadow-sm hover:shadow-md transition-shadow border border-slate-200/80 overflow-hidden flex flex-col">
          <div class="h-56 overflow-hidden">
            <img src="/assets/images/past-trauma-card.jpg" alt="Past Trauma" class="w-full h-full object-cover hover:scale-105 transition-transform duration-500">
          </div>
          <div class="p-6 flex-1 flex flex-col justify-between space-y-4">
            <div>
              <h4 class="text-xl font-bold text-brand-navy mb-2">Past Trauma</h4>
              <p class="text-slate-600 text-sm leading-relaxed">
                the past doesn’t always stay in the past. Our early experiences shape our present, whether we want it to or not. Understanding and addressing past traumas is a critical part of moving forward.
              </p>
            </div>
            <a href="/post/healing-from-past-trauma-a-journey-toward-recovery/" class="inline-flex items-center text-sm font-semibold text-brand-navy hover:text-amber-600 transition-colors pt-2">
              Learn More →
            </a>
          </div>
        </div>

      </div>

      <!-- CTA Button -->
      <div class="text-center pt-16">
        <a href="/contact-3/" class="inline-block bg-brand-navy hover:bg-brand-700 text-white font-bold px-10 py-4 rounded-full text-lg shadow-lg hover:shadow-xl transition-all transform hover:-translate-y-0.5">
          Let's Chat!
        </a>
      </div>

    </div>
  </section>
"""
    footer = get_footer()
    return head + nav + content + footer

def generate_about():
    head = get_head(
        title="ABOUT ME | Good Therapy",
        description="Learn more about Kelly Roper, therapist at Good Therapy Colorado. Providing CBT, mindfulness, and compassionate therapy in Colorado Springs and via telehealth.",
        canonical_url="/about-me/",
        og_image="/assets/images/kelly-roper.jpg"
    )
    nav = get_nav("about")
    content = """
  <!-- Header Banner -->
  <section class="bg-brand-cream border-b border-orange-100 py-16 px-4 text-center">
    <div class="max-w-4xl mx-auto">
      <span class="text-xs uppercase tracking-widest text-slate-500 font-bold block mb-2">About Good Therapy</span>
      <h1 class="text-4xl sm:text-5xl font-extrabold text-brand-navy tracking-tight">ABOUT ME</h1>
    </div>
  </section>

  <!-- Bio Section -->
  <section class="py-16 sm:py-24 px-4 sm:px-6 lg:px-8 max-w-7xl mx-auto">
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-start">
      
      <!-- Headshot Column -->
      <div class="lg:col-span-5">
        <div class="sticky top-28">
          <div class="relative">
            <div class="absolute -top-4 -left-4 w-full h-full bg-brand-cream rounded-3xl -z-10"></div>
            <img src="/assets/images/kelly-roper.jpg" alt="Kelly Roper, Therapist at Good Therapy Colorado" class="rounded-3xl shadow-xl w-full object-cover max-h-[560px]">
          </div>
          <div class="mt-6 text-center lg:text-left space-y-1">
            <h2 class="text-2xl font-bold text-brand-navy">Kelly Roper</h2>
            <p class="text-slate-600 font-medium">Licensed Therapist · Good Therapy Colorado</p>
            <p class="text-sm text-slate-500">Colorado Springs Office &amp; Telehealth in CO &amp; OK</p>
          </div>
        </div>
      </div>

      <!-- Bio Text Column -->
      <div class="lg:col-span-7 space-y-6 text-slate-700 text-lg leading-relaxed">
        <div class="inline-block text-xs uppercase tracking-widest text-brand-navy font-bold bg-brand-100 px-3 py-1 rounded-md">
          Meet Your Therapist
        </div>
        
        <h3 class="text-3xl font-extrabold text-brand-navy tracking-tight">
          "Therapy doesn’t have to be heavy — I believe in the power of humor and genuine connection."
        </h3>

        <p>
          My name is Kelly, I am a therapist dedicated to helping individuals and families navigate life’s ups and downs. I specialize in working with adults, children and their families, providing personalized support that meets their individual needs.
        </p>

        <p>
          I’m passionate about employing <strong>Cognitive Behavioral Therapy (CBT)</strong> as a framework or approach in my practice, alongside <strong>Mindfulness techniques</strong> and providing educational material that clients can use. Active listening is at the heart of my approach, allowing me to truly connect with my clients and support their journey toward personal growth.
        </p>

        <p>
          Therapy doesn’t have to be heavy—I believe in the power of humor to create a relaxed and welcoming environment. My goal is to promote effective therapeutic interventions while providing up-to-date information that empowers my clients.
        </p>

        <p>
          When you work with me, you can expect a supportive space where you can explore your thoughts and feelings, learn practical skills, and, hopefully, share a laugh or two along the way.
        </p>

        <div class="p-6 bg-brand-50 border border-brand-200/80 rounded-2xl space-y-3">
          <h4 class="font-bold text-brand-navy text-xl">Core Therapeutic Focus:</h4>
          <ul class="grid grid-cols-1 sm:grid-cols-2 gap-2 text-base text-slate-700">
            <li class="flex items-center gap-2">✓ Cognitive Behavioral Therapy (CBT)</li>
            <li class="flex items-center gap-2">✓ Mindfulness &amp; Stress Reduction</li>
            <li class="flex items-center gap-2">✓ Family Systems &amp; Dynamics</li>
            <li class="flex items-center gap-2">✓ Healthy Boundary Setting</li>
            <li class="flex items-center gap-2">✓ Adults, Children &amp; Families</li>
            <li class="flex items-center gap-2">✓ Person-Centered Support</li>
          </ul>
        </div>

        <p class="font-semibold text-brand-navy text-xl pt-2">
          Let’s embark on this journey together!
        </p>

        <div class="pt-4">
          <a href="/contact-3/" class="inline-block bg-brand-navy hover:bg-brand-700 text-white font-bold px-8 py-3.5 rounded-full text-lg shadow-lg hover:shadow-xl transition-all">
            Let's Chat!
          </a>
        </div>

      </div>

    </div>
  </section>
"""
    footer = get_footer()
    return head + nav + content + footer

def generate_contact():
    head = get_head(
        title="CONTACT | Good Therapy",
        description="Contact Good Therapy Colorado. Located at 1586 S. 21st Suite 20, Colorado Springs, CO. Call (405) 210-6683 or email goodtherapycolorado@gmail.com.",
        canonical_url="/contact-3/"
    )
    nav = get_nav("contact")
    content = """
  <!-- Header Banner -->
  <section class="bg-brand-cream border-b border-orange-100 py-16 px-4 text-center">
    <div class="max-w-4xl mx-auto">
      <span class="text-xs uppercase tracking-widest text-slate-500 font-bold block mb-2">Get in Touch</span>
      <h1 class="text-4xl sm:text-5xl font-extrabold text-brand-navy tracking-tight">Let's Connect!</h1>
      <p class="text-slate-600 mt-3 text-lg">We would love to hear from you. Reach out with questions or to schedule a session.</p>
    </div>
  </section>

  <!-- Contact Grid -->
  <section class="py-16 sm:py-24 px-4 sm:px-6 lg:px-8 max-w-7xl mx-auto">
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-12">
      
      <!-- Info Column -->
      <div class="lg:col-span-5 space-y-8">
        <div>
          <h2 class="text-2xl font-bold text-brand-navy mb-6">Contact Information</h2>
          <p class="text-slate-600 leading-relaxed mb-6">
            Whether you are considering therapy for yourself or a loved one, we are here to support you.
          </p>
        </div>

        <div class="space-y-6">
          
          <div class="flex items-start gap-4 p-5 rounded-2xl bg-white border border-slate-200/80 shadow-sm">
            <div class="p-3 bg-brand-100 text-brand-navy rounded-xl">
              <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"></path>
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"></path>
              </svg>
            </div>
            <div>
              <h3 class="font-bold text-slate-900 text-base">Office Address</h3>
              <p class="text-slate-600 text-sm mt-1">1586 S. 21st Suite 20<br>Colorado Springs, CO 80904</p>
              <a href="https://maps.google.com/?q=1586+S+21st+Ste+20+Colorado+Springs+CO+80904" target="_blank" rel="noopener noreferrer" class="inline-block text-xs font-semibold text-brand-navy hover:underline mt-2">
                Open in Google Maps →
              </a>
            </div>
          </div>

          <div class="flex items-start gap-4 p-5 rounded-2xl bg-white border border-slate-200/80 shadow-sm">
            <div class="p-3 bg-brand-100 text-brand-navy rounded-xl">
              <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path>
              </svg>
            </div>
            <div>
              <h3 class="font-bold text-slate-900 text-base">Email</h3>
              <p class="text-slate-600 text-sm mt-1">Send us an email anytime:</p>
              <a href="mailto:goodtherapycolorado@gmail.com" class="text-sm font-semibold text-brand-navy hover:text-blue-800 transition-colors block mt-1">
                goodtherapycolorado@gmail.com
              </a>
            </div>
          </div>

          <div class="flex items-start gap-4 p-5 rounded-2xl bg-white border border-slate-200/80 shadow-sm">
            <div class="p-3 bg-brand-100 text-brand-navy rounded-xl">
              <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"></path>
              </svg>
            </div>
            <div>
              <h3 class="font-bold text-slate-900 text-base">Phone</h3>
              <p class="text-slate-600 text-sm mt-1">Call or leave a confidential message:</p>
              <a href="tel:4052106683" class="text-sm font-semibold text-brand-navy hover:text-blue-800 transition-colors block mt-1">
                (405) 210-6683
              </a>
            </div>
          </div>

        </div>

        <div class="p-5 bg-amber-50/60 border border-amber-200/80 rounded-2xl">
          <h4 class="font-bold text-amber-900 text-sm mb-1">Telehealth Availability</h4>
          <p class="text-xs text-amber-800 leading-relaxed">
            We are fully licensed to conduct secure HIPAA-compliant telehealth sessions throughout both <strong>Colorado</strong> and <strong>Oklahoma</strong>.
          </p>
        </div>

      </div>

      <!-- Form Column -->
      <div class="lg:col-span-7">
        <div class="bg-white p-8 sm:p-10 rounded-3xl border border-slate-200 shadow-md">
          <h2 class="text-2xl font-bold text-brand-navy mb-2">Send a Message</h2>
          <p class="text-slate-600 text-sm mb-8">
            Fill out the form below and we will get back to you promptly.
          </p>

          <form id="contact-form" action="mailto:goodtherapycolorado@gmail.com" method="GET" class="space-y-6">
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
              <div>
                <label for="name" class="block text-xs font-semibold uppercase tracking-wider text-slate-700 mb-2">Full Name *</label>
                <input type="text" id="name" name="name" required placeholder="Jane Doe" class="w-full px-4 py-3 rounded-xl border border-slate-300 focus:outline-none focus:ring-2 focus:ring-brand-navy focus:border-brand-navy text-sm">
              </div>
              <div>
                <label for="email" class="block text-xs font-semibold uppercase tracking-wider text-slate-700 mb-2">Email Address *</label>
                <input type="email" id="email" name="email" required placeholder="jane@example.com" class="w-full px-4 py-3 rounded-xl border border-slate-300 focus:outline-none focus:ring-2 focus:ring-brand-navy focus:border-brand-navy text-sm">
              </div>
            </div>

            <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
              <div>
                <label for="phone" class="block text-xs font-semibold uppercase tracking-wider text-slate-700 mb-2">Phone Number</label>
                <input type="tel" id="phone" name="phone" placeholder="(123) 456-7890" class="w-full px-4 py-3 rounded-xl border border-slate-300 focus:outline-none focus:ring-2 focus:ring-brand-navy focus:border-brand-navy text-sm">
              </div>
              <div>
                <label for="preference" class="block text-xs font-semibold uppercase tracking-wider text-slate-700 mb-2">Preferred Appointment</label>
                <select id="preference" name="preference" class="w-full px-4 py-3 rounded-xl border border-slate-300 focus:outline-none focus:ring-2 focus:ring-brand-navy focus:border-brand-navy text-sm bg-white">
                  <option value="Telehealth (Colorado)">Telehealth (Colorado)</option>
                  <option value="Telehealth (Oklahoma)">Telehealth (Oklahoma)</option>
                  <option value="In-Person (Colorado Springs)">In-Person (Colorado Springs)</option>
                  <option value="Not sure / General question">Not sure / General question</option>
                </select>
              </div>
            </div>

            <div>
              <label for="message" class="block text-xs font-semibold uppercase tracking-wider text-slate-700 mb-2">Your Message *</label>
              <textarea id="message" name="body" rows="5" required placeholder="Tell us how we can help..." class="w-full px-4 py-3 rounded-xl border border-slate-300 focus:outline-none focus:ring-2 focus:ring-brand-navy focus:border-brand-navy text-sm"></textarea>
            </div>

            <button type="submit" class="w-full bg-brand-navy hover:bg-brand-700 text-white font-bold py-4 px-8 rounded-xl text-base transition-all shadow-md hover:shadow-lg">
              Send Message
            </button>

            <p class="text-xs text-slate-500 text-center leading-relaxed">
              If you prefer, you can also email us directly at <a href="mailto:goodtherapycolorado@gmail.com" class="text-brand-navy font-semibold underline">goodtherapycolorado@gmail.com</a>.
            </p>
          </form>

        </div>
      </div>

    </div>
  </section>
"""
    footer = get_footer()
    return head + nav + content + footer

def generate_faq():
    head = get_head(
        title="FAQ | Good Therapy",
        description="Frequently Asked Questions about therapy sessions, telehealth in Colorado and Oklahoma, in-person counseling in Colorado Springs, and therapeutic modalities.",
        canonical_url="/faq/"
    )
    nav = get_nav("faq")
    content = """
  <!-- Header Banner -->
  <section class="bg-brand-cream border-b border-orange-100 py-16 px-4 text-center">
    <div class="max-w-4xl mx-auto">
      <span class="text-xs uppercase tracking-widest text-slate-500 font-bold block mb-2">Common Questions</span>
      <h1 class="text-4xl sm:text-5xl font-extrabold text-brand-navy tracking-tight">Frequently Asked Questions</h1>
      <p class="text-slate-600 mt-3 text-lg">Here are answers to the most common questions about our practice and services.</p>
    </div>
  </section>

  <!-- FAQ Accordion Section -->
  <section class="py-16 sm:py-24 px-4 sm:px-6 lg:px-8 max-w-4xl mx-auto">
    <div class="space-y-6">
      
      <!-- FAQ 1 -->
      <details class="group bg-white rounded-2xl border border-slate-200 p-6 shadow-sm [&_summary::-webkit-details-marker]:hidden" open>
        <summary class="flex items-center justify-between cursor-pointer font-bold text-lg sm:text-xl text-brand-navy">
          <span>Who do you work with?</span>
          <span class="ml-4 flex-shrink-0 text-slate-400 group-open:rotate-180 transition-transform">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
          </span>
        </summary>
        <p class="mt-4 text-slate-600 leading-relaxed text-base">
          At Good Therapy, we work with adults, children, and their families. Whether you are facing anxiety, depression, relationship difficulties, trauma recovery, or major life transitions, we provide personalized care tailored to your unique needs.
        </p>
      </details>

      <!-- FAQ 2 -->
      <details class="group bg-white rounded-2xl border border-slate-200 p-6 shadow-sm [&_summary::-webkit-details-marker]:hidden">
        <summary class="flex items-center justify-between cursor-pointer font-bold text-lg sm:text-xl text-brand-navy">
          <span>Do you offer telehealth or in-person appointments?</span>
          <span class="ml-4 flex-shrink-0 text-slate-400 group-open:rotate-180 transition-transform">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
          </span>
        </summary>
        <p class="mt-4 text-slate-600 leading-relaxed text-base">
          We offer both! In-person appointments are held at our Colorado Springs office (1586 S. 21st Suite 20, Colorado Springs, CO 80904). We also offer secure, HIPAA-compliant telehealth sessions to clients residing anywhere in Colorado and Oklahoma.
        </p>
      </details>

      <!-- FAQ 3 -->
      <details class="group bg-white rounded-2xl border border-slate-200 p-6 shadow-sm [&_summary::-webkit-details-marker]:hidden">
        <summary class="flex items-center justify-between cursor-pointer font-bold text-lg sm:text-xl text-brand-navy">
          <span>What therapeutic approaches do you use?</span>
          <span class="ml-4 flex-shrink-0 text-slate-400 group-open:rotate-180 transition-transform">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
          </span>
        </summary>
        <p class="mt-4 text-slate-600 leading-relaxed text-base">
          We utilize evidence-based modalities including Cognitive Behavioral Therapy (CBT), Mindfulness techniques, person-centered therapy, and strength-based approaches. We adapt our framework to what works best for you and integrate humor and genuine empathy to make the space comfortable.
        </p>
      </details>

      <!-- FAQ 4 -->
      <details class="group bg-white rounded-2xl border border-slate-200 p-6 shadow-sm [&_summary::-webkit-details-marker]:hidden">
        <summary class="flex items-center justify-between cursor-pointer font-bold text-lg sm:text-xl text-brand-navy">
          <span>How do I schedule an appointment or get started?</span>
          <span class="ml-4 flex-shrink-0 text-slate-400 group-open:rotate-180 transition-transform">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
          </span>
        </summary>
        <p class="mt-4 text-slate-600 leading-relaxed text-base">
          Getting started is easy. You can reach out through our <a href="/contact-3/" class="text-brand-navy font-semibold underline">Contact page</a>, send an email directly to <a href="mailto:goodtherapycolorado@gmail.com" class="text-brand-navy font-semibold underline">goodtherapycolorado@gmail.com</a>, or give us a call at <a href="tel:4052106683" class="text-brand-navy font-semibold underline">(405) 210-6683</a>. We will discuss your goals, answer any questions, and set up your first session.
        </p>
      </details>

      <!-- FAQ 5 -->
      <details class="group bg-white rounded-2xl border border-slate-200 p-6 shadow-sm [&_summary::-webkit-details-marker]:hidden">
        <summary class="flex items-center justify-between cursor-pointer font-bold text-lg sm:text-xl text-brand-navy">
          <span>What should I expect in our first session?</span>
          <span class="ml-4 flex-shrink-0 text-slate-400 group-open:rotate-180 transition-transform">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
          </span>
        </summary>
        <p class="mt-4 text-slate-600 leading-relaxed text-base">
          The first session is a relaxed intake conversation. We’ll get to know each other, discuss what brings you to therapy, explore your background and current challenges, and identify what goals or outcomes you’d like to work towards. You are always in control of the pace.
        </p>
      </details>

    </div>

    <!-- Contact CTA -->
    <div class="mt-16 text-center bg-brand-50 border border-brand-200 rounded-3xl p-8 sm:p-10 space-y-4">
      <h3 class="text-2xl font-bold text-brand-navy">Still have questions?</h3>
      <p class="text-slate-600 max-w-xl mx-auto">
        Don't hesitate to reach out. We are happy to talk through any details before you schedule.
      </p>
      <a href="/contact-3/" class="inline-block bg-brand-navy hover:bg-brand-700 text-white font-bold px-8 py-3.5 rounded-full text-base shadow transition-all">
        Let's Chat!
      </a>
    </div>
  </section>
"""
    footer = get_footer()
    return head + nav + content + footer

def generate_blog():
    head = get_head(
        title="BLOG | Good Therapy",
        description="Articles and mental wellness insights from Kelly Roper at Good Therapy Colorado. Explore mindfulness, healthy boundaries, family dynamics, and trauma recovery.",
        canonical_url="/blog/"
    )
    nav = get_nav("blog")

    cards_html = []
    for post in BLOG_POSTS:
        slug = post['slug']
        title = post['title']
        cover = post.get('cover', '/assets/images/mindfulness-card.jpg')
        excerpt = post.get('excerpt', '')
        date = post.get('date', 'Nov 1, 2024')
        read_time = post.get('read_time', '4 min read')
        cat = post.get('category', 'Mental Health')

        card = f"""
        <article class="bg-white rounded-2xl shadow-sm hover:shadow-md transition-shadow border border-slate-200/80 overflow-hidden flex flex-col">
          <a href="/post/{slug}/" class="block h-56 overflow-hidden">
            <img src="{cover}" alt="{title}" class="w-full h-full object-cover hover:scale-105 transition-transform duration-500">
          </a>
          <div class="p-6 flex-1 flex flex-col justify-between space-y-4">
            <div>
              <div class="flex items-center gap-2 text-xs font-semibold text-amber-700 uppercase tracking-wider mb-2">
                <span>{cat}</span> · <span>{read_time}</span>
              </div>
              <h2 class="text-xl font-bold text-brand-navy hover:text-blue-800 transition-colors mb-2">
                <a href="/post/{slug}/">{title}</a>
              </h2>
              <p class="text-slate-600 text-sm leading-relaxed">
                {excerpt}
              </p>
            </div>
            <div class="pt-4 border-t border-slate-100 flex items-center justify-between text-xs text-slate-500">
              <span>By Kelly Roper</span>
              <span>{date}</span>
            </div>
          </div>
        </article>
        """
        cards_html.append(card)

    content = f"""
  <!-- Header Banner -->
  <section class="bg-brand-cream border-b border-orange-100 py-16 px-4 text-center">
    <div class="max-w-4xl mx-auto">
      <span class="text-xs uppercase tracking-widest text-slate-500 font-bold block mb-2">Resources &amp; Insights</span>
      <h1 class="text-4xl sm:text-5xl font-extrabold text-brand-navy tracking-tight">Good Therapy Blog</h1>
      <p class="text-slate-600 mt-3 text-lg">Practical guides, mental wellness tools, and insights for everyday life.</p>
    </div>
  </section>

  <!-- Blog Cards Grid -->
  <section class="py-16 sm:py-24 px-4 sm:px-6 lg:px-8 max-w-7xl mx-auto">
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
      {''.join(cards_html)}
    </div>
  </section>
"""
    footer = get_footer()
    return head + nav + content + footer

def generate_post(post):
    slug = post['slug']
    title = post['title']
    cover = post.get('cover', '/assets/images/hero-mountains.jpg')
    date = post.get('date', 'Nov 1, 2024')
    read_time = post.get('read_time', '4 min read')
    cat = post.get('category', 'Mental Wellness')
    excerpt = post.get('excerpt', '')

    head = get_head(
        title=f"{title} | Good Therapy",
        description=excerpt,
        canonical_url=f"/post/{slug}/",
        og_image=cover
    )
    nav = get_nav("blog")

    body_elements = []
    first_image_skipped = False

    for item in post.get('items', []):
        itype = item.get('type')
        if itype == 'heading':
            level = item.get('level', 'h3')
            txt = item.get('text', '')
            if txt:
                body_elements.append(f'<h3 class="text-2xl font-bold text-brand-navy mt-10 mb-4 tracking-tight">{txt}</h3>')
        elif itype == 'image':
            src = item.get('src', '')
            alt = item.get('alt', '')
            # If it's the very first image and matches the hero, we can show it nicely in body
            body_elements.append(f"""
            <figure class="my-8">
              <img src="{src}" alt="{alt}" class="rounded-2xl shadow-md mx-auto max-w-full h-auto object-cover max-h-[460px] w-full">
            </figure>
            """)
        elif itype == 'paragraph':
            raw = item.get('html', '')
            if raw:
                body_elements.append(f'<p class="text-slate-700 text-lg leading-relaxed mb-6">{raw}</p>')

    content = f"""
  <!-- Article Header -->
  <header class="bg-brand-cream border-b border-orange-100 py-16 px-4">
    <div class="max-w-4xl mx-auto">
      <div class="mb-4">
        <a href="/blog/" class="inline-flex items-center gap-1.5 text-xs font-semibold uppercase tracking-wider text-slate-500 hover:text-brand-navy transition-colors">
          ← Back to all posts
        </a>
      </div>
      <div class="flex items-center gap-3 text-xs font-semibold uppercase tracking-wider text-amber-800 mb-3">
        <span>{cat}</span> · <span>{read_time}</span>
      </div>
      <h1 class="text-3xl sm:text-4xl md:text-5xl font-extrabold text-brand-navy tracking-tight leading-tight mb-6">
        {title}
      </h1>
      <div class="flex items-center gap-4 text-sm text-slate-600">
        <div class="flex items-center gap-2.5">
          <img src="/assets/images/kelly-roper.jpg" alt="Kelly Roper" class="w-10 h-10 rounded-full object-cover border border-slate-300">
          <div>
            <p class="font-bold text-slate-900 leading-tight">Kelly Roper</p>
            <p class="text-xs text-slate-500">Therapist · Good Therapy Colorado</p>
          </div>
        </div>
        <span class="text-slate-300">•</span>
        <span>{date}</span>
      </div>
    </div>
  </header>

  <!-- Article Body -->
  <article class="py-16 px-4 sm:px-6 lg:px-8 max-w-3xl mx-auto">
    <div class="prose prose-lg max-w-none">
      {''.join(body_elements)}
    </div>

    <!-- Author Box -->
    <div class="mt-16 p-8 rounded-3xl bg-brand-50 border border-brand-200/80 flex flex-col sm:flex-row items-center sm:items-start gap-6">
      <img src="/assets/images/kelly-roper.jpg" alt="Kelly Roper" class="w-24 h-24 rounded-2xl object-cover shadow-sm flex-shrink-0">
      <div class="space-y-2 text-center sm:text-left">
        <h3 class="font-bold text-xl text-brand-navy">About Kelly Roper</h3>
        <p class="text-sm text-slate-600 leading-relaxed">
          Kelly Roper is a licensed therapist dedicated to supporting adults, children, and families with personalized care, Cognitive Behavioral Therapy (CBT), and mindfulness. In-person appointments available in Colorado Springs and telehealth in Colorado and Oklahoma.
        </p>
        <div class="pt-2">
          <a href="/contact-3/" class="inline-block text-xs font-bold uppercase tracking-wider text-brand-navy hover:underline">
            Reach out to Kelly →
          </a>
        </div>
      </div>
    </div>

    <!-- Bottom Navigation -->
    <div class="mt-12 pt-8 border-t border-slate-200 flex justify-between items-center text-sm">
      <a href="/blog/" class="font-semibold text-brand-navy hover:underline">
        ← Back to Blog
      </a>
      <a href="/contact-3/" class="bg-brand-navy text-white font-bold px-6 py-2.5 rounded-full hover:bg-brand-700 transition-colors text-xs uppercase tracking-wider">
        Let's Chat!
      </a>
    </div>
  </article>
"""
    footer = get_footer()
    return head + nav + content + footer

def generate_sitemap():
    urls = [
        ("https://www.goodtherapycolorado.com/", "2026-05-22", "1.0"),
        ("https://www.goodtherapycolorado.com/about-me", "2026-05-22", "0.8"),
        ("https://www.goodtherapycolorado.com/contact-3", "2026-05-22", "0.8"),
        ("https://www.goodtherapycolorado.com/faq", "2026-05-22", "0.7"),
        ("https://www.goodtherapycolorado.com/blog", "2026-05-22", "0.8"),
    ]
    for p in BLOG_POSTS:
        urls.append((f"https://www.goodtherapycolorado.com/post/{p['slug']}", "2024-11-01", "0.6"))

    xml = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for loc, lastmod, priority in urls:
        xml.append(f"""  <url>
    <loc>{loc}</loc>
    <lastmod>{lastmod}</lastmod>
    <priority>{priority}</priority>
  </url>""")
    xml.append('</urlset>')
    return '\n'.join(xml)

def generate_robots():
    return """User-agent: *
Allow: /

Sitemap: https://www.goodtherapycolorado.com/sitemap.xml
"""

def generate_redirects():
    # Cloudflare Pages _redirects file
    return """# Cloudflare Pages 301 redirects
/contact /contact-3 301
/contact/ /contact-3 301
/about /about-me 301
/about/ /about-me 301
"""

def main():
    print("Building static site for Good Therapy Colorado...")

    # 1. Homepage
    home_html = generate_home()
    with open(os.path.join(SITE_DIR, 'index.html'), 'w') as f:
        f.write(home_html)
    print("✓ index.html")

    # 2. About
    about_dir = os.path.join(SITE_DIR, 'about-me')
    os.makedirs(about_dir, exist_ok=True)
    about_html = generate_about()
    with open(os.path.join(about_dir, 'index.html'), 'w') as f:
        f.write(about_html)
    with open(os.path.join(SITE_DIR, 'about-me.html'), 'w') as f:
        f.write(about_html)
    print("✓ about-me/index.html & about-me.html")

    # 3. Contact (both /contact-3 and /contact)
    contact_dir = os.path.join(SITE_DIR, 'contact-3')
    os.makedirs(contact_dir, exist_ok=True)
    contact_html = generate_contact()
    with open(os.path.join(contact_dir, 'index.html'), 'w') as f:
        f.write(contact_html)
    with open(os.path.join(SITE_DIR, 'contact-3.html'), 'w') as f:
        f.write(contact_html)
    
    # Also support /contact/
    alt_contact_dir = os.path.join(SITE_DIR, 'contact')
    os.makedirs(alt_contact_dir, exist_ok=True)
    with open(os.path.join(alt_contact_dir, 'index.html'), 'w') as f:
        f.write(contact_html)
    print("✓ contact-3/ & contact/ pages")

    # 4. FAQ
    faq_dir = os.path.join(SITE_DIR, 'faq')
    os.makedirs(faq_dir, exist_ok=True)
    faq_html = generate_faq()
    with open(os.path.join(faq_dir, 'index.html'), 'w') as f:
        f.write(faq_html)
    with open(os.path.join(SITE_DIR, 'faq.html'), 'w') as f:
        f.write(faq_html)
    print("✓ faq/index.html & faq.html")

    # 5. Blog listing
    blog_dir = os.path.join(SITE_DIR, 'blog')
    os.makedirs(blog_dir, exist_ok=True)
    blog_html = generate_blog()
    with open(os.path.join(blog_dir, 'index.html'), 'w') as f:
        f.write(blog_html)
    with open(os.path.join(SITE_DIR, 'blog.html'), 'w') as f:
        f.write(blog_html)
    print("✓ blog/index.html & blog.html")

    # 6. Blog Posts
    for post in BLOG_POSTS:
        slug = post['slug']
        post_dir = os.path.join(SITE_DIR, 'post', slug)
        os.makedirs(post_dir, exist_ok=True)
        post_html = generate_post(post)
        with open(os.path.join(post_dir, 'index.html'), 'w') as f:
            f.write(post_html)
        print(f"✓ post/{slug}/index.html")

    # 7. Sitemap & Robots & Redirects
    with open(os.path.join(SITE_DIR, 'sitemap.xml'), 'w') as f:
        f.write(generate_sitemap())
    print("✓ sitemap.xml")

    with open(os.path.join(SITE_DIR, 'robots.txt'), 'w') as f:
        f.write(generate_robots())
    print("✓ robots.txt")

    with open(os.path.join(SITE_DIR, '_redirects'), 'w') as f:
        f.write(generate_redirects())
    print("✓ _redirects")

    print("\nAll pages generated successfully!")

if __name__ == '__main__':
    main()
