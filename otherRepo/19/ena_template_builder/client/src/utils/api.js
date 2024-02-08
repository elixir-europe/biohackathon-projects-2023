// Utils for interacting with API

export const BASE_URL = '/api'

export const get = (path) => fetch(`${BASE_URL}${path}`)
  .then((response) => response.json())

export const post = (path, data) =>
  fetch(`${BASE_URL}${path}`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.error) {
        alert('Error: ' + data.error)
      }
      return data
    })
