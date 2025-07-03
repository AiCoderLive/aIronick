// Navigation module
class Navigation {
    constructor() {
        this.init();
    }

    init() {
        this.bindEvents();
        this.setupMobileToggle();
    }

    bindEvents() {
        // Handle navigation clicks
        document.querySelectorAll('.nav-link').forEach(link => {
            link.addEventListener('click', (e) => {
                e.preventDefault();
                this.handleNavClick(e.target);
            });
        });
    }

    setupMobileToggle() {
        const toggleButton = document.querySelector('.navbar-toggler');
        const navCollapse = document.querySelector('.navbar-collapse');
        
        if (toggleButton && navCollapse) {
            toggleButton.addEventListener('click', () => {
                navCollapse.classList.toggle('show');
            });
        }
    }

    handleNavClick(link) {
        // Remove active class from all links
        document.querySelectorAll('.nav-link').forEach(navLink => {
            navLink.classList.remove('active');
        });
        
        // Add active class to clicked link
        link.classList.add('active');
        
        // Close mobile menu if open
        const navCollapse = document.querySelector('.navbar-collapse');
        if (navCollapse && navCollapse.classList.contains('show')) {
            navCollapse.classList.remove('show');
        }
    }

    setActiveLink(sectionName) {
        document.querySelectorAll('.nav-link').forEach(link => {
            link.classList.remove('active');
        });
        
        const targetLink = document.querySelector(`[onclick="showSection('${sectionName}')"]`);
        if (targetLink) {
            targetLink.classList.add('active');
        }
    }
}

// Initialize navigation when DOM is ready
document.addEventListener('DOMContentLoaded', function() {
    window.navigation = new Navigation();
});