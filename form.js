const form = document.querySelector('form');
const checkmark = document.querySelector('.form-check-input');
const submitButton = document.querySelector('.submitBtn');
const formHeading = document.querySelector('.form-header');

// getting form data
form.addEventListener('submit', (e) => {
    e.preventDefault();

    // getting data and in real life it would be sent to server
    const formData = new FormData(form);
    const name = formData.get('name');
    const email = formData.get('email');
    const subject = formData.get('subject');
    const message = formData.get('message');

    form.remove();
    formHeading.innerHTML = '👏🏻 THANK YOU ';
})

// making the submit button enabled/disabled depending on if constent is checked or not
checkmark.addEventListener('click', (e) => {
    submitButton.disabled = !e.target.checked
})