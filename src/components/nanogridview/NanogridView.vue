<template>
  <div class="container-md" id="picogrid_view">
    <div class="row info-bar header">
      <div class="col-md-2 main-label"><span class="middle font-weight-bold">Block Nr</span></div>
      <div class="col-md-2 main-info text-center"><span class="middle font-weight-bold" :style="{color: greyedOut}">{{ currentBlock | pad(6) }}</span></div>
      <div class="col-md-8 timestamp-label">
        <span class="font-weight-bold">Timestamp (DD-MM-YY HH:MM:SS)</span>
        <br>
        <span class="timestamp-info" :style="{color: greyedOut}">{{ displayTimestamp() }}</span>
      </div>
    </div>
    <div class="row">
      <div class="col-md-4 main-label previous_hash"><span class="font-weight-bold previous_hash">PREVIOUS HASH</span></div>
      <div class="col-md-8 main-info previous_hash"><span class="previous_hash" v-html="viewHashCode(previousHash)"></span></div>
    </div>
    <div class="row header secondary">
      <div class="col-md-3 secondary-label">Picogrid Nr</div>
      <div class="col-md-1 secondary-label">CAT</div>
      <div class="col-md-2 secondary-label">Power [W/H]</div>
      <div class="col-md-6 secondary-label">Picogrid Hash Consumption Hash</div>
    </div>
    <div v-for="index in numberOfPicogrids"
         :key="'pv_' + index"
         class="row data">
      <NanogridData :picogridReference="index"
                    :rowColor="rowColors[index - 1]"></NanogridData>
    </div>
    <div class="row info-bar footer">
      <div class="col-md-2 main-label"><span class="middle font-weight-bold">POW (DoD)</span></div>
      <div class="col-md-2 main-label text-center timestamp-label bg-grey">
        <span class="font-weight-bold border-bottom">Number of ZEROS</span>
        <div class="main-info timestamp-info">4</div>
      </div>
      <div class="col-md-8 main-label text-center timestamp-label bg-grey">
        <span class="font-weight-bold">BLOCK HASH DIGEST</span>
        <br>
        <div class="main-info timestamp-info" :style="{color: greyedOut}" v-html="viewHashCode(picogridTotalHash)"></div>
      </div>
    </div>
  </div>
</template>

<script>
import NanogridData from './NanogridData.vue'

export default {
  data: function() {
    return {
      numberOfPicogrids: 11,
      rowColors: ['#e2efda', '#ddebf7', '#f5d9ff', '#f5d9ff', '#fce4d6', '#ededed', '#c7e9f3', '#f0ea00', '#ccff66', '#ffbde9', '#ffcb97'] 
    }
  },
  components: {
    NanogridData
  },
  methods: {
    displayTimestamp: function() {
      return this.currentDate(new Date())
    },
    viewHashCode: function(hashes) {
      let hash = hashes[1]
      if (typeof(hash) !== "string") {
        hash = hash[hash.length - 1] 
      }
      return  hash !== undefined ? hash : "&nbsp;"
    },
    currentDate: function(curDate) {
      let todaysDay = curDate.getDate()
      let day = (todaysDay < 10 ? "0" : "") + todaysDay
      let todaysMonth = curDate.getMonth() + 1
      let month = (todaysMonth < 10 ? "0" : "") + todaysMonth
      let today = `${day}/${month}/${curDate.getFullYear()}`
      let hours = curDate.getHours()
      let am_pm = hours >= 12 ? 'PM' : 'AM'
      let time = `${hours > 12 ? hours - 12 : hours}:${curDate.getMinutes()}:${curDate.getSeconds()} ${am_pm}`
      return `${today} ${time}`
    }
  },
  computed: {
    picogridTotalHash: function() {
      return this.$store.getters.hashCodes
    },
    previousHash: function() {
      return this.$store.getters.previousHash
    },
    currentBlock: function() {
      return this.$store.getters.hashCodes[1].length
    },
    greyedOut: function() {
      return this.$store.getters.displayGrid ? "black" : "#ddd"
    }
  },
  filters: {
    pad: function(num, width, prefix) {
      prefix = prefix || "0"
      num = num + ""
      return num.length >= width ? num : new Array(width - num.length + 1).join(prefix) + num
    }
  }
}
</script>

<style scoped>
#picogrid_view {
  background-color: #808080;
  padding: 5px 20px;
  margin-bottom: 50px;
}

#picogrid_view div {
  font-size: 12px;
  color: black;
}

#picogrid_view div.row.header div,
#picogrid_view div.row.footer div {
  border: 1px solid black;
}

.main-label {
  background-color: #d9e1f2;
}

.row.header.secondary {
  margin-bottom:5px;
}

.main-info {
  background-color: white;
}

.timestamp-label {
  background-color: #fce4d6;
}

.secondary-label {
  background-color: white;
  font-size: 12pt !important;
}

.row.footer {
  margin-top: 5px;
}

.footer span {
  font-size: 12pt;
  white-space: nowrap;
}

.info-bar.header div span {
  font-size: 14pt;
}

span.middle {
  display: inline-block;
  vertical-align: middle;
  padding-top: 12px;
}

.timestamp-label {
  padding: 0;
}

.timestamp-label span {
  padding: 0 15px;
}

.timestamp-info {
  border: 0 !important;
  background-color: white;
  padding: 0 15px;
  font-size: 14pt !important;
  display: block;
}

div.previous_hash {
  border-left: 1px solid black;
  border-right: 1px solid black;
  border-bottom: none !important;
}

span.previous_hash {
  margin: 5px 0px !important;
  display: inline-block;
  font-size: 14pt;
}

.bg-grey {
  background-color: #d9e1f2;
}

.border-bottom {
  border-bottom: 1px solid black !important;
  display: block;
}
</style>
