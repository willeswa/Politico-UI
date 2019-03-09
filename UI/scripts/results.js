const voteNavItem = document.getElementById('vote-nav-item'),
    logoutBut = document.getElementById('log-but'),
    resultsParentNode = document.getElementById('main-node'),
    officeResultList = document.getElementById('office-result-list'),
    homeBut = document.getElementById('home'),
    homeLink = document.getElementById('home-a'),
    resultsSlip = document.getElementById('result-slip'),
    rclose = document.getElementById('rclose'),
    officeNames = document.getElementById('rh2');

if (window.localStorage.getItem('email') == null) {
    voteNavItem.style.display = 'none';
    logoutBut.innerHTML = 'LOGIN';
    homeBut.innerHTML = 'HOME';
    homeLink.setAttribute('href', 'index.html');
}

document.title = 'POLITIKO | Results'

getOffices()


logoutBut.onclick = (event) => {
    event.preventDefault();
    window.localStorage.clear()
    window.location.replace('signin.html')
}

rclose.onclick = event => {
    event.preventDefault()
    clearNode()
    resultsSlip.style.display = 'none';
    document.title = 'POLITIKO | Results'
}

function clearNode() {
    while (officeResultList.firstChild) {
        officeResultList.removeChild(officeResultList.firstChild);
    }
}


function getOffices() {
    return fetch('https://politiko-api.herokuapp.com/api/v2/offices')
        .then(response => response.json())
        .then(data => {
            officesResults = data.data;

            officesResults.map(office => {
                let resultDiv = createNode('div'),
                    ul = createNode('ul'),
                    li = createNode('li'),
                    h3 = createNode('h4'),
                    button = createNode('button');

                button.innerHTML = 'View Results';
                h3.innerHTML = office.office_name;
                h3.id = 'h3';
                resultDiv.className += 'padit border-bottom';
                button.className += 'result-count'
                button.id = 'result-but' + office.office_id;

                append(resultDiv, h3);
                append(resultDiv, button);
                append(li, resultDiv);
                append(ul, li)
                append(resultsParentNode, ul);


                const viewResult = document.getElementById(button.id);

                viewResult.onclick = event => {
                    event.preventDefault()

                    resultsSlip.style.display = 'block';

                    fetch('https://politiko-api.herokuapp.com/api/v2/office/' + office.office_id + '/result')
                        .then(response => response.json())
                        .then(data => {
                            document.title = office.office_name;
                            success = data['data'];
                            error = data['error'];
                            if (success) {
                                officeNames.innerHTML = office.office_name;
                                results = data.data
                                if (results.length > 0) {
                                    results.map(result => {
                                        let candidateName = createNode('div'),
                                            h4 = createNode('h4'),
                                            p = createNode('p'),
                                            li = createNode('li');

                                        h4.innerHTML = result.candidate;
                                        p.innerHTML = result.results + ' Votes';
                                        candidateName.className += 'padit border-bottom';
                                        p.className += 'result-count';

                                        append(candidateName, h4)
                                        append(candidateName, p)
                                        append(li, candidateName)
                                        append(officeResultList, li)

                                    })
                                } else {
                                    let h4 = createNode('h4'),
                                        li = createNode('li');

                                        h4.innerHTML = 'There are no results for this office.';
                                        h4.className += 'padit border-bottom';
                                        append(li, h4)
                                        append(officeResultList, li)
                                }
                            } else {
                                console.log(error)
                            }

                        })
                }

            })

        })



}


function createNode(element) {
    return document.createElement(element);
}

function append(parent, element) {
    return parent.appendChild(element);
}