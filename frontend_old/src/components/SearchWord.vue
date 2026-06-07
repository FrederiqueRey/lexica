
<template>
    <input :value="text" @input="onInput" placeholder="Search a Greek Word">
    <p></p>
    <span v-html="info"></span>



</template>

<script>
import axios from "axios";

export default {

  data() {
    return {
      info: '',
      text:'',
      url_api:'',
    };
  },

 

  methods: {
    onInput(e) {
      this.text = e.target.value
      this.url_api = 'http://localhost:8000/word/mgl/' + this.text

      this.axios
      .get(this.url_api)
      .then((response) => {
        this.info = response.data[0].d;
        console.log("api response :", response.data);
      })
      .catch((error) => {
        console.log(error);
      });

    }
  }

}

</script>

<style>
  #app {
    font-family: Brill-Roman, Brill-Bold, Brill-Italic, Brill-BoldItalic;
    src: url(/src/assets/fonts/Brill-Roman.ttf);
    src: url(/src/assets/fonts/Brill-Bold.ttf);
    src: url(/src/assets/fonts/Brill-Italic.ttf);
    src: url(/src/assets/fonts/Brill-BoldItalic.ttf);
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    font-size: 20px;
    text-align: justify;
    color: #2c3e50;
    margin-top: 60px;
  }

  b {
    font-weight: bold;
  }

</style>
