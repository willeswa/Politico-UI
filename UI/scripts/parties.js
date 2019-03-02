const parties_url = 'https://politiko-api.herokuapp.com/api/v2/parties',
    voteNavItem = document.getElementById('vote-nav-item'),
    logBut = document.getElementById('log-but'),
    totalParties = document.getElementById('total-parties'),
    partiesParentNode = document.getElementById('main-node');

if (window.localStorage.getItem('email') == null) {
    voteNavItem.style.display = 'none';
    logBut.innerHTML = 'LOGIN';
    logBut.setAttribute('href', 'signin.html')
}

getParties()

function getParties() {
    return fetch(parties_url)
        .then(response => response.json())
        .then(all_parties => {
            let all_part = all_parties.data;
            if (all_part.length > 0) {
                all_part.map(party => {
                    let div1 = createNode('div'),
                        div2 = createNode('div'),
                        div3 = createNode('div'),
                        img = createNode('img'),
                        p = createNode('p'),
                        h3 = createNode('h3');


                    totalParties.innerHTML = `(${all_part.length})`;
                    document.title = 'POLITIKO | ' + all_part.length + ' Parties';
                    p.innerHTML = `${party.hq_address}`;
                    h3.innerHTML = `${party.party_name}`;
                    img.src = party.logo_url;
                    div1.className += 'img';
                    div2.className += 'info';
                    div3.className += 'candidate';

                    append(div1, img)
                    append(div2, h3)
                    append(div2, p)
                    append(div3, div1)
                    append(div3, div2)
                    append(partiesParentNode, div3)
                })
            } else {
                let div1 = createNode('div'),
                    p = createNode('p');

                totalParties.innerHTML = `(${all_part.length})`;
                document.title = 'POLITIKO | ' + all_part.length + ' Parties';
                p.innerHTML = "There are currently no parties registered. However, you can register your own party by sending a request to the admin. Login to get started!";
                p.className += 'padit';

                append(div1, p);
                append(partiesParentNode, div1)
            }
        })
}

function createNode(element) {
    return document.createElement(element);
}

function append(parent, element) {
    return parent.appendChild(element);
}