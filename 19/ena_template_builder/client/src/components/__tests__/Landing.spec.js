import { describe, it, expect } from 'vitest'

import { mount } from '@vue/test-utils'
import Landing from '../Landing.vue'

describe('Landing', () => {
  it('renders properly', () => {
    const wrapper = mount(Landing)
    expect(wrapper.text()).toContain('ENA upload forms')
  })
})
