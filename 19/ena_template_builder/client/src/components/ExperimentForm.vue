<template>
  <h1>Experiment</h1>

  <pre>
    {{ this.schema ? this.schema : 'Loading...' }}
  </pre>
</template>


<script>
  import { useSchemaStore } from '@/stores/schema'

  const store = useSchemaStore()

  export default {
    name: 'ExperimentForm',
    data() {
      return {
        schema: null,
      }
    },
    mounted() {
      store.getSchema('experiment').then( data => this.schema = data)
    }
  }
</script>
