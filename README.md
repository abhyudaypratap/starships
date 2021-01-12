# Starship

![Starship](https://github.com/abhyudaypratap/starships/workflows/Starships%20application/badge.svg)


*Starship is a retrival software written in Python using the micro framework Flask.*

Currently, following features are implemented:

* Retrieve list of all starships
* Sort starships with Hyperdrive rating



## Quickstart


This is how you set up an development instance of Starship:
# Setup for development

### Install backend dependencies
* [postgres (version>= 11)](https://www.postgresql.org/)
* [virtualenv](https://virtualenv.pypa.io/en/stable/)

## Backend Set
### setup env files
Add `.env` files.(check env-sample)

### virtualenv setup
* `vitualenv venv`
* `source venv/bin/activate`

### install requirements
`pip install -r requirements/requirements.txt`


## Database Setup
* Create a db `starwars_db`
* Setup DB
    * Run below commands in terminal after creating database to intialize and populate the DB
    ```json
    python manage.py db initdb
    python manage.py db migrate
    python manage.py db upgrade
    python manage.py update_starships
    ```


* Run the development server
    * `flask run`
* Visit [localhost:5000](http://localhost:5000)

* APIs
Refer to [STARSHIPS.md](docs/api/STARSHIPS.md).

## Deployment
Deployment done on Google cloud using github actions
* Just add the credentials to secrets in GitHub settings for deployment
