# Blockchain Demo App - Hashes and Categories

## Abstract

**Blockchain Demo App** is a simulation of a powergrid event blockchain, where the power events (e.g., lights on, refrigerator cycling, etc) of a given household (picogrid) is registered every given seconds and added as a block in a blockchain. This app has several displays of such events:

1. _Blockchain Demo_ - a display of a number of houses (1 to 100), with hardcoded data (same data for every household), and a demonstration of modifications attempts to the created block hash. The hash of the data is a SHA-256 encoding of the text provided by the values and headers. If any modification is made to the data (editable field), a red frame indicates that the current hash for a given household is not the original encoding. This is propagated to the following blocks (household hashes), also demonstrating the level of complexity required to change any block in the blockchain.

1. _Events Hash_ - Each event is requested from the [Event Queue](https://github.com/gcastilhos/blockchain1), displayed and its hash is calculated on the right-hand tab. A total hash encoding of all hashes is shown at bottom, with a yellow frame. This simulation cycles through 100 events, then return to 1. All events are unique, provided by the event queue.

1. _Events Categories_ - Event Use Categorisation Filtering, using hardcoded data stored in JSON files in the server. It demonstrates the grouping of events by category (e.g., LIGHTING), showing the total for each category for each request. The refresh rate is set at 5 seconds. Each request has a set of JSON files that are read from the server and provide the event data and category grouping. The justification for this approach is that this application was meant to run only from the GitHub `gh-pages` branch, not from Heroku. This is the only app that does not fetch the data from the Event Queue API.

1. _Picogrid Categories_ - A full-fledged event categorization app, fetching the events from the Event Queue API and grouping the total of up to 50 events into categories, with total power consumption shown on the right-hand tab. There is a refresh of the screen every 50 events (aka batch).

1. _11 Picogrid Hashes_ - Picogrid Event Summary, a consolidate consumption per use category. This apps shows 11 picogrid summaries, each one receiving events from the Event Queue API, and calculating the total consumption in real time. In the bottom section (HASH BLOCKS), the total hash encoding for all 11 picogrids are shown overtime. This app cycles through a 200-second period to produce the hash code for a given batch, i.e., events are received and accumulated for 200 seconds and then a hash code of the snapshot at that moment is taken. This will form a block in the blockchain.

1. _Nanogrid View_ - Consolidated Consumption Per use Category - This view shows the nanogrid of 11 picogrids, with details of real-time readings, timestamp, and previous hash. Every  200-second interval, the hash is calculated with Proof-Of-Work (POW) consensus protocol, performed by the same Event Queue API, on a different endpoint (https://eventqueue.herokupapp.com/hash). 

1. _Nanogrid Snapshot_ - A snapshot from the moment of the block hash code creation. It shows the total consumption per category for each picogrid in the nanogrid.

The application is Vue.js SPA (Single Page App), with no server-side in the backend. For that matter, it is a static application, with the Vue.js app taking care of handling the front-end rendering and dagta fetching. The event records are provided by the [event queue server](https://eventqueue.herokuapp.com/events). Check the [GitHub project blockchain1](https://github.com/gcastilhos/blockchain1) for more details.

## Project setup (using vue-cli and yarn package manager)
```
yarn install
```

### Compiles and hot-reloads for development
```
yarn serve
```

### Compiles and minifies for production
```
yarn build
```

### Lints and fixes files
```
yarn lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).


### Added Modules
* axios
* bootstrap
* jest (for testing)
* sha256
* vue-router
* vuex

### Environment Variables

These variables are set in the `.env` files, as needed

```
VUE_APP_DELAY=1000 # Delay between calls to local server
VUE_APP_MAX_BATCH=10 # Number of requests before running the block creation algorithm (hash)
VUE_APP_HEADERS='{"Access-Control-Allow-Origin": "http://localhost:5000/"}' # Header to use CORS (see below)
VUE_APP_DATA_API_URI=http://localhost:5000/events # Local server (event queue)
```

> Example:  
  VUE_APP_DELAY=10000 # Setting a 10-second delay between requests

The files to place the environment variables are

* .env.production
* .env.local

Along with that, also the `NODE_ENV` variable should be set in both staging and production environments.

On `Heroku` (NOTE: if not set, assumed development)
```
heroku config:set NODE_ENV=development --app eventcategorization-dev # if not set, assumed as development
heroku config:set NODE_ENV=production --app eventcategorization-staging
heroku config:set NODE_ENV=production --app eventcategorization
```

#### MAX_BLOCKS

It is possible to set the maximum number of blocks that can be displayed. Setting the environment variable
```
VUE_APP_MAX_BLOCKS=<number_of_blocks>
```

in any `.env` file will provide the value for the application.

### The static.json File

For static applications, a `static.json` file must be added, following the format
```
{
  "root": "dist",
  "clean_urls": true,
  "routes": {
    "/**": "index.html"
  }
}
```

Also, ensure that these buildpacks are installed (check the [deployment page][1] for more details)

```
heroku buildpacks:add heroku/nodejs
heroku buildpacks:add https://github.com/heroku/heroku-buildpack-static
```

## Heroku Apps

* https://blockchain1aus-dev.herokuapp.com # Development
* https://blockchain1aus-staging.herokuapp.com # Staging
* https://blockchain1aus.herokuapp.com # Production


### Heroku NODE_ENV

ON Heroku, each environment should have its `NODE_ENV` variable set

```
heroku config:set NODE_ENV=development --app blockchainpicogrid-dev
heroku config:set NODE_ENV=staging --app blockchainpicogrid-stage
heroku config:set NODE_ENV=production --app blockchainpicogrid
```

#### Setting CORS

The Cross-Origin Resource Sharing header in necessary in order to access the event queue API and Proof of Work (hashing) functionality. This is set in the `VUE_APP_HEADERS` environment variable.
