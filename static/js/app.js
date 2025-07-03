// Main application entry point
// This file serves as the main coordinator for all modules

// Global application state
window.aIronick = {
    currentSection: 'home',
    isLoading: false,
    modules: {}
};

// Initialize application
document.addEventListener('DOMContentLoaded', function() {
    console.log('aIRONick application starting...');
    
    // Wait for all modules to load
    setTimeout(() => {
        initializeApp();
    }, 100);
});

function initializeApp() {
    // Hide loading spinner
    const loadingElement = document.getElementById('loading');
    if (loadingElement) {
        loadingElement.classList.add('d-none');
    }
    
    // Show default section
    showSection('home');
    
    console.log('aIRONick application initialized successfully');
}

// Global function for section switching (used by onclick events)
function showSection(sectionName) {
    if (window.app) {
        window.app.showSection(sectionName);
    } else {
        // Fallback for direct calls
        document.querySelectorAll('.section').forEach(section => {
            section.classList.add('d-none');
        });
        
        const targetSection = document.getElementById(sectionName + '-section');
        if (targetSection) {
            targetSection.classList.remove('d-none');
        }
        
        window.aIronick.currentSection = sectionName;
    }
}