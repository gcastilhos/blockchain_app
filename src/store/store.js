import Vuex from 'vuex'
import Vue from 'vue'
Vue.use(Vuex)
import {INITIAL_HASH} from '@/mockdata'
import axios from 'axios'
import sha256 from 'sha256'

const ENCODE_API_URI = process.env.VUE_APP_ENCODE_API_URI || "/hash"
const HEADERS = JSON.parse(process.env.VUE_APP_HEADERS || "{}")
const DISPLAY_DELAY = parseInt(process.env.VUE_APP_DISPLAY_DELAY || 15000)
const NUMBER_OF_PICOGRIDS = 11

export default new Vuex.Store({
  state: {
    picogridTotals: [[], []],
    picogridSubTotals: [[], []],
    previousHash: [INITIAL_HASH, INITIAL_HASH],
    hashCodes: [[], []],
    totalsIndex: [-1, -1],
    displayGrid: false,
    snapShotView: [],
    flagSnapshot: false
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
      return state.picogridTotals
    },
    currentIndex: state => {
      return state.totalsIndex
    },
    displayGrid: state => {
      return state.displayGrid
    },
    snapShotViews: state => {
      return state.snapShotView
    },
    flagSnapshot: state => {
      return state.flagSnapshot
    }
  },
  mutations: {
    addPicogridTotals(state, payload) {
      state.picogridSubTotals[payload.index].push(payload.totals)
      if (state.picogridSubTotals[payload.index].length == NUMBER_OF_PICOGRIDS) {
        let sortedValuesAsString = state.picogridSubTotals[payload.index].sort((a, b) => b[1] < a[1]).map(a => JSON.stringify(a.slice(2))).join(',')
        state.picogridTotals[payload.index].push(sortedValuesAsString)
        state.totalsIndex[payload.index]++
        state.picogridSubTotals[payload.index] = []
      }
    },
    updatePreviousHash(state, payload) {
      state.previousHash[payload.index] = payload.newHash
    },
    addHashCodes(state, payload) {
      state.hashCodes[payload.index].push(payload.newHash)
    },
    displayGridNow(state, payload) {
      state.displayGrid = payload.value
    },
    addSnapshotView(state, payload) {
      state.snapShotView.push(payload.block)
      state.flagSnapshot = false
    },
    flagSnapshot(state, payload) {
      state.flagSnapshot = payload.value
    }
  },
  actions: {
    async addPicogridTotals(context, payload) {
      context.commit('addPicogridTotals', payload)
      let index = payload.index
      let currentTotals = context.getters.picogridTotalsCurrent
      let hashCodes = context.getters.hashCodes
      let currentIndex = context.getters.currentIndex
      let previousHash = context.getters.previousHash
      if (currentTotals[index].length > 0 && hashCodes[index].length < currentIndex[index] + 1) {
        try {
          let data = encodeURIComponent(currentTotals[index]).replaceAll("%22", "").replaceAll("%2C", "").replaceAll("%5B", "a").replaceAll("%5D", "z")
          let uri = `${ENCODE_API_URI}?previous=${previousHash[index]}&data=${data}`
          console.log(`HEADERS: ${HEADERS}`)
          let response = await axios.get(uri, {timeout: 20000, headers: HEADERS})
          let hashCode = response.data[1]
          context.commit('addHashCodes', {newHash: hashCode, index: index})
          context.commit('displayGridNow', {value: true})
          setTimeout(() => {
            context.commit('flagSnapshot', {value: true})
            context.commit('displayGridNow', {value: false})
            context.commit('updatePreviousHash', {newHash: hashCode, index: index})
          }, DISPLAY_DELAY)
        } catch(error) {
          console.log("Error while encoding data: " + error)
          context.commit('addHashCodes', {newHash: sha256(previousHash[index]), index: index})
        }
      }
    },
    addSnapshot(context, payload) {
      localStorage['snapshot' + payload.block] = payload.snapshot
      context.commit('addSnapshotView', payload)
    },
    flagSnapshot(context, payload) {
      context.commit('flagSnapshot', payload)
    }
  }
})
