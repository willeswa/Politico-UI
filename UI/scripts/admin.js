const offices = 'https://politiko-api.herokuapp.com/api/v2/offices',
    parties = 'https://politiko-api.herokuapp.com/api/v2/parties',
    candidates = 'https://politiko-api.herokuapp.com/api/v2/office/1/politicians',
    parties_nav = document.getElementById('parties'),
    offices_nav = document.getElementById('offices'),
    candidates_nav = document.getElementById('candidates'),
    addEntity = document.getElementById('add-entity'),
    addOfficeEntity = document.getElementById('add-office-entity'),
    creationResponse = document.getElementById('creation-response'),
    logout = document.getElementById('logout'),
    headingSelector = document.getElementById('selector'),
    ol = document.getElementById('entity'),
    close = document.getElementById('close'),
    eClose = document.getElementById('eclose'),
    oClose = document.getElementById('oclose'),
    newOfficeBut = document.getElementById('new-office-but'),
    entityForm = document.getElementById('new-entity-form'),
    editEntityForm = document.getElementById('edit-entity-form'),
    newOfficeForm = document.getElementById('office-entity-form'),
    party_but = document.getElementById('create-party-but');


if (window.localStorage.getItem('is_admin')) {
    token = window.localStorage.getItem('token');
    addEntity.classList = 'add-entity';
    addEntity.innerHTML = 'Add Party';
    headingSelector.innerHTML = 'All Parties';

    getParties();

    offices_nav.onclick = (event) => {
        event.preventDefault();

        clearNode()
        addOfficeEntity.classList = 'add-entity'
        addOfficeEntity.innerHTML = 'Add Office';
        addEntity.innerHTML = " "
        addEntity.classList.remove('add-entity');
        headingSelector.innerHTML = 'All Offices';

        getOffices()

    }

    parties_nav.onclick = (event) => {
        event.preventDefault();
        clearNode()
        let addEntity = document.getElementById('add-entity');
        addEntity.classList = 'add-entity';
        addEntity.innerHTML = 'Add Party';
        addOfficeEntity.innerHTML = " ";
        addOfficeEntity.classList.remove('add-entity');
        headingSelector.innerHTML = 'All Parties';
        getParties();
    }


    candidates_nav.onclick = (event) => {
        event.preventDefault();
        clearNode()
        let addCandidate = document.getElementById('add-entity');
        addCandidate.classList.remove('add-entity')
        addEntity.innerHTML = '';
        addEntity.classList.remove('add-entity');
        addOfficeEntity.classList.remove('add-entity');
        addOfficeEntity.innerHTML = " ";
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


addEntity.onclick = (event) => {
    event.preventDefault();
    entityForm.style.display = 'block';
}

addOfficeEntity.onclick = (event) => {
    event.preventDefault();
    newOfficeForm.style.display = 'block';
}

close.onclick = (event) => {
    event.preventDefault();
    entityForm.style.display = 'none';
}

eClose.onclick = (event) => {
    event.preventDefault();
    editEntityForm.style.display = 'none';
}

oClose.onclick = (event) => {
    event.preventDefault();
    newOfficeForm.style.display = 'none';
}

party_but.onclick = (event) => {
    event.preventDefault();


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
                error = result['error'],
                span = document.getElementById('response');
            if (success) {
                window.location.reload(true)
            } else if (error) {
                span.innerHTML = error;
                span.className += "admin-error";
            } else {
                span.innerHTML = result['msg'] + '. Login to continue!';
                span.className += "admin-error";
            }
        })
}


newOfficeBut.onclick = (event) => {
    event.preventDefault();

    let officeName = document.getElementById('office-name').value,
        officeType = document.getElementById('office-type').value;

    newOfficeData = JSON.stringify(
        {
            office_name: officeName,
            office_type: officeType
        }
    )

    let officeFetch = {
        method: 'POST',
        body: newOfficeData,
        headers: new Headers(
            {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + token
            }
        )
    }

    fetch(offices, officeFetch)
        .then(response => response.json())
        .then(result => {
            console.log(result)
            let success = result['data'],
                error = result['error'],
                span = document.getElementById('office-response');
            if (success) {
                window.location.reload(true)
            } else if (error) {
                span.innerHTML = error;
                span.className += "admin-error";
            } else {
                span.innerHTML = result['msg'] + '. Login to continue!';
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
                    let li = createNode('li'),
                        span1 = createNode('span'),
                        span2 = createNode('span'),
                        h3 = createNode('h3'),
                        div1 = createNode('div'),
                        div2 = createNode('div'),
                        o2 = createNode('i')
                        div3 = createNode('div');

                    h3.innerHTML = `${office.office_name}`;
                    span1.innerHTML = `${office.created_on}`;
                    span2.innerHTML = `${office.office_type}`;
                    o2.className += 'far fa-trash-alt';
                    o2.id = 'del' + office.office_id;
                    div3.style.display = 'flex';
                    div1.style.width = '90%';
                    div2.className += 'del';
                    li.className += 'colorit';

                    append(div1, span1)
                    append(div1, span2)
                    append(div1, h3)
                    append(div2, o2)
                    append(div3, div1)
                    append(div3, div2)
                    append(li, div3)
                    append(ol, li)

                    const del_id = document.getElementById(o2.id);
                    del_id.onclick = (event) => {
                        event.preventDefault();
                        alert('Are you sure you want to delete "' + office.office_name+'"');
                        delReq = {
                            method: 'DELETE',
                            path: office.office_id,
                            headers: new Headers(
                                {
                                    'Content-Type': 'application/json',
                                    'Authorization': 'Bearer ' + token
                                }
                            )
                        }
                        fetch('https://politiko-api.herokuapp.com/api/v2/offices/' + office.office_id, delReq)
                            .then(response => response.json())
                            .then(data => {
                                let success = data['data'],
                                    error = data['error'],
                                    msg = data['msg'];

                                if (success) {
                                    window.location.reload();
                                }
                                else if (error) {
                                    console.log(error)
                                } else {
                                    console.log(msg)
                                }
                            })
                    }

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
                    i1.id = 'edit' + party.party_id
                    i2.id = 'del' + party.party_id
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

                    const del_id = document.getElementById(i2.id);
                    del_id.onclick = (event) => {
                        alert('Are you sure you want to delete this party?')
                        event.preventDefault()
                        delReq = {
                            method: 'DELETE',
                            path: party.party_id,
                            headers: new Headers(
                                {
                                    'Content-Type': 'application/json',
                                    'Authorization': 'Bearer ' + token
                                }
                            )
                        }
                        fetch('https://politiko-api.herokuapp.com/api/v2/parties/' + party.party_id, delReq)
                            .then(response => response.json())
                            .then(data => {
                                let success = data['data'],
                                    error = data['error'],
                                    defaultResponse = document.getElementById('creation-response');

                                if (success) {
                                    window.location.reload();
                                }
                                else if (error) {
                                    defaultResponse.innerHTML = error;
                                } else {
                                    defaultResponse.innerHTML = data['msg'] + '! Please login to continue.';;
                                    defaultResponse.className += 'error-text';
                                }
                            })
                    }

                    const edit_id = document.getElementById(i1.id);
                    edit_id.onclick = (event) => {
                        event.preventDefault()
                        editEntityForm.style.display = 'block';
                        fetch('https://politiko-api.herokuapp.com/api/v2/parties/' + party.party_id)
                            .then(response => response.json())
                            .then(data => {
                                let success = data['data'],
                                    error = data['error'];

                                if (success) {
                                    let logoUrl = document.getElementById('elogo-url'),
                                        hqAddress = document.getElementById('ehq_address'),
                                        editPartyBut = document.getElementById('edit-party-but');
                                    logoUrl.value = party.logo_url;
                                    hqAddress.value = party.hq_address;


                                    editPartyBut.onclick = (event) => {
                                        newName = document.getElementById('eparty-name').value;
                                        let editReq = {
                                            method: 'PUT',
                                            body: JSON.stringify(
                                                {
                                                    party_name: newName
                                                }
                                            ),
                                            headers: new Headers(
                                                {
                                                    'Content-Type': 'application/json',
                                                    'Authorization': 'Bearer ' + token
                                                }
                                            )
                                        }
                                        console.log(editReq)
                                        event.preventDefault()
                                        fetch('https://politiko-api.herokuapp.com/api/v2/parties/' + party.party_id + '/name', editReq)
                                            .then(response => response.json())
                                            .then(data => {
                                                let success = data['data'],
                                                    error = data['error'],
                                                    span = document.getElementById('response1');

                                                if (success) {
                                                    span.innerHTML = success;
                                                    window.location.reload(true)
                                                } else if (error) {
                                                    span.innerHTML = error;
                                                    span.className += "admin-error";
                                                } else {
                                                    span.innerHTML = data['msg'] + '. Login again to continue!';
                                                    span.className += "admin-error";
                                                }
                                            })
                                    }

                                }
                                else if (error) {
                                    let defaultResponse = document.getElementById('creation-response');
                                    defaultResponse.innerHTML = error;
                                    defaultResponse.className += 'error-text';
                                }
                            })
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

function clearNode() {
    while (ol.firstChild) {
        ol.removeChild(ol.firstChild);
    }
}