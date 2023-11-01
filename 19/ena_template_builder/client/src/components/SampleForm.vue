<template>
  <h1>Sample</h1>

  <pre>
    {{ this.schema ? this.schema : 'Loading...' }}
  </pre>
</template>


<script>
  import { useSchemaStore } from '@/stores/schema'

  const store = useSchemaStore()

  export default {
    name: 'SampleForm',
    data() {
      return {
        schema: null,
      }
    },
    mounted() {
      store.getSchema('sample').then( data => this.schema = data)
    }
  }
</script>
