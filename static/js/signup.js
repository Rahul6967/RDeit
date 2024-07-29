// signup.js
document.getElementById('passwordForm').addEventListener('submit', function(event) {
    var password = document.getElementById('password').value;
    var confirmPassword = document.getElementById('confirmPassword').value;
    var message = document.getElementById('message');

    if (password !== confirmPassword) {
        event.preventDefault(); // Prevent form submission if passwords do not match
        message.style.color = 'red';
        message.textContent = 'Passwords do not match.';
    } else {
        message.style.color = 'green';
        message.textContent = '';
        // Form will be submitted normally since event.preventDefault() is not called
    }
});
