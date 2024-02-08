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
          <RouterLink to="/submit">Finish</RouterLink>
          <span v-if="this.schema" class="template-details">
            Template {{ this.schema.identifier }}
            <v-tooltip
              activator="parent"
              location="bottom"
              :max-width="this.schema.description.length < 200 ? 300 : 600"
              style="overflow-wrap: break-word;"
            >
              <p class="lead">
                {{ this.schema.title }}
              </p>
              {{ this.schema.description }}
            </v-tooltip>
          </span>
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
  data() {
    return {
      schema: null,
    }
  },
  mounted() {
    import('@/stores/schema.js')
      .then( m => {
        const { useSchemaStore } = m;
        const schemaStore = useSchemaStore();
        schemaStore.getSchema().then( data => this.schema = data )
      })
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
.template-details {
  float: right;
  background: #ddddea;
  padding: .5rem 1rem;
  margin-top: -.5rem;
  border-radius: .5rem;
  user-select: none;
  cursor: default;
}
</style>
