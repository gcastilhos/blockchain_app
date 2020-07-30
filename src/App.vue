<template>
  <div id="app" class="container-fluid">
    <div class="row">
      <div class="col-12">
        <nav class="navbar">
          <ul class="nav justify-content-center">
            <li class="nav-item">
              <router-link to="/eventshouses" class="nav-link active">Blockchain Demo</router-link>
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
              <router-link to="/picogridview" class="nav-link">Picogrid View</router-link>
            </li>
          </ul>
        </nav>
      </div>
    </div>
    <div class="row">
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
import EventsHouses from './components/houses/EventsHouses.vue'
import EventsHash from './components/hash/EventsHash.vue'
import EventCategorization from './components/categorization/EventCategorization.vue'
import CellSeparator from './components/CellSeparator.vue'
Vue.use(VueRouter);

var router = new VueRouter({
  mode: 'history',
  routes: [
    {path: '/eventshouses', component: EventsHouses},
    {path: '/eventshash', component: EventsHash},
    {path: '/eventcategorization', component: EventCategorization},
    {path: '/picogrid', component: CellSeparator},
    {path: '/picogrid11', component: CellSeparator},
    {path: '/picogridview', component: CellSeparator}
  ]
})

export default {
  router,
  name: 'App',
}
</script>

<style>
body {
  background-color: lightBlue !important;
}
</style>
