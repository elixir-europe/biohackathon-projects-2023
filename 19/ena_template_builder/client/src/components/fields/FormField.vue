<template>
  <div class="form-group">
    <label :for="field.name">{{ this.capitalize(field.name) }} <span v-if="requiredField">*</span></label>
    <SelectInput v-if="field.field_type === 'TEXT_CHOICE_FIELD'" :field="field"/>
    <input v-else :class="getInputClass(field.field_type)" :id="field.name" :name="field.name" type="text" :placeholder="field.placeholder" />
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
  computed: {
    requiredField() {
      return this.field.cardinality === 'mandatory'
    }
  },
  methods: {
    capitalize(text) {
      return capitalize(text)
    },
    mapFieldType(type) {
      // Not currently used as all field.field_type values resolve to "text"
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
        case 'BOOLEAN_FIELD':
          return 'form-check-input'
        default:
          return 'form-control'
      }
    }
  }
}
</script>
