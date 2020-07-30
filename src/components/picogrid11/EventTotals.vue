<template>
  <div class="hash-frame">
    Block #{{ totalsNumber }}: <span class="hash mono">{{ totals }}</span>
  </div>
</template>

<script>
export default {
  props: ['totals', 'totalsNumber']
}
</script>

<style scoped>
div {
  border: 1px solid grey;
  padding: 3px;
  border-radius: 5px;
  font-weight: bold;
  font-size: 2.2em;
  word-wrap: break-word;
  margin-bottom: 15px;
  text-align: center;
}

span.hash {
  background-color: lightGrey;
  padding: 5px;
  font-family: Courier;
}
</style>
