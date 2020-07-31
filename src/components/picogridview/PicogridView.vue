<template>
  <div class="message" v-html="message"></div>
</template>

<script>
export default {
  data: function() {
    return {
      message: "&#x26CF; Under construction &#x26CF;"
    }
  }
}
</script>

<style scoped>
.message {
  width: 100%;
  height: 50px;
  font-size: 3em;
  color: darkBlue;
  text-align: center;
}
</style>
