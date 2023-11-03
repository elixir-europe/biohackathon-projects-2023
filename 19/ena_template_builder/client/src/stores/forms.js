import { ref } from 'vue'
import { defineStore } from 'pinia'


export const useFormStore = defineStore('formData', () => {
  const formState = ref({
    'study': [],
    'experiment': [],
    'run': [],
    'sample': [],
  })
  const setFormData = async (name, data) => {
    formState.value[name] = data
  }
  return { formState, setFormData }
})
