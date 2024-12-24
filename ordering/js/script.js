// script.js

// Select the video and hover message elements
const video = document.getElementById('video');
const hoverMessage = document.getElementById('hover-message');

// Display hover message only when the video is buffering/loading
video.addEventListener('waiting', () => {
    if (hoverMessage) {
        hoverMessage.style.display = 'block'; // Show the hover message
    }
});

// Hide hover message once the video starts playing
video.addEventListener('play', () => {
    if (hoverMessage) {
        hoverMessage.style.display = 'none'; // Hide the hover message
    }
});

// Intersection Observer to control video play/pause based on visibility
const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
        if (entry.isIntersecting) {
            video.play(); // Play the video when visible
        } else {
            video.pause(); // Pause the video when out of view
        }
    });
}, { threshold: 0.5 }); // 50% of video must be visible

// Start observing the video element
observer.observe(video);

// Optional: Add hover effect for video to zoom in on hover
video.addEventListener('mouseenter', () => {
    video.style.transform = 'scale(1.1)'; // Slight zoom effect
    video.style.transition = 'transform 0.5s'; // Smooth transition
});

// Reset the zoom effect when the mouse leaves the video
video.addEventListener('mouseleave', () => {
    video.style.transform = 'scale(1)'; // Reset zoom
});
