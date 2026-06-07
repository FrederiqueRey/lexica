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
  <div>
    <input :value="text" @input="onInput" placeholder="Search a Greek Word">
    <div v-if="info.length">
      <div v-for="item in info" :key="item.id">
        <h2>{{ item.m.join(', ') }}</h2>
        <p><span v-html="item.d"></span></p>
        <hr>
      </div>
    </div>
  </div>
</template>