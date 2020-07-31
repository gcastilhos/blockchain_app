<template>
  <div id="events_houses">
    <div class="container-fluid">
      <div v-for="(row, indRow) in rows"
           :key="'r_' + indRow"
           class="row">
        <div class="col-1" v-if="indRow == 0">
           <label class="blocks font-weight-bold" for="numberOfBlocks">Number of houses (up to 100):</label>
           <input type="number" id="numberOfBlocks" name="numberOfBlocks" @keyup="updateRows" v-model="blocks" min="1" max="100" maxlength="3"/>
        </div>
        <div class="col-1" v-else></div>
        <div v-for="(column, indCol) in numCols(row)"
             :key="'c_' + indCol"
             class="col-5 text-left">
          <house-blockchain v-on:get-hash="getNewHash($event)"
                            :index="getIndex(row, column)"
                            :houseNo="getIndex(row, column)"
                            :active="active[getIndex(row, column)]"
                            :hash="hash[getIndex(row, column)]"
                            :eventData="eventData[getIndex(row, column)]"
                            :blockNo="blockNo + getIndex(row, column)"
                            :previousHash="previousHash[getIndex(row, column)]"
                            :originalHash="originalHash[getIndex(row, column)]"
                            :blocks="validBlocks"
                            :nonce="nonce[getIndex(row, column)]">
          </house-blockchain>
        </div>
        <div class="col-1"></div>
      </div>
    <div class="right"></div>
  </div>
  </div>
</template>

<script>
import Vue from 'vue'
import VueRouter from 'vue-router'
import sha256 from 'sha256'
import HouseBlockchain from './HouseBlockchain.vue'
import {MOCK_EVENT_DATA, INITIAL_HASH} from '@/mockdata'
Vue.use(VueRouter)

const MAX_BLOCKS = parseInt(process.env.VUE_APP_MAX_BLOCKS || 100)

var isValidHash = function(hashCode) {
   if (hashCode !== undefined) {
     return hashCode.startsWith("000")
   }
   return false
}

var router = new VueRouter({
  mode: 'history',
  routes: []
})

export default {
  router,
  data: function() {
    return {
      blockNo: 432,
      hash: new Array(MAX_BLOCKS).fill(''),
      previousHash: new Array(MAX_BLOCKS).fill(''),
      nonce: new Array(MAX_BLOCKS).fill(0),
      eventData: new Array(MAX_BLOCKS).fill(MOCK_EVENT_DATA),
      originalHash: new Array(MAX_BLOCKS).fill(''),
      active: new Array(MAX_BLOCKS).fill(false),
      blocks: 1,
      rows: 1
    }
  },
  components: {
    houseBlockchain: HouseBlockchain
  },
  methods: {
    encode: function(id) {
      var nonce = -1
      var hashCode = undefined
      while (!isValidHash(hashCode)) {
        nonce++
        var textToEncode = this.previousHash[id] + this.eventData[id] + nonce
        hashCode = sha256(textToEncode)
      }
      return {"nonce": nonce, "hash": hashCode}
    },
    getNewHash: function(data) {
      this.$set(this.eventData, data.id, data.data)
      this.getHash(data.id)
    },
    getHash: function(id) {
      var data = this.encode(id)
      this.$set(this.nonce, id, data.nonce)
      this.$set(this.hash, id, data.hash)
      if (this.originalHash[id] === '') {
        this.$set(this.originalHash, id, this.hash[id])
      } else {
        this.$set(this.active, id, (this.originalHash[id] != this.hash[id]))
      }
      if (id < this.blocks - 1) {
        this.$set(this.previousHash, id + 1, this.hash[id])
        this.getHash(id + 1)
      }
    },
    numCols: function(rows) {
      if (2 * rows > this.blocks) {
        return 1
      }
      return 2
    },
    getIndex: function(row, column) {
      return 2 * row + column - 3; 
    },
    setInitialHash: function() {
      this.$set(this.previousHash, 0, INITIAL_HASH)
    },
    updateRows: function() {
      this.rows = Math.ceil(this.validBlocks / 2); 
      this.setInitialHash()
      this.getHash(0)
    }
  },
  mounted: function() {
    this.rows = Math.ceil(this.validBlocks / 2); 
    this.setInitialHash()
    this.getHash(0)
  },
  computed: {
    validBlocks: function() {
      let blocks = parseInt(this.blocks)
      return isNaN(blocks) ? 1 : blocks < 1 ? 1 : Math.min(blocks, MAX_BLOCKS)
    }
  }
}
</script>

<style>
#events_houses {
  padding-bottom: 50px;
}
#numberOfBlocks {
  width: 55px;
  padding: 1px;
}

label.blocks {
  color: darkBlue;
}
</style>
