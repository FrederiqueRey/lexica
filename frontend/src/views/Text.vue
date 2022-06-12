<template>
  <div class="text_edition">
    <h1>This is the Text page</h1>
    <ul>
        <li v-for="post in posts" :key="post.id">{{ post }}</li>
        <li>toto</li>
    </ul>
  </div>
</template>

<script>



export default {
  data(){
    return {
      posts: []
    };
  },
  mounted() {
    this.axios
      .get("http://localhost:8000/student/")
      .then((response) => {
        this.posts = response.data;
      })
      .catch((error) => {
        console.log(error);
      });
  },

  methods:{
    updatePost() {
      this.axios
        .get("http://localhost:8000/student/")
        .then((response) => {
          this.posts = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    }
  }
};
</script>