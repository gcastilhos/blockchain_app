# blockchain_app

## Project setup
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


## Added Modules

* axios
* express
* jest
* node-fetch
* sha256
* vue-router
* vuex
# events_hash

## Project setup
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

### Environment Variables

To set the delay time between requests to the events server, in milliseconds
```
VUE_APP_DELAY=#####
```

> Example:  
  VUE_APP_DELAY=10000 # Setting a 10-second delay between requests

The files to place the environment variables are

* .env.production
* .env.staging
* .env.local

Along with that, also the `NODE_ENV` variable should be set in both staging and production environments.

On `Heroku` (NOTE: if not set, assumed development)
```
heroku config:set NODE_ENV=staging --app blockchainevents-staging
heroku config:set NODE_ENV=production --app blockchainevents
```

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

[1]: https://cli.vuejs.org/guide/deployment.html#heroku
# events_hash

## Project setup
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

## Environment Variables

To set any environment variable to be read by the Vue app use
```
VUE_APP_<name>=<value>
```

> Example:  
  VUE_APP_DELAY=10000 # Setting a 10-second delay between requests

This variable must be in a `.env.*` file. The files are specific for each environment

* .env.production
* .env.staging
* .env.local

Along with that, also the `NODE_ENV` variable should be set in both staging and production environments.

On `Heroku`
```
heroku config:set NODE_ENV=development --app eventcategorization-dev # if not set, assumed as development
heroku config:set NODE_ENV=staging --app eventcategorization-staging
heroku config:set NODE_ENV=production --app eventcategorization
```

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

[1]: https://cli.vuejs.org/guide/deployment.html#heroku
# events_houses

## Project setup
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

## Environment Variables

The files to place the environment variables are

* .env.production
* .env.staging
* .env.local

Along with that, also the `NODE_ENV` variable should be set in both staging and production environments.

On `Heroku` (NOTE: if not set, assumed development)
```
heroku config:set NODE_ENV=staging --app blockchainevents-staging
heroku config:set NODE_ENV=production --app blockchainevents
```

### MAX_BLOCKS

It is possible to set the maximum number of blocks that can be displayed. Setting the environment variable
```
VUE_APP_MAX_BLOCKS=<number_of_blocks>
```

in any `.env` file will provide the value for the application.

## The static.json File

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
heroku buildpacks:add heroku/nodejs --app <heroku app>
heroku buildpacks:add https://github.com/heroku/heroku-buildpack-static --app <heroku app>
```

### Heroku Apps

* eventshouses-dev
* eventshouses-staging
* eventshouses

[1]: https://cli.vuejs.org/guide/deployment.html#heroku
# blockchain_picogrid

## Project setup
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
# blockchain_picogrid_11

## Project setup
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

## Additional Modules

* axios
* bootstrap
* express
* jest (for testing)
* node-fetch
* sha256
* vue-router
* vuex

## Events Server For Testing

The environment variables are set in `.env.local` for development. The `.env` file follows this convention for each environemnt

```
.env.local # local environment
.env.development # blockchainpicogrid11-dev
.env.staging # blockchainpicogrid11-stage
.env.production # blockchainpicogrid11
```

These variables are set locally

```
VUE_APP_DELAY=1000 # Delay between calls to local server
VUE_APP_MAX_BATCH=10 # Number of requests before running the block creation algorithm (hash)
VUE_APP_HEADERS='{"Access-Control-Allow-Origin": "http://localhost:5000/"}' # Header to use CORS (see below)
VUE_APP_DATA_API_URI=http://localhost:5000/events # Local server (event queue)
```

### Heroku NODE_ENV

ON Heroku, each environment should have its `NODE_ENV` variable set

```
heroku config:set NODE_ENV=development --app blockchainpicogrid-dev
heroku config:set NODE_ENV=staging --app blockchainpicogrid-stage
heroku config:set NODE_ENV=production --app blockchainpicogrid
```

### Setting CORS

