//Bootstrap
//import 'bootstrap/dist/css/bootstrap.css';

//Axios link to the FastAPI backend
/*import axios from 'axios';
import VueAxios from "vue-axios";
Vue.use(VueAxios, axios);
axios.defaults.withCredentials = true;
axios.defaults.baseURL = 'http://0.0.0.0:8000/';  // the FastAPI backend
*/
//Creation of the vue frontend
import Vue from 'vue'
import App from './App.vue'
import router from './router'

Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
