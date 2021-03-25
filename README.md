# Weather_api

This app takes data from an external API (OpenWeather) to obtain climatological data for few cities.

These are the cities: Barcelona, Paris, Dubai, Amsterdam, Luanda, Montreal, Jakarta, Istanbul, Cairo, Singapore.

The weather of each city is stored in a Database.

The app creates endpoints to consume the data using Django framework.

# Technologies

* Python
* Django framework
* Postgresql
* Docker

# Installation

This project runs in Docker and use Django

* Migrate all the changes to build your Database:
`docker-compose run web python manage.py migrate`

# Run

* Run this docker command to set up the Django server:
`docker-compose up`

* Django app will run at port 8000:
`localhost:8000/`

*  Populate the Database with 10 cities:
`localhost:8000/populate_db/`

* Show weather data from all the cities in API view:
`localhost:8000/cities/`

* Show weather data from an specific city:
`localhost:8000/city/`

# Tests

* Run unit tests:
`docker-compose run web python manage.py test -v 2`

