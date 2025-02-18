let slideIndex = 0;
const slides = document.querySelectorAll(".slide");

function showSlides() {
    // Hide all slides
    slides.forEach((slide) => (slide.style.display = "none"));

    // Increment slide index
    slideIndex++;
    if (slideIndex > slides.length) slideIndex = 1;

    // Show the current slide
    slides[slideIndex - 1].style.display = "block";

    // Automatically change slide every 5 seconds
    setTimeout(showSlides, 5000);
}

function changeSlide(n) {
    slideIndex += n - 1;
    if (slideIndex < 0) slideIndex = slides.length - 1;
    if (slideIndex >= slides.length) slideIndex = 0;
    showSlides();
}

// Initialize slideshow
document.addEventListener("DOMContentLoaded", () => {
    showSlides();
});
