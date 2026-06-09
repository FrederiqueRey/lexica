<template>
  <div class="min-h-screen bg-white">
    <!-- Navbar -->
    <nav class="flex items-center gap-4 px-6 py-3 border-b border-gray-200">
      <!-- Logo -->
      <span class="font-semibold text-gray-800 shrink-0">LSJ</span>
      <!-- Barre de recherche -->
       <div class="relative flex-1 flex items-center border border-gray-300 rounded-lg px-3 py-2 gap-2">
        <span><MagnifyingGlassIcon class="size-6" /></span>
        <input
          v-model="text"
          type="text"
          placeholder="Search a word..."
          class="flex-1 focus:outline-none text-gray-700"
        />
        <ul v-if="results.length && !selected" class="absolute top-full mt-1 w-full bg-white border border-gray-200 rounded-lg shadow-lg z-10">
          <li v-for="item in results" :key="item.id" @click="selectedWord(item)" class="px-4 py-2 cursor-pointer hover:bg-gray-50 border-b border-gray-100 last:border-0">
            {{ item.m[0] }}
          </li>
        </ul>  
       </div>
     
      <!-- Icônes droite -->
        <div class="flex items-center gap-3 text-gray-400 shrink-0">
          <button><Cog6ToothIcon class="size-6" /></button>
          <button><InformationCircleIcon class="size-6" /></button>
        </div>
    </nav>
    
    <!-- Contenu principal -->
    <main class="max-w-2xl mx-auto mt-16 px-4">
      <div v-if="selected" class="mt-8 p-6 border border-gray-200 rounded-xl">
        <h2 class="text-2xl font-semibold mb-4">{{ selected.m[0] }}</h2>
        <p v-html="selected.d"></p>
      </div>
    </main>

  </div>
</template>

<script setup>
// import SearchWord from './components/SearchWord.vue'
import { Cog6ToothIcon, InformationCircleIcon, MagnifyingGlassIcon } from '@heroicons/vue/24/solid'
import { ref, watch } from 'vue'
import axios from 'axios'

const text = ref('')
const results = ref([])
const selected = ref(null)

watch(text, async (newText) => {
  selected.value = null
  if (newText) {
    const response = await axios.get(`http://localhost:8000/word/mgl/${newText}`)
    results.value = response.data
  }
  else {
    results.value = []
  }
})

function selectedWord(word) {
  selected.value = word
  results.value = []
}
</script>


