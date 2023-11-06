<template>
  <h1 class="mb-5">Run</h1>

  <p v-if="!schema">Loading...</p>

  <div v-else>
    <p>{{ schema.description }}</p>

    <EditableTable v-if="schema" :schema="schema" :formStoreKey="this.formName" />

    <br>
    <br>
    <a class="btn btn-primary" href="/sample">Next</a>
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
