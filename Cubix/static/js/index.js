// index.js — Home page

// "Explore Programs" → Programs page
var exploreBtn = document.querySelector('.explore');
if (exploreBtn) {
    exploreBtn.addEventListener('click', function () {
        window.location.href = 'program.html';
    });
}

// "Learn More" → About page
var learnBtn = document.querySelector('.learn-more');
if (learnBtn) {
    learnBtn.addEventListener('click', function () {
        window.location.href = 'about.html';
    });
}

// "Read More" announcement links → Admissions page
document.querySelectorAll('.read-more').forEach(function (link) {
    link.addEventListener('click', function (e) {
        e.preventDefault();
        window.location.href = 'admissions.html';
    });
});

