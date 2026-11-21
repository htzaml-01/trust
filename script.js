/**
 * TRUST CORPORATION - INTERACTIONS
 * Sticky Navbar Handler | FAQ Accordion | Forms
 */

document.addEventListener('DOMContentLoaded', () => {
  // 1. STICKY NAVBAR ON SCROLL
  const header = document.getElementById('siteHeader');
  
  function handleScroll() {
    if (!header) return;
    if (window.scrollY > 40) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }
  }

  window.addEventListener('scroll', handleScroll, { passive: true });
  window.addEventListener('touchmove', handleScroll, { passive: true });
  handleScroll(); // Trigger initial state

  // 2. MOBILE MENU TOGGLE
  const mobileToggle = document.getElementById('mobileToggle');
  const navMenu = document.getElementById('navMenu');
  const navBackdrop = document.getElementById('navBackdrop');

  function closeMobileNav() {
    navMenu?.classList.remove('open');
    mobileToggle?.classList.remove('active');
    header?.classList.remove('nav-open');
    navBackdrop?.classList.remove('open');
    document.body.style.overflow = '';
  }

  function openMobileNav() {
    navMenu?.classList.add('open');
    mobileToggle?.classList.add('active');
    header?.classList.add('nav-open');
    navBackdrop?.classList.add('open');
    document.body.style.overflow = 'hidden';
  }

  let lastToggleTime = 0;
  function toggleMobileNav(e) {
    if (e) {
      e.preventDefault();
      e.stopPropagation();
      if (e.stopImmediatePropagation) e.stopImmediatePropagation();
    }
    const now = Date.now();
    if (now - lastToggleTime < 350) return;
    lastToggleTime = now;

    const isCurrentlyOpen = navMenu?.classList.contains('open');
    if (isCurrentlyOpen) {
      closeMobileNav();
    } else {
      openMobileNav();
    }
  }

  if (mobileToggle) {
    mobileToggle.addEventListener('click', toggleMobileNav, { capture: true });
    mobileToggle.addEventListener('touchend', toggleMobileNav, { capture: true, passive: false });
  }

  if (navBackdrop) {
    navBackdrop.addEventListener('click', (e) => {
      e.preventDefault();
      closeMobileNav();
    });
    navBackdrop.addEventListener('touchend', (e) => {
      e.preventDefault();
      closeMobileNav();
    }, { passive: false });
  }

  // Only close mobile nav if the link is a hash anchor (#service-1).
  // For page URLs (/services/, /about/, etc.), allow native browser navigation!
  navMenu?.querySelectorAll('.nav-link').forEach(link => {
    link.addEventListener('click', function(e) {
      const href = this.getAttribute('href');
      if (href && href.startsWith('#')) {
        closeMobileNav();
      }
    });
  });

  // Close on Escape key
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && navMenu?.classList.contains('open')) {
      closeMobileNav();
    }
  });

  // Query parameter support for testing / headless screenshot
  const urlParams = new URLSearchParams(window.location.search);
  if (urlParams.has('menu')) {
    toggleMobileNav();
  }
  if (urlParams.has('scrolled')) {
    header?.classList.add('scrolled');
  }
  const scrollTarget = urlParams.get('scroll');
  if (scrollTarget) {
    const targetEl = document.getElementById(scrollTarget);
    if (targetEl) {
      targetEl.scrollIntoView({ behavior: 'instant' });
      handleScroll();
    }
  }

  // 3. FAQ ACCORDION (1 open at a time or toggle)
  const accordionItems = document.querySelectorAll('.accordion-item');

  accordionItems.forEach(item => {
    const headerBtn = item.querySelector('.accordion-header');
    if (headerBtn) {
      headerBtn.addEventListener('click', () => {
        const isActive = item.classList.contains('active');

        // Close all other accordion items
        accordionItems.forEach(other => {
          if (other !== item) {
            other.classList.remove('active');
            other.querySelector('.accordion-header')?.setAttribute('aria-expanded', 'false');
          }
        });

        // Toggle current item
        if (isActive) {
          item.classList.remove('active');
          headerBtn.setAttribute('aria-expanded', 'false');
        } else {
          item.classList.add('active');
          headerBtn.setAttribute('aria-expanded', 'true');
        }
      });
    }
  });

  // 4. CONTACT FORM SUBMISSION FEEDBACK
  const contactForm = document.getElementById('contactForm');
  const formStatus = document.getElementById('formStatus');

  if (contactForm && formStatus) {
    contactForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const submitBtn = contactForm.querySelector('button[type="submit"]');
      const originalText = submitBtn.textContent;
      submitBtn.textContent = 'Submitting...';
      submitBtn.disabled = true;

      setTimeout(() => {
        submitBtn.textContent = originalText;
        submitBtn.disabled = false;
        formStatus.textContent = 'Thank you! Your interest has been submitted successfully. Our team will contact you shortly.';
        formStatus.className = 'form-status success';
        formStatus.style.display = 'block';
        contactForm.reset();

        setTimeout(() => {
          formStatus.style.display = 'none';
        }, 6000);
      }, 700);
    });
  }

  // 5. NEWSLETTER FORM FEEDBACK
  const newsletterForm = document.getElementById('newsletterForm');
  const newsletterStatus = document.getElementById('newsletterStatus');

  if (newsletterForm && newsletterStatus) {
    newsletterForm.addEventListener('submit', (e) => {
      e.preventDefault();
      newsletterStatus.textContent = 'Thank you for subscribing to our industry newsletter!';
      newsletterStatus.style.display = 'block';
      newsletterForm.reset();

      setTimeout(() => {
        newsletterStatus.style.display = 'none';
      }, 5000);
    });
  }

  // 6. VIDEO AUTOPLAY FALLBACK
  const heroVideo = document.querySelector('.hero-video-bg');
  if (heroVideo) {
    heroVideo.play().catch(err => {
      console.log('Autoplay muted playback initiated:', err);
    });
  }

  // 7. BULLETPROOF INFINITE MARQUEE CAROUSEL RUNNER
  function initMarqueeCarousel() {
    const marquees = document.querySelectorAll('.partners-marquee-section');
    marquees.forEach(section => {
      const track = section.querySelector('.marquee-track');
      if (!track || track.dataset.marqueeInitialized) return;
      track.dataset.marqueeInitialized = 'true';

      // Ensure no CSS animation conflicts with smooth JS runner
      track.style.animation = 'none';
      track.style.webkitAnimation = 'none';

      const firstGroup = track.querySelector('.marquee-group');
      if (!firstGroup) return;

      let pos = 0;
      let paused = false;
      const speed = 0.9; // Smooth continuous scroll speed

      track.addEventListener('mouseenter', () => { paused = true; });
      track.addEventListener('mouseleave', () => { paused = false; });
      track.addEventListener('touchstart', () => { paused = true; }, { passive: true });
      track.addEventListener('touchend', () => { paused = false; }, { passive: true });

      function step() {
        if (!paused) {
          pos += speed;
          const groupWidth = firstGroup.offsetWidth;
          if (groupWidth > 0 && pos >= groupWidth) {
            pos = 0;
          }
          track.style.transform = 'translate3d(-' + pos + 'px, 0, 0)';
          track.style.webkitTransform = 'translate3d(-' + pos + 'px, 0, 0)';
        }
        requestAnimationFrame(step);
      }
      requestAnimationFrame(step);
    });
  }

  // Initialize immediately and after window loads (ensuring all SVG dimensions are ready)
  initMarqueeCarousel();
  window.addEventListener('load', initMarqueeCarousel);
});
