// Navigation module
class Navigation {
    constructor() {
        this.init();
    }

    init() {
        console.log('Navigation module initializing...');
        this.setupMobileToggle();
        this.bindEvents();
        console.log('Navigation module initialized');
    }

    bindEvents() {
        // Handle navigation clicks - but don't prevent the onclick from working
        document.querySelectorAll('.nav-link').forEach(link => {
            // Remove any existing click event listeners to avoid conflicts
            link.addEventListener('click', (e) => {
                // Don't prevent default - let the onclick attribute work
                this.handleNavClick(link);
            });
        });
    }

    setupMobileToggle() {
        const toggleButton = document.querySelector('.navbar-toggler');
        const navCollapse = document.querySelector('.navbar-collapse');

        if (toggleButton && navCollapse) {
            toggleButton.addEventListener('click', (e) => {
                e.preventDefault();
                e.stopPropagation();

                console.log('Mobile toggle clicked');

                // Simple toggle without Bootstrap dependency
                if (navCollapse.classList.contains('show')) {
                    navCollapse.classList.remove('show');
                } else {
                    navCollapse.classList.add('show');
                }
            });
        }
    }

    handleNavClick(link) {
        console.log('Navigation link clicked:', link.textContent);

        // Remove active class from all links
        document.querySelectorAll('.nav-link').forEach(navLink => {
            navLink.classList.remove('active');
        });

        // Add active class to clicked link
        link.classList.add('active');

        // Close mobile menu if open
        this.closeMobileMenu();
    }

    closeMobileMenu() {
        const navCollapse = document.querySelector('.navbar-collapse');
        if (navCollapse && navCollapse.classList.contains('show')) {
            navCollapse.classList.remove('show');
            console.log('Mobile menu closed');
        }
    }

    setActiveLink(sectionName) {
        console.log('Setting active link for section:', sectionName);

        document.querySelectorAll('.nav-link').forEach(link => {
            link.classList.remove('active');
        });

        const targetLink = document.querySelector(`[onclick="showSection('${sectionName}')"]`);
        if (targetLink) {
            targetLink.classList.add('active');
        }
    }
}

// Make Navigation available globally
window.Navigation = Navigation;