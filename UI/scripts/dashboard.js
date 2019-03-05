const logoutBut = document.getElementById('logout'),
    editProfileBut = document.getElementById('edit-prof'),
    profile = document.getElementById('profile'),
    editForm = document.getElementById('edit-form'),
    submitEdit = document.getElementById('submit-edit'),
    cancel = document.getElementById('cancel');

logout()

if (window.localStorage.getItem('token') !== null) {

    

    editProfileBut.onclick = (event) => {
        event.preventDefault()
        profile.style.display = 'none';
        editForm.style.display = 'block';
        
    }

    submitEdit.onclick = (event) => {
        event.preventDefault();
        window.location.reload();
    }

    cancel.onclick = (event) => {
        event.preventDefault();
        profile.style.display = 'block';
        editForm.style.display = 'none';
    }

} else {
    window.location.replace('index.html');
}

function logout() {
    logoutBut   .onclick = (event) => {
        event.preventDefault();
        window.localStorage.clear();
        window.location.replace('signin.html');
    }
}