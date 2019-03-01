const offices = 'https://politiko-api.herokuapp.com/api/v2/offices',
    parties = 'https://politiko-api.herokuapp.com/api/v2/parties',
    candidates = 'https://politiko-api.herokuapp.com/api/v2/office/1/politicians',
    parties_nav = document.getElementById('parties'),
    offices_nav = document.getElementById('offices'),
    createEntity = document.getElementById('create-entity'),
    candidates_nav = document.getElementById('candidates'),
    addEntity = document.getElementById('add-entity'),
    logout = document.getElementById('logout'),
    headingSelector = document.getElementById('selector'),
    ol = document.getElementById('entity'),
    close = document.getElementById('close'),
    entityForm = document.getElementById('new-entity-form'),
    party_but = document.getElementById('create-party-but');

if (window.localStorage.getItem('is_admin')) {
    getParties();
    addEntity.classList = 'add-entity';
    addEntity.innerHTML = 'Add Party';
    headingSelector.innerHTML = 'All Parties'

    offices_nav.onclick = (event) => {
        event.preventDefault();
        createEntity.setAttribute('href', 'new_office.html');
        addEntity.classList = 'add-entity'
        addEntity.innerHTML = 'Add Office';
        headingSelector.innerHTML = 'All Offices';

        getOffices()

    }

    parties_nav.onclick = (event) => {
        event.preventDefault();
        let addEntity = document.getElementById('add-entity');
        addEntity.classList = 'add-entity';
        addEntity.innerHTML = 'Add Party';
        createEntity.setAttribute('href', 'new_party.html');
        headingSelector.innerHTML = 'All Parties';
        getParties();
    }


    candidates_nav.onclick = (event) => {
        event.preventDefault();
        let addCandidate = document.getElementById('add-entity');
        addCandidate.classList.remove('add-entity')
        addEntity.innerHTML = '';
        headingSelector.innerHTML = 'All Candidates';
    }

    logout.onclick = (event) => {
        event.preventDefault();
        window.localStorage.clear()
        window.location.replace('index.html')
    }
} else {
    window.location.replace('index.html')
}


createEntity.onclick = (event) => {
    event.preventDefault();
    entityForm.style.display = 'block';
}

close.onclick = (event) => {
    event.preventDefault();
    entityForm.style.display = 'none';
}

party_but.onclick = (event) => {
    event.preventDefault();
    token = window.localStorage.getItem('token');

    let partyName = document.getElementById('party-name').value,
        hqAddress = document.getElementById('hq_address').value,
        logoUrl = document.getElementById('logo-url').value;

    partyData = JSON.stringify(
        {
            party_name: partyName,
            hq_address: hqAddress,
            logo_url: logoUrl
        }
    )

    let newPartyData = {
        method: 'POST',
        body: partyData,
        headers: new Headers(
            {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + token
            }
        )
    }

    fetch(parties, newPartyData)
        .then(response => response.json())
        .then(result => {
            let success = result['data'],
                error = result['error'];

            if (success) {
                window.location.reload()
            } else if (error) {
                let span = document.getElementById('response');
                span.innerHTML = error;
                span.className += "admin-error";
            }
        })
}




function createNode(element) {
    return document.createElement(element);
}

function append(parent, element) {
    return parent.appendChild(element);
}

function getOffices() {
    return fetch(offices)
        .then(response => response.json())
        .then(all_offices => {
            let all_off = all_offices.data;
            if (all_off.length > 0) {
                all_off.map(office => {
                    let a = createNode('a'),
                        li = createNode('li'),
                        span1 = createNode('span'),
                        span2 = createNode('span'),
                        h3 = createNode('h3');

                    h3.innerHTML = `${office.office_name}`;
                    span1.innerHTML = `${office.created_on}`;
                    span2.innerHTML = `${office.office_type}`;

                    append(li, span1)
                    append(li, span2)
                    append(li, h3)
                    append(a, li)
                    append(ol, a)
                    
                })

            } else {
                let li = createNode('li'),
                    h3 = createNode('h3');
                h3.innerHTML = "You have not declared any open offices for vying at the moment. Click the Add Office button above to create a new office.";
                append(li, h3);
                append(ol, li);
            }
        })
        .catch(error => {
            console.log(error)
        })
}

function getParties() {
    return fetch(parties)
        .then(response => response.json())
        .then(all_parties => {
            let all_part = all_parties.data;
            if (all_part.length > 0) {
                all_part.map(party => {
                    let div2 = createNode('div'),
                        div3 = createNode('div'),
                        div4 = createNode('div'),
                        div1 = createNode('div'),
                        li = createNode('li'),
                        img = createNode('img'),
                        span2 = createNode('span'),
                        span1 = createNode('span'),
                        h3 = createNode('h3'),
                        i1 = createNode('i'),
                        i2 = createNode('i');


                    h3.innerHTML = `${party.party_name}`;
                    span1.innerHTML = `${party.created_on}`;
                    span2.innerHTML = `${party.hq_address}`;
                    img.src = party.logo_url;
                    div2.style.width = '20%';
                    li.style.display = 'flex';
                    div4.className += 'entity-info';
                    img.className += 'thumbnail';
                    i1.className += 'far fa-edit';
                    i2.className += 'far fa-trash-alt';
                    div3.className += 'edit-delete';

                    append(div1, span1)
                    append(div1, span2)
                    append(div1, h3)
                    append(div3, i1)
                    append(div3, i2)
                    append(div2, img)
                    append(div4, div1)
                    append(div4, div3)
                    append(li, div2)
                    append(li, div4)
                    append(ol, li)

                    const dels_party = document.getElementsByClassName('fa-trash-alt');
                        let i = 0
                        while (i < dels_party.length) {
                            dels_party[i].onclick = (event) => {
                                event.preventDefault();
                                window.localStorage.setItem('party_id', party.party_id)
                                console.log(dels_party)
                            }

                            i++;
                        }
                })
            } else {
                let li = createNode('li'),
                    h3 = createNode('h3');
                h3.innerHTML = "There are no parties in the system at the moment. Click the Add Party button above to create a new party.";
                append(li, h3);
                append(ol, li);
            }

        })
        .catch(error => {
            console.log(error)
        })
}
