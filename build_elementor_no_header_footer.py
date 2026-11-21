import os, re

CDN_BASE = "https://htzaml-01.github.io/trust/"

os.makedirs("elementor", exist_ok=True)

with open("styles.css", "r", encoding="utf-8") as f:
    css_content = f.read()

with open("script.js", "r", encoding="utf-8") as f:
    js_content = f.read()

css_cdn = re.sub(
    r'url\([\'"]?asset/([^\'")]+)[\'"]?\)',
    lambda m: f'url("{CDN_BASE}asset/{m.group(1)}")',
    css_content
)

PAGES = [
    ("index.html", "03-PAGE-HOME.html", "Home Page"),
    ("about.html", "04-PAGE-ABOUT.html", "About Us Page"),
    ("services.html", "05-PAGE-SERVICES.html", "Services Page"),
    ("industries.html", "06-PAGE-INDUSTRIES.html", "Industries Page"),
    ("blog.html", "07-PAGE-BLOG.html", "Blog Page"),
    ("contact.html", "08-PAGE-CONTACT.html", "Contact Page"),
]

def extract_main_content(html_file):
    with open(html_file, "r", encoding="utf-8") as f:
        html_raw = f.read()

    main_match = re.search(r'(<main[^>]*>.*?</main>)', html_raw, re.DOTALL)
    if main_match:
        content = main_match.group(1)
    else:
        body_match = re.search(r'<body[^>]*>(.*?)</body>', html_raw, re.DOTALL)
        content = body_match.group(1) if body_match else html_raw
        content = re.sub(r'<header[^>]*>.*?</header>', '', content, flags=re.DOTALL)
        content = re.sub(r'<div[^>]*class=["\'][^"\']*mobile-nav-backdrop[^"\']*["\'][^>]*>.*?</div>', '', content, flags=re.DOTALL)
        content = re.sub(r'<div[^>]*class=["\'][^"\']*mobile-drawer[^"\']*["\'][^>]*>.*?</div>', '', content, flags=re.DOTALL)
        content = re.sub(r'<footer[^>]*>.*?</footer>', '', content, flags=re.DOTALL)

    # Strip red circle action buttons on all pages except blog
    if html_file != "blog.html":
        content = re.sub(
            r'<a\s+[^>]*class=["\'][^"\']*(?:circle-action-btn|circle-action-btn-red|circle-action-btn-white)[^"\']*["\'][^>]*>.*?</a>\s*',
            '',
            content,
            flags=re.DOTALL
        )

    content = re.sub(r'<script\s+src="script\.js[^"]*"[^>]*></script>', '', content)

    content = re.sub(
        r'(src|href)=["\']asset/([^"\']+)["\']',
        lambda m: f'{m.group(1)}="{CDN_BASE}asset/{m.group(2)}"',
        content
    )

    content = re.sub(r'href=["\']index\.html["\']', 'href="/"', content)
    content = re.sub(r'href=["\']about\.html["\']', 'href="/about/"', content)
    content = re.sub(r'href=["\']services\.html["\']', 'href="/services/"', content)
    content = re.sub(r'href=["\']industries\.html["\']', 'href="/industries/"', content)
    content = re.sub(r'href=["\']fleet\.html["\']', 'href="/fleet/"', content)
    content = re.sub(r'href=["\']blog\.html["\']', 'href="/blog/"', content)
    content = re.sub(r'href=["\']contact\.html["\']', 'href="/contact/"', content)
    content = re.sub(r'href=["\']services\.html(#service-[0-9]+)["\']', r'href="/services/\1"', content)

    return content.strip()

def build_content_only_page(html_file, out_name, title_desc):
    body_content = extract_main_content(html_file)

    output = f"""<!--
==============================================================================
TRUST CORPORATION - ELEMENTOR CONTENT TEMPLATE (NO HEADER, NO FOOTER)
File: {out_name} ({title_desc})
100% Edge-to-Edge Full Bleed | Zero White Edge Gaps | Content Only
Clean Permalinks: Home (/), About (/about/), Services (/services/),
Industries (/industries/), Blog (/blog/), Contact (/contact/)
All assets loaded via CDN: {CDN_BASE}
Paste into: Page Editor (Elementor Full Width)
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
  max-width: 100vw !important;
  background-color: #ffffff !important;
  padding: 36px 0 28px !important;
  border-top: 1px solid #eeeeee !important;
  border-bottom: 1px solid #eeeeee !important;
  overflow: hidden !important;
  overflow-x: clip !important;
  contain: paint !important;
  display: block !important;
  margin: 0 !important;
  box-sizing: border-box !important;
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
  overflow-x: clip !important;
  contain: paint !important;
  display: flex !important;
  align-items: center !important;
  padding: 0 !important;
  border: none !important;
  background: transparent !important;
  scrollbar-width: none !important;
  box-sizing: border-box !important;
}}

.elementor-trust-wrapper .partners-marquee-section::-webkit-scrollbar {{
  display: none !important;
}}

.elementor-trust-wrapper .marquee-track {{
  display: flex !important;
  width: max-content !important;
  overflow: visible !important;
  contain: layout !important;
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

<!-- Interactive Content Scripts (FAQ Accordion, Marquee Carousel, Forms - Header Excluded) -->
<script>
(function() {{
  // 1. FAQ ACCORDION (1 open at a time or toggle)
  const accordionItems = document.querySelectorAll('.accordion-item');
  accordionItems.forEach(item => {{
    const headerBtn = item.querySelector('.accordion-header');
    if (headerBtn) {{
      headerBtn.addEventListener('click', (e) => {{
        e.preventDefault();
        const isActive = item.classList.contains('active');

        // Close all other accordion items
        accordionItems.forEach(other => {{
          if (other !== item) {{
            other.classList.remove('active');
            other.querySelector('.accordion-header')?.setAttribute('aria-expanded', 'false');
          }}
        }});

        // Toggle current item
        if (isActive) {{
          item.classList.remove('active');
          headerBtn.setAttribute('aria-expanded', 'false');
        }} else {{
          item.classList.add('active');
          headerBtn.setAttribute('aria-expanded', 'true');
        }}
      }});
    }}
  }});

  // 2. BULLETPROOF INFINITE MARQUEE CAROUSEL RUNNER
  function initMarqueeCarousel() {{
    const marquees = document.querySelectorAll('.partners-marquee-section');
    marquees.forEach(section => {{
      const track = section.querySelector('.marquee-track');
      if (!track || track.dataset.marqueeInitialized) return;
      track.dataset.marqueeInitialized = 'true';

      const groups = track.querySelectorAll('.marquee-group');
      if (groups.length === 1) {{
        track.appendChild(groups[0].cloneNode(true));
      }}

      let paused = false;
      let pos = 0;
      const speed = 0.9;

      track.addEventListener('mouseenter', () => {{ paused = true; }});
      track.addEventListener('mouseleave', () => {{ paused = false; }});
      track.addEventListener('touchstart', () => {{ paused = true; }}, {{ passive: true }});
      track.addEventListener('touchend', () => {{ paused = false; }}, {{ passive: true }});

      function step() {{
        if (!paused) {{
          pos += speed;
          const firstGroup = track.querySelector('.marquee-group');
          const groupWidth = firstGroup ? firstGroup.offsetWidth : 1200;
          if (pos >= groupWidth) {{
            pos -= groupWidth;
          }}
          track.style.transform = 'translate3d(' + (-pos) + 'px, 0, 0)';
        }}
        requestAnimationFrame(step);
      }}
      requestAnimationFrame(step);
    }});
  }}
  initMarqueeCarousel();
  window.addEventListener('load', initMarqueeCarousel);

  // 3. NEWSLETTER FORM FEEDBACK
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

  // 4. CONTACT PAGE FORM HANDLER
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
    target_path = os.path.join("elementor", out_name)
    with open(target_path, "w", encoding="utf-8") as f:
        f.write(output)
    print(f"Generated {target_path} ({len(output)} bytes)")


def generate_header_template():
    CDN_LOGO = f"{CDN_BASE}asset/logo-trust.png"
    return f"""<!--
==============================================================================
TRUST CORPORATION - ROYAL ELEMENTOR KIT / THEME BUILDER HEADER
File: 01-HEADER.html
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
   STICKY NAVBAR
   ========================================================================== */
.site-header {{
  font-family: 'Manrope', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  width: 100% !important;
  margin: 0 !important;
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 1000000 !important;
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
  background: transparent !important;
  border: none !important;
  cursor: pointer !important;
  padding: 8px !important;
  width: 48px !important;
  height: 48px !important;
  align-items: center !important;
  justify-content: center !important;
  flex-direction: column !important;
  gap: 5px !important;
  z-index: 1000002 !important;
  pointer-events: auto !important;
  touch-action: manipulation !important;
  -webkit-tap-highlight-color: transparent !important;
  position: relative !important;
}}

.site-header .mobile-toggle span {{
  display: block !important;
  width: 24px !important;
  height: 2px !important;
  background-color: #1a1a1c !important;
  pointer-events: none !important;
  transition: background-color 0.2s ease, transform 0.2s ease, opacity 0.2s ease !important;
}}

.site-header.scrolled .mobile-toggle span,
.site-header.nav-open .mobile-toggle span,
.site-header.header-solid .mobile-toggle span,
.site-header .mobile-toggle.active span {{
  background-color: #1a1a1c !important;
}}

.site-header .mobile-toggle.active span:nth-child(1) {{
  transform: translateY(7px) rotate(45deg) !important;
}}

.site-header .mobile-toggle.active span:nth-child(2) {{
  opacity: 0 !important;
}}

.site-header .mobile-toggle.active span:nth-child(3) {{
  transform: translateY(-7px) rotate(-45deg) !important;
}}

/* Backdrop for Mobile Drawer */
.mobile-nav-backdrop {{
  display: none;
  position: fixed !important;
  top: 0 !important;
  left: 0 !important;
  right: 0 !important;
  bottom: 0 !important;
  width: 100vw !important;
  height: 100vh !important;
  height: 100dvh !important;
  background-color: rgba(0, 0, 0, 0.45) !important;
  z-index: 999990 !important;
  touch-action: manipulation !important;
}}

.mobile-nav-backdrop.open {{
  display: block !important;
}}

/* Mobile Responsive */
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

  .site-header .nav-menu {{
    position: fixed !important;
    top: 72px !important;
    right: 0 !important;
    left: auto !important;
    width: 280px !important;
    max-width: 85vw !important;
    height: calc(100vh - 72px) !important;
    height: calc(100dvh - 72px) !important;
    background-color: #ffffff !important;
    flex-direction: column !important;
    align-items: flex-start !important;
    text-align: left !important;
    padding: 30px 20px !important;
    gap: 6px !important;
    box-shadow: -8px 0 28px rgba(0, 0, 0, 0.15) !important;
    display: flex !important;
    visibility: hidden !important;
    pointer-events: none !important;
    transform: translateX(100%) !important;
    transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1), visibility 0.3s ease !important;
    z-index: 1000001 !important;
    overflow-y: auto !important;
    -webkit-overflow-scrolling: touch !important;
  }}

  .site-header .nav-menu.open {{
    visibility: visible !important;
    pointer-events: auto !important;
    transform: translateX(0) !important;
  }}

  .site-header .nav-link {{
    color: #1a1a1c !important;
    font-size: 17px !important;
    font-weight: 600 !important;
    width: 100% !important;
    display: flex !important;
    align-items: center !important;
    justify-content: flex-start !important;
    padding: 14px 18px !important;
    border-radius: 8px !important;
    box-sizing: border-box !important;
    cursor: pointer !important;
    text-decoration: none !important;
    touch-action: manipulation !important;
    pointer-events: auto !important;
    -webkit-tap-highlight-color: rgba(186, 20, 26, 0.1) !important;
  }}

  .site-header .nav-link:hover,
  .site-header .nav-link:active {{
    background-color: #f1f5f9 !important;
    color: #ba141a !important;
  }}

  .site-header .nav-link::after {{
    background-color: #1a1a1c !important;
  }}
}}

/* WordPress Admin Bar Compatibility */
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

<header class="site-header" id="siteHeader">
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
        <a href="/blog/" class="nav-link">Blog</a>
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

<script>
(function() {{
  const header = document.getElementById('siteHeader');
  const mobileToggle = document.getElementById('mobileToggle');
  const navMenu = document.getElementById('navMenu');
  const navBackdrop = document.getElementById('navBackdrop');

  if (!header) return;

  // 1. SMART ADAPTIVE HEADER
  function checkHeroPresence() {{
    const hasDarkHero = document.querySelector('.hero-section, .hero-video-bg, .section-about-hero, .section-services-hero');
    if (!hasDarkHero) {{
      header.classList.add('header-solid');
      if (!document.body.classList.contains('has-header-clearance')) {{
        document.body.classList.add('has-header-clearance');
        const currentPad = parseInt(window.getComputedStyle(document.body).paddingTop, 10) || 0;
        document.body.style.paddingTop = (currentPad + header.offsetHeight) + 'px';
      }}
    }}
  }}
  checkHeroPresence();
  window.addEventListener('load', checkHeroPresence);

  // 2. STICKY SCROLL
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

  // 3. DYNAMIC ACTIVE PAGE LINK
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

    if (!matched && (currentPath === '/' || currentPath === '')) {{
      const homeLink = header.querySelector('.nav-link[href="/"]');
      if (homeLink) homeLink.classList.add('active');
    }}
  }} catch(e) {{
    console.warn('Nav active link detection:', e);
  }}

  // 4. MOBILE DRAWER
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

  let lastToggleTime = 0;
  function toggleMobileNav(e) {{
    if (e) {{
      e.preventDefault();
      e.stopPropagation();
      if (e.stopImmediatePropagation) e.stopImmediatePropagation();
    }}
    const now = Date.now();
    // 450ms cooldown prevents mobile touchend + synthetic click double-fire
    if (now - lastToggleTime < 450) return;
    lastToggleTime = now;

    if (navMenu?.classList.contains('open')) {{
      closeMobileNav();
    }} else {{
      openMobileNav();
    }}
  }}

  if (mobileToggle) {{
    // capture: true intercepts the click FIRST and terminates duplicate listeners with stopImmediatePropagation
    mobileToggle.addEventListener('click', toggleMobileNav, {{ capture: true }});
    mobileToggle.addEventListener('touchend', toggleMobileNav, {{ capture: true, passive: false }});
  }}

  if (navBackdrop) {{
    function handleBackdrop(e) {{
      if (e.target === navBackdrop) {{
        e.preventDefault();
        closeMobileNav();
      }}
    }}
    navBackdrop.addEventListener('click', handleBackdrop);
    navBackdrop.addEventListener('touchend', handleBackdrop, {{ passive: false }});
  }}

  if (navMenu) {{
    navMenu.addEventListener('click', function(e) {{
      // Stop clicks inside drawer from reaching backdrop
      e.stopPropagation();
    }});
    navMenu.addEventListener('touchend', function(e) {{
      // Stop touches inside drawer from reaching backdrop
      e.stopPropagation();
    }}, {{ passive: true }});
  }}

  // 5. BULLETPROOF LINK NAVIGATION (CAPTURE PHASE)
  // Intercepts any click on .nav-link in capture phase BEFORE any page script can hide the menu or cancel navigation!
  document.addEventListener('click', function(e) {{
    const link = e.target.closest('#siteHeader .nav-link, #navMenu .nav-link, .site-header .nav-link');
    if (!link) return;

    const href = link.getAttribute('href');
    if (!href) return;

    // In-page hash anchor (#services, #contact)
    if (href.startsWith('#')) {{
      closeMobileNav();
      return;
    }}

    // If clicking current page: just close drawer
    try {{
      const targetUrl = new URL(link.href, window.location.origin);
      const currentUrl = new URL(window.location.href);
      if (targetUrl.pathname.replace(/\\/+$/, '') === currentUrl.pathname.replace(/\\/+$/, '')) {{
        closeMobileNav();
        return;
      }}
    }} catch(err) {{}}

    // For page navigation (/about/, /services/, /contact/, etc.):
    // STOP all conflicting scripts from running or hiding the menu prematurely!
    e.preventDefault();
    e.stopPropagation();
    if (e.stopImmediatePropagation) e.stopImmediatePropagation();

    // Directly navigate without hindrance
    window.location.href = link.href;
  }}, true); // TRUE = CAPTURE PHASE! Runs FIRST before ANY other listener!

  document.addEventListener('keydown', function(e) {{
    if (e.key === 'Escape' && navMenu?.classList.contains('open')) {{
      closeMobileNav();
    }}
  }});
}})();
</script>
"""

def generate_footer_template():
    with open("index.html", "r", encoding="utf-8") as f:
        html_raw = f.read()

    footer_match = re.search(r'(<footer\s+class="site-footer">.*?</footer>)', html_raw, re.DOTALL)
    if not footer_match:
        return ""
    footer_content = footer_match.group(1)
    footer_content = re.sub(r'(src|href)=["\']asset/([^"\']+)["\']', lambda m: f'{m.group(1)}="{CDN_BASE}asset/{m.group(2)}"', footer_content)

    footer_content = re.sub(r'href=["\']index\.html["\']', 'href="/"', footer_content)
    footer_content = re.sub(r'href=["\']about\.html["\']', 'href="/about/"', footer_content)
    footer_content = re.sub(r'href=["\']services\.html["\']', 'href="/services/"', footer_content)
    footer_content = re.sub(r'href=["\']industries\.html["\']', 'href="/industries/"', footer_content)
    footer_content = re.sub(r'href=["\']fleet\.html["\']', 'href="/fleet/"', footer_content)
    footer_content = re.sub(r'href=["\']blog\.html["\']', 'href="/blog/"', footer_content)
    footer_content = re.sub(r'href=["\']contact\.html["\']', 'href="/contact/"', footer_content)
    footer_content = re.sub(r'href=["\']services\.html(#service-[0-9]+)["\']', r'href="/services/\1"', footer_content)

    return f"""<!--
==============================================================================
TRUST CORPORATION - ELEMENTOR STANDALONE FOOTER TEMPLATE
File: 02-FOOTER.html
WordPress Clean Permalinks: Home (/), About (/about/), Services (/services/),
Industries (/industries/), Blog (/blog/), Contact (/contact/)
All assets loaded via CDN: {CDN_BASE}
==============================================================================
-->

<!-- Google Fonts: Manrope -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet">

<style>
/* Zero Gap Reset for Footer */
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

.elementor-trust-wrapper .footer-brand-link,
.elementor-trust-wrapper .footer-logo-wrap,
.elementor-trust-wrapper a.footer-brand-link,
.elementor-trust-wrapper a.footer-logo-wrap,
a.footer-brand-link {{
  display: inline-block !important;
  margin-bottom: 24px !important;
  text-decoration: none !important;
  flex-shrink: 0 !important;
  max-width: 130px !important;
}}

.elementor-trust-wrapper .footer-logo-img,
.elementor-trust-wrapper img.footer-logo-img,
img.footer-logo-img {{
  height: 38px !important;
  max-height: 38px !important;
  width: auto !important;
  max-width: 130px !important;
  display: block !important;
  object-fit: contain !important;
}}

{css_cdn}
</style>

<div class="elementor-trust-wrapper">
{footer_content}
</div>

<script>
(function() {{
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
}})();
</script>
"""

def main():
    print("=" * 70)
    print("BUILDING CLEAN ELEMENTOR PACK (EXACTLY 8 NUMBERED FILES)")
    print("=" * 70)

    # Clean existing elementor/ dir of obsolete files
    valid_names = {"01-HEADER.html", "02-FOOTER.html", "03-PAGE-HOME.html", "04-PAGE-ABOUT.html", 
                   "05-PAGE-SERVICES.html", "06-PAGE-INDUSTRIES.html", "07-PAGE-BLOG.html", "08-PAGE-CONTACT.html",
                   "09-TEMPLATE-ARTICLE.html", "10-THEME-BUILDER-SINGLE-POST.html"}
    for f in os.listdir("elementor"):
        if f not in valid_names:
            target_path = os.path.join("elementor", f)
            if os.path.isfile(target_path):
                os.remove(target_path)
                print(f"Removed outdated file: elementor/{f}")

    # 1. Header
    with open("elementor/01-HEADER.html", "w", encoding="utf-8") as f:
        f.write(generate_header_template())
    print("Generated elementor/01-HEADER.html")

    # 2. Footer
    with open("elementor/02-FOOTER.html", "w", encoding="utf-8") as f:
        f.write(generate_footer_template())
    print("Generated elementor/02-FOOTER.html")

    # 3-8. Pages
    for html_file, out_name, desc in PAGES:
        build_content_only_page(html_file, out_name, desc)

    print("=" * 70)
    print("SUCCESS! Only the 8 numbered files exist in elementor/.")
    print("=" * 70)

if __name__ == "__main__":
    main()
