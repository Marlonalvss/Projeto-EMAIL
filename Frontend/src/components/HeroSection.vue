<script lang="ts" setup>
import ThemeToggle from './UI/ThemeToggle.vue';

</script>

<template>
  <section class="relative overflow-hidden transition-colors duration-500">
    <div class="absolute inset-0 pointer-events-none" />
    <div class="flex justify-end">
        <div class="mt-2 mr-12">
          <ThemeToggle/>
        </div>
      </div>
    <div class="container relative mx-auto px-4 py-16 md:py-24">
      
      <div class="mx-auto max-w-3xl text-center">
        <h1 class="mb-6 text-4xl font-bold text-[var(--chat-text)] md:text-6xl">
          Classificador de E-mail Inteligente
        </h1>
        <p class="text-lg text-[var(--chat-text)] md:text-xl">
          Analise e compreenda o significado de seu e-mail instantaneamente.
        </p>
      </div>
    </div>
  </section>
</template>

<style scoped>


</style>