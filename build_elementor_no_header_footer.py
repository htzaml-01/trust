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


def generate_header_template(mode="smart"):
    """
    mode: 'smart' (default - transparent on dark hero, solid white on subpages/blog),
          'transparent' (transparent at top, solid on scroll),
          'solid' (always solid white)
    """
    header_class = "site-header"
    if mode == "solid":
        header_class += " header-solid"

    CDN_LOGO = f"{CDN_BASE}asset/logo-trust.png"

    html_output = f"""<!--
==============================================================================
TRUST CORPORATION - ROYAL ELEMENTOR KIT / ELEMENTOR THEME BUILDER HEADER
Mode: {mode.upper()}
100% Responsive | Full Bleed Zero Margin | Mobile Slide Drawer | CDN Logo
Clean Permalinks: Home (/), About (/about/), Services (/services/),
Industries (/industries/), Fleet (/fleet/), Contact (/contact/)
Dynamic Active Page Detection | WP Admin Bar Compatible
==============================================================================
-->

<!-- Google Fonts: Manrope -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet">

<style>
/* ==========================================================================
   ROYAL ELEMENTOR KIT & ELEMENTOR FULL-WIDTH ZERO-GAP RESET
   ========================================================================== */
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

/* ==========================================================================
   STICKY NAVBAR - PURE FRAMER REPLICA
   ========================================================================== */
.site-header {{
  font-family: 'Manrope', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  width: 100% !important;
  margin: 0 !important;
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 99999;
  height: 92px;
  display: flex;
  align-items: center;
  background-color: transparent;
  border-bottom: 1px solid rgba(255, 255, 255, 0.14);
  box-shadow: none;
  box-sizing: border-box !important;
  transition: background-color 0.35s cubic-bezier(0.16, 1, 0.3, 1),
              border-color 0.35s ease,
              box-shadow 0.35s ease,
              height 0.3s ease;
}}

.site-header *,
.site-header *::before,
.site-header *::after {{
  box-sizing: border-box !important;
}}

/* Scrolled state: Solid clean white with subtle shadow */
.site-header.scrolled {{
  background-color: #ffffff !important;
  border-bottom: 1px solid rgba(0, 0, 0, 0.08) !important;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.06) !important;
  height: 84px;
}}

/* Nav open state: Solid clean white when mobile menu is open */
.site-header.nav-open {{
  background-color: #ffffff !important;
  border-bottom: 1px solid rgba(0, 0, 0, 0.08) !important;
}}

/* Solid mode (for pages with white hero / blog / subpages) */
.site-header.header-solid {{
  background-color: #ffffff !important;
  border-bottom: 1px solid rgba(0, 0, 0, 0.08) !important;
  box-shadow: 0 1px 12px rgba(0, 0, 0, 0.03) !important;
}}

.header-container {{
  width: 100%;
  max-width: 100%;
  margin: 0;
  padding: 0 44px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}}

/* Logo */
.site-header .brand-logo {{
  display: inline-flex !important;
  align-items: center !important;
  text-decoration: none !important;
  height: 44px !important;
  max-height: 44px !important;
  flex-shrink: 0 !important;
}}

.site-header .logo-img {{
  height: 38px !important;
  max-height: 38px !important;
  width: auto !important;
  max-width: 130px !important;
  object-fit: contain !important;
  display: block !important;
}}

/* Right side navigation */
.site-header .header-right {{
  display: flex;
  align-items: center;
  gap: 36px;
}}

.site-header .nav-menu {{
  display: flex;
  align-items: center;
  gap: 30px;
  margin: 0;
  padding: 0;
  list-style: none;
}}

.site-header .nav-link {{
  font-family: 'Manrope', sans-serif;
  font-size: 15px;
  font-weight: 500;
  color: #ffffff;
  display: inline-flex;
  align-items: center;
  position: relative;
  padding: 6px 0;
  text-decoration: none !important;
  background: transparent;
  border: none;
  transition: color 0.25s ease;
  line-height: 1.2;
}}

.site-header .nav-link::after {{
  content: "";
  position: absolute;
  bottom: -2px;
  left: 0;
  width: 100%;
  height: 2px;
  background-color: #ffffff;
  opacity: 0;
  transform: scaleX(0);
  transform-origin: center;
  transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1),
              opacity 0.25s ease,
              background-color 0.25s ease;
}}

.site-header .nav-link:hover::after,
.site-header .nav-link.active::after {{
  opacity: 1 !important;
  transform: scaleX(1) !important;
}}

.site-header .nav-link:hover,
.site-header .nav-link.active {{
  color: #ffffff;
}}

/* Scrolled Nav Link Colors: Dark text + Dark Underline */
.site-header.scrolled .nav-link,
.site-header.header-solid .nav-link {{
  color: #1a1a1c !important;
}}

.site-header.scrolled .nav-link:hover,
.site-header.scrolled .nav-link.active,
.site-header.header-solid .nav-link:hover,
.site-header.header-solid .nav-link.active {{
  color: #1a1a1c !important;
}}

.site-header.scrolled .nav-link::after,
.site-header.header-solid .nav-link::after {{
  background-color: #1a1a1c !important;
}}

/* Mobile Toggle Hamburger Button */
.site-header .mobile-toggle {{
  display: none;
  background: transparent;
  border: none;
  cursor: pointer;
  padding: 8px;
  width: 44px;
  height: 44px;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  gap: 5px;
  z-index: 100001;
  touch-action: manipulation;
  -webkit-tap-highlight-color: transparent;
}}

.site-header .mobile-toggle span {{
  display: block;
  width: 22px;
  height: 2px;
  background-color: #ffffff;
  pointer-events: none;
  transition: background-color 0.2s ease, transform 0.2s ease, opacity 0.2s ease;
}}

.site-header.scrolled .mobile-toggle span,
.site-header.nav-open .mobile-toggle span,
.site-header.header-solid .mobile-toggle span,
.site-header .mobile-toggle.active span {{
  background-color: #1a1a1c !important;
}}

.site-header .mobile-toggle.active span:nth-child(1) {{
  transform: translateY(7px) rotate(45deg);
}}

.site-header .mobile-toggle.active span:nth-child(2) {{
  opacity: 0;
}}

.site-header .mobile-toggle.active span:nth-child(3) {{
  transform: translateY(-7px) rotate(-45deg);
}}

/* Backdrop for Mobile Drawer */
.mobile-nav-backdrop {{
  display: none;
  position: fixed;
  top: 72px;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.4);
  z-index: 99998;
  touch-action: manipulation;
}}

.mobile-nav-backdrop.open {{
  display: block !important;
}}

/* ==========================================================================
   MOBILE & TABLET RESPONSIVE (MAX-WIDTH: 1024PX)
   ========================================================================== */
@media (max-width: 1024px) {{
  .site-header {{
    height: 72px;
  }}

  .site-header.scrolled {{
    height: 72px !important;
  }}

  .header-container {{
    padding: 0 20px;
  }}

  .site-header .logo-img {{
    height: 32px !important;
    max-height: 32px !important;
    max-width: 110px !important;
  }}

  .site-header .mobile-toggle {{
    display: flex !important;
  }}

  /* Mobile Drawer Menu (Slides in from right) */
  .site-header .nav-menu {{
    position: fixed;
    top: 72px;
    right: 0 !important;
    left: auto !important;
    width: 270px;
    max-width: 80vw;
    height: calc(100vh - 72px);
    background-color: #ffffff;
    flex-direction: column;
    align-items: flex-start;
    text-align: left;
    padding: 36px 30px;
    gap: 22px;
    box-shadow: -8px 0 28px rgba(0, 0, 0, 0.12);
    display: flex;
    visibility: hidden;
    pointer-events: none;
    transform: translateX(100%);
    transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1), visibility 0.3s ease;
    z-index: 100000;
    overflow-y: auto;
    -webkit-overflow-scrolling: touch;
  }}

  .site-header .nav-menu.open {{
    visibility: visible !important;
    pointer-events: auto !important;
    transform: translateX(0) !important;
  }}

  .site-header .nav-link {{
    color: #1a1a1c !important;
    font-size: 16px;
    font-weight: 500;
    width: auto;
    align-self: flex-start;
    justify-content: flex-start;
    padding: 6px 0;
  }}

  .site-header .nav-link::after {{
    background-color: #1a1a1c !important;
  }}
}}

/* ==========================================================================
   WORDPRESS ADMIN BAR COMPATIBILITY
   ========================================================================== */
body.admin-bar .site-header {{
  top: 32px !important;
}}

body.admin-bar .site-header .nav-menu {{
  top: 104px !important;
  height: calc(100vh - 104px) !important;
}}

body.admin-bar .mobile-nav-backdrop {{
  top: 104px !important;
}}

@media screen and (max-width: 782px) {{
  body.admin-bar .site-header {{
    top: 46px !important;
  }}

  body.admin-bar .site-header .nav-menu {{
    top: 118px !important;
    height: calc(100vh - 118px) !important;
  }}

  body.admin-bar .mobile-nav-backdrop {{
    top: 118px !important;
  }}
}}
</style>

<!-- ==========================================================================
     NAVBAR HTML MARKUP
     ========================================================================== -->
<header class="{header_class}" id="siteHeader">
  <div class="header-container">
    <a href="/" class="brand-logo" aria-label="TRUST Corporation Home">
      <img src="{CDN_LOGO}" alt="TRUST EADYRA LINE" class="logo-img" width="102" height="38" />
    </a>

    <div class="header-right">
      <nav class="nav-menu" id="navMenu">
        <a href="/" class="nav-link">Home</a>
        <a href="/about/" class="nav-link">About</a>
        <a href="/services/" class="nav-link">Services</a>
        <a href="/industries/" class="nav-link">Industries</a>
        <a href="/fleet/" class="nav-link">Fleet</a>
        <a href="/contact/" class="nav-link">Contact</a>
      </nav>

      <button class="mobile-toggle" id="mobileToggle" aria-label="Toggle Navigation">
        <span></span>
        <span></span>
        <span></span>
      </button>
    </div>
  </div>
</header>

<div class="mobile-nav-backdrop" id="navBackdrop"></div>

<!-- ==========================================================================
     INTERACTIVE SCRIPT (SCROLL, ACTIVE LINK DETECTION & MOBILE DRAWER)
     ========================================================================== -->
<script>
(function() {{
  const header = document.getElementById('siteHeader');
  const mobileToggle = document.getElementById('mobileToggle');
  const navMenu = document.getElementById('navMenu');
  const navBackdrop = document.getElementById('navBackdrop');

  if (!header) return;

  // 1. SMART ADAPTIVE HEADER (Detects dark hero vs white page / blog)
  const isSolidByDefault = header.classList.contains('header-solid');
  function checkHeroPresence() {{
    if (isSolidByDefault) return;
    const hasDarkHero = document.querySelector('.hero-section, .hero-video-bg, .section-about-hero, .section-services-hero');
    if (!hasDarkHero) {{
      header.classList.add('header-solid');
      // If normal page without hero padding, add top clearance
      if (!document.body.classList.contains('has-header-clearance')) {{
        document.body.classList.add('has-header-clearance');
        const currentPad = parseInt(window.getComputedStyle(document.body).paddingTop, 10) || 0;
        document.body.style.paddingTop = (currentPad + header.offsetHeight) + 'px';
      }}
    }}
  }}
  checkHeroPresence();
  window.addEventListener('load', checkHeroPresence);

  // 2. STICKY SCROLL BEHAVIOR
  function handleScroll() {{
    if (window.scrollY > 40) {{
      header.classList.add('scrolled');
    }} else {{
      header.classList.remove('scrolled');
    }}
  }}
  window.addEventListener('scroll', handleScroll, {{ passive: true }});
  window.addEventListener('touchmove', handleScroll, {{ passive: true }});
  handleScroll();

  // 3. DYNAMIC ACTIVE PAGE LINK HIGHLIGHTING
  try {{
    const currentPath = window.location.pathname.replace(/\\/+$/, '') || '/';
    const navLinks = header.querySelectorAll('.nav-link');
    let matched = false;

    navLinks.forEach(link => {{
      const linkPath = new URL(link.href, window.location.origin).pathname.replace(/\\/+$/, '') || '/';
      if (linkPath === currentPath) {{
        link.classList.add('active');
        matched = true;
      }} else {{
        link.classList.remove('active');
      }}
    }});

    // Fallback: If on homepage
    if (!matched && (currentPath === '/' || currentPath === '')) {{
      const homeLink = header.querySelector('.nav-link[href="/"]');
      if (homeLink) homeLink.classList.add('active');
    }}
  }} catch(e) {{
    console.warn('Nav active link detection:', e);
  }}

  // 4. MOBILE DRAWER CONTROLS
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

  function toggleMobileNav(e) {{
    if (e) {{
      e.preventDefault();
      e.stopPropagation();
    }}
    if (navMenu?.classList.contains('open')) {{
      closeMobileNav();
    }} else {{
      openMobileNav();
    }}
  }}

  if (mobileToggle) {{
    mobileToggle.addEventListener('click', toggleMobileNav);
    mobileToggle.addEventListener('touchend', function(e) {{
      e.preventDefault();
      toggleMobileNav(e);
    }}, {{ passive: false }});
  }}

  if (navBackdrop) {{
    navBackdrop.addEventListener('click', function(e) {{
      e.preventDefault();
      closeMobileNav();
    }});
    navBackdrop.addEventListener('touchend', function(e) {{
      e.preventDefault();
      closeMobileNav();
    }}, {{ passive: false }});
  }}

  // Close when clicking nav link
  header.querySelectorAll('.nav-link').forEach(link => {{
    link.addEventListener('click', closeMobileNav);
  }});

  // Close on Escape key
  document.addEventListener('keydown', function(e) {{
    if (e.key === 'Escape' && navMenu?.classList.contains('open')) {{
      closeMobileNav();
    }}
  }});
}})();
</script>
"""
    return html_output


def build_elementor_headers():
    """Build dedicated standalone navbar templates for Royal Elementor Kit Theme Builder."""
    # 1. Smart Adaptive Nav (default for Theme Builder Header)
    smart_nav = generate_header_template(mode="smart")
    with open("elementor/elementor-nav.html", "w", encoding="utf-8") as f:
        f.write(smart_nav)
    with open("elementor/elementor-header.html", "w", encoding="utf-8") as f:
        f.write(smart_nav)
    print("Generated elementor/elementor-nav.html & elementor/elementor-header.html")

    # 2. Transparent Nav (specifically for transparent hero / Home)
    trans_nav = generate_header_template(mode="transparent")
    with open("elementor/elementor-nav-transparent.html", "w", encoding="utf-8") as f:
        f.write(trans_nav)
    print("Generated elementor/elementor-nav-transparent.html")

    # 3. Solid White Nav (specifically for white subpages / blog)
    solid_nav = generate_header_template(mode="solid")
    with open("elementor/elementor-nav-solid.html", "w", encoding="utf-8") as f:
        f.write(solid_nav)
    print("Generated elementor/elementor-nav-solid.html")


def main():
    print("=" * 70)
    print("BUILDING ELEMENTOR PACK (NO NAV MENU & NO FOOTER - CONTENT ONLY)")
    print("=" * 70)

    for html_file, desc in PAGES:
        build_content_only_page(html_file, desc)

    # Also build standalone headers for Royal Elementor Kit Theme Builder
    build_elementor_headers()

    print("=" * 70)
    print("SUCCESS! All content-only Elementor templates have been generated.")
    print("=" * 70)

if __name__ == "__main__":
    main()
