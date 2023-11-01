import { ref } from 'vue'
import { defineStore } from 'pinia'
import { get } from '@/utils/api'

let fetched = ref(false)
let data = ref({})

export const useSchemaStore = defineStore('schemaData', () => {
  async function getSchema(key) {
    if (!fetched.value) {
      data.value = await get('/schema').then( data => this.schema = data.schema )
      fetched.value = true
    }
    return data.value.schemas[key]
  }

  return { getSchema }
})
