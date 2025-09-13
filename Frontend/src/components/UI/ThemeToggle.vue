// src/components/ThemeToggle.vue
<script setup lang="ts">
import { ref } from 'vue'

const theme = ref<'light' | 'dark'>('light')

// Detecta o tema inicial do sistema
if (window.matchMedia('(prefers-color-scheme: dark)').matches) {
  theme.value = 'dark'
  document.documentElement.setAttribute('data-theme', 'dark')
}

const toggleTheme = () => {
  theme.value = theme.value === 'light' ? 'dark' : 'light'
  document.documentElement.setAttribute('data-theme', theme.value)
}
</script>

<template>
  <button
    class="text-[var(--chat-text)] text-3xl cursor-pointer transition-colors duration-200 hover:text-[var(--chat-accent)] dark:hover:text-[var(--chat-accent)]"
    @click="toggleTheme"
    aria-label="Alternar tema"
  >
    <span v-if="theme === 'light'">
      <!-- Ícone Sol -->
      <svg xmlns="http://www.w3.org/2000/svg" class="inline h-8 w-8" fill="none" viewBox="0 0 24 24" stroke="currentColor">
        <circle cx="12" cy="12" r="5" stroke="currentColor" stroke-width="2" fill="currentColor"/>
        <path stroke="currentColor" stroke-width="2" d="M12 1v2M12 21v2M4.22 4.22l1.42 1.42M18.36 18.36l1.42 1.42M1 12h2M21 12h2M4.22 19.78l1.42-1.42M18.36 5.64l1.42-1.42"/>
      </svg>
    </span>
    <span v-else>
      <!-- Ícone Lua mais fina -->
      <svg xmlns="http://www.w3.org/2000/svg" class="inline h-8 w-8" viewBox="0 0 24 24" fill="currentColor">
  <path d="M21 12.79A9 9 0 1111.21 3a7 7 0 109.79 9.79z"/>
</svg>

    </span>
  </button>
</template>
