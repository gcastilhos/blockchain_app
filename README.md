# Blockchain Demo App - Hashes and Categories

## Abstract

**Blockchain Demo App** is a simulation of a powergrid event blockchain, where the power events (e.g., lights on, refrigerator cycling, etc) of a given household (picogrid) is registered every given seconds and added as a block in a blockchain. This app has several displays of such events:

1. _Blockchain Demo_ - a display of a number of houses (1 to 100), with hardcoded data (same data for every household), and a demonstration of modifications attempts to the created block hash. The hash of the data is a SHA-256 encoding of the text provided by the values and headers. If any modification is made to the data (editable field), a red frame indicates that the current hash for a given household is not the original encoding. This is propagated to the following blocks (household hashes), also demonstrating the level of complexity required to change any block in the blockchain.

1. _Events Hash_ - Each event is requested from the [Event Queue](https://github.com/gcastilhos/blockchain1), displayed and its hash is calculated on the right-hand tab. A total hash encoding of all hashes is shown at bottom, with a yellow frame. This simulation cycles through 100 events, then return to 1. All events are  

The application is Vue.js SPA (Single Page App), with no servers in the backend. For that matter, it is a static application, with the Vue.js app taking care of handling the front-end rendering and data fetching. The event records are provided by the [event queue server](https://eventqueue.herokuapp.com/events). Please, check 

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
