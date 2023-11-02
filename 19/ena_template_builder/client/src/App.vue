<template>
  <main>
    <header>
      <div class="wrapper">
        <nav>
          <RouterLink to="/">Intro</RouterLink>
          <RouterLink to="/study">Study</RouterLink>
          <RouterLink to="/experiment">Experiment</RouterLink>
          <RouterLink to="/run">Run</RouterLink>
          <RouterLink to="/sample">Sample</RouterLink>
          <RouterLink to="/submit">Submit</RouterLink>
        </nav>
      </div>
    </header>

    <RouterView />

  </main>
</template>

<script>
import { RouterLink, RouterView } from 'vue-router';

export default {
  name: 'App',
  components: {
    RouterLink,
    RouterView,
  },
};
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
  margin-bottom: 1rem;
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
