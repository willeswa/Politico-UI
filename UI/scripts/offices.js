const offices = 'https://politiko-api.herokuapp.com/api/v2/offices',
    ol = document.getElementById('main-node'),
    logout = document.getElementById('logout'),
    voteNow = document.getElementById('vote-now'),
    homeBut = document.getElementById('home'),
    homeLink = document.getElementById('home-a');


    
    if(window.localStorage.getItem('email') === null) {
        logout.innerHTML = 'LOGIN';
        voteNow.style.display = 'none';
        homeBut.innerHTML = 'HOME';
        homeLink.setAttribute('href', 'index.html');
    }

getOffices()

logout.onclick = (event) => {
    event.preventDefault();
    window.localStorage.clear()
    window.location.replace('signin.html')
}

function getOffices() {
    return fetch(offices)
        .then(response => response.json())
        .then(all_offices => {
            let all_off = all_offices.data;
            document.title = 'POLITIKO | ' + all_off.length+ ' Positions';
            if (all_off.length > 0) {
                all_off.map(office => {
                    let li = createNode('li'),
                        span1 = createNode('span'),
                        span2 = createNode('span'),
                        h3 = createNode('h3'),
                        div1 = createNode('div'),
                        div2 = createNode('div'),
                        vie = createNode('button'),
                    div3 = createNode('div');

                    
                    h3.innerHTML = `${office.office_name}`;
                    span1.innerHTML = `${office.created_on}`;
                    span2.innerHTML = `${office.office_type}`;
                    span2.className += 'office-span';
                    vie.innerHTML = 'Apply';
                    vie.id = 'vie';
                    vie.className += 'success-color';
                    div3.style.display = 'flex';
                    div1.style.width = '90%';
                    li.className += 'colorit user-office';

                    append(div1, span1)
                    append(div1, span2)
                    append(div1, h3)
                    append(div2, vie)
                    append(div3, div1)
                    append(div3, div2)
                    append(li, div3)
                    append(ol, li)
                })
            }
        })

}

function createNode(element) {
    return document.createElement(element);
}

function append(parent, element) {
    return parent.appendChild(element);
}