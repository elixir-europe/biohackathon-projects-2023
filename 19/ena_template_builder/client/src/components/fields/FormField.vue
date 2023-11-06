<template>
  <div v-if="display === 'form'" class="form-group">
    <label :for="field.name">{{ this.capitalize(field.name) }} <span v-if="requiredField">*</span></label>
    <SelectInput v-if="field.field_type === 'TEXT_CHOICE_FIELD'" :field="field"/>
    <input
      v-else
      type="text"
      :class="getInputClass(field.field_type)"
      :id="field.name"
      :name="field.name"
      :placeholder="field.placeholder"
      @input="$emit('input', $event)"
      @keydown.exact="$emit('keydown.exact', $event)"
    />
    <small>{{ field.description }}</small>
  </div>

  <SelectInput
    v-if="display === 'table' && field.field_type === 'TEXT_CHOICE_FIELD'"
    ref="input"
    :field="field"
    @input="$emit('blur', $event)"
  />
  <input
    v-if="display === 'table' && field.field_type === 'TEXT_FIELD'"
    ref="input"
    type="text"
    :class="getInputClass(field.field_type)"
    :id="field.name"
    :name="field.name"
    :placeholder="field.placeholder"
    @blur="$emit('blur', $event)"
    @keydown.exact="$emit('keydown', $event)"
  />
</template>

<script>
import { capitalize } from '@/utils/text'
import SelectInput from './SelectInput.vue'

export default {
  name: 'FormField',
  emits: [
    'blur',
    'keydown',
  ],
  props: {
    // 'onKeydown.exact': Function,
    field: Object,
    display: {
      type: String,
      default: 'form',
      validator(value) {
        return ['form', 'table'].includes(value)
      }
    },
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
    },
    focus() {
      this.$refs.input.focus()
    },
  }
}
</script>

<style scoped>
  .form-control {
    border: none;
    padding: 0.35rem;
    font-size: .8rem;
  }
  .noborder {
    border: none;
  }
</style>
