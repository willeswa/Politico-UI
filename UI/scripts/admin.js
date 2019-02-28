const edit = 'https://politiko-api.herokuapp.com/api/v2/parties/1/name',
    offices = 'https://politiko-api.herokuapp.com/api/v2/offices',
    parties = 'https://politiko-api.herokuapp.com/api/v2/parties',
    candidates = 'https://politiko-api.herokuapp.com/api/v2/office/1/politicians',
    parties_nav = document.getElementById('parties'),
    offices_nav = document.getElementById('offices'),
    entityLink = document.getElementById('entity-link'),
    candidates_nav = document.getElementById('candidates'),
    addParty = document.getElementById('add-entity'),
    logout = document.getElementById('logout'),
    headingSelector = document.getElementById('selector'),
    ol = document.getElementById('entity');

if (window.localStorage.getItem('is_admin')) {
    addParty.classList = 'add-entity';
    addParty.innerHTML = 'Add Party';
    headingSelector.innerHTML = 'All Parties'

    offices_nav.onclick = (event) => {
        event.preventDefault();
        let addOffice = document.getElementById('add-entity');
        entityLink.setAttribute('href', 'new_office.html');
        addOffice.classList = 'add-entity'
        addOffice.innerHTML = 'Add Office';
        headingSelector.innerHTML = 'All Offices';

        fetch(offices)
            .then(response => response.json())
            .then(all_offices => {
                let all_off = all_offices.data;
                let a = createNode('a'),
                    li = createNode('li'),
                    span1 = createNode('span'),
                    span2 = createNode('span'),
                    h3 = createNode('h3');
                if (all_off.length > 0) {
                    all_off.map(office => {

                        h3.innerHTML = `${office.office_name}`
                        span1.innerHTML = `${office.created_on}`
                        span2.innerHTML = `${office.office_type}`

                        append(li, span1)
                        append(li, span2)
                        append(li, h3)
                        append(a, li)
                        append(ol, a)
                    })
                } else {
                    console.log(all_off)
                    h3.innerHTML = 'There are no open positions for vying! Create one by clicking the Add Office button above';
                    append(li, h3)
                    append(ol, li)
                }

            })
            .catch(error => {
                console.log(error)
            })
    }

    parties_nav.onclick = (event) => {
        event.preventDefault();
        let addParty = document.getElementById('add-entity');
        addParty.classList = 'add-entity';
        addParty.innerHTML = 'Add Party';
        entityLink.setAttribute('href', 'new_party.html');
        headingSelector.innerHTML = 'All Parties';
    }


    candidates_nav.onclick = (event) => {
        event.preventDefault();
        let addCandidate = document.getElementById('add-entity');
        addCandidate.classList.remove('add-entity')
        addParty.innerHTML = '';
        headingSelector.innerHTML = 'All Candidates';
    }

    logout.onclick = (event) => {
        event.preventDefault();
        window.localStorage.clear()
        window.location.replace('index.html')
    }
} else {
    window.location.replace('auth_admin.html')
}

function createNode(element) {
    return document.createElement(element);
}

function append(parent, element) {
    return parent.appendChild(element);
}