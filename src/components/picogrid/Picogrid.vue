<template>
  <div id="picogrid">
    <div class="container-fluid">
      <div class="row">
        <div class="col-9 big-font text-center">
          <span>DAILY EVENT TABLE - BATCH {{ batch }}</span>
        </div>
        <div class="col-3 big-font font-18 red text-center">
          <span>CONSUMPTION<br />CONSOLIDATION&nbsp;PER<br />CATEGORY</span>
        </div>
      </div>
      <div class="row">
        <div class="col-9">
          <records-table :records="records"
                         :header="header"
                         :finalHash="finalHash"
                         :batch="batch"
                         >
          </records-table>
        </div>
        <div class="col-3">
          <categories-table :records="records">
          </categories-table>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Vue from 'vue'
import RecordsTable from './RecordsTable.vue'
import CategoriesTable from './CategoriesTable.vue'
import VueRouter from 'vue-router'
import axios from 'axios'
import {MOCK_DATA} from '@/mockdata.js'
import encode from '@/encoder.js'
Vue.use(VueRouter)

var router = new VueRouter({
  mode: 'history',
  routes: []
});

const DATA_API_URI = process.env.VUE_APP_DATA_API_URI || "/events"
const MAX_BATCH = parseInt(process.env.VUE_APP_MAX_BATCH || 50)

export default {
  router,
  data: function () {
    return {
      records: [],
      header: [],
      finalHash: '',
      batch: 1,
      interval: parseInt(process.env.VUE_APP_DELAY || 10000)
    }
  },
  components: {
    'records-table': RecordsTable,
    'categories-table': CategoriesTable
  },
  methods: {
    getData: async function(next_batch) {
      var data
      try {
        let response = await axios.get(DATA_API_URI, {timeout: 10000,
                                                      headers: {"Access-Control-Allow-Origin": "http://localhost:5000/"}
        })
        data = response.data
        console.log("Data:" + data.data)
        console.log("Columns:" + data.columns)
      } catch (error) {
        console.error("Error: " + error)
        data = MOCK_DATA
      }
      this.records.push(data.data[0])
      this.batch = next_batch
      this.header = data.columns
      this.encodeAll()
    },
    encodeAll: function() {
      var finalHash = ''
      this.records.forEach((rec) => {
        finalHash += encode(rec)
      })
      this.finalHash = encode(finalHash)
    },
  },
  mounted: function() {
    this.getData(this.batch)
  },
  created: function() {
    setInterval(function() {
      let next_batch
      if (this.batch === MAX_BATCH) {
        next_batch = 1
        this.records.splice(0, MAX_BATCH)
      } else {
        next_batch = this.batch + 1
      }
      this.getData(next_batch)
    }.bind(this), this.interval)
  }
}
</script>

<style scoped>
/**
 * app div
 */
#picogrid {
  font-size: 8pt;
  font-family: Arial, Helvetica, Sans-serif;
}

body {
  background-color: lightBlue !important;
}

.container-fluid {
  padding-top: 50px;
  padding-bottom: 50px;
  width: 97% !important;
}

/**
 * Table
 */

.header {
    font-weight: bold;
    word-wrap: break-word;
    border-top: 1px black solid;
    border-bottom: 1px black solid;
}

td, th {
    padding: 5px 10px;
}

tr.row {
  display: table-row;
}

/**
 * Font styles
 */

.dark-blue {
    background-color: #038cfc;
}

.big-font {
    font-size: 24pt;
    font-family: Arial, Helvetica, Sans-serif;
    font-weight: bold;
}

.font-18 {
    font-size: 18pt;
}

.red {
    color: red;
}
</style>
