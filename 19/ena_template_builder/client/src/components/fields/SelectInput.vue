<template>
  <select
    class="custom-select"
    ref="select"
    @input="validateInput($event)"
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
  watch: {
    selectedValue() {
      if (!this.field.cv.includes(this.selectedValue)) {
        this.$emit('input', { target: { value: '' } })
      }
    }
  },
  methods: {
    capitalize(text) {
      return capitalize(text)
    },
    focus() {
      this.$refs.select.focus()
    },
  }
}
</script>
