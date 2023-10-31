// Utils for interacting with API

export const BASE_URL = 'http://localhost:5000';

export const post = (path, data) => fetch(
    `${BASE_URL}${path}`,
    {
        method: 'POST',
        headers: {
        'Content-Type': 'application/json'
        },
        body: JSON.stringify(data),
    }
)
.then((response) => response.json())
.then((data) => {
    if (data.error) {
        alert("Error: " + data.error);
    }
    return data;
});

export const submitForms = (formData) => post('/submit', formData);
