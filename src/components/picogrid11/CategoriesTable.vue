<template>
  <div>
    <div><h5 v-html="'Picogrid 001.001.0' + lpad(picogridNumber)"></h5></div>
    <table id="totals">
      <tr>
        <th v-for="(item, index) in categoryHeader"
            v-html="item"
            :key="'total' + index"
            class="grey text-center text-bold">
        </th>
      </tr>
      <tr v-for="(total, rowIndex) in categoryTotals" :key="rowIndex">
        <td v-for="(item, index) in total"
            :key="'total_' + index"
            :class="{'text-right': index == 2, 'text-left': index !== 2}"
            class="grey">
          {{ item }}
        </td>
      </tr>
    </table>
  </div>
</template>

<script>
import axios from 'axios'
import {MOCK_DATA} from '@/mockdata'

const MAX_BATCH = parseInt(process.env.VUE_APP_MAX_BATCH || 50)
const DATA_API_URI = process.env.VUE_APP_DATA_API_URI || "/events"
const HEADERS = JSON.parse(process.env.VUE_APP_HEADERS || "{}")

export default {
  props: {
    interval: Number,
    picogridNumber: Number
  },
  data: function() {
    return {     
      header: [],
      totals: [],
      records: [],
      eventNumbers: [],
      categoryHeader: ['Use<br />Category', 'Name&nbsp;of&nbsp;the&nbsp;Category', 'TOTAL<br />in&nbsp;KWH'],
      batch: 1
    }
  },
  filters: {
    recordAsString: function(record) {
        return record.join("|")
    }
  },
  methods: {
    lpad: function(num) {
      if (num < 10) {
        return "0" + num;
      } else if (num < 100) {
        return num;
      }
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
    setInterval(function() {
      if (this.batch % MAX_BATCH === 0) {
        let totals = this.categoryTotals.slice()
        totals.splice(0, 0, this.picogridNumber)
        totals.splice(0, 0, this.batch)
        this.$store.dispatch('addPicogridTotals', {totals: totals})
        this.records.splice(0, MAX_BATCH)
      }
      this.batch = this.batch + 1
      this.getData(this.batch)
    }.bind(this), this.interval)
  },
  computed: {
    categoryTotals: function() {
      let categMap = new Map()
      this.records.forEach(rec => {
        let powerConsumption = parseFloat(rec[12])
        let category = rec[13] + '|' + rec[14]
        categMap.set(category, categMap.has(category) ? powerConsumption + categMap.get(category) : powerConsumption)
      })
      let totals = []
      let entries = categMap.entries()
      let pair = entries.next()
      while (pair !== undefined && pair.value !== undefined) {
        let category = pair.value[0].split('|')
        totals.push([category[0], category[1], pair.value[1].toFixed(2)])
        pair = entries.next()
      }
      return totals.sort()
    }
 }
}
</script>

<style>
table#totals {
  margin: 0 auto;
  border-collapse: separate;
  border-spacing: 5px;
}

div#totals .row .cell {
  font-size: 12pt;
}

.grey {
  background-color: #e8ebf5;
}

table#totals th {
  padding: 5px;
  white-space: normal;
}

table#totals td {
  padding: 5px;
  white-space: nowrap;
}

h5 {
    font-size: 12pt !important;
    font-weight: bold;
    margin: 5px 0;
    text-align: center;
    padding-top: 20px;
}
</style>
