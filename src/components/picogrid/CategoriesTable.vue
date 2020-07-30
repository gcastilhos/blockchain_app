<template>
  <div>
    <div><h5 v-html="'Initial Event Number: ' + initialNumber"></h5></div>
    <div><h5 v-html="'Last Event Number:&nbsp&nbsp;&nbsp;' + finalNumber"></h5></div>
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
import encode from '@/encoder.js'

export default {
  props: {
    records: Array
  },
  data: function() {
    return {     
      header: [],
      totals: [],
      eventNumbers: [],
      categoryHeader: ['Use<br />Category', 'Name&nbsp;of&nbsp;the&nbsp;Category', 'TOTAL<br />in&nbsp;KWH'],
      batch: 1
    }
  },
  filters: {
    encode,
    recordAsString: function(record) {
        return record.join("|")
    }
  },
  methods: {
    getTotals: function() {
      this.records.each(rec => {
        this.totals.push(rec[12, 14])
      })
    },
    align: function(index) {
      return this.textAlignment[index] == 0 ? 'left' : 'right'
    }
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
    },
    initialNumber: function() {
      if (this.records[0] !== undefined) {
        return this.records[0][0]
      }
      return ''
    },
    finalNumber: function() {
      if (this.records.length !== undefined && this.records[this.records.length - 1] !== undefined) {
        return this.records[this.records.length - 1][0]
      }
      return ''
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
    font-size: 16pt;
    font-weight: bold;
    margin: 5px 0;
    text-align: center;
}

div#toBlockchain {
  margin-top: 20px;
}
</style>
