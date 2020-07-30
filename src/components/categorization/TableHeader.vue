<template>
  <div class="red">
    <h2 class="big_font" v-if="titleH2 != undefined" v-html="titleH2"></h2>
    <h4 class="big_font" v-if="titleH4 != undefined" v-html="titleH4"></h4>
  </div>
</template>

<script>
export default {
  props : {
    titleH2: {
      type: String
    },
    titleH4: {
      type: String
    }
  }
}
</script>

<style scoped>
.big_font {
  font-size: 24pt;
  font-family: Arial, Helvetica, Sans-serif;
  font-weight: bold;
  text-align: center;
}

h4.big_font {
  font-size: 18pt;
  margin-top:20px;
  margin-bottom: 20px;
}
</style>
