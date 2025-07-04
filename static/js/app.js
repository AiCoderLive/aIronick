// Main application entry point
// This file serves as the main coordinator for all modules

// Global application state
window.aIronick = {
    currentSection: 'home',
    isLoading: false,
    modules: {},
    initialized: false
};

// Global function for section switching (used by onclick events)
function showSection(sectionName) {
    console.log('Switching to section:', sectionName);

    // Hide all sections
    document.querySelectorAll('.section').forEach(section => {
        section.classList.add('d-none');
    });

    // Show selected section
    const targetSection = document.getElementById(sectionName + '-section');
    if (targetSection) {
        targetSection.classList.remove('d-none');
        console.log('Section shown:', sectionName);
    } else {
        console.error('Section not found:', sectionName + '-section');
    }

    // Update navigation
    updateNavigation(sectionName);

    // Update global state
    window.aIronick.currentSection = sectionName;
}

// Update navigation active state
function updateNavigation(sectionName) {
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

// Initialize application
function initializeApp() {
    console.log('Initializing aIRONick application...');

    // Hide loading spinner immediately
    const loadingElement = document.getElementById('loading');
    if (loadingElement) {
        loadingElement.classList.add('d-none');
        console.log('Loading spinner hidden');
    }

    // Initialize sections
    initializeSections();

    // Show home section by default
    showSection('home');

    // Mark as initialized
    window.aIronick.initialized = true;

    console.log('aIRONick application initialized successfully');
}

// Initialize sections
function initializeSections() {
    // Hide all sections first
    document.querySelectorAll('.section').forEach(section => {
        section.classList.add('d-none');
    });

    console.log('Sections initialized');
}

// Initialize when DOM is ready
document.addEventListener('DOMContentLoaded', function() {
    console.log('DOM loaded, starting initialization...');

    // Small delay to ensure all resources are loaded
    setTimeout(function() {
        initializeApp();
    }, 100);
});

// Fallback initialization
window.addEventListener('load', function() {
    if (!window.aIronick.initialized) {
        console.log('Fallback initialization triggered');
        initializeApp();
    }
});

// Emergency fallback - force hide loading after 2 seconds
setTimeout(function() {
    const loadingElement = document.getElementById('loading');
    if (loadingElement && !loadingElement.classList.contains('d-none')) {
        console.warn('Emergency fallback: hiding loading spinner');
        loadingElement.classList.add('d-none');

        if (!window.aIronick.initialized) {
            initializeApp();
        }
    }
}, 2000);