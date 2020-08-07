<template>
  <div class="col-md-12">
    <div class="row font-weight-bold"
         :style="{backgroundColor: rowColor}">
      <div class="col-md-3">{{ picogridNumber }}</div>
      <div class="col-md-1"><img :src="require(`../../assets/triangle_link${downArrow}.png`)" class="show-data" @click="showDataExecute">Total</div>
      <div class="col-md-2">{{ totalConsumption }}</div>
      <div class="col-md-6">{{ totalConsumptionHash }}</div>
    </div>
    <div v-for="(category, index) in categoryTotals"
         :key="'pr' + picogridNumber + '_' + index" 
         class="row"
         :style="{backgroundColor: index % 2 == 0 ? 'white' : rowColor}"
         v-show="showData">
      <div class="col-md-3">{{ picogridNumber }}</div>
      <div class="col-md-1">{{ category[0] }}</div>
      <div class="col-md-2">{{ parseFloat(category[1]).toFixed(2) }}</div>
      <div class="col-md-6">{{ categoryTotalHash(index) }}</div>
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
  props: ['picogridReference', 'rowColor'],
  data: function() {
    return {
      categories: [],
      records: [],
      batch: 1,
      downArrow: "",
      showData: false,
      displayStatus: 0
    }
  },
  methods: {
    categoryTotalHash: function(index) {
      return sha256(parseFloat(this.categoryTotals[index][1]).toFixed(2))
    },
    getData: async function(nextBatch) {
      var data
      try {
        let response = await axios.get(DATA_API_URI, {timeout: 10000, headers: HEADERS})
        data = response.data
      } catch (error) {
        console.error("Error: " + error)
        data = MOCK_DATA
      }
      this.records.push(data.data[0])
      this.batch = nextBatch
    },
    showDataExecute: function() {
      this.showData = !this.showData
      this.downArrow = this.showData ? "_down" : ""
    }
  },
  mounted: function() {
    this.getData(this.batch)
  },
  created: function() {

    let finiteStateMachine = () => {
      if (this.displayStatus === 0) {
        this.batch += 1
        this.getData(this.batch)
      } else if (this.displayStatus === 3) {
        if (this.batch % MAX_BATCH === 0) {
          this.records.splice(0, MAX_BATCH)
        }
        this.displayStatus = 0
        this.batch += 1
        this.getData(this.batch)
      }
      if (this.$store.getters.displayGrid) {
        this.displayStatus = 2
      } else if (this.displayStatus === 2) {
        this.displayStatus = 3
      }
    }

    let interval = parseInt(process.env.VUE_APP_DELAY || 10000)
    setInterval(function() {
      if (this.batch % MAX_BATCH === 0 && this.displayStatus === 0) {
        let totals = this.categoryTotals.slice()
        totals.splice(0, 0, this.picogridReference)
        totals.splice(0, 0, this.batch)
        this.$store.dispatch('addPicogridTotals', {totals: totals, index: 1})
        this.displayStatus = 1
      }
      finiteStateMachine()
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
    totalConsumption: function() {
      if (this.categoryTotals.length > 0) {
        return this.categoryTotals
                 .map(pair => parseFloat(pair[1]))
                 .reduce((accum, value) => accum + value)
                 .toFixed(2)
      }
      return []
    },
    totalConsumptionHash: function() {
      return sha256(this.totalConsumption)
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
    },
    showDataLabel: function() {
      return this.showData ? "Hide" : "Show"
    }
  }
}
</script>

<style>
div.space {
  height: 20px;
  border: none !important;
  background-color: white;
}

.show-data {
  cursor: pointer;
  width: 12px;
  height: 12px;
  margin-right: 5px;
  margin-left: -2px;
  margin-top: -3px;
}
</style>
