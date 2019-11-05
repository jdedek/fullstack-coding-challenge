# Unbabel Fullstack Challenge

This is my solution for the [Unbabel Fullstack Challenge](https://github.com/Unbabel/fullstack-coding-challenge).
After the installation you can find the system under: http://localhost/

## Getting Started

### Prerequisites

* Docker


### Installing

In order to install the system put the .env file with the enviroment variables into 

```
/src
```
after that cd into /src and build the system with docker-compose.

```
docker-compose up --build
```

### Database Setup
Before you can test the system, you have to execute the database migrations.
The database starts in an empty state so you have to create translations in the UI to add them into the database.

```
docker-compose exec backend flask db init
```

```
docker-compose exec backend flask db migrate
```

```
docker-compose exec backend flask db upgrade
```


## Running the tests
You can run the tests by typing:
```
docker-compose exec backend pytest -s
```

## Built With

* [Flask](https://palletsprojects.com/p/flask/) - Microframework
* [Vue.js](https://vuejs.org/) - Frontend Framework
* [Nginx](https://www.nginx.com/) - Load Balancer and Webserver
* [Postgres](https://www.postgresql.org/) - Database
* [uWSGI](https://uwsgi-docs.readthedocs.io/en/latest/) - WSGI Server
* [Docker](https://www.docker.com/) - Container


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
