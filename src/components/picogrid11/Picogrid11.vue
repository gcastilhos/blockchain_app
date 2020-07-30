<template>
  <div id="picogrid11">
    <div class="container-xl title">
      <div class="row">
        <div class="col-xl-12 big-font text-center red">
          <span>CONSUMPTION CONSOLIDATION PER CATEGORY</span>
        </div>
      </div>
    </div>
    <div class="container-xl slider">
      <div v-for="rowInd in 4" 
           :key="'r' + rowInd"
           class="row">
        <div v-for="colInd in 3"
             :key="'c' + colInd"
             class="col-xl-4">
          <categories-table v-if="gridNumber(rowInd, colInd) < 12"
                            :interval="interval"
                            :picogridNumber="gridNumber(rowInd, colInd)">
          </categories-table>
        </div>
      </div>
    </div>
    <div class="container-xl title">
      <div class="row">
        <div class="col-xl-12 big-font text-center red">
          <span>HASH BLOCKS</span>
        </div>
      </div>
    </div>
    <div id="hash" class="container-xl slider">
      <div v-for="(item, index) in picogridItems" :key="'r' + index" class="row">
        <div class="col-xl-12">
          <event-totals :totals="item" :totalsNumber="index"></event-totals>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import CategoriesTable from './CategoriesTable.vue'
import EventTotals from './EventTotals.vue'

export default {
  data: function () {
    return {
      batch: 1,
      interval: parseInt(process.env.VUE_APP_DELAY || 10000)
    }
  },
  components: {
    'categories-table': CategoriesTable,
    'event-totals': EventTotals
  },
  methods: {
    gridNumber: function(row, col) {
      return (row - 1) * 3 + col
    }
  },
  created: function() {
    console.log("DELAY: " + this.interval)
  },
  computed: {
    picogridItems: function() {
      return this.$store.getters.hashCodes
    }
  }
}
</script>

<style>
/**
 * app div
 */
#app {
  font-size: 8pt;
  font-family: Arial, Helvetica, Sans-serif;
}

body {
  background-color: lightBlue !important;
}

.container-xl.title {
  padding-top: 50px;
  padding-bottom: 50px;
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

/**
 * Font styles
 */

.dark-blue {
    background-color: #038cfc;
}

.big-font {
    font-size: 20pt;
    font-family: Arial, Helvetica, Sans-serif;
    font-weight: bold;
}

.font-18 {
    font-size: 18pt;
}

.red {
    color: red;
}

.slider {
  width: 100%;
  height: 1000px;
  overflow-y: scroll;
  margin-bottom: 50px;
}
</style>
