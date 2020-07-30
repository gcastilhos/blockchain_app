<template>
    <div class="no_space_break"><h5 v-html="eventNumberText"></h5></div>
</template>

<script>
export default {
  props: {
    eventNumberText: {
      type: String
    }
  }
}
</script>

<style scoped>
h5 {
    font-size: 16pt;
    font-weight: bold;
    margin: 5px 0;
    text-align: center;
}
</style>
