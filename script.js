function openForm(formId) {
    // Hide all forms and remove active class from tab buttons
    const forms = document.querySelectorAll('.form');
    forms.forEach(form => form.classList.remove('active'));

    const buttons = document.querySelectorAll('.tab-button');
    buttons.forEach(button => button.classList.remove('active'));

    // Show the selected form and set active class on the corresponding button
    document.getElementById(formId).classList.add('active');
    document.querySelector(.tab-button[onclick="openForm('${formId}')"]).classList.add('active');
}

// Default form display
document.addEventListener('DOMContentLoaded', () => {
    openForm('customerForm');
});