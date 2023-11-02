<template>
  <h1 class="mb-5">Experiment</h1>

  <p v-if="!this.schema">Loading...</p>

  <p v-else>{{ this.schema.description }}</p>

  <div ref="table"></div>

  <div v-if="this.schema">
    <br>
    <hr>
    <br>
    <p><em>Rendered from the following spec:</em></p>
    <pre style="color: grey;">{{ this.schema }}</pre>
  </div>

</template>


<script>
  import { TabulatorFull as Tabulator } from 'tabulator-tables'
  import { useSchemaStore } from '@/stores/schema'

  const store = useSchemaStore()
  const START_ROWS = 5;

  export default {
    name: 'ExperimentForm',
    data() {
      return {
        schema: null,
        tabulator: null, // hold table data
        tableData: [],
      }
    },
    mounted() {
      store.getSchema('experiment').then( data => {
        this.schema = data
        this.tabulator = new Tabulator(this.$refs.table, {
          data: this.tableData,
          reactiveData: true,
          columns: this.columnsFromSchema(data),
          clipboard: true,
          keybindings:{
              "navLeft" : "37",
              "navRight" : "39",
          },
        });
        this.addRows(START_ROWS);
      })
    },
    methods: {
      columnsFromSchema(schema) {
        return schema.fields.map( field => {
          return {
            title: this.idToTitle(field.name),
            field: field.name,
            sorter: 'string',
            tooltip: field.description,
            editor: 'input',
          }
        })
      },
      idToTitle(id) {
        return id.split('_')
          .map( word => word.charAt(0).toUpperCase() + word.slice(1) )
          .join(' ')
      },
      addRows(n) {
        for (let i = 0; i < n; i++) {
          this.tableData.push(
            this.schema.fields.reduce( (acc, field) => {
              acc[field.name] = ''
              return acc
            }, {})
          )
        }
      },
    }
  }
</script>
