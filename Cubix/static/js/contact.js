// contact.js — Contact form handler

document.getElementById('contactForm').addEventListener('submit', function (e) {
    e.preventDefault();

    var name    = document.getElementById('name').value.trim();
    var email   = document.getElementById('email').value.trim();
    var subject = document.getElementById('subject').value.trim();
    var message = document.getElementById('message').value.trim();

    if (!name || !email || !subject || !message) {
        alert('Please fill in all fields.');
        return;
    }

    // Show success message (UI only — no backend)
    var success = document.getElementById('formSuccess');
    success.style.display = 'block';
    this.reset();

    // Hide success message after 4 seconds
    setTimeout(function () {
        success.style.display = 'none';
    }, 4000);
});


