<template>
  <div ref="table"></div>
  <button class="btn btn-primary" @click="() => this.addRows(1)">Add row</button>
</template>

<script>
import { TabulatorFull as Tabulator } from 'tabulator-tables'
import { useFormStore } from '@/stores/forms'

const START_ROWS = 5
const { formState, setFormData } = useFormStore()

export default {
  name: 'EditableTable',
  props: {
    schema: Object,
    storeKey: String,
  },
  data() {
    return {
      tabulator: null
    }
  },
  computed: {
    data() {
      return formState[this.storeKey]
    },
  },
  mounted() {
    if (Object.keys(this.schema).length) {
      if (!this.data.length) {
        this.addRows(START_ROWS)
      }
      // This is not listening to changes in data...
      // TODO: trying with store accessed directly instead of through prop...
      this.tabulator = new Tabulator(this.$refs.table, {
        data: this.data,
        reactiveData: true,
        columns: this.columnsFromSchema(this.schema),
        clipboard: true,
        keybindings: {
          navLeft: '37',
          navRight: '39'
        }
      })
    }
  },
  methods: {
    setData(data) {
      setFormData(this.storeKey, data)
    },
    columnsFromSchema(schema) {
      return schema.fields.map((field) => {
        return {
          title: this.idToTitle(field.name),
          field: field.name,
          sorter: 'string',
          tooltip: field.description,
          editor: 'input'
        }
      })
    },
    idToTitle(id) {
      return id
        .split('_')
        .map((word) => word.charAt(0).toUpperCase() + word.slice(1))
        .join(' ')
    },
    addRows(n) {
      const rows = []
      for (let i = 0; i < n; i++) {
        rows.push(
          this.schema.fields.reduce((acc, field) => {
            acc[field.name] = ''
            return acc
          }, {})
        )
      }
      const newData = this.data.concat(rows)
      this.setData(newData)
    }
  }
}
</script>
