<template>
  <div class="min-h-screen bg-[#97b7d6]">
    <!-- Navbar -->
    <nav class="flex items-center gap-4 px-6 py-3 border-b border-gray-200 bg-white">
      <!-- Logo -->
      <span class="font-semibold text-gray-800 shrink-0">LSJ</span>
      <!-- Barre de recherche -->
       <div class="relative flex-1 flex items-center border border-gray-300 rounded-lg px-3 py-2 gap-2">
        <span><MagnifyingGlassIcon class="size-6" /></span>
        <input
          v-model="text"
          @keydown="onKeydown"
          type="text"
          placeholder="Search a word..."
          class="flex-1 focus:outline-none text-gray-700"
        />
        <ul v-if="results.length && !selected" class="absolute top-full mt-1 left-0 w-full bg-white border border-gray-200 rounded-lg shadow-lg z-10">
          <li v-for="(item, index) in results"
          :key="item.id"
          @click="selectedWord(item)"
          :class="['px-4 py-2 cursor-pointer border-b border-gray-100 last:border-0', index === activeIndex ? 'bg-gray-100' : 'hover:bg-gray-50']">
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

      <!-- Mots précédents -->
      <div v-if="selected">
        <div v-for="word in neighbors.before" :key="word.id"
        @click="selectedWord(word)"
        class="p-3 mt-2 border border-gray-100 rounded-xl text-gray-400 cursor-pointer hover:bg-gray-50 bg-white">
        {{ word.m[0] }}
        </div> 
      </div>

      <!-- Carte principale -->
      <div v-if="selected" class="mt-2 p-6 border border-gray-200 rounded-xl bg-white">
        <h2 class="text-2xl font-semibold mb-4">{{ selected.m[0] }}</h2>
        <p v-html="selected.d"></p>
      </div>

      <!-- Mots suivants -->
      <div v-if = "selected">
        <div v-for="word in neighbors.after" :key="word.id"
        @click="selectedWord(word)"
        class="p-3 mt-2 border border-gray-100 rounded-xl text-gray-400 cursor-pointer hover:bg-gray-50 bg-white">
        {{ word.m[0] }}
      </div>
      </div>
    </main>

  </div>
</template>

<script setup>
// import SearchWord from './components/SearchWord.vue'
import { Cog6ToothIcon, InformationCircleIcon, MagnifyingGlassIcon } from '@heroicons/vue/24/solid'
import { ref, watch } from 'vue'
import axios from 'axios'

const text = ref('')                            // texte saisi dans la recherche
const results = ref([])                         // liste de l'autocomplete
const selected = ref(null)                      // mot selectionné et affiché dans la carte principale
const activeIndex = ref(-1)                     // index de la liste de navigation (pour les touches up/down)
const neighbors = ref({before: [], after: []})  // mots voisins à afficher avant après la carte sélectionnée

watch(text, async (newText) => {
  activeIndex.value = -1
  selected.value = null
  if (newText) {
    const response = await axios.get(`http://localhost:8000/word/mgl/${newText}`)
    results.value = response.data
  }
  else {
    results.value = []
  }
})

async function selectedWord(word) {
  selected.value = word
  results.value = []
  const response = await axios.get(`http://localhost:8000/word/${word.id}/neighbors`)
  neighbors.value = response.data
  document.querySelector('input').focus()
}

function onKeydown(e) {
  if (e.key === 'ArrowDown' && results.value.length) {
    e.preventDefault()
    activeIndex.value = Math.min(activeIndex.value + 1, results.value.length - 1)
  } else if (e.key === 'ArrowUp' && results.value.length) {
    e.preventDefault()
    activeIndex.value = Math.max(activeIndex.value - 1, 0)
  } else if (e.key === 'Enter' && activeIndex.value >= 0) {
    selectedWord(results.value[activeIndex.value])
  } else if (e.key === 'ArrowDown' && selected.value && !results.value.length) {
    selectedWord(neighbors.value.after[0])
  } else if (e.key === 'ArrowUp' && selected.value && !results.value.length) {
    selectedWord(neighbors.value.before[neighbors.value.before.length - 1])
  }
}
</script>


