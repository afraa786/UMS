document.addEventListener('DOMContentLoaded', () => {
    const editButton = document.getElementById('editButton');
    const editForm = document.querySelector('.edit-form');
    const cancelButton = document.getElementById('cancelButton');

    editButton.addEventListener('click', () => {
        editForm.classList.toggle('hidden');
        editButton.textContent = editForm.classList.contains('hidden') ? 'Edit Profile' : 'Cancel Edit';
    });

    cancelButton.addEventListener('click', () => {
        editForm.classList.add('hidden');
        editButton.textContent = 'Edit Profile';
    });
});
