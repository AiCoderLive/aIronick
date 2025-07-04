// Main application module
class App {
    constructor() {
        this.currentSection = 'home';
        this.initialized = false;
        this.init();
    }

    init() {
        console.log('App module initializing...');

        // Remove the DOMContentLoaded event listener since we're already in DOM ready state
        this.hideLoading();
        this.initializeSections();
        this.showSection(this.currentSection);

        this.initialized = true;
        console.log('App module initialized');
    }

    initializeSections() {
        // Hide all sections first
        document.querySelectorAll('.section').forEach(section => {
            section.classList.add('d-none');
        });

        console.log('Sections initialized by App module');
    }

    showSection(sectionName) {
        console.log('App.showSection called with:', sectionName);

        // Hide all sections
        document.querySelectorAll('.section').forEach(section => {
            section.classList.add('d-none');
        });

        // Show selected section
        const targetSection = document.getElementById(sectionName + '-section');
        if (targetSection) {
            targetSection.classList.remove('d-none');
            console.log('Section displayed:', sectionName);
        } else {
            console.error('Section not found:', sectionName + '-section');
        }

        // Update navigation
        this.updateNavigation(sectionName);

        // Update current section
        this.currentSection = sectionName;

        // Close mobile menu if open
        this.closeMobileMenu();
    }

    updateNavigation(sectionName) {
        // Remove active class from all links
        document.querySelectorAll('.nav-link').forEach(link => {
            link.classList.remove('active');
        });

        // Add active class to current link
        const currentLink = document.querySelector(`[onclick="showSection('${sectionName}')"]`);
        if (currentLink) {
            currentLink.classList.add('active');
        }
    }

    closeMobileMenu() {
        const navCollapse = document.querySelector('.navbar-collapse');
        if (navCollapse && navCollapse.classList.contains('show')) {
            navCollapse.classList.remove('show');
        }
    }

    showLoading() {
        const loadingElement = document.getElementById('loading');
        if (loadingElement) {
            loadingElement.classList.remove('d-none');
        }
    }

    hideLoading() {
        const loadingElement = document.getElementById('loading');
        if (loadingElement) {
            loadingElement.classList.add('d-none');
            console.log('Loading hidden by App module');
        }
    }
}

// Make App available globally
window.App = App;ssss