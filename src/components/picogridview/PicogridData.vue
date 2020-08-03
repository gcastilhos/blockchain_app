<template>
  <div class="col-md-12">
    <div class="row">
      <div class="col-md-3">{{ picogridNumber }}</div>
      <div class="col-md-1">Total</div>
      <div class="col-md-2">4561</div>
      <div class="col-md-6">0005100308e7e0bea95a3e88e4e406c37133f0929c80866bda04bc0bce53a14</div>
    </div>
    <div v-for="(category, index) in categoryTotals"
         :key="'pr' + picogridNumber + '_' + index" 
         class="row">
      <div class="col-md-3">{{ picogridNumber }}</div>
      <div class="col-md-1">{{ category[0] }}</div>
      <div class="col-md-2">{{ parseInt(category[1]) }}</div>
      <div class="col-md-6">{{ categoryHash(index) }}</div>
    </div>
    <div class="row">
      <div class="col-md-12 space"></div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import sha256 from 'sha256'
import {lpad} from '@/stringformat'
import {MOCK_DATA} from '@/mockdata'

const MAX_BATCH = parseInt(process.env.VUE_APP_MAX_BATCH || 50)
const DATA_API_URI = process.env.VUE_APP_DATA_API_URI || "/events"
const HEADERS = JSON.parse(process.env.VUE_APP_HEADERS || "{}")

export default {
  props: ['picogridReference'],
  data: function() {
    return {
      categories: [],
      records: [],
      batch: 1,
      header: []
    }
  },
  methods: {
    categoryHash: function(numberReference) {
      return sha256(numberReference)
    },
    getData: async function(next_batch) {
      var data
      try {
        let response = await axios.get(DATA_API_URI, {timeout: 10000, headers: HEADERS})
        data = response.data
      } catch (error) {
        console.error("Error: " + error)
        data = MOCK_DATA
      }
      this.records.push(data.data[0])
      this.batch = next_batch
      this.header = data.columns
    }
  },
  mounted: function() {
    this.getData(this.batch)
  },
  created: function() {
    let interval = parseInt(process.env.VUE_APP_DELAY || 10000)
    setInterval(function() {
      if (this.batch % MAX_BATCH === 0) {
        let totals = this.categoryTotals.slice()
        totals.splice(0, 0, this.picogridReference)
        totals.splice(0, 0, this.batch)
        // this.$store.dispatch('addPicogridTotals', {totals: totals})
        this.records.splice(0, MAX_BATCH)
      }
      this.batch = this.batch + 1
      this.getData(this.batch)
    }.bind(this), interval)
  },
  computed: {
    useCategories: function() {
      let catNumbers = [...Array(9).keys()]
      let categories = []
      catNumbers.forEach(row => {
        categories.push(String.fromCharCode(65 + row)) 
      })
      return categories
    },
    picogridNumber: function() {
      return "001.001." + lpad("0", this.picogridReference)
    },
    categoryTotals: function() {

      let categoriesData = () => {
        let categMap = new Map()
        this.records.forEach(rec => {
          let powerConsumption = parseFloat(rec[12])
          let category = rec[13]
          categMap.set(category, categMap.has(category) ? powerConsumption + categMap.get(category) : powerConsumption)
        })
        return categMap.entries()
      }

      let totals = []
      let entries = categoriesData()
      let pair = entries.next()
      while (pair !== undefined && pair.value !== undefined) {
        let category = pair.value[0]
        totals.push([category[0], pair.value[1].toFixed(2)])
        pair = entries.next()
      }
      return totals.sort()
    }
  }
}
</script>

<style>
div.space {
  height: 20px;
}
</style>
