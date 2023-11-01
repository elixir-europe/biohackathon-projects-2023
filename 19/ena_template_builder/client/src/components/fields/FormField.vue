<template>
  <div class="form-group">
    <label :for="field.name">{{ this.capitalize(field.name) }} <span v-if="field.required">*</span></label>
    <SelectInput v-if="field.cv" :field="field"/>
    <input v-else :class="getInputClass(field.type)" :id="field.name" :name="field.name" :type="mapFieldType(field.type)" :placeholder="field.placeholder" />
    <small>{{ field.description }}</small>
  </div>
</template>

<script>
import { capitalize } from '@/utils/text'
import SelectInput from './SelectInput.vue'

export default {
  name: 'FormField',
  props: {
    field: Object,
  },
  components: {
    SelectInput: SelectInput,
  },
  methods: {
    capitalize(text) {
      return capitalize(text)
    },
    mapFieldType(type) {
      switch (type) {
        case 'string':
          return 'text'
        case 'number':
          return 'number'
        case 'boolean':
          return 'checkbox'
        default:
          return 'text'
      }
    },
    getInputClass(type) {
      switch (type) {
        case 'boolean':
          return 'form-check-input'
        default:
          return 'form-control'
      }
    }
  }
}
</script>
