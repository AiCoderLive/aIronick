// Main application module
class App {
    constructor() {
        this.currentSection = 'home';
        this.init();
    }

    init() {
        this.bindEvents();
        this.hideLoading();
        this.hideAllSections();
        this.showSection(this.currentSection);
    }

    bindEvents() {
        document.addEventListener('DOMContentLoaded', () => {
            this.hideLoading();
            this.showSection(this.currentSection);
        });
    }

    showSection(sectionName) {
        // Hide all sections
        document.querySelectorAll('.section').forEach(section => {
            section.classList.add('d-none');
        });
        
        // Show selected section
        const targetSection = document.getElementById(sectionName + '-section');
        if (targetSection) {
            targetSection.classList.remove('d-none');
        }
        
        // Update navigation
        document.querySelectorAll('.nav-link').forEach(link => {
            link.classList.remove('active');
        });
        
        // Add active class to current link
        const currentLink = document.querySelector(`[onclick="showSection('${sectionName}')"]`);
        if (currentLink) {
            currentLink.classList.add('active');
        }
        
        this.currentSection = sectionName;
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
        }
    }

    hideAllSections() {
        document.querySelectorAll('.section').forEach(section => {
            section.classList.add('d-none');
        });
    }
}

// Global function for onclick events
function showSection(sectionName) {
    if (window.app) {
        window.app.showSection(sectionName);
    }
}

// Initialize app when DOM is ready
document.addEventListener('DOMContentLoaded', function() {
    window.app = new App();
});