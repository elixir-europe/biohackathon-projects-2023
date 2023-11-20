<template>
  <select
    class="custom-select"
    ref="select"
    @keydown.exact="$event.preventDefault() && $emit('keydown', $event)"
  >
    <option value=""></option>
    <option v-for="option in field.cv" :key="option" :value="option" :selected="option === this.selectedValue">{{ option }}</option>
  </select>
</template>

<script>
import { capitalize } from '@/utils/text'

export default {
  name: 'SelectInput',
  props: {
    field: Object,
    selectedValue: String,
  },
  methods: {
    capitalize(text) {
      return capitalize(text)
    },
    focus() {
      this.$refs.select.focus()
    }
  }
}
</script>
