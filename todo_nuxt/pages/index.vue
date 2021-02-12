<template>
  <div class="container">
    <h1 class="title has-text-primary mt-5 mb-5">MOMENTUM</h1>
    <div class="columns">
      <div class="column is-4" v-for="status in taskStatuses">
        <p class="status has-background-primary has-text-white-ter mb-4">{{ status.toUpperCase() }}</p>
        <div class="board">
          <div v-for="task in tasks" v-bind:key="task.id">
            <div class="card mt-5" v-if="task.status === status">
              <header class="card-header">
                <h2 class="card-header-title">
                  {{ task.title }}
                </h2>
                <button v-on:click="deleteTask(task.id)" class="button is-primary mt-2 mr-5">DELETE</button>
              </header>
              <hr>
              <div class="card-content">
                <p>{{ task.description }}</p>
              </div>
              <footer class="card-footer">
                <a href="#" class="card-footer-item" v-if="status != 'todo'">To Do</a>
                <a href="#" class="card-footer-item" v-if="status != 'in progress'">In Progress</a>
                <a href="#" class="card-footer-item" v-if="status != 'done'">Done</a>
              </footer>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  modules: [
    '@nuxtjs/axios',
  ],
  head() {
    return {
      title: "Home | Momentum"
    };
  },
  components: {
  },
  async asyncData({ $axios, params }) {
    try {
      let tasks = await $axios.$get(`/tasks/`);
      return {
        tasks
      };
    } catch (e) {
      console.log(e);
      return {
        tasks: [],
      };
    }
  },
  data() {
    return {
      tasks: [],
      taskStatuses: ["todo", "in progress", "done"]
    };
  },
  methods: {
    async deleteTask(task_id) {
      try {
        await this.$axios.$delete(`/tasks/${task_id}/`);
        let updatedTasks = await this.$axios.$get("/tasks/");
        this.tasks = updatedTasks;
      } catch (e) {
        console.log(e);
      }
    }
  }
};
</script>

<style>
  body {
    background-color: hsl(0%, 0%, 96%);
  }
  h1 {
      text-align: center;
  }
  .card-header {
    box-shadow: none;
  }
  .cross {
    text-align: right;
  }
  .status {
    border-radius: 0.1em;
    font-size: 1.5em;
    font-weight: bolder;
    text-align: center;
  }
</style>
