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

# Blockchain Demo App

A demonstration application using blockchain technology.

## Host

[Blockchain1 on Heroku](https://blockchain1aus.herokuapp.com/)

### Production Environment

Setting the `PRODUCTION` flag in the production environment.
```
heroku config:add PRODUCTION=True --app blockchain1aus
```

### Security Policy

The module `Talisman` requires a custom policy to allow common resources, including
JS libraries, fonts, and images.

```
heroku config:add CSP_DIRECTIVES="default-src 'self'; img-src *; script-src 'unsafe-eval' 'self' *.jsdelivr.net unpkg.com;" --app blockcahin1aus # or other app
```

Local environment
```
export CSP_DIRECTIVES="default-src 'self'; img-src *; script-src 'unsafe-eval' 'self' *.jsdelivr.net unpkg.com;"
```

## Techonology Stack

* Python 3.8.3
* Flask
* Vue.js

## Event Queue

A third phase of the project includes a remote API providing records on a minute-by-minute basis. The actual API hosted on [heroku.com](https://eventqueue.herokuapp.com/events) will provided a record upon request. A queue runs on the server and guarantees that every record is unique.
