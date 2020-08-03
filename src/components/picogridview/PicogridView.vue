<template>
  <div class="container-md">
    <div class="row info-bar">
      <div class="col-md-2"><span class="font-weight-bold">Block Nr</span></div>
      <div class="col-md-2"><span class="font-weight-bold">{{ blockNumber }}</span></div>
      <div class="col-md-8"><span class="font-weight-bold">Timestamp (DD-MM-YY HH:MM:SS)<br>{{ currentDate }}</span></div>
    </div>
    <div class="row">
      <div class="col-md-4"><span class="font-weight-bold">PREVIOUS HASH</span></div>
      <div class="col-md-8"><span>0005100308e7e0bea95a3e88e4e406c37133f0929c80866bda04bc0bce53a14</span></div>
    </div>
    <div class="row">
      <div class="col-md-3">Picogrid Nr</div>
      <div class="col-md-1">CAT</div>
      <div class="col-md-2">Power [W/H]</div>
      <div class="col-md-6">Picogrid Hash Consumption Hash</div>
    </div>
    <div v-for="index in 11"
         :key="'pv_' + index"
         class="row">
      <PicogridData :picogridReference="index"></PicogridData>
    </div>
    <div class="row info-bar">
      <div class="col-md-2"><span class="font-weight-bold">POW (DoD)</span></div>
      <div class="col-md-2"><span class="font-weight-bold">Number of ZEROS</span><br>3</div>
      <div class="col-md-8"><span class="font-weight-bold">BLOCK HASH DIGEST<br>0005100308e7e0bea95a3e88e4e406c37133f0929c80866bda04bc0bce53a14</span></div>
    </div>
  </div>
</template>

<script>
import PicogridData from './PicogridData.vue'

export default {
  data: function() {
    return {
      initialHash: "0005100308e7e0bea95a3e88e4e406c37133f0929c80866bda04bc0bce53a14",
      blockNumber: "000001"
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
    }
  }
}
</script>

<style scoped>
div.info-bar div {
 margin: auto 0;
}
</style>
