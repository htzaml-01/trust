/**
 * TRUST CORPORATION - INTERACTIONS
 * Sticky Navbar Handler | FAQ Accordion | Forms
 */

document.addEventListener('DOMContentLoaded', () => {
  // 1. STICKY NAVBAR ON SCROLL
  const header = document.getElementById('siteHeader');
  
  function handleScroll() {
    if (window.scrollY > 40) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }
  }

  window.addEventListener('scroll', handleScroll, { passive: true });
  handleScroll(); // Trigger initial state

  // 2. MOBILE MENU TOGGLE
  const mobileToggle = document.getElementById('mobileToggle');
  const navMenu = document.getElementById('navMenu');
  const navBackdrop = document.getElementById('navBackdrop');

  function closeMobileNav() {
    navMenu?.classList.remove('open');
    mobileToggle?.classList.remove('active');
    navBackdrop?.classList.remove('open');
  }

  function toggleMobileNav() {
    const isOpen = navMenu?.classList.toggle('open');
    mobileToggle?.classList.toggle('active', isOpen);
    navBackdrop?.classList.toggle('open', isOpen);
  }

  if (mobileToggle) {
    mobileToggle.addEventListener('click', toggleMobileNav);
  }

  if (navBackdrop) {
    navBackdrop.addEventListener('click', closeMobileNav);
  }

  // Close mobile nav when clicking a link
  navMenu?.querySelectorAll('.nav-link').forEach(link => {
    link.addEventListener('click', closeMobileNav);
  });

  // Query parameter support for testing / headless screenshot
  const urlParams = new URLSearchParams(window.location.search);
  if (urlParams.has('menu')) {
    toggleMobileNav();
  }
  const scrollTarget = urlParams.get('scroll');
  if (scrollTarget) {
    const targetEl = document.getElementById(scrollTarget);
    if (targetEl) {
      targetEl.scrollIntoView({ behavior: 'instant' });
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
});
