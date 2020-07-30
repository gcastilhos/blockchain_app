<template>
  <div id="slider">
    <table id="records">
      <thead>
        <tr>
          <th v-for="(item, index) in header" 
              :key="'head_' + index"
              class="header dark-blue">
            {{ item }}
          </th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(record, rowIndex) in records"
            :key="'rec_' + rowIndex">
          <td v-for="(item, index) in record"
              :key="'val_' + index"
              class="record original dark-blue text mono"
              :style="{textAlign: index > 12 ? 'left' : 'right'}"
              v-html="item">
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import encode from '@/encoder.js'

export default {
  props: {
    header: Array,
    records: Array,
    finalHash: String,
    batch: Number
  },
  filters: {
    encode,
    recordAsString: function(record) {
      return record.join("|")
    }
  },
  computed: {
    numberOfEvents: function() {
      if (this.batch == 1) {
        return "1 event"
    }
      return "each " + this.batch + " events"
    }
  }
}
</script>

<style>
#slider {
  width: 100%;
  height: 650px;
  overflow-x: scroll;
  overflow-y: scroll;
}

.record.original {
    text-align: right;
    white-space: nowrap;
}

.text {
    font-family: "Lucida Console", Monaco, Courier, monospace;
}

.mono {
    font-family: "Lucida Console", Monaco, Courier, monospace;
}
</style>
