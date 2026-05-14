// program.js — Programs page interactions

// Smooth scroll for "Apply Now" hero button
document.querySelector('.explore') && document.querySelector('.explore').addEventListener('click', function () {
    document.querySelector('.programs-section').scrollIntoView({ behavior: 'smooth' });
});


window.addEventListener("scroll", function () {
    const navbar = document.getElementById("navbar");

    if (window.scrollY > 50) {
        navbar.classList.add("transparent");
    } else {
        navbar.classList.remove("transparent");
    }
});


