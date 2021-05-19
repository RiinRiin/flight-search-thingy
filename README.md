# ODS Full Stack Coding Assignment.

## Implementation

**Preferred technology:**
* Python
* Angular

## Getting Started

### Prerequisites

Have the following installed on your machine:
- [ ] [Install Docker](https://hub.docker.com/?overlay=onboarding)

### Running Flask Application

1. Run Docker Desktop Application

2. Go into commandline and copy/paste this docker image. It will pull and run the image.
```
docker run -d -p 5000:5000 riinriindocker/flight-search-thingy
```

3. API Endpoints
```
Grabs all flights:
http://localhost:5000/api/flight

Grabs matching stations (even if partially filled)
http://localhost:5000/api/<station>
```

You can alternatively find my docker image in the docker hub:
```
https://hub.docker.com/r/riinriindocker/flight-search-thingy
```
### Running Angular Application

1. Run Docker Desktop Application

2. Go into commandline and copy/paste this docker image. It will pull and run the image.
```
docker run -d -p 80:80 riinriindocker/dashboard
```

3. Go to the url
```
http://localhost:80
```

### NOTE
1. When first starting the applicaiton, it could take some time to load all the data. (5-15 seconds)

2. When using the search bar, autocomplete does not show up when holding SHIFT + alphanumeric.

3. User must press ENTER to complete the search and query the results. It is possible to do dynamic search but query from serverside slows it down so I had to limit through user presing ENTER to query. It could be good idea to add pagination and limit results to 10.

4. Even after clicking on the auto suggestion the user must press ENTER to complete the search.

5. The search bar allows partial filters: if user submits the letter 'a', it will query all origin/destination that has the letter 'a'.

