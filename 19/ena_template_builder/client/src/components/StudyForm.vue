<template>
  <h1>Study</h1>

  <p v-if="!this.schema">Loading...</p>

  <div v-else>
    <p>{{ this.schema.description }}</p>

    <FormField v-for="field in this.schema.fields" :key="field.name" :field="field"></FormField>

    <a class="btn btn-primary" href="/experiment">Next</a>

    <!-- <p><em>Rendered from the following spec:</em></p>
    <pre style="color: grey;">{{ this.schema }}</pre> -->

  </div>
</template>

<script>
  import { useSchemaStore } from '@/stores/schema'
  import FormField from './fields/FormField.vue'

  const store = useSchemaStore()

  export default {
    name: 'StudyForm',
    components: {
      FormField: FormField,
    },
    data() {
      return {
        schema: null,
      }
    },
    mounted() {
      store.getSchema('study').then( data => this.schema = data)
    }
  }
</script>
