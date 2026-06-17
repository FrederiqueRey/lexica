<script>
import axios from "axios";
export default {
  data() {
    return {
      info: [],
      text: ''
    }
  },

  watch: {
    text(newText) {
      if (newText) {
        axios
          .get(`http://localhost:8000/word/mgl/${newText}`)
          .then((response) => {
            this.info = response.data;
          })
          .catch((error) => {
            console.log(error);
          });
      } else {
        this.info = '';
      }
    }
  },

  methods: {
    onInput(e) {
      this.text = e.target.value;
    }
  }
}
</script>

<template>
  <div class=""min-h-screen bg-white>

  </div>
</template>