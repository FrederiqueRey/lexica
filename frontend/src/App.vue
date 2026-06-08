<template>
  <div class="min-h-screen bg-white">
    <!-- Navbar -->
    <nav class="flex items-center gap-4 px-6 py-3 border-b border-gray-200">
      <!-- Logo -->
      <span class="font-semibold text-gray-800 shrink-0">LSJ</span>
      <!-- Barre de recherche -->
       <div class="flex-1 flex items-center border border-gray-300 rounded-lg px-3 py-2 gap-2">
        <span><MagnifyingGlassIcon class="size-6" /></span>
        <input
          type="text"
          placeholder="Search a word..."
          class="flex-1 focus:outline-none text-gray-700"
        />
       </div>
      <!-- Icônes droite -->
        <div class="flex items-center gap-3 text-gray-400 shrink-0">
          <button><Cog6ToothIcon class="size-6" /></button>
          <button><InformationCircleIcon class="size-6" /></button>
        </div>
    </nav>
    
    <!-- Contenu principal -->
    <main class="max-w-2xl mx-auto mt-16 px-4">
    </main>

  </div>
</template>

<script setup>
import SearchWord from './components/SearchWord.vue'
import { Cog6ToothIcon, MagnifyingGlassCircleIcon } from '@heroicons/vue/24/solid'
import { InformationCircleIcon } from '@heroicons/vue/24/solid'
import { MagnifyingGlassIcon} from '@heroicons/vue/24/solid'


</script>


