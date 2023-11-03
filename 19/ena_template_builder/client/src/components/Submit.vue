<template>
  <h1>Review and submit</h1>
  <p>
    After submission, your submitted metadata will be written to tabular output
    files which will be available in your Galaxy history after the tool
    terminates (this may take up to 10 seconds).
  </p>
  <button class="btn btn-primary" @click="submitForm">Submit</button>
</template>

<script>
import { useFormStore } from '@/stores/forms.js';
import { submitForms } from '@/utils/api.js';

export default {
  methods: {
    submitForm() {
      const { formStore } = useFormStore();
      submitForms(formStore.value()).then((data) => {
        if (data.status === 'success') {
          formStore.reset();
          this.$router.push('/success');
        }
      });
    }
  },
};
</script>

<style scoped>
</style>
