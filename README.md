# ODS Full Stack Coding Assignment

## Assignment

Create a web application that allows a user to search for flights and display the results in a tabular view.

## Features

1. Allow the user to enter a station (destination or origin) to search flights. Display the results in a table.

2. Provide an auto-suggest feature for station.

3. Provide two RESTful endpoints supporting the functionality listed in steps 1 and 2.

## Datasource

A zipped CSV file of flights is available in /data/flights.csv. Each row in the CSV file represents a flight.

## Implementation

**Preferred technology:**
* Python
* Angular

However, you may use other tech if you are more comfortable with something else. You can use any additional technologies/frameworks/DBs/libraries you would like to.

## Getting Started

### Prerequisites

Have the following installed on your machine:
- [ ] [Install Docker](https://hub.docker.com/?overlay=onboarding)

### Running Flask Application

1. Run Docker Desktop Application

2. Go into commandline and copy/paste this docker image. It will pull and run the image.
```
$ docker run -d -p 5000:5000 riinriindocker/flight-search-thingy
```

3. Go to the url
```
http://localhost:5000/api/flight
http://localhost:5000/api/<station>
```

You can alternatively find my docker image in the docker hub:
```
https://hub.docker.com/r/riinriindocker/flight-search-thingy
```
