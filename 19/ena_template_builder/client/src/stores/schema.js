import { ref } from 'vue'
import { defineStore } from 'pinia'
import { get } from '@/utils/api'

const HARD_CODED_ID = 'ERC000012'

let fetched = ref(false)
let data = ref({})

export const useSchemaStore = defineStore('schemaData', () => {
  async function getSchema(key) {
    const identifier = HARD_CODED_ID // TODO: should be fetched or selected
    if (!fetched.value) {
      data.value = await get(`/schema/${identifier}`).then(
        data => this.schema = data.schema
      )
      fetched.value = true
    }
    if (key) {
      return data.value[key]
    }
    return data.value
  }

  return { getSchema }
})
