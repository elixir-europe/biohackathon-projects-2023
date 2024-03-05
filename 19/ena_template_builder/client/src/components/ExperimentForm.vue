<template>
  <h1 class="mb-5">Experiment</h1>

  <p v-if="!schema">Loading...</p>

  <div v-else>
    <p>{{ schema.description }}</p>

    <EditableTable v-if="schema" :schema="schema" :formStoreKey="this.formName" />

    <br>
    <br>
    <a class="btn btn-primary" href="/run">Next</a>
  </div>
</template>


<script>
  import { useSchemaStore } from '@/stores/schema'
  import EditableTable from './EditableTable.vue'

  const schemaStore = useSchemaStore()

  export default {
    name: 'ExperimentForm',
    components: {
      EditableTable: EditableTable,
    },
    data() {
      return {
        schema: null,
        formName: 'experiment',
      }
    },
    mounted() {
      schemaStore.getSchema(this.formName)
        .then( data => {
          this.schema = data
        })
    },
    methods: {},
  }
</script>
