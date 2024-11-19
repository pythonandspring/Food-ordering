function previewProfilePicture() {
    const fileInput = document.getElementById('profilePictureInput');
    if (fileInput.files && fileInput.files[0]) {
        const reader = new FileReader();
        reader.onload = function (e) {
            const profileContainer = document.querySelector('.profile-pic-container');
            profileContainer.style.backgroundImage = `url(${e.target.result})`;
            profileContainer.style.backgroundSize = 'cover';
            profileContainer.style.backgroundPosition = 'center';
        };
        reader.readAsDataURL(fileInput.files[0]);
    }
}