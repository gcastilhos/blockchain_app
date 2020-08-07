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
