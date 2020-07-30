<template>
  <div id="event_categorization">
    <div class="table">
      <div class="row">
        <div class="cell">
          <table-header v-bind:title-h2="titleEvents"
                        v-bind:title-h4="subTitleEvents">
          </table-header>
        </div>
        <div class="cell">
          <table-header v-bind:title-h4="titleTotals"></table-header>
        </div>
      </div>
      <div>
        <div class="cell dark_blue">
          <table class="categ">
            <tr> 
              <th v-for="(item, index) in header"
                  v-html="item"
                  :style="{textAlign: align(index)}"
                  :key="'header_' + index">
              </th>
            </tr>
            <tr class="red_line" 
                v-for="(record, rowIndex) in records"
                :key="'event_' + rowIndex"
                :class="{red_line: rowIndex > 0}">
              <td v-for="(item, index) in record"
                  :style="{backgroundColor: eventColor(record[13]), textAlign: align(index)}"
                  :key="'value_' + index"
                  v-html="item">
              </td>
            </tr>
          </table>
        </div>
        <div class="cell">
          <event-number v-bind:event-number-text="eventNumbers[0]"></event-number>
          <event-number v-bind:event-number-text="eventNumbers[1]"></event-number>
          <table id="totals" class="totals">
            <tr>
              <th v-for="(item, index) in categoryHeader"
                  v-html="item"
                  :key="'total' + index"
                  class="grey header">
              </th>
            </tr>
            <tr v-for="(total, rowIndex) in totals" :key="rowIndex">
              <td v-for="(item, index) in total"
                  :key="'total_' + index"
                  class="grey border_lightBlue">
                {{ item }}
              </td>
            </tr>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import EventNumber from './EventNumber.vue';
import TableHeader from './TableHeader.vue';
import sha256 from 'sha256';
import axios from 'axios';

var categoryColors = {
    'A': 'white',
    'B': 'cyan',
    'C': 'yellow',
    'D': 'orange',
    'E': 'lightGreen',
    'F': 'magenta',
    'G': 'pink',
    'H': 'lightGrey',
    'UNDETM': 'brown',
};

export default {
  data: function() {
    return {     
      records: [],
      header: [],
      totals: [],
      eventNumbers: [],
      categoryHeader: ['Use<br />Category', 'Name&nbsp;of&nbsp;the&nbsp;Category', 'TOTAL<br />in&nbsp;KWH'],
      batch: 1,
      textAlignment: [1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
      titleEvents: 'EVENT USE  CATEGORIZATION',
      subTitleEvents: '(Grouping and FILTERING as per USAGE.)',
      titleTotals: 'CONSUMPTION<br />CONSOLIDATION&nbsp;PER<br />CATEGORY'
    }
  },
  components: {
    eventNumber: EventNumber,
    tableHeader: TableHeader
  },
  filters: {
    encode: function(text) {
      if (text !== '') {
        return sha256(text);
      }
      return text;
    },
    recordAsString: function(record) {
        return record.join("|");
    }
  },
  methods: {
    getData: async function(batch) {
      let response = await axios.get("./data/events_" + batch + ".json");
      let data = response.data;
      this.records.splice(data.data.length);
      data.data.forEach((rec, index) => this.$set(this.records, index, rec));
      this.header.splice(data.columns.length);
      this.header = data.columns;
    },
    getTotals: async function(batch) {
      let respPowerComposition = await axios.get("./data/power_composition_" + batch + ".json");
      let data = respPowerComposition.data;
      this.totals.splice(data.data.length);
      data.data.forEach((rec, index) => this.$set(this.totals, index, rec));
      let respEventNumbers = await axios.get("./data/event_numbers_" + batch + ".json");
      respEventNumbers.data.forEach((rec, index) => this.$set(this.eventNumbers, index, rec));
    },
    eventColor: function(category) {
      return categoryColors[category];
    },
    align: function(index) {
      return this.textAlignment[index] == 0 ? 'left' : 'right';
    }
  },
  mounted: function() {
    this.getData(this.batch);
    this.getTotals(this.batch);
  },
  created: function() {
    setInterval(function() {
      this.batch = this.batch === 15 ? 1 : this.batch + 1;
      this.getData(this.batch);
      this.getTotals(this.batch);
    }.bind(this), 5000)
  }
}
</script>

<style>
/**
 * Table-like DIVs
 */

div {
  font-size: 8pt;
  font-family: Arial, Helvetica, Sans-serif;
}

div.table {
  padding: 50px;
  table-layout: fixed;
}

div.head div.cell.header {
  font-weight: bold;
  word-wrap: break-word;
  border-bottom: 1px black solid;
}

div.cell {
  display: table-cell;
  padding: 5px 10px;
}

.dark_blue {
  background-color: #038cfc;
}

div.cell.record.original {
  width: 600px;
  white-space: nowrap;
}

div.cell.separator {
  width:75px;
}

/**
 *
 */

div#totals.table {
  padding: 0;
}

div#totals.table .row .cell {
  font-size: 12pt;
}

/**
 * Hash specific styles
 */

.text {
  font-family: "Lucida Console", Monaco, Courier, monospace;
}

div.text.hash {
  background-color: lightGrey;
  border: 1px black solid;
  padding: 2px;
  text-align: center;
}

div.final_hash {
  background-color: lightBlue;
  padding: 0;
  text-align: center;
}

div.final_hash div.row.yellow div.cell {
  padding: 10px;
}

div.note {
  text-align: center;
  font-size: 14pt;
  font-weight: bold;
  border: 1px black solid;
  padding: 2px;
  background-color: white;
}

/**
 * Generic styles
 */

.red {
  color: red;
}

.grey {
  background-color: #e8ebf5;
}

.border_lightBlue {
  border: 1px solid lightBlue;
}

.light_blue {
  background-color: lightBlue;
}

.yellow {
  background-color: yellow;
}

.header {
  font-weight: bold;
}

.mono {
  font-family: "Lucida Console", Monaco, Courier, monospace;
}

.no_space_break {
  white-space: nowrap;
}

.text_left {
  text-align: left;
}

.colspan {
  column-span: all;
}

.red_border {
  border: 1px red solid;
}

.red_bottom_border {
  border-bottom: 1px red solid;
}

.red_left_border {
  border-left: 1px red solid;
}

.red_right_border {
  border-right: 1px red solid;
}

.bottom_border {
  border-bottom: 1px black solid;
}

div.no_lateral_padding {
  padding-right: 0;
  padding-left: 0;
}

/**
 * Events categorization
 */

table.categ, table.totals {
  border-collapse: separate;
}

table.categ {
  border-spacing: 0px 7px;
}

table.totals {
  border-spacing: 5px;
}

table.categ th,
table.totals th {
  padding: 5px;
  white-space: wrap;
}

table.categ td,
table.totals td {
  padding: 5px;
  white-space: nowrap;
}

table.categ tr.red_line {
  outline-width: 2px;
  outline-color: red;
  outline-style: outset;
}
</style>
