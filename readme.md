[![Codacy Badge](https://api.codacy.com/project/badge/Grade/58dafbd4f2ef434ca483e5450ebfa716)](https://app.codacy.com/app/willeswa/politico-app?utm_source=github.com&utm_medium=referral&utm_content=willeswa/politico-app&utm_campaign=Badge_Grade_Dashboard)
[![Build Status](https://travis-ci.com/willeswa/politico-app.svg?branch=develop)](https://travis-ci.com/willeswa/politico-app) [![Coverage Status](https://coveralls.io/repos/github/willeswa/politico-app/badge.svg?branch=develop)](https://coveralls.io/github/willeswa/politico-app?branch=develop) <a href="https://codeclimate.com/github/willeswa/politico-app/maintainability"><img src="https://api.codeclimate.com/v1/badges/840ff34fc071372d8a3f/maintainability" /></a>
## Project Overview
Politico is an application that enables citizens to give their mandate to politicians running for different government offices while building trust in the process through transparency.

## Required Features
1. A user should be able to sign up to Politico 
2. A user with an account should be able to log into Politico
3. An administrator should be able to crete a political party in Politico
4. A user with an account should be able to declare candidacy for specific post
5. A user should be able to see election results
6. A user should be able to get a specific politician profile
7. A user should be able to get all parties record
8. An admin should be able to delete a political party
9. A user should be able to log out of Politico
10. Admin should be able to edit a party information

# Installation and Setup
Clone the repository.
```
https://github.com/willeswa/politico-app.git
```

## Create a virtual environment

```
python3 -p python3 venv;
```
If you need to install virtualenv:
```
virtualenv venv
```

## Activate the virtual environment
Before you begin you will need to activate the corresponding environment
```
source venv/bin/activate
```
## Install requirements
```
pip install -r requirements.txt
```

## Running the application
After the configuration, you will run the app 
```
export FLASK_ENV=development
export FLASK_APP=run.py
flask run
```
You can now tests the following endpoints via postman to experience how the application works:
### Endpoints

|   ENDPOINT                            | METHOD                    | STATUS                               |
|---------------------------------------|:-------------------------:|:------------------------------------:|
|         /offices                      |  GET                      |  Retrieves all offices               |
| /offices                              |  POST                     |  Creates an office                   |
| /parties                              |  GET                      |  REtrieves all parties               |
| /parties                              |  POST                     |  Creates a party                     |
| /parties/<party_id>                   |  GET                      |  Retrieves a party given an id       |
| /parties/<party_id>/name              |  PUT                      |  Changes the name of a party give id |
| /parties/<party_id>                   |  DELETE                   |  Deletes a party given an id         |
| /offices/<offices_id>                 |  GET                      |  Gets a specific office              |


## Running tests
The API has automated endpoints running on unnitests and powered by pytest.
To run the tests locally,
CD into the root of the app and use:
```
pytest --cov=app
```
