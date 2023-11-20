<template>
  <!-- Form view: -->
  <div v-if="display === 'form'" class="form-group">
    <label :for="field.name">{{ this.capitalize(field.name) }} <span v-if="requiredField">*</span></label>
    <SelectInput
      v-if="field.field_type === 'TEXT_CHOICE_FIELD'"
      :field="field"
      :selectedValue="inputValue"
      @input="$emit('blur', $event)"
    />
    <input
      v-if="field.field_type === 'TEXT_FIELD'"
      type="text"
      :class="getInputClass(field.field_type)"
      :id="field.name"
      :name="field.name"
      :placeholder="field.placeholder"
      :value="inputValue"
      @blur="$emit('blur', $event)"
    />
    <textarea
      v-if="field.field_type === 'TEXT_AREA_FIELD'"
      class="form-control"
      :id="field.name"
      :name="field.name"
      :placeholder="field.placeholder"
      rows="5"
      :value="inputValue"
      @blur="$emit('blur', $event)"
    ></textarea>
    <small>{{ field.description }}</small>
  </div>

  <!-- Table view: -->
  <SelectInput
    v-if="display === 'table' && field.field_type === 'TEXT_CHOICE_FIELD'"
    ref="input"
    class="noborder"
    :field="field"
    :selectedValue="inputValue"
    @input="$emit('blur', $event)"
    @keydown.exact="$emit('keydown', $event)"
  />
  <input
    v-if="display === 'table' && ['TEXT_FIELD', 'TEXT_AREA_FIELD'].includes(field.field_type)"
    ref="input"
    type="text"
    :class="getInputClass(field.field_type) + ' noborder'"
    :id="field.name"
    :name="field.name"
    :value="inputValue"
    :placeholder="field.placeholder"
    @blur="$emit('blur', $event)"
    @keydown.exact="$emit('keydown', $event)"
  />

  <!-- TODO: need a special input field for textarea -->

</template>

<script>
import { capitalize } from '@/utils/text'
import SelectInput from './SelectInput.vue'

const VALID_FIELD_TYPES = ['TEXT_FIELD', 'TEXT_AREA_FIELD', 'TEXT_CHOICE_FIELD']

export default {
  name: 'FormField',
  emits: [
    'blur',
    'keydown',
  ],
  props: {
    inputValue: String,
    field: {
      type: Object,
      validator(value) {
        return VALID_FIELD_TYPES.includes(value.field_type)
      }
    },
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
      const input = this.$refs.input
      input && input.focus()
    },
  }
}
</script>

<style scoped>
  .form-control {
    padding: 0.35rem;
    font-size: .8rem;
  }
  .noborder {
    border: none;
  }
</style>
