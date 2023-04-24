# API - Restful with Flask

API using Flask as a framework for basic CRUD (Create, Read, Update and Delete).

## Run on your pc

- Linux
```bash
mkdir api_flask && cd api_flask
git clone https://github.com/rafael-hsm/flask_api.git
chmod +x run.sh
run.sh
```

- Windows
```bash
mkdir api_flask && cd api_flask
git clone https://github.com/rafael-hsm/flask_api.git
run.sh
```

You can go to http://127.0.0.1:5000/api/v1/contacts - to access/get all contacts.Endpoint "contacts" must be used for updating and deleting.
http://127.0.0.1:5000/api/v1/register to enter a new user and http://127.0.0.1:5000/api/v1/login to authenticate. 

## Database
In main.py I'm informing the "testing" parameter for the app, with that we can create a db in basedir. During development I'm using docker to create a database, if you want to use docker, in the main.py file change to "development" and use the command `sudo docker run --name pglocal -e "POSTGRES_PASSWORD=some_security" - p 5432:5432 -d postgres`, in the lines below there are more instructions about postgres


## Tools
- Python 3.8.10
- WSL2
- VSCode
- Docker
- Postgres
- Flask-restful
- Insomnia

### Annotations along of course
```python
pipenv --python 3.8.10
pip install pipenv
pipenv install flask
pipenv shell
```

Note. To connect to a postgres database using WSL, you need to have the following library installed:
```bash
sudo apt-get update && sudo apt-get install -y libpq-dev
```

Command to use postgres via Docker:
`sudo docker run --name pglocal -e "POSTGRES_PASSWORD=exemplo" -p 5432:5432 -d postgres`

To run docker with bash available use the command
`sudo docker exec -it pglocal bash`

Access Postgres with the command:
`psql -U postgres`

Creating the database:
`create database flask_contacts;`

View all created databases;
`\l`

Connect to the database:
`\connect flask_contacts;`

Selecting data from a table:
`SELECT * FROM nome_da_tabela;`

Check used ports and get the PID:
`sudo lsof -i :<porta>`

Closing a process:
`sudo kill PID`

Command to create the tables/models in the database and doing the migrate and updating:
`flask db init`
`flask db migrate`
`flask db update`
