import Vuex from 'vuex'
import Vue from 'vue'
Vue.use(Vuex)
import {INITIAL_HASH} from '@/mockdata'
import axios from 'axios'
import sha256 from 'sha256'

const ENCODE_API_URI = process.env.VUE_APP_ENCODE_API_URI || "/hash"
const HEADERS = JSON.parse(process.env.VUE_APP_HEADERS || "{}")

export default new Vuex.Store({
  state: {
    picogridTotals: [],
    picogridSubTotals: [],
    previousHash: INITIAL_HASH,
    hashCodes: [],
    totalsIndex: -1
  },
  getters: {
    picogridsHashes: state => {
      return state.picogridTotals
    },
    previousHash: state => {
      return state.previousHash
    },
    hashCodes: state => {
      return state.hashCodes
    },
    picogridTotalsCurrent: state => {
      return state.totalsIndex >= 0 ? state.picogridTotals[state.totalsIndex] : undefined
    },
    currentIndex: state => {
      return state.totalsIndex
    }
  },
  mutations: {
    addPicogridTotals(state, payload) {
      state.picogridSubTotals.push(payload.totals)
      if (state.picogridSubTotals.length == 11) {
        let sortedValuesAsString = state.picogridSubTotals.sort((a, b) => b[1] < a[1]).map(a => JSON.stringify(a.slice(2))).join(',')
        state.picogridTotals.push(sortedValuesAsString)
        state.totalsIndex++
        state.picogridSubTotals = []
      }
    },
    updatePreviousHash(state, payload) {
      state.previousHash = payload.newHash
    },
    addHashCodes(state, payload) {
      state.hashCodes.push(payload.newHash)
    }
  },
  actions: {
    async addPicogridTotals(context, payload) {
      context.commit('addPicogridTotals', payload)
      let currentTotals = context.getters.picogridTotalsCurrent
      let hashCodes = context.getters.hashCodes
      let currentIndex = context.getters.currentIndex
      let previousHash = context.getters.previousHash
      if (currentTotals !== undefined && hashCodes.length < currentIndex + 1) {
        try {
          let uri = `${ENCODE_API_URI}?previous=${previousHash}&data=${encodeURIComponent(currentTotals)}`
          let response = await axios.get(uri, {timeout: 10000, headers: HEADERS})
          let hashCode = response.data[1]
          context.commit('addHashCodes', {newHash: hashCode})
          context.commit('updatePreviousHash', {newHash: hashCode})
        } catch(error) {
          console.log("Error while encoding data: " + error)
          context.commit('addHashCodes', {newHash: sha256(previousHash)})
        }
      }
    }
  }
})
