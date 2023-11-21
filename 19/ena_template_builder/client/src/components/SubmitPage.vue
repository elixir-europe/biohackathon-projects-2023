<template>
  <h1>Generate tables</h1>
  <p>
    After submission, your metadata will be written to tabular output
    files which will be available in your Galaxy history after the tool
    terminates (&lt; 10 seconds).
  </p>
  <button class="btn btn-primary" @click="submitForm">Generate</button>

  <!-- For debugging state: -->
  <!-- <p class="my-5">Data:</p><pre>{{ data }}</pre> -->

</template>

<script>
import { useFormStore } from '@/stores/forms.js';
import { useSchemaStore } from '@/stores/schema.js';
import { post } from '@/utils/api.js';

export default {
  name: 'SubmitPage',
  data() {
    return {
      data: null,
      schema: null,
    }
  },
  mounted() {
    this.getData().then( d => this.data = d )
  },
  methods: {
    async getData() {
      const { getFormData } = useFormStore()
      const { getSchema } = useSchemaStore()
      this.schema = await getSchema()
      const formState = await getFormData()
      const cleaned_forms = this.clean_forms(formState)
      return {
        ...cleaned_forms,
        schema: this.schema,
      }
    },
    clean_forms(forms) {
      const cleaned_forms = {}
      Object.keys(forms).forEach( formKey => {
        const cleaned_rows = forms[formKey].filter( row => {
          return Object.keys(row).reduce(
            (acc, fieldName) => acc || row[fieldName] !== '',
            false)
        })
        cleaned_forms[formKey] = cleaned_rows
      })
      return cleaned_forms
    },
    async submitForm() {
      post('/submit', this.data).then((res) => {
        if (res.status === 'success') {
          this.$router.push('/success');
        } else {
          alert("Error submitting form")
        }
      })
    },
  },
};
</script>
