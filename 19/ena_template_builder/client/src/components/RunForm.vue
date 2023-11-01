<template>
  <h1>Run</h1>

  <pre>
    {{ this.schema ? this.schema : 'Loading...' }}
  </pre>
</template>


<script>
  import { useSchemaStore } from '@/stores/schema'

  const store = useSchemaStore()

  export default {
    name: 'RunForm',
    data() {
      return {
        schema: null,
      }
    },
    mounted() {
      store.getSchema('run').then( data => this.schema = data)
    }
  }
</script>
