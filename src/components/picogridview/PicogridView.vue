<template>
  <div class="container-md" id="picogrid_view">
    <div class="row info-bar header">
      <div class="col-md-2 main-label"><span class="middle font-weight-bold">Block Nr</span></div>
      <div class="col-md-2 main-info text-center"><span class="middle font-weight-bold">{{ blockNumber }}</span></div>
      <div class="col-md-8 timestamp-label">
        <span class="font-weight-bold">Timestamp (DD-MM-YY HH:MM:SS)</span>
        <br>
        <div class="timestamp-info">{{ currentDate }}</div>
      </div>
    </div>
    <div class="row">
      <div class="col-md-4 main-label previous_hash"><span class="font-weight-bold previous_hash">PREVIOUS HASH</span></div>
      <div class="col-md-8 main-info previous_hash"><span class="previous_hash">0000510308e7e0bea95a3e88e4e406c37133f0929c80866bda04bc0bce53a14</span></div>
    </div>
    <div class="row header secondary">
      <div class="col-md-3 secondary-label">Picogrid Nr</div>
      <div class="col-md-1 secondary-label">CAT</div>
      <div class="col-md-2 secondary-label">Power [W/H]</div>
      <div class="col-md-6 secondary-label">Picogrid Hash Consumption Hash</div>
    </div>
    <div v-for="index in 11"
         :key="'pv_' + index"
         class="row data">
      <PicogridData :picogridReference="index"
                    :rowColor="rowColors[index - 1]"></PicogridData>
    </div>
    <div class="row info-bar footer">
      <div class="col-md-2 main-label"><span class="font-weight-bold">POW (DoD)</span></div>
      <div class="col-md-2 main-label"><span class="font-weight-bold">Number of ZEROS</span><br><div class="main-info">4</div></div>
      <div class="col-md-8 main-label"><span class="font-weight-bold">BLOCK HASH DIGEST</span><br><div class="main-info">{{ picogridTotalHash |  viewHashCode }}</div></div>
    </div>
  </div>
</template>

<script>
import PicogridData from './PicogridData.vue'

export default {
  data: function() {
    return {
      initialHash: "0005100308e7e0bea95a3e88e4e406c37133f0929c80866bda04bc0bce53a14",
      blockNumber: "000001",
      rowColors: ['#e2efda', '#ddebf7', '#f5d9ff', '#f5d9ff', '#fce4d6', '#ededed', '#c7e9f3', '#f0ea00', '#ccff66', '#ffbde9', '#ffcb97'] 
    }
  },
  components: {
    PicogridData
  },
  computed: {
    currentDate: function() {
      let currentDate = new Date()
      let todaysDay = currentDate.getDate()
      let day = (todaysDay < 10 ? "0" : "") + todaysDay
      let todaysMonth = currentDate.getMonth() + 1
      let month = (todaysMonth < 10 ? "0" : "") + todaysMonth
      let today = `${day}/${month}/${currentDate.getFullYear()}`
      let hours = currentDate.getHours()
      let am_pm = hours >= 12 ? 'PM' : 'AM'
      let time = `${hours > 12 ? hours - 12 : hours}:${currentDate.getMinutes()}:${currentDate.getSeconds()} ${am_pm}`
      return `${today} ${time}`
    },
    picogridTotalHash: function() {
      return this.$store.getters.hashCodes
    }
  },
  filters: {
    viewHashCode: function(hashes) {
      let hash = hashes[1]
      return hash[hash.length - 1]
    }
  }
}
</script>

<style scoped>
#picogrid_view {
  background-color: #808080;
  padding: 5px 20px;
}

#picogrid_view div {
  font-size: 12px;
  color: black;
}

/*div.info-bar div {
 margin: auto 0;
}*/

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
</style>
