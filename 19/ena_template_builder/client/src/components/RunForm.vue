<template>
  <h1 class="mb-5">Run</h1>

  <p v-if="!schema">Loading...</p>

  <div v-else>
    <p>{{ schema.description }}</p>

    <EditableTable v-if="schema" :schema="schema" :formStoreKey="this.formName" />

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
    name: 'RunForm',
    components: {
      EditableTable: EditableTable,
    },
    data() {
      return {
        schema: null,
        formName: 'run',
      }
    },
    mounted() {
      schemaStore.getSchema(this.formName)
        .then( data => {
          this.schema = data
        })
    },
  }
</script>
