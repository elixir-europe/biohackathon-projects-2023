<template>
  <h1 class="mb-5">Experiment</h1>

  <p v-if="!schema">Loading...</p>

  <div v-else>
    <p>{{ schema.description }}</p>

    <EditableTable v-if="schema" :schema="schema" storeKey="experiment" />

    <br>
    <hr>
    <br>
    <p><em>Rendered from the following spec:</em></p>
    <pre style="color: grey;">{{ this.schema }}</pre>
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
      }
    },
    mounted() {
      schemaStore.getSchema('experiment')
        .then( data => {
          this.schema = data
        })
    },
  }
</script>
