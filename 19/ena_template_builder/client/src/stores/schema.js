import { ref } from 'vue'
import { defineStore } from 'pinia'

export const useSchemaStore = defineStore('schemaData', () => {
  const schemaState = ref({})
  return { schemaState }
})
