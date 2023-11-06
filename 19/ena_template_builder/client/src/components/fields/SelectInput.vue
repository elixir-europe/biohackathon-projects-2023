<template>
    <select class="custom-select noborder">
        <option value=""></option>
        <option v-for="option in field.cv" :key="option" :value="option">{{ option }}</option>
    </select>
</template>

<script>
import { capitalize } from '@/utils/text'

export default {
    name: 'SelectInput',
    props: {
        field: Object,
    },
    methods: {
        capitalize(text) {
            return capitalize(text)
        },
    }
}
</script>
