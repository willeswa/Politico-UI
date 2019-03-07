const url = 'https://politiko-api.herokuapp.com/api/v2/auth/signin';
let login = document.getElementById('login-but');

if (window.localStorage.getItem('email') !== null) {
    let p = document.getElementById('success')
    p.innerHTML = 'Successfully registered! Now login to exercise your right.';
    p.className += 'success';
} else {

    login.onclick = (event) => {
        event.preventDefault();
        let email = document.getElementById('email').value,
            password = document.getElementById('password').value,
            login_data = JSON.stringify({
                email: email,
                password: password
            })

        let fetchSignin = {
            method: 'POST',
            body: login_data,
            headers: new Headers(
                {
                    'Content-Type': 'application/json'
                }
            )
        }

        fetch(url, fetchSignin)
            .then(res => res.json())
            .then(data => {
                let success = data['data'],
                    error = data['error'];

                if (success) {
                    console.log(data)
                    let isAdmin = data['data'][0]['user']['is_admin'],
                        token = data['data'][0]['token'],
                        userId = data['data'][0]['user']['user_id'],
                        email = data['data'][0]['user']['email'],
                        firstname = data['data'][0]['user']['firstname'],
                        lastname = data['data'][0]['user']['lastname'],
                        othername = data['data'][0]['user']['othername'],
                        phonNumber = data['data'][0]['user']['phone_number'],
                        passportUrl = data['data'][0]['user']['passport_url'];

                    window.localStorage.setItem('token', token)
                    window.localStorage.setItem('email', email)
                    window.localStorage.setItem('is_admin', isAdmin)
                    window.localStorage.setItem('user_id', userId)
                    window.localStorage.setItem('firstname', firstname)
                    window.localStorage.setItem('lastname', lastname)
                    window.localStorage.setItem('phone_number', phonNumber)
                    window.localStorage.setItem('othername', othername)
                    window.localStorage.setItem('passport_url', passportUrl)

                    if (isAdmin) {
                        window.location.replace('admin.html')
                    } else {
                        window.location.replace('dashboard.html')
                    }
                }
                else if (error) {
                    let p = document.getElementById('success');
                    p.classList.remove('success')
                    p.classList.add('error')
                    p.innerHTML = error;
                }
            })
    }


}