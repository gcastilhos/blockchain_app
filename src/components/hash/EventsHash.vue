<template>
  <div id="events_hash" class="container-fluid">
    <div class="row">
      <div class="col-8">
        <table>
          <thead>
            <tr>
              <th class="header big-font black" colspan="15">
                  <span>DAILY EVENT TABLE - BATCH {{ batch }}</span>
              </th>
            </tr>
            <tr>
              <th v-for="(item, index) in header" :key="'head_' + index" class="header dark-blue">
                {{ item }}
              </th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(record, rowIndex) in records" :key="'rec_' + rowIndex">
              <td v-for="(item, index) in record" :key="'val_' + index" class="record original dark-blue text mono" v-html="item">
              </td>
            </tr>
          </tbody>
        </table>
      </div>
      <div class="col-4">
        <table>
          <thead>
            <tr>
              <th class="big-font red">
                <span>EVENT HASHING</span>
              </th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(record, rowIndex) in records" :key="'hash_' + rowIndex">
              <td class="record dark-blue">
                <div class="text hash">
                  {{ record | recordAsString | encode }}
                </div>
              </td>
            </tr>
            <tr>
              <td class="final-hash">
                <div class="text note no-lateral-padding">
                  <span>Block HASH for {{numberOfEvents}}</span>
                </div>
              </td>
            </tr>
            <tr>
              <td class="yellow final-hash">
                <div class="text hash">
                  {{ finalHash }}
                </div>
              </td>
            </tr>
          </tbody>
        </table>
 </div>
    </div>
  </div>
</template>

<script>
import sha256 from 'sha256';
import axios from 'axios';
import {MOCK_DATA} from '@/mockdata'

const DATA_API_URI = process.env.VUE_APP_DATA_API_URI || "/events";
const HEADERS = JSON.parse(process.env.VUE_APP_HEADERS || "{}")

var encode = function(text) {
  if (text !== '') {
    return sha256(text);
  }
  return text;
};

export default {
  data: function () {
    return {
      records: [],
      header: [],
      finalHash: '',
      batch: 1,
      interval: parseInt(process.env.VUE_APP_DELAY || 10000)
    }
  },
  filters: {
    encode,
    recordAsString: function(record) {
      return record.join("|");
    },
  },
  methods: {
    getData: async function(next_batch) {
      var data;
      try {
        let response = await axios.get(DATA_API_URI, {timeout: 10000, headers: HEADERS});
        data = response.data;
        console.log("Data:" + data.data);
        console.log("Columns:" + data.columns);
      } catch (error) {
        console.error("Error: " + error);
        data = MOCK_DATA;
      }
      this.records.push(data.data[0]);
      this.batch = next_batch;
      this.header = data.columns;
      this.encodeAll();
    },
    encodeAll: function() {
      var finalHash = '';
      this.records.forEach((rec) => {
        finalHash += encode(rec);
      });
      this.finalHash = encode(finalHash);
    },
  },
  computed: {
    numberOfEvents: function() {
      if (this.batch == 1) {
        return "1 event";
    }
      return "each " + this.batch + " events"
    }
  },
  mounted: function() {
    this.getData(this.batch);
  },
  created: function() {
    setInterval(function() {
      let next_batch;
      if (this.batch === 100) {
        next_batch = 1;
        this.records.splice(0, 100);
      } else {
        next_batch = this.batch + 1;
      }
      this.getData(next_batch);
    }.bind(this), this.interval);
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

/**
 * Table
 */

table {
    padding: 50px;
    border-spacing: 0;
}

.header {
    font-weight: bold;
    word-wrap: break-word;
    border-bottom: 1px black solid;
}

td, th {
    padding: 2px 4px;
}

.dark-blue {
    background-color: #038cfc;
}

.record.original {
    text-align: right;
    white-space: nowrap;
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

.final-hash {
    background-color: lightBlue;
    padding: 5px 0;
    text-align: center;
}

.final-hash.yellow {
    padding: 10px;
}

div.note {
    text-align: center;
    font-size: 10pt;
    font-weight: bold;
    border: 1px black solid;
    padding: 2px;
    background-color: white;
}

/**
 * Generic styles
 */

.big-font {
    font-size: 16pt;
    font-family: Arial, Helvetica, Sans-serif;
    font-weight: bold;
    text-align: center;
}

.red {
    color: red;
}

.light-blue {
    background-color: lightBlue;
}

.yellow {
    background-color: yellow;
}

.mono {
    font-family: "Lucida Console", Monaco, Courier, monospace;
}

div.no-lateral-padding {
    padding-right: 0;
    padding-left: 0;
}
</style>
