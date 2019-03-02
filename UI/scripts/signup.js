const url = 'https://politiko-api.herokuapp.com/api/v2/auth/signup';
let register = document.getElementById('register');

window.localStorage.clear()
if (window.localStorage.getItem('email') == null) {
    document.getElementById('logbut').innerHTML = 'LOGIN';
    document.getElementById('log-link').setAttribute('href', 'signin.html');
}

register.onclick = (event) => {
    event.preventDefault();
    let firstname = document.getElementById('firstname').value;
    let lastname = document.getElementById('lastname').value;
    let othername = document.getElementById('othername').value;
    let email = document.getElementById('email').value;
    let password = document.getElementById('password').value;
    let phone_number = document.getElementById('phone_number').value;
    let passport_url = document.getElementById('passport_url').value;

    let form_data = JSON.stringify({
        firstname: firstname,
        lastname: lastname,
        othername: othername,
        email: email,
        password: password,
        phone_number: phone_number,
        passport_url: passport_url
    })

    let fetchData = {
        method: 'POST',
        body: form_data,
        headers: new Headers(
            {
                'Content-Type': 'application/json'
            }
        )
    }

    fetch(url, fetchData)
        .then(res => res.json())

        .then(data => {
            let success = data['data'],
                error = data['error'];

            if (success) {
                window.localStorage.setItem('email', email)
                window.location.replace('signin.html')
            }
            else if (error) {
                let error_p = document.getElementById('error');
                error_p.innerHTML = error;
                error_p.className += "error";
                console.log(error)
            }
        })
        .catch(error => {
            let error_p = document.getElementById('error');
            error_p.innerHTML = error;
            error_p.className += "error";
            console.log(error)
        })

}