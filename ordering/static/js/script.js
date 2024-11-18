// script.js

// Play the video when it is hovered over
document.querySelector('.interactive-video').addEventListener('mouseenter', function() {
    document.getElementById('video').play();
});

document.querySelector('.interactive-video').addEventListener('mouseleave', function() {
    document.getElementById('video').pause();
});

// Smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth',
            block: 'start'
        });
    });
});
