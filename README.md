# Starship

![Starship](https://github.com/abhyudaypratap/starships/workflows/Starships%20application/badge.svg)


*Starship is a retrival software written in Python using the micro framework Flask.*

Currently, following features are implemented:

* Retrieval a list of all starships
* Hyperdrive rating



## Quickstart


This is how you set up an development instance of Starship:
# Setup

### Install backend dependencies
* [postgres (version>= 11)](https://www.postgresql.org/)
* [virtualenv](https://virtualenv.pypa.io/en/stable/)

## Database Setup
* Create a db `starwars_db`

## Backend Set
### setup env files
Add `.env` files.

### virtualenv setup
* `vitualenv venv`
* `source venv/bin/activate`

### install requirements
`pip install -r requirements/requirements.txt`

* Install dependencies and Starship
    * `make install`
* Run the development server
    * `flask run`
* Visit [localhost:5000](http://localhost:5000)
