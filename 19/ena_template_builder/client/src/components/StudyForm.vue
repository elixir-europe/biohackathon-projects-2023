<template>
  <h1>Study</h1>

  <button class="btn btn-primary my-5" @click="this.loadExampleData">
    Load example data
  </button>

  <p v-if="!this.schema">Loading...</p>

  <div v-else>
    <p>{{ this.schema.description }}</p>

    <FormField
      v-for="field in this.schema.fields"
      :key="field.name"
      :field="field"
      :inputValue="data[0][field.name]"
      @blur="setFieldValue(field.name, $event.target.value)"
    />

    <a class="btn btn-primary" href="/experiment">Next</a>

    <!-- For debugging state: -->
    <!-- <p>Data:</p><pre>{{ data }}</pre> -->

    <!-- From debugging schema: -->

    <!-- <p><em>Rendered from the following spec:</em></p>
    <pre style="color: grey;">{{ this.schema }}</pre> -->

  </div>
</template>

<script>
  import { useSchemaStore } from '@/stores/schema'
  import { useFormStore } from '@/stores/forms'
  import FormField from './fields/FormField.vue'

  const store = useSchemaStore()
  const formStore = useFormStore()

  export default {
    name: 'StudyForm',
    components: {
      FormField: FormField,
    },
    data() {
      return {
        schema: null,
        formStoreKey: 'study',
      }
    },
    computed: {
      data() {
        return formStore.getFormData(this.formStoreKey)
      },
    },
    mounted() {
      store.getSchema('study').then( schema => {
        this.schema = schema
        if (!this.data.length) {
          const blankRow = schema.fields.reduce( (obj, field) => ({...obj, [field.name]: ''}), {})
          formStore.$patch( (state) => {
            state[this.formStoreKey].push(blankRow)
          })
        }
      })
    },
    methods: {
      setFieldValue(field_name, value) {
        formStore.$patch( (state) => {
          state[this.formStoreKey][0][field_name] = value
          state.hasChanged = true
        })
      },
      loadExampleData() {
        formStore.loadExampleData();
      }
    }
  }
</script>
