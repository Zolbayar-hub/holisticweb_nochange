// Hamburger menu functionality
const hamburger = document.getElementById('hamburger');
const mobileMenu = document.getElementById('mobile-menu');
const mobileAuthBtn = document.getElementById('mobile-auth-btn');
const desktopAuthBtn = document.getElementById('desktop-auth-btn');

// Ensure hamburger starts in correct state
function initializeHamburger() {
    if (hamburger && mobileMenu) {
        hamburger.classList.remove('active');
        mobileMenu.classList.remove('active');
    }
}

// Initialize on DOM content loaded
document.addEventListener('DOMContentLoaded', function() {
    // Initialize hamburger menu
    initializeHamburger();
    
    // Initialize services carousel when page is ready
    setTimeout(() => {
        new ServicesCarousel();
    }, 50);
    
    // Initialize about images carousel
    setTimeout(() => {
        window.aboutCarouselInstance = new AboutImageCarousel();
    }, 100);
    
    // Initialize auth buttons
    setTimeout(() => {
        initializeAuthButtons();
    }, 150);
});

// Function to toggle menu
function toggleMobileMenu(e) {
    e.preventDefault();
    e.stopPropagation();
    
    if (hamburger && mobileMenu) {
        const isActive = hamburger.classList.contains('active');
        
        if (isActive) {
            hamburger.classList.remove('active');
            mobileMenu.classList.remove('active');
        } else {
            hamburger.classList.add('active');
            mobileMenu.classList.add('active');
        }
    }
}

// Support both click + touchstart for better mobile support
if (hamburger) {
    ['click', 'touchstart'].forEach(evt => {
        hamburger.addEventListener(evt, toggleMobileMenu, { passive: false });
    });
}

// Close mobile menu when clicking on links
document.querySelectorAll('.mobile-menu a').forEach(link => {
    link.addEventListener('click', () => {
        hamburger.classList.remove('active');
        mobileMenu.classList.remove('active');
    });
});

// Close mobile menu when clicking outside
document.addEventListener('click', (e) => {
    if (!hamburger.contains(e.target) && !mobileMenu.contains(e.target)) {
        hamburger.classList.remove('active');
        mobileMenu.classList.remove('active');
    }
});

// Prevent mobile menu from closing when clicking inside it
mobileMenu.addEventListener('click', (e) => {
    e.stopPropagation();
});

// Smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Override auth.js initialization to use our auth buttons
function initializeAuthButtons() {
    updateAuthButtons().catch(error => {
        console.error('Failed to update auth buttons:', error);
        // Buttons already have default state
    });
}

async function updateAuthButtons() {
    try {
        const status = await checkAuthStatus();
        
        // Update both mobile and desktop auth buttons
        const authButtons = [mobileAuthBtn, desktopAuthBtn].filter(btn => btn);
        
        authButtons.forEach(btn => {
            if (status.logged_in) {
                btn.textContent = 'Logout';
                btn.classList.add('logout-btn');
                btn.onclick = async () => {
                    try {
                        const res = await logout();
                        if (res.message) {
                            location.reload();
                        }
                    } catch (error) {
                        console.error('Logout error:', error);
                    }
                };
            } else {
                btn.textContent = 'Login';
                btn.classList.remove('logout-btn');
                btn.onclick = showLoginModal;
            }
        });
    } catch (error) {
        console.error('Error checking auth status:', error);
        const authButtons = [mobileAuthBtn, desktopAuthBtn].filter(btn => btn);
        authButtons.forEach(btn => {
            btn.textContent = 'Login';
            btn.classList.remove('logout-btn');
            btn.onclick = showLoginModal;
        });
    }
}

// Also initialize on window load as fallback
window.addEventListener('load', function() {
    initializeHamburger();
});

// Contact form handling
document.querySelector('.contact-form').addEventListener('submit', function(e) {
    e.preventDefault();
    
    const form = this;
    const submitBtn = form.querySelector('button[type="submit"]');
    const originalText = submitBtn.textContent;
    
    // Disable submit button and show loading state
    submitBtn.disabled = true;
    submitBtn.textContent = 'Sending...';
    
    // Prepare form data
    const formData = new FormData(form);
    
    // Send the form data
    fetch(form.action, {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            alert(data.message);
            form.reset();
        } else {
            alert(data.message || 'There was an error sending your message. Please try again.');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('There was an error sending your message. Please try again.');
    })
    .finally(() => {
        // Re-enable submit button
        submitBtn.disabled = false;
        submitBtn.textContent = originalText;
    });
});

// Services Carousel Functionality
class ServicesCarousel {
    constructor() {
        this.grid = document.getElementById('services-grid');
        this.prevBtn = document.getElementById('carousel-prev');
        this.nextBtn = document.getElementById('carousel-next');
        this.indicators = document.getElementById('mobile-indicators');
        this.indicatorDots = this.indicators ? this.indicators.querySelectorAll('.indicator-dot') : [];
        this.cards = this.grid ? this.grid.querySelectorAll('.service-card') : [];
        this.currentIndex = 0;
        this.cardsToShow = window.innerWidth <= 768 ? 1 : 3; // Show 1 on mobile, 3 on desktop
        
        if (this.grid && this.cards.length > 0) {
            this.init();
        }
    }
    
    init() {
        // Only show carousel if there are more cards than the display limit
        if (this.cards.length <= this.cardsToShow) {
            this.hideCarouselButtons();
            return;
        }
        
        this.setupEventListeners();
        this.updateCarousel();
        this.updateButtons();
        
        // Handle window resize
        window.addEventListener('resize', () => {
            const newCardsToShow = window.innerWidth <= 768 ? 1 : 3;
            if (newCardsToShow !== this.cardsToShow) {
                this.cardsToShow = newCardsToShow;
                this.currentIndex = 0; // Reset to beginning
                this.updateCarousel();
                this.updateButtons();
                
                // Show/hide buttons based on card count
                if (this.cards.length <= this.cardsToShow) {
                    this.hideCarouselButtons();
                } else {
                    this.showCarouselButtons();
                }
            }
        });
    }
    
    setupEventListeners() {
        if (this.prevBtn) {
            this.prevBtn.addEventListener('click', () => this.prev());
        }
        if (this.nextBtn) {
            this.nextBtn.addEventListener('click', () => this.next());
        }
        
        // Setup indicator dots for mobile
        if (this.indicatorDots.length > 0) {
            this.indicatorDots.forEach((dot, index) => {
                dot.addEventListener('click', () => {
                    this.goToSlide(index);
                });
            });
        }
        
        // Enhanced touch/swipe support for mobile
        this.setupTouchSupport();
    }
    
    setupTouchSupport() {
        if (!this.grid) return;
        
        let startX = 0;
        let startY = 0;
        let isDragging = false;
        let startTime = 0;
        
        const isMobile = window.innerWidth <= 768;
        if (!isMobile) return; // Only add touch support on mobile
        
        // Prevent default touch behaviors that might interfere
        this.grid.style.touchAction = 'pan-x';
        
        this.grid.addEventListener('touchstart', (e) => {
            const touch = e.touches[0];
            startX = touch.clientX;
            startY = touch.clientY;
            startTime = Date.now();
            isDragging = true;
            
            // Prevent text selection and other default behaviors
            e.preventDefault();
        }, { passive: false });
        
        this.grid.addEventListener('touchmove', (e) => {
            if (!isDragging) return;
            
            const touch = e.touches[0];
            const deltaX = Math.abs(touch.clientX - startX);
            const deltaY = Math.abs(touch.clientY - startY);
            
            // If horizontal movement is more significant, prevent vertical scrolling
            if (deltaX > deltaY && deltaX > 10) {
                e.preventDefault();
            }
        }, { passive: false });
        
        this.grid.addEventListener('touchend', (e) => {
            if (!isDragging) return;
            isDragging = false;
            
            const touch = e.changedTouches[0];
            const endX = touch.clientX;
            const endY = touch.clientY;
            const timeDiff = Date.now() - startTime;
            
            const diffX = startX - endX;
            const diffY = startY - endY;
            const absDiffX = Math.abs(diffX);
            const absDiffY = Math.abs(diffY);
            
            // Only trigger swipe if:
            // 1. Horizontal movement is more significant than vertical
            // 2. Minimum distance is met
            // 3. Swipe was reasonably fast (under 500ms)
            if (absDiffX > absDiffY && absDiffX > 50 && timeDiff < 500) {
                if (diffX > 0) {
                    // Swiped left - go to next
                    this.next();
                } else {
                    // Swiped right - go to previous  
                    this.prev();
                }
            }
        }, { passive: true });
        
        // Add visual feedback on touch
        this.grid.addEventListener('touchstart', () => {
            this.grid.style.opacity = '0.8';
        });
        
        this.grid.addEventListener('touchend', () => {
            this.grid.style.opacity = '1';
        });
    }
    
    prev() {
        if (this.currentIndex > 0) {
            this.currentIndex--;
            this.updateCarousel();
            this.updateButtons();
            this.updateIndicators();
        }
    }
    
    next() {
        const maxIndex = this.cards.length - this.cardsToShow;
        if (this.currentIndex < maxIndex) {
            this.currentIndex++;
            this.updateCarousel();
            this.updateButtons();
            this.updateIndicators();
        }
    }
    
    goToSlide(index) {
        const maxIndex = this.cards.length - this.cardsToShow;
        this.currentIndex = Math.max(0, Math.min(index, maxIndex));
        this.updateCarousel();
        this.updateButtons();
        this.updateIndicators();
    }
    
    updateCarousel() {
        if (!this.grid) return;
        
        // Simple approach: calculate card width + gap for mobile
        if (window.innerWidth <= 768) {
            // On mobile, each card takes full container width with minimal margins
            const containerWidth = this.grid.parentElement.offsetWidth;
            const translateX = -(this.currentIndex * (containerWidth + 16)); // container width + small gap
            this.grid.style.transform = `translateX(${translateX}px)`;
        } else {
            // Desktop uses the original calculation
            const cardWidth = this.cards[0].offsetWidth;
            const gap = 32; // 2rem in pixels
            const translateX = -(this.currentIndex * (cardWidth + gap));
            this.grid.style.transform = `translateX(${translateX}px)`;
        }
    }
    
    updateButtons() {
        if (!this.prevBtn || !this.nextBtn) return;
        
        const maxIndex = this.cards.length - this.cardsToShow;
        
        this.prevBtn.disabled = this.currentIndex === 0;
        this.nextBtn.disabled = this.currentIndex >= maxIndex;
    }
    
    updateIndicators() {
        if (this.indicatorDots.length > 0) {
            this.indicatorDots.forEach((dot, index) => {
                dot.classList.toggle('active', index === this.currentIndex);
            });
        }
    }
    
    hideCarouselButtons() {
        if (this.prevBtn) this.prevBtn.style.display = 'none';
        if (this.nextBtn) this.nextBtn.style.display = 'none';
    }
    
    showCarouselButtons() {
        if (this.prevBtn) this.prevBtn.style.display = 'block';
        if (this.nextBtn) this.nextBtn.style.display = 'block';
    }
    
    hideSwipeHint() {
        const hint = document.querySelector('.mobile-swipe-hint');
        if (hint) {
            hint.style.display = 'none';
        }
    }
    
    // Hide swipe hint after first interaction
    hideSwipeHintAfterInteraction() {
        setTimeout(() => {
            const hint = document.querySelector('.mobile-swipe-hint');
            if (hint) {
                hint.style.opacity = '0';
                hint.style.transition = 'opacity 0.5s ease';
                setTimeout(() => {
                    hint.style.display = 'none';
                }, 500);
            }
        }, 3000); // Hide after 3 seconds
    }
}

// About Image Carousel Functionality
class AboutImageCarousel {
    constructor() {
        this.carousel = document.querySelector('.about-carousel');
        this.slides = document.querySelectorAll('.about-slide');
        this.prevBtn = document.getElementById('about-prev');
        this.nextBtn = document.getElementById('about-next');
        this.dots = document.querySelectorAll('.about-carousel-dots .about-dot');
        this.currentSlide = 0;
        this.autoSlideInterval = null;
        
        if (this.carousel && this.slides.length > 0) {
            this.init();
        }
    }
    
    init() {
        this.setupEventListeners();
        this.startAutoSlide();
        
        // Pause auto-slide on hover
        this.carousel.addEventListener('mouseenter', () => this.pauseAutoSlide());
        this.carousel.addEventListener('mouseleave', () => this.startAutoSlide());
    }
    
    setupEventListeners() {
        // Navigation buttons
        if (this.prevBtn) {
            this.prevBtn.addEventListener('click', () => {
                this.pauseAutoSlide();
                this.prevSlide();
                this.startAutoSlide();
            });
        }
        
        if (this.nextBtn) {
            this.nextBtn.addEventListener('click', () => {
                this.pauseAutoSlide();
                this.nextSlide();
                this.startAutoSlide();
            });
        }
        
        // Dot indicators
        this.dots.forEach((dot, index) => {
            dot.addEventListener('click', () => {
                this.pauseAutoSlide();
                this.goToSlide(index);
                this.startAutoSlide();
            });
        });
        
        // Touch/swipe support for mobile
        let startX = 0;
        let endX = 0;
        
        this.carousel.addEventListener('touchstart', (e) => {
            startX = e.touches[0].clientX;
        });
        
        this.carousel.addEventListener('touchend', (e) => {
            endX = e.changedTouches[0].clientX;
            this.handleSwipe(startX, endX);
        });
    }
    
    handleSwipe(startX, endX) {
        const difference = startX - endX;
        const threshold = 50; // Minimum swipe distance
        
        if (Math.abs(difference) > threshold) {
            this.pauseAutoSlide();
            if (difference > 0) {
                // Swipe left - next slide
                this.nextSlide();
            } else {
                // Swipe right - previous slide
                this.prevSlide();
            }
            this.startAutoSlide();
        }
    }
    
    goToSlide(index) {
        // Remove active class from current slide and dot
        this.slides[this.currentSlide].classList.remove('active');
        this.dots[this.currentSlide].classList.remove('active');
        
        // Update current slide index
        this.currentSlide = index;
        
        // Add active class to new slide and dot
        this.slides[this.currentSlide].classList.add('active');
        this.dots[this.currentSlide].classList.add('active');
    }
    
    nextSlide() {
        const nextIndex = (this.currentSlide + 1) % this.slides.length;
        this.goToSlide(nextIndex);
    }
    
    prevSlide() {
        const prevIndex = (this.currentSlide - 1 + this.slides.length) % this.slides.length;
        this.goToSlide(prevIndex);
    }
    
    startAutoSlide() {
        this.pauseAutoSlide(); // Clear any existing interval
        
        // Check if current slide is a video
        const currentSlideElement = this.slides[this.currentSlide];
        const hasVideo = currentSlideElement && currentSlideElement.querySelector('video[data-video-slide]');
        
        if (hasVideo) {
            // Don't auto-advance on video slides - let the video control the timing
            console.log('Video slide detected - auto-slide paused');
            return;
        }
        
        this.autoSlideInterval = setInterval(() => {
            this.nextSlide();
        }, 4000); // Change slide every 4 seconds for image slides
    }
    
    pauseAutoSlide() {
        if (this.autoSlideInterval) {
            clearInterval(this.autoSlideInterval);
            this.autoSlideInterval = null;
        }
    }
}

// Testimonials Carousel Functionality
class TestimonialsCarousel {
    constructor() {
        this.grid = document.getElementById('testimonials-grid');
        this.prevBtn = document.getElementById('testimonial-prev');
        this.nextBtn = document.getElementById('testimonial-next');
        this.cards = this.grid ? this.grid.querySelectorAll('.testimonial-card') : [];
        this.currentIndex = 0;
        this.cardsToShow = window.innerWidth <= 768 ? 1 : window.innerWidth <= 1024 ? 2 : 3;
        
        if (this.grid && this.cards.length > 0) {
            this.init();
        }
    }
    
    init() {
        // Only show carousel if there are more cards than the display limit
        if (this.cards.length <= this.cardsToShow) {
            this.hideCarouselButtons();
            return;
        }
        
        this.setupEventListeners();
        this.updateCarousel();
        this.updateButtons();
        
        // Handle window resize
        window.addEventListener('resize', () => {
            const newCardsToShow = window.innerWidth <= 768 ? 1 : window.innerWidth <= 1024 ? 2 : 3;
            if (newCardsToShow !== this.cardsToShow) {
                this.cardsToShow = newCardsToShow;
                this.currentIndex = 0; // Reset to beginning
                this.updateCarousel();
                this.updateButtons();
                
                // Show/hide buttons based on card count
                if (this.cards.length <= this.cardsToShow) {
                    this.hideCarouselButtons();
                } else {
                    this.showCarouselButtons();
                }
            }
        });
    }
    
    setupEventListeners() {
        if (this.prevBtn) {
            this.prevBtn.addEventListener('click', () => this.prev());
        }
        if (this.nextBtn) {
            this.nextBtn.addEventListener('click', () => this.next());
        }
    }
    
    prev() {
        if (this.currentIndex > 0) {
            this.currentIndex--;
            this.updateCarousel();
            this.updateButtons();
        }
    }
    
    next() {
        const maxIndex = this.cards.length - this.cardsToShow;
        if (this.currentIndex < maxIndex) {
            this.currentIndex++;
            this.updateCarousel();
            this.updateButtons();
        }
    }
    
    updateCarousel() {
        if (!this.grid) return;
        
        const cardWidth = this.cards[0].offsetWidth;
        const gap = 32; // 2rem in pixels
        const translateX = -(this.currentIndex * (cardWidth + gap));
        
        this.grid.style.transform = `translateX(${translateX}px)`;
    }
    
    updateButtons() {
        if (!this.prevBtn || !this.nextBtn) return;
        
        const maxIndex = this.cards.length - this.cardsToShow;
        
        this.prevBtn.disabled = this.currentIndex === 0;
        this.nextBtn.disabled = this.currentIndex >= maxIndex;
    }
    
    hideCarouselButtons() {
        if (this.prevBtn) this.prevBtn.style.display = 'none';
        if (this.nextBtn) this.nextBtn.style.display = 'none';
    }
    
    showCarouselButtons() {
        if (this.prevBtn) this.prevBtn.style.display = 'block';
        if (this.nextBtn) this.nextBtn.style.display = 'block';
    }
}
