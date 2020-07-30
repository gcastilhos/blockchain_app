<template>
<form>
  <div>
    <div class="house_no">Block <span v-html="lpad(houseNo + 1)" /></div>
    <img class="roof" src="../../assets/roof.png">
  </div>
  <table v-bind:class="{bg_red: active && blocks > 1 }">
    <tr>
      <th colspan="4">Consumption Data registered in a Blockchain Database</th>
    </tr>
    <tr>
      <td class="label">Block No</td>
      <td class="text">
        {{ blockNo | blockNoFormat }}
      </td>
      <td class="label dark_blue">Nonce</td>
      <td class="text">
        <input disabled="true" type="text" v-model="nonce" />
      </td>
    </tr>
    <tr>
      <td class="label purple">Previous&nbsp;Hash</td>
      <td class="text" colspan="3">
        <input class="red" disabled="true" type="text" v-model="previousHash" />
      </td>
    </tr>
    <tr>
      <td class="label big_font">Event<br/>Data</td>
      <td class="text" colspan="3">
        <textarea @keyup="getNewHash" v-model="evData"></textarea>
      </td>
    </tr>
    <tr>
      <td class="label">Block&nbsp;Hash</td>
      <td class="text" colspan="3">
        <input class="hash" disabled="true" type="text" v-model="hash" />
      </td>
    </tr>
  </table>
  <br />
  <table class="no_border">
    <tr>
      <td class="label narrow">SHA&nbsp;256</td>
      <td class="text" colspan="3"> 
        <input class="hash"  v-bind:class="{bg_red: active}" disabled="true" type="text" v-model="originalHash" />
      </td>
    </tr>
  </table>
</form>
</template>

<script>

export default {
  props: {
    index: Number,
    houseNo: Number,
    active: Boolean,
    hash: String,
    eventData: String,
    blockNo: Number,
    previousHash: String,
    originalHash: String,
    blocks: Number,
    nonce: Number
  },
  data: function() {
    return {
      evData: this.eventData
    }
  },
  methods: {
    lpad: function(num) {
      if (num < 10) {
        return "&nbsp;&nbsp;" + num;
      } else if (num < 100) {
        return "&nbsp;" + num;
      } else {
        return num;
      }
    },
    getNewHash: function() {
      this.$emit('get-hash', {id: this.index, data: this.evData});
    }
  },
  filters: {
    blockNoFormat: function(num) {
      return ("000" + num).slice(-6);
    }
  }
}
</script>

<style scoped>
/**
 * Table elements
 */
table {
    border: solid 2px grey; 
    border-spacing: 5px;
    background-color: #e2f0d9;
    width: 432px;
}

table.no_border {
    border: none;
    background-color: white;
}

th {
    text-align: left;
    font-size: 10pt;
    font-family: Calibri, Arial, Sans-serif;
}

td {
    border: solid 1pt #325490; 
    margin: 0;
    font-size: 8pt;
    background-color: #729fcf;
    font-family: Calibri, Arial, "Arial Narrow";
}

td.text {
    background-color: #e7e6e6; 
}

td.label {
    text-align: center;
    color: white;
    border-radius: 5px;
    font-weight: bold;
}

td.label.narrow {
    width: 16%;
}

td.big_font {
    font-size: 16pt;
    text-align: center;
}

td.dark_blue {
    background-color: #002060;
}

td.purple {
    background-color: #7030a0;
}

td.red {
    color: red;
}

/**
 * Graphical elements
 */

.roof {
    width: 100%;
    margin-bottom: 5px;
    object-fit: contain;
}

.house_no {
    position: relative;
    left: 168px;
    top: 80px;
    font-size: 16pt;
    font-weight: bold;
    font-family: Cablibri, Arial, Sans-serif;
}

.bg_red {
    background-color: red;
}

/**
 * Input elements
 */
input[type=text] {
    border: none;
    font-size: 8pt;
    background-color: #e7e6e6;
    color: black;
    width: 80%;
    font-family: Calibri, Arial, Sans-serif;
    font-weight: bold;
    font-size: 8pt;
}

input[type=text].red {
    color: red;
    font-weight: normal;
    width: 99%;
}

input[type=text].bg_red {
    background-color: red;
}

input[type=text].hash {
    font-weight: normal;
    width: 99%;
}

textarea {
    font-family: Calibri, Arial, Sans-serif;
    font-size: 8pt;
    background-color: #e7e6e6;
    color: black;
    border: medium none;
    width: 340px;
    display: block;
    overflow: hidden;
    resize: none;
    height: 150px;
}
</style>
