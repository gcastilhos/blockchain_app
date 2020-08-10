<template>
  <div id="app" class="container-fluid">
    <div class="row">
      <div class="col-12">
        <nav class="navbar navbar-expand">
          <div class="navbar-brand">Picogrid Blockchain</div>
          <button class="navbar-toggler"
                  type="button"
                  data-toggle="collapse"
                  data-target="#navbarSupportedContent"
                  aria-controls="navbarSupportedContent"
                  aria-expanded="false"
                  aria-label="Toggle navigation">
            <span class="navbar-toggler-icon">Toggle Button</span>
          </button>
          <ul class="navbar-nav mr-auto">
            <li class="nav-item">
              <router-link to="/" class="nav-link">Home</router-link>
            </li>
            <li class="nav-item">
              <router-link to="/eventshouses" class="nav-link">Blockchain Demo</router-link>
            </li>
            <li class="nav-item">
              <router-link to="/eventshash" class="nav-link">Events Hashes</router-link>
            </li>
            <li class="nav-item">
              <router-link to="/eventcategorization" class="nav-link">Event Categories</router-link>
            </li>
            <li class="nav-item">
              <router-link to="/picogrid" class="nav-link">Picogrid Categories</router-link>
            </li>
            <li class="nav-item">
              <router-link to="/picogrid11" class="nav-link">11 Picogrid Hashes</router-link>
            </li>
            <li class="nav-item">
              <router-link to="/nanogridview" class="nav-link">Nanogrid View</router-link>
            </li>
            <li class="nav-item">
              <router-link to="/nanogridsnapshot" class="nav-link">Nanogrid Snapshot</router-link>
            </li>
          </ul>
        </nav>
      </div>
    </div>
    <div class="row apps">
      <div class="col-12">
        <keep-alive>
          <router-view></router-view>
        </keep-alive>
      </div>
    </div>
  </div>
</template>

<script>
import Vue from 'vue';
import VueRouter from 'vue-router';
import PicogridHome from './components/PicogridHome.vue'
import EventsHouses from './components/houses/EventsHouses.vue'
import EventsHash from './components/hash/EventsHash.vue'
import EventCategorization from './components/categorization/EventCategorization.vue'
import Picogrid from './components/picogrid/Picogrid.vue'
import Picogrid11 from './components/picogrid11/Picogrid11.vue'
import NanogridView from './components/nanogridview/NanogridView.vue'
import NanogridSnapshot from './components/nanogridsnapshot/NanogridSnapshot.vue'
import {BootstrapVue} from 'bootstrap-vue'
Vue.use(VueRouter)
Vue.use(BootstrapVue)

var router = new VueRouter({
  mode: 'history',
  routes: [
    {path: '', component: PicogridHome},
    {path: '/eventshouses', component: EventsHouses},
    {path: '/eventshash', component: EventsHash},
    {path: '/eventcategorization', component: EventCategorization},
    {path: '/picogrid', component: Picogrid},
    {path: '/picogrid11', component: Picogrid11},
    {path: '/nanogridview', component: NanogridView},
    {path: '/nanogridsnapshot', component: NanogridSnapshot}
  ]
})

export default {
  router,
  name: 'App'
}
</script>

<style>
body {
  background-color: lightBlue !important;
}

nav {
  color: darkBlue;
  border-bottom: 1px solid darkBlue;
}

.router-link-exact-active {
  font-weight: bold;
  text-shadow: 1px 1px #ddd;
}

.nav-link {
  color: darkBlue;
  font-size: 1.1em;
}

.apps {
  margin-top: 50px;
}
</style>
