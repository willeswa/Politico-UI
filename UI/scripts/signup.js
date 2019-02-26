const url = 'https://politiko-api.herokuapp.com/api/v2/auth/signup';
let register = document.getElementById('register');

register.onclick = (event) => {
    event.preventDefault();
    let firstname = document.getElementById('firstname');
    let secondname = document.getElementById('secondname');
    let othername = document.getElementById('othername');
    let email = document.getElementById('email');
    let password = document.getElementById('password');
    let phone_number = document.getElementById('phone_number');
    let passport_url = document.getElementById('passport_url');

    fetch(url, {
        mode: 'cors',
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(
            {
                firstname: firstname,
                secondname: secondname,
                othername: othername,
                email: email,
                password: password,
                phone_number: phone_number,
                passport_url: passport_url
            }
        )
    })
    .then(res => res.json())
    .then(data => {
        let success = data['data'],
            error = data['error'];
        
        if (success) {
            document.getElementById('error-message').innerHTML = '';
            window.location.replace('dashboard.html')
        }
    })
    .catch(error => {
        console.log(error)
    })

}