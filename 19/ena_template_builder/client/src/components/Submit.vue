<template>
  <h1>Review and submit</h1>
  <button @click="submitForm">Submit</button>
</template>

<script>
import { useFormStore } from './stores/forms.js';
import { submitForms } from './utils/api.js';

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
