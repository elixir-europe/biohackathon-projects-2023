# Notes 

## GitHub REST API

- Retrieve repositories with `topic` "bioinformatics" (randomly).
  ```
  https://api.github.com/search/repositories?q=topic:{topic}&per_page={per_page}
  ```
  Example:
  ```sh
  https://api.github.com/search/repositories?q=topic:bioinformatics&per_page=50
  ```
  - `per_page` is the number of repositories retrieved.

- Retrieve metadata of a GitHub repository:
  ```
  https://api.github.com/repos/{user}/{repo}
  ```
  Example:
  ```sh
  https://api.github.com/repos/ddangelov/Top2Vec
  ```
