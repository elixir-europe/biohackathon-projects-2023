import { defineStore } from 'pinia'


export const useFormStore = defineStore('formData', {
  state: () => ({
    'study': [],
    'experiment': [],
    'run': [],
    'sample': [],
  }),
  actions: {
    getFormData(formName) {
      return this[formName]
    },
    setFormData(formName, data) {
      this[formName] = data
    },
  }
})
