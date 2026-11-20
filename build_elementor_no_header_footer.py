import os, re

CDN_BASE = "https://htzaml-01.github.io/trust/"

# Output directories
os.makedirs("elementor", exist_ok=True)
os.makedirs("elementor/no-header-footer", exist_ok=True)

# Load CSS and JS
with open("styles.css", "r", encoding="utf-8") as f:
    css_content = f.read()

with open("script.js", "r", encoding="utf-8") as f:
    js_content = f.read()

# Replace asset URLs in CSS with CDN
css_cdn = re.sub(
    r'url\([\'"]?asset/([^\'")]+)[\'"]?\)',
    lambda m: f'url("{CDN_BASE}asset/{m.group(1)}")',
    css_content
)

PAGES = [
    ("index.html", "Home Page (Content Only)"),
    ("about.html", "About Us Page (Content Only)"),
    ("services.html", "Services Page (Content Only)"),
    ("industries.html", "Industries Page (Content Only)"),
    ("fleet.html", "Fleet Page (Content Only)"),
    ("contact.html", "Contact Page (Content Only)"),
]

def extract_main_content(html_file):
    with open(html_file, "r", encoding="utf-8") as f:
        html_raw = f.read()

    # Extract strictly from <main to </main>
    main_match = re.search(r'(<main[^>]*>.*?</main>)', html_raw, re.DOTALL)
    if main_match:
        content = main_match.group(1)
    else:
        # Fallback: strip header, backdrop, drawer, footer
        body_match = re.search(r'<body[^>]*>(.*?)</body>', html_raw, re.DOTALL)
        content = body_match.group(1) if body_match else html_raw
        content = re.sub(r'<header[^>]*>.*?</header>', '', content, flags=re.DOTALL)
        content = re.sub(r'<div[^>]*class=["\'][^"\']*mobile-nav-backdrop[^"\']*["\'][^>]*>.*?</div>', '', content, flags=re.DOTALL)
        content = re.sub(r'<div[^>]*class=["\'][^"\']*mobile-drawer[^"\']*["\'][^>]*>.*?</div>', '', content, flags=re.DOTALL)
        content = re.sub(r'<footer[^>]*>.*?</footer>', '', content, flags=re.DOTALL)

    # Strip script tags inside main if any
    content = re.sub(r'<script\s+src="script\.js[^"]*"[^>]*></script>', '', content)

    # Replace local asset/ paths with CDN
    content = re.sub(
        r'(src|href)=["\']asset/([^"\']+)["\']',
        lambda m: f'{m.group(1)}="{CDN_BASE}asset/{m.group(2)}"',
        content
    )

    # Convert .html links to WordPress clean permalinks
    content = re.sub(r'href=["\']index\.html["\']', 'href="/"', content)
    content = re.sub(r'href=["\']about\.html["\']', 'href="/about/"', content)
    content = re.sub(r'href=["\']services\.html["\']', 'href="/services/"', content)
    content = re.sub(r'href=["\']industries\.html["\']', 'href="/industries/"', content)
    content = re.sub(r'href=["\']fleet\.html["\']', 'href="/fleet/"', content)
    content = re.sub(r'href=["\']contact\.html["\']', 'href="/contact/"', content)

    # Specific anchor permalinks
    content = re.sub(r'href=["\']services\.html(#service-[0-9]+)["\']', r'href="/services/\1"', content)

    return content.strip()

def build_content_only_page(html_file, title_desc):
    body_content = extract_main_content(html_file)
    page_slug = os.path.splitext(html_file)[0]

    output = f"""<!--
==============================================================================
TRUST CORPORATION - ELEMENTOR CONTENT TEMPLATE (NO HEADER, NO FOOTER)
Page: {html_file} ({title_desc})
100% Edge-to-Edge Full Bleed | Zero White Edge Gaps | Content Only
WordPress Clean Permalinks: Home (/), About (/about/), Services (/services/),
Industries (/industries/), Fleet (/fleet/), Contact (/contact/)
All assets loaded via CDN: {CDN_BASE}
Ideal for: Elementor Theme Builder Header & Footer, or Default Theme Header/Footer
==============================================================================
-->

<!-- Google Fonts: Manrope -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet">

<style>
/* ==========================================================================
   COMPLETE FULL-SCREEN ZERO-GAP RESET (ELIMINATES ALL WHITE GAPS & MARGINS)
   ========================================================================== */
html,
body,
body.page,
body.page-template-default,
body.elementor-default,
body.elementor-page,
#page,
#content,
#primary,
#main,
.site,
.site-content,
.site-main,
.entry-content,
.post-inner,
.singular,
.hentry,
.elementor,
.elementor-section,
.elementor-section-wrap,
.elementor-container,
.elementor-column,
.elementor-column-wrap,
.elementor-widget-wrap,
.elementor-widget,
.elementor-widget-html,
.elementor-widget-container,
.elementor-element,
.elementor-element-populated,
.e-con,
.e-con-inner,
.e-con-boxed,
.e-con-full,
.e-parent {{
  margin: 0 !important;
  padding: 0 !important;
  border: 0 !important;
  outline: 0 !important;
  box-shadow: none !important;
  max-width: 100% !important;
  width: 100% !important;
  box-sizing: border-box !important;
  --padding-top: 0px !important;
  --padding-bottom: 0px !important;
  --padding-left: 0px !important;
  --padding-right: 0px !important;
  --gap: 0px !important;
  --container-widget-spacing: 0px !important;
  --widgets-spacing: 0px !important;
}}

html {{
  overflow-x: hidden !important;
}}

body {{
  overflow-x: hidden !important;
}}

.elementor-section.elementor-section-boxed > .elementor-container,
.elementor-section-boxed > .elementor-container,
.e-con-boxed > .e-con-inner {{
  max-width: 100% !important;
  width: 100% !important;
  padding: 0 !important;
  margin: 0 !important;
}}

/* Main container wrapper */
.elementor-trust-wrapper {{
  font-family: 'Manrope', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  color: #1a1a1c;
  line-height: 1.6;
  width: 100% !important;
  max-width: 100% !important;
  overflow-x: hidden !important;
  box-sizing: border-box !important;
  margin: 0 !important;
  padding: 0 !important;
  background-color: transparent;
}}

.elementor-trust-wrapper *,
.elementor-trust-wrapper *::before,
.elementor-trust-wrapper *::after {{
  box-sizing: border-box !important;
}}

/* Hero Section & Text Protection */
.elementor-trust-wrapper .hero-section {{
  position: relative !important;
  width: 100% !important;
  min-height: 100vh !important;
  height: auto !important;
  display: flex !important;
  flex-direction: column !important;
  justify-content: center !important;
  padding-top: 140px !important;
  padding-bottom: 80px !important;
  overflow: hidden !important;
  margin: 0 !important;
}}

.elementor-trust-wrapper .hero-line {{
  display: block !important;
  white-space: normal !important;
  word-break: normal !important;
}}

/* Strict Marquee & Partners Section Protection */
.elementor-trust-wrapper .section-brand-carousel {{
  position: relative !important;
  width: 100% !important;
  background-color: #ffffff !important;
  padding: 36px 0 28px !important;
  border-top: 1px solid #eeeeee !important;
  border-bottom: 1px solid #eeeeee !important;
  overflow: hidden !important;
  display: block !important;
  margin: 0 !important;
}}

.elementor-trust-wrapper .partners-title-wrap {{
  width: 100% !important;
  text-align: center !important;
  margin: 0 auto 22px auto !important;
  display: block !important;
  padding: 0 20px !important;
}}

.elementor-trust-wrapper .partners-eyebrow {{
  display: inline-block !important;
  font-size: 13px !important;
  font-weight: 700 !important;
  letter-spacing: 0.12em !important;
  text-transform: uppercase !important;
  color: #606068 !important;
}}

.elementor-trust-wrapper .partners-marquee-section {{
  position: relative !important;
  width: 100% !important;
  max-width: 100% !important;
  overflow: hidden !important;
  display: flex !important;
  align-items: center !important;
  padding: 0 !important;
  border: none !important;
  background: transparent !important;
  scrollbar-width: none !important;
}}

.elementor-trust-wrapper .partners-marquee-section::-webkit-scrollbar {{
  display: none !important;
}}

.elementor-trust-wrapper .marquee-track {{
  display: flex !important;
  width: max-content !important;
  overflow: visible !important;
  animation: marqueeScroll 26s linear infinite !important;
}}

.elementor-trust-wrapper .marquee-group {{
  display: flex !important;
  align-items: center !important;
  flex-shrink: 0 !important;
}}

.elementor-trust-wrapper .marquee-brand-item {{
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  padding: 0 42px !important;
  height: 52px !important;
  flex-shrink: 0 !important;
}}

.elementor-trust-wrapper .marquee-brand-item img {{
  height: 38px !important;
  max-height: 42px !important;
  width: auto !important;
  max-width: 160px !important;
  object-fit: contain !important;
  opacity: 1 !important;
  filter: none !important;
  display: block !important;
}}

/* Seamless Grid Rapet Protection */
.elementor-trust-wrapper .services-seamless-grid {{
  display: grid !important;
  grid-template-columns: repeat(3, minmax(0, 1fr)) !important;
  gap: 0 !important;
  width: 100% !important;
  margin: 0 !important;
  padding: 0 !important;
}}

.elementor-trust-wrapper .service-seamless-col {{
  display: flex !important;
  flex-direction: column !important;
  width: 100% !important;
  margin: 0 !important;
  padding: 0 !important;
  background-color: #ffffff !important;
}}

.elementor-trust-wrapper .service-col-media {{
  width: 100% !important;
  aspect-ratio: 1.50376 !important;
  overflow: hidden !important;
  margin: 0 !important;
  padding: 0 !important;
}}

.elementor-trust-wrapper .service-col-media img {{
  width: 100% !important;
  height: 100% !important;
  object-fit: cover !important;
  display: block !important;
}}

@media (max-width: 1024px) {{
  .elementor-trust-wrapper .services-seamless-grid {{
    grid-template-columns: repeat(2, 1fr) !important;
  }}
}}

@media (max-width: 768px) {{
  .elementor-trust-wrapper .services-seamless-grid {{
    grid-template-columns: 1fr !important;
  }}
}}

{css_cdn}
</style>

<!-- Main Page HTML Markup (Content Only: No Nav Menu & No Footer) -->
<div class="elementor-trust-wrapper elementor-content-only">
{body_content}
</div>

<!-- Interactive Scripts (FAQ Accordion, Marquee, Video Autoplay, Forms) -->
<script>
(function() {{
{js_content}

  // Newsletter handler
  const form = document.getElementById('newsletterForm');
  const status = document.getElementById('newsletterStatus');
  if (form && status) {{
    form.addEventListener('submit', function(e) {{
      e.preventDefault();
      status.style.display = 'block';
      status.style.color = '#10b981';
      status.textContent = 'Thank you for subscribing to TRUST Corporation updates!';
      form.reset();
    }});
  }}

  // Contact Page Form handler
  const contactForm = document.getElementById('contactPageForm');
  const contactStatus = document.getElementById('contactPageStatus');
  const submitBtn = document.getElementById('btnContactSubmit');

  if (contactForm && contactStatus) {{
    contactForm.addEventListener('submit', function(e) {{
      e.preventDefault();
      if (submitBtn) {{
        submitBtn.textContent = 'Transmitting Dispatch Request...';
        submitBtn.disabled = true;
      }}

      setTimeout(function() {{
        if (submitBtn) {{
          submitBtn.textContent = 'Request Sent!';
          submitBtn.style.background = '#059669';
        }}
        contactStatus.style.display = 'block';
        contactForm.reset();

        setTimeout(function() {{
          if (submitBtn) {{
            submitBtn.textContent = 'Submit Formal Request';
            submitBtn.disabled = false;
            submitBtn.style.background = '';
          }}
          contactStatus.style.display = 'none';
        }}, 6000);
      }}, 600);
    }});
  }}
}})();
</script>
"""

    # 1. Output to elementor/no-header-footer/elementor-{slug}.html
    path1 = f"elementor/no-header-footer/elementor-{page_slug}.html"
    with open(path1, "w", encoding="utf-8") as f:
        f.write(output)
    print(f"Generated {path1} ({len(output)} bytes)")

    # 2. Output to elementor/elementor-{slug}-no-nav-footer.html
    path2 = f"elementor/elementor-{page_slug}-no-nav-footer.html"
    with open(path2, "w", encoding="utf-8") as f:
        f.write(output)
    print(f"Generated {path2} ({len(output)} bytes)")

    # 3. Output to elementor/elementor-{slug}-content.html
    path3 = f"elementor/elementor-{page_slug}-content.html"
    with open(path3, "w", encoding="utf-8") as f:
        f.write(output)
    print(f"Generated {path3} ({len(output)} bytes)")


def build_elementor_header():
    """Separate standalone Elementor Theme Builder Header template."""
    with open("index.html", "r", encoding="utf-8") as f:
        html_raw = f.read()

    header_match = re.search(r'(<header\s+class="site-header"[^>]*>.*?</header>)', html_raw, re.DOTALL)
    if not header_match:
        print("Could not find header in index.html")
        return
    header_content = header_match.group(1)
    header_content = re.sub(
        r'(src|href)=["\']asset/([^"\']+)["\']',
        lambda m: f'{m.group(1)}="{CDN_BASE}asset/{m.group(2)}"',
        header_content
    )

    # Convert .html links
    header_content = re.sub(r'href=["\']index\.html["\']', 'href="/"', header_content)
    header_content = re.sub(r'href=["\']about\.html["\']', 'href="/about/"', header_content)
    header_content = re.sub(r'href=["\']services\.html["\']', 'href="/services/"', header_content)
    header_content = re.sub(r'href=["\']industries\.html["\']', 'href="/industries/"', header_content)
    header_content = re.sub(r'href=["\']fleet\.html["\']', 'href="/fleet/"', header_content)
    header_content = re.sub(r'href=["\']contact\.html["\']', 'href="/contact/"', header_content)

    output = f"""<!--
==============================================================================
TRUST CORPORATION - ELEMENTOR STANDALONE HEADER TEMPLATE (ZERO-GAP FULL BLEED)
Ideal for: Elementor Theme Builder Header Template
WordPress Clean Permalinks: Home (/), About (/about/), Services (/services/),
Industries (/industries/), Fleet (/fleet/), Contact (/contact/)
All assets loaded via CDN: {CDN_BASE}
==============================================================================
-->

<!-- Google Fonts: Manrope -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet">

<style>
/* Header Zero Gap Reset */
.elementor-section,
.elementor-container,
.elementor-column,
.elementor-widget-wrap,
.elementor-widget-container,
.e-con,
.e-con-inner,
.e-con-boxed,
.e-parent {{
  margin: 0 !important;
  padding: 0 !important;
  border: 0 !important;
  max-width: 100% !important;
  width: 100% !important;
  --padding-top: 0px !important;
  --padding-bottom: 0px !important;
  --padding-left: 0px !important;
  --padding-right: 0px !important;
  --gap: 0px !important;
}}

/* Header Logo Protection */
.elementor-trust-wrapper .brand-logo,
.elementor-trust-wrapper a.brand-logo {{
  display: inline-flex !important;
  align-items: center !important;
  height: 44px !important;
  max-height: 44px !important;
  text-decoration: none !important;
  flex-shrink: 0 !important;
}}

.elementor-trust-wrapper .logo-img,
.elementor-trust-wrapper img.logo-img {{
  height: 38px !important;
  max-height: 38px !important;
  width: auto !important;
  max-width: 130px !important;
  object-fit: contain !important;
  display: block !important;
}}

body.admin-bar .site-header,
.admin-bar .site-header {{
  top: 32px !important;
}}

@media screen and (max-width: 782px) {{
  body.admin-bar .site-header,
  .admin-bar .site-header {{
    top: 46px !important;
  }}
}}

{css_cdn}
</style>

<div class="elementor-trust-wrapper">
{header_content}
  <div class="mobile-nav-backdrop" id="navBackdrop"></div>
</div>

<script>
(function() {{
  const header = document.getElementById('siteHeader');
  function handleScroll() {{
    if (!header) return;
    if (window.scrollY > 40) {{
      header.classList.add('scrolled');
    }} else {{
      header.classList.remove('scrolled');
    }}
  }}
  window.addEventListener('scroll', handleScroll, {{ passive: true }});
  handleScroll();

  const mobileToggle = document.getElementById('mobileToggle');
  const navMenu = document.getElementById('navMenu');
  const navBackdrop = document.getElementById('navBackdrop');

  function closeMobileNav() {{
    navMenu?.classList.remove('open');
    mobileToggle?.classList.remove('active');
    header?.classList.remove('nav-open');
    navBackdrop?.classList.remove('open');
    document.body.style.overflow = '';
  }}

  function openMobileNav() {{
    navMenu?.classList.add('open');
    mobileToggle?.classList.add('active');
    header?.classList.add('nav-open');
    navBackdrop?.classList.add('open');
    document.body.style.overflow = 'hidden';
  }}

  if (mobileToggle) {{
    mobileToggle.addEventListener('click', function(e) {{
      e.preventDefault();
      if (navMenu?.classList.contains('open')) {{
        closeMobileNav();
      }} else {{
        openMobileNav();
      }}
    }});
  }}

  if (navBackdrop) {{
    navBackdrop.addEventListener('click', closeMobileNav);
  }}

  navMenu?.querySelectorAll('.nav-link').forEach(link => {{
    link.addEventListener('click', closeMobileNav);
  }});
}})();
</script>
"""
    out_name = "elementor/elementor-header.html"
    with open(out_name, "w", encoding="utf-8") as f:
        f.write(output)
    print(f"Generated {out_name} ({len(output)} bytes)")


def main():
    print("=" * 70)
    print("BUILDING ELEMENTOR PACK (NO NAV MENU & NO FOOTER - CONTENT ONLY)")
    print("=" * 70)

    for html_file, desc in PAGES:
        build_content_only_page(html_file, desc)

    # Also build standalone header for Theme Builder Header
    build_elementor_header()

    print("=" * 70)
    print("SUCCESS! All content-only Elementor templates have been generated.")
    print("=" * 70)

if __name__ == "__main__":
    main()
