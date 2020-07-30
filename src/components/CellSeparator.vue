<template>
  <div class="separator" v-html="space"></div>
</template>

<script>
export default {
  data: function() {
    return {
      space: "&nbsp;",
    }
  }
}
</script>

<style scoped>
.separator {
  width: 25px;
}
</style>
