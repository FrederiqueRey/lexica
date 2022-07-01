<script>
export default {
  data() {
    return {
      text: ''
    }
  },

  mounted() {
    this.axios
      .get("http://localhost:8000/word/mgl/pater")
      .then((response) => {
        this.info = response.data;
      })
      .catch((error) => {
        console.log(error);
      })
  },

  methods: {
    onInput(e) {
      this.text = e.target.value
    }
  }
  
}
</script>

<template>
    <input :value="text" @input="onInput" placeholder="Search a Greek Word">
    <p>{{ text }}</p>
    <p>{{ info }}</p>

</template>
