// JavaScript function to toggle between login and registration forms
function toggleForm(formId) {
    const loginForm = document.getElementById('login-form');
    const registerForm = document.getElementById('register-form');

    if (formId === 'login-form') {
        loginForm.style.display = 'block';
        registerForm.style.display = 'none';
    } else if (formId === 'register-form') {
        loginForm.style.display = 'none';
        registerForm.style.display = 'block';
    }
}