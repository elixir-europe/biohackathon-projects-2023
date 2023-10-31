import { ref } from 'vue'
import { defineStore } from 'pinia'

export const useFormStore = defineStore('formData', () => {
  const formState = ref({})
  return { formState }
})
