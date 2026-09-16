/* ----------------------------------------------------
   Main Portfolio UI Controller - main.js
   ---------------------------------------------------- */

document.addEventListener('DOMContentLoaded', () => {
  // Initialize Lucide Icons
  if (window.lucide) {
    lucide.createIcons();
  }

  // 1. Sticky Navbar & Active Link Highlight
  const navbar = document.querySelector('.navbar');
  const sections = document.querySelectorAll('section[id]');
  const navLinks = document.querySelectorAll('.nav-link');

  window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
      navbar.classList.add('scrolled');
    } else {
      navbar.classList.remove('scrolled');
    }

    let current = '';
    sections.forEach(section => {
      const sectionTop = section.offsetTop - 100;
      const sectionHeight = section.offsetHeight;
      if (window.scrollY >= sectionTop && window.scrollY < sectionTop + sectionHeight) {
        current = section.getAttribute('id');
      }
    });

    navLinks.forEach(link => {
      link.classList.remove('active');
      if (link.getAttribute('href') === `#${current}`) {
        link.classList.add('active');
      }
    });
  });

  // 2. Resume Tab Switching
  const resumeTabBtns = document.querySelectorAll('.resume-tabs .tab-btn');
  const resumeTabContents = document.querySelectorAll('.resume-tab-content');

  resumeTabBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const targetTab = btn.getAttribute('data-tab');

      resumeTabBtns.forEach(b => b.classList.remove('active'));
      resumeTabContents.forEach(c => c.classList.remove('active'));

      btn.classList.add('active');
      const activeContent = document.getElementById(`resume-${targetTab}`);
      if (activeContent) activeContent.classList.add('active');
    });
  });

  // 3. Skill Matrix Category Filtering
  const skillChips = document.querySelectorAll('.filter-chip');
  const skillCards = document.querySelectorAll('.skill-category-card');

  skillChips.forEach(chip => {
    chip.addEventListener('click', () => {
      const filter = chip.getAttribute('data-filter');

      skillChips.forEach(c => c.classList.remove('active'));
      chip.classList.add('active');

      skillCards.forEach(card => {
        const cat = card.getAttribute('data-category');
        if (filter === 'all' || cat === filter) {
          card.style.display = 'block';
          card.style.animation = 'fadeIn 0.4s ease';
        } else {
          card.style.display = 'none';
        }
      });
    });
  });

  // 4. Contact Form Submission
  const contactForm = document.getElementById('contact-form');
  const toastAlert = document.getElementById('toast-alert');
  const toastMsg = document.getElementById('toast-message');

  if (contactForm) {
    contactForm.addEventListener('submit', async (e) => {
      e.preventDefault();
      
      const submitBtn = contactForm.querySelector('button[type="submit"]');
      const originalText = submitBtn.innerHTML;
      submitBtn.innerHTML = `<i data-lucide="loader-2" class="spin"></i> Sending...`;
      if (window.lucide) lucide.createIcons();

      const formData = {
        name: document.getElementById('contact-name').value,
        email: document.getElementById('contact-email').value,
        subject: document.getElementById('contact-subject').value,
        message: document.getElementById('contact-message').value
      };

      try {
        const res = await fetch('/api/contact', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(formData)
        });

        const data = await res.json();
        
        if (res.ok && data.status === 'success') {
          showToast(data.message || 'Message sent successfully!');
          contactForm.reset();
        } else {
          showToast('Failed to send message. Please try again.', 'error');
        }
      } catch (err) {
        showToast('Error connecting to backend API.', 'error');
      } finally {
        submitBtn.innerHTML = originalText;
        if (window.lucide) lucide.createIcons();
      }
    });
  }

  function showToast(message, type = 'success') {
    if (!toastAlert) return;
    toastMsg.textContent = message;
    toastAlert.classList.add('show');
    setTimeout(() => {
      toastAlert.classList.remove('show');
    }, 4500);
  }
});
