<template>
  <div class="editableTable">
    <table v-if="schema">
      <thead>
        <tr>
          <th v-for="field in schema.fields" :key="field.name">
            <div class="d-flex">
              <div class="col p-0">
                {{ idToTitle(field.name) }}
                <span v-if="field.units">({{ field.units }})</span>
                <span v-if="field.cardinality === 'mandatory'" class="ml-1" style="user-select: none;">*</span>
              </div>
              <div class="col-auto p-0 ml-2">
                <span class="info">
                  i
                  <v-tooltip
                    activator="parent"
                    location="top"
                    :max-width="field.description.length < 200 ? 300 : 600"
                    style="overflow-wrap: break-word;"
                  >
                    <span v-if="field.cardinality === 'mandatory'" class="tip required">Required</span>
                    <span v-if="field.cardinality === 'optional'" class="tip optional">Optional</span>
                    {{ field.description }}
                  </v-tooltip>
                </span>
              </div>
            </div>
          </th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(row, rowIx) in data" :key="rowIx">
          <td v-for="field in schema.fields" :key="field.name + rowIx">
            <FormField
              display="table"
              :field="field"
              :ref="getInputRef(rowIx, field.name)"
              :inputValue="row[field.name]"
              @blur="updateCell(rowIx, field.name, $event.target.value)"
              @keydown.exact="inputKeydown($event, rowIx, field.name)"
            />
          </td>
        </tr>
      </tbody>
    </table>
  </div>

  <button class="btn btn-secondary mr-2 my-2" @click="this.addRows(1)">Add row</button>
  <button class="btn btn-secondary mr-2 my-2" disabled>Copy table to clipboard</button>


  <!-- For debugging state: -->
  <!-- <div><p>Row 1 data:</p><pre>{{ data[0] }}</pre></div> -->

</template>

<script>

// Functionality to clone:
// - clipboard paste from XLSX
// - copy all to clipboard

import FormField from './fields/FormField.vue'
import { useFormStore } from '@/stores/forms'

const INIT_ROWS = 5;
const formStore = useFormStore()

export default {
  name: 'EditableTable',
  components: {
    FormField: FormField,
  },
  props: {
    schema: Object,
    formStoreKey: String,
  },
  data() {
    return {
      undoData: [],
    }
  },
  computed: {
    data() {
      return formStore.getFormData(this.formStoreKey)
    },
  },
  mounted() {
    if (!this.data.length) {
      this.initRows()
    }
    document.addEventListener('keydown', (event) => {
      // Bind ctrl+z to setDataUndo
      if (event.ctrlKey && event.key === 'z') {
        this.setDataUndo()
      }
    })
  },
  methods: {
    updateCell(rowIx, field_name, value) {
      // console.log('updateCell', rowIx, field_name, value)
      formStore.$patch( (state) => {
        state[this.formStoreKey][rowIx][field_name] = value
        state.hasChanged = true
      })
    },
    setData(data) {
      this.undoData.unshift(this.data)
      formStore.$patch( (state) => {
        state[this.formStoreKey] = data
        state.hasChanged = true
      })
    },
    setDataUndo() {
      this.setData(this.undoData.shift())
      this.undoData.shift()
    },
    idToTitle(id) {
      return id
        .split('_')
        .map((word) => word.charAt(0).toUpperCase() + word.slice(1))
        .join(' ')
    },
    initRows() {
      this.addRows(INIT_ROWS)
    },
    addRows(num_rows) {
      const blankRows = []
      this.blankRow = this.schema.fields.reduce( (obj, field) => {
        obj[field.name] = ''
        return obj
      }, {})
      for (let i = 0; i < num_rows; i++) {
        blankRows.push({...this.blankRow})
      }
      const newData = [...this.data, ...blankRows]
      this.setData(newData)
    },
    getInputRef(rowIx, fieldName) {
      return `input_row${rowIx}_${fieldName}`
    },
    inputKeydown(event, rowIx, fieldName) {
      let newRowIx
      let newFieldName
      switch (event.key) {
        case 'Enter':
          // navigate cell down
          newRowIx = Math.min(rowIx + 1, this.data.length - 1)
          newFieldName = fieldName
          break
        case 'ArrowUp':
          // navigate cell up
          newRowIx = Math.max(rowIx - 1, 0)
          newFieldName = fieldName
          break
        case 'ArrowDown':
          // navigate cell down
          newRowIx = Math.min(rowIx + 1, this.data.length - 1)
          newFieldName = fieldName
          break
        case 'ArrowLeft':
          // navigate cell left
          newRowIx = rowIx
          newFieldName = this.schema.fields[Math.max(
            this.schema.fields.findIndex((val) => val.name === fieldName) - 1,
            0)].name
          break
        case 'ArrowRight':
          // navigate cell right
          newRowIx = rowIx
          newFieldName = this.schema.fields[Math.min(
            this.schema.fields.findIndex((val) => val.name === fieldName) + 1,
            this.schema.fields.length - 1)].name
          break
        default:
          return
      }
      // const field = this.$refs[this.getInputRef(newRowIx, newFieldName)][0]
      // field && field.focus()
      this.$refs[this.getInputRef(newRowIx, newFieldName)][0].focus()
    },
  },
}
</script>

<style scoped>
  .editableTable {
    max-width: 100%;
    overflow-x: auto;
    font-size: .8rem;
    white-space: nowrap;
  }
  .editableTable table {
    width: 100%;
  }
  .editableTable th {
    padding: 0.5rem;
    background: #eee;
  }
  .editableTable th, .editableTable td {
    border: 1px solid #dee2e6;
    min-width: 150px;
    width: fit-content;
  }
  .editableTable td {
    padding: 0 2px;
  }
  span.info {
    color: #aaa;
    font-size: 1rem;
    border: 1px solid #aaa;
    border-radius: 50%;
    line-height: 1.1;
    padding: 0 .4rem;
    cursor: default;
    user-select: none;
  }
  .tip {
    color: white;
    padding: .1rem .5rem;
    border-radius: .5rem;
    line-height: 1.1;
    cursor: default;
    user-select: none;
  }
  .tip.required {
    background: #e35027;
  }
  .tip.optional {
    background: #888;
  }
</style>
