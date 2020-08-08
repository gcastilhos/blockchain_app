<template>
  <div id="nanogrid_snapshot" class="container-md">
    <div class="row">
      <div class="col-md-12 text-center">
        <label for="block_number" class="block-number font-weight-bold">Choose the block number:</label>
        <input type="number" class="block-number " min="1" :max="maxBlock" size="3" name="block_number" @change="getCurrentBlock($event)">
      </div>
    </div>
    <snapshotData class="row"
                  v-html="fromStorage">
    </snapshotData>
  </div>
</template>

<script>
const TRIANGLE = '/img/triangle_link.fbaab044.png'
const TRIANGLE_DOWN = '/img/triangle_link_down.a33343dc.png'

const SnapshotData = {
  render: function(h) {
    return h('div', this.$slots.default)
  }
}

export default {
  data: function() {
    return {
      displayBlock: 0
    }
  },
  computed: {
    nanoIds: function() {
      return this.$store.getters.snapShotViews
    },
    maxBlock: function() {
      return this.$store.getters.snapShotViews.length
    },
    fromStorage: function() {
      return localStorage[`snapshot${this.displayBlock}`]
    }
  },
  components: {
    snapshotData: SnapshotData
  },
  methods: {
    getCurrentBlock: function(event) {
      this.displayBlock = event.target.valueAsNumber
    }
  },
  updated: function() {
    let dataLinks = document.getElementsByClassName('show-data', this.$el)
    if (dataLinks.length > 0) {
      for (let i = 0; i < 11; ++i) {
        let link = dataLinks[i]
        let parentNode = link.parentNode.parentNode.parentNode
        let rows = parentNode.querySelectorAll('.row')
        let hiddenRows = []
        rows.forEach(row => {
          if (row.style.display === 'none') {
            hiddenRows.push(row)
          }
        })
        link.addEventListener('click', function(event) {
          let img = event.target
          let isDown = img.src.search('down') > -1
          img.src = isDown ? TRIANGLE : TRIANGLE_DOWN
          hiddenRows.forEach(row => {
            row.style.display = isDown ? 'none' : 'flex'
          })
        })
      }
    } 
  }
}
</script>

<style>
label.block-number {
  font-size: 1.5em;
  color: darkBlue;
  padding-right: 10px;
}

input[type="number"].block-number {
  font-size: 1.5em;  
}
</style>
