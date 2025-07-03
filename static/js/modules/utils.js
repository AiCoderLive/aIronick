// Utility functions
class Utils {
    static showElement(element) {
        if (element) {
            element.classList.remove('d-none');
        }
    }

    static hideElement(element) {
        if (element) {
            element.classList.add('d-none');
        }
    }

    static toggleElement(element) {
        if (element) {
            element.classList.toggle('d-none');
        }
    }

    static fadeIn(element, duration = 500) {
        if (element) {
            element.style.opacity = '0';
            element.style.transition = `opacity ${duration}ms ease-in-out`;
            element.classList.remove('d-none');
            
            setTimeout(() => {
                element.style.opacity = '1';
            }, 10);
        }
    }

    static fadeOut(element, duration = 500) {
        if (element) {
            element.style.opacity = '1';
            element.style.transition = `opacity ${duration}ms ease-in-out`;
            
            setTimeout(() => {
                element.style.opacity = '0';
                setTimeout(() => {
                    element.classList.add('d-none');
                }, duration);
            }, 10);
        }
    }

    static createElement(tag, className = '', textContent = '') {
        const element = document.createElement(tag);
        if (className) {
            element.className = className;
        }
        if (textContent) {
            element.textContent = textContent;
        }
        return element;
    }

    static debounce(func, wait) {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                func(...args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    }

    static formatDate(date) {
        return new Date(date).toLocaleDateString('pl-PL', {
            year: 'numeric',
            month: 'long',
            day: 'numeric'
        });
    }

    static formatTime(date) {
        return new Date(date).toLocaleTimeString('pl-PL', {
            hour: '2-digit',
            minute: '2-digit'
        });
    }
}

// Make Utils available globally
window.Utils = Utils;