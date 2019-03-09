const logoutBut = document.getElementById('logout'),
    editProfileBut = document.getElementById('edit-prof'),
    profile = document.getElementById('profile'),
    editForm = document.getElementById('edit-form'),
    submitEdit = document.getElementById('submit-edit'),
    cancel = document.getElementById('cancel'),
    results = document.getElementById('vote-node'),
    loggedInName = document.getElementById('loggedin-name'),
    loggedEmail = document.getElementById('loggedin-email'),
    loggedPhoneNumber = document.getElementById('loggedin-phone-number'),
    loggedinPassport = document.getElementById('loggedin-passport'),
    profIcon = document.getElementById('prof-icon'),
    editProfName = document.getElementById('edit-prof-name');

logout()

if (window.localStorage.getItem('token') !== null) {

    document.title = 'POLITIKO | ' + window.localStorage.getItem('lastname');
    const user_id = window.localStorage.getItem('user_id'),
        user_email = window.localStorage.getItem('email'),
        user_firstname = window.localStorage.getItem('firstname'),
        user_lastname = window.localStorage.getItem('lastname'),
        user_othername = window.localStorage.getItem('othername'),
        userPassport = window.localStorage.getItem('passport_url'),
        phoneNumber = window.localStorage.getItem('phone_number');

    userNames = user_firstname + ' ' + user_othername + ' ' + user_lastname;

    loggedInName.innerHTML = userNames;
    loggedEmail.innerHTML = user_email;
    loggedPhoneNumber.innerHTML = phoneNumber;
    loggedinPassport.setAttribute('src', userPassport);
    editProfName.innerHTML = userNames;

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

    console.log(user_id)

    fetch('https://politiko-api.herokuapp.com/api/v2/users/' + user_id + '/history')
        .then(response => response.json())
        .then(data => {
            success = data['data'];
            error = data['error'];

            voteHistory = data.data;

            if (success) {
                if (voteHistory.length == 0) {
                    let nullResult = createNode('li');
                    nullResult.innerHTML = 'You have no election history. Go ahead and vote for your favorite candidates and be part of the change.';
                    nullResult.className += ('no-results-display result');
                    append(results, nullResult);
                } else {

                    let voteNode = document.getElementById('vote-node');

                    voteHistory.map(voteHistory => {
                        let h3 = createNode('h3'),
                            parentLi = createNode('li'),
                            ol = createNode('ol'),
                            childLi = createNode('li'),
                            p1 = createNode('p'),
                            p = createNode('p');
                        h3.innerHTML = voteHistory.office;
                        p1.innerHTML = 'Voted: ' + voteHistory.candidate;
                        parentLi.className += ('result');

                        append(childLi, p1)
                        append(childLi, p)
                        append(ol, childLi)
                        append(parentLi, h3)
                        append(parentLi, ol)
                        append(voteNode, parentLi)

                    })
                }
            } else {
                console.log(error)
            }
        })

} else {
    window.location.replace('signin.html');
}

function logout() {
    logoutBut.onclick = (event) => {
        event.preventDefault();
        window.localStorage.clear();
        window.location.replace('signin.html');
    }
}

function createNode(element) {
    return document.createElement(element);
}

function append(parent, element) {
    return parent.appendChild(element);
}
