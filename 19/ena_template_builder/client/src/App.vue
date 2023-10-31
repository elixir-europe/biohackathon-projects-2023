<template>
  <main>
    <header>
      <div class="wrapper">
        <nav>
          <RouterLink to="/">Intro</RouterLink>
          <RouterLink to="/form-1">Form 1</RouterLink>
          <RouterLink to="/form-2">Form 2</RouterLink>
          <RouterLink to="/submit">Submit</RouterLink>
        </nav>
      </div>
    </header>

    <RouterView />
  </main>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router';

// TODO: Fetch forms schema from backend and save to store

</script>

<style scoped>
main {
  padding: 0 1rem;
  margin: 0 auto;
  max-width: 1000px;
}
nav {
  padding: 1rem 0;
  border-bottom: 1px solid grey;
}
nav > a {
  margin: .25rem .5rem;
  padding: .25rem .5rem;
  text-decoration: none;
}
nav > a.router-link-active {
  color: white;
  background-color: cornflowerblue;
}
</style>
