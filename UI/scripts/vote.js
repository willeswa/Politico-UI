const ol = document.getElementById('main-node'),
    token = window.localStorage.getItem('token'),
    logout = document.getElementById('logout');

if (token) {
    document.title = 'POLITIKO | ' + window.localStorage.getItem('lastname');
    fetchCandidates();
} else {
    window.location.replace('index.html');
}

logout.onclick = (event) => {
    event.preventDefault();
    window.localStorage.clear();
    window.location.replace('signin.html');
}


function fetchCandidates() {
    fetch('https://politiko-api.herokuapp.com/api/v2/offices')
        .then(response => response.json())
        .then(data => {
            let success = data['data'],
                error = data['error'];

            if (success) {

                let offices = data.data;
                if (offices.length > 0) {
                    offices.map(office => {
                        officeId = office.office_id;

                        fetch('https://politiko-api.herokuapp.com/api/v2/office/' + officeId + '/politicians')
                            .then(response => response.json())
                            .then(data => {
                                let candidates = data.data;
                                console.log(candidates)
                                if (candidates.length > 0) {
                                    candidates.map(candidate => {

                                        let li = createNode('li'),
                                            span1 = createNode('span'),
                                            span2 = createNode('span'),
                                            span3 = createNode('span'),
                                            h3 = createNode('h4'),
                                            div1 = createNode('div'),
                                            div2 = createNode('div'),
                                            div3 = createNode('div');
                                        butt = createNode('button');

                                        h3.innerHTML = `${candidate.candidate_name}`;
                                        span1.innerHTML = `${candidate.party}`;
                                        span2.innerHTML = `${candidate.office}`;
                                        li.style.display = 'flex';
                                        div3.classList.add('office-inf')
                                        div1.style.width = '90%';
                                        div2.className += 'del';
                                        li.className += 'colorit';
                                        span3.classList.add('id-style');
                                        butt.innerHTML = 'Vote Now'
                                        span3.innerHTML = `${candidate.related_userid}`;
                                        butt.id = 'votebut' + candidate.related_userid;
                                        butt.className += 'padbut';

                                        append(div1, span1)
                                        append(div1, span2)
                                        append(div1, h3)
                                        append(div3, div1)
                                        append(div3, div2)
                                        append(li, span3)
                                        append(li, div3)
                                        append(li, butt)
                                        append(ol, li)

                                        let candidateId = parseInt(candidate.related_userid),
                                            thisOfficeId = parseInt(candidate.office_id);

                                        let voteData = JSON.stringify(
                                            {
                                                candidate_id: candidateId,
                                                office_id: thisOfficeId
                                            }
                                        )

                                        console.log(voteData)
                                        voteButt = document.getElementById(butt.id);

                                        voteNow(voteButt, voteData)

                                    })
                                } else {
                                    clearNode()
                                    let li = createNode('li');
                                    li.innerHTML = 'There are no candidates at the moment. You can register recieved applications by clicking the Add Candidate button above.'
                                    li.className += 'padit';

                                    append(ol, li);
                                }
                            })
                    })
                } else {
                    clearNode()
                    let li = createNode('li');
                    li.innerHTML = 'There are no offices for candidates to vie for at the moment. Add offices first.'
                    li.className += 'padit';
                    append(ol, li);
                }

            }
        })
}


function createNode(element) {
    return document.createElement(element);
}

function append(parent, element) {
    return parent.appendChild(element);
}

function clearNode() {
    while (ol.firstChild) {
        ol.removeChild(ol.firstChild);
    }
}

function voteNow(button, voteData) {
    button.onclick = event => {
        event.preventDefault()

        let fetchVote = {
            method: 'POST',
            body: voteData,
            headers: new Headers({
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + token
            })
        };

        fetch('https://politiko-api.herokuapp.com/api/v2/votes', fetchVote)
            .then(response => response.json())
            .then(data => {
                let success = data['data'],
                    error = data['error'];
                if (success) {
                    window.location.replace('results.html');
                } else if (error) {
                    alert(error)
                } else {
                    alert('You have been logged out. Please login to continue');
                }
            })
    }
}