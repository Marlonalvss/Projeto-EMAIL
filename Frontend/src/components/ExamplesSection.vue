<script setup lang="ts">
import { defineEmits } from 'vue'

const examples = [
  { title: "Elogio ao Produto", content: "Adorei a qualidade do produto! Chegou rápido e exatamente como descrito. Recomendo muito!" },
  { title: "Reclamação de Cliente", content: "O atendimento foi péssimo e o produto chegou com defeito. Muito decepcionado com a compra." },
  { title: "Dúvida sobre Funcionalidade", content: "Gostaria de saber se o produto é compatível com Windows 11 e qual o prazo de garantia." }
]

const emit = defineEmits<{
  (e: 'exampleSelected', text: string): void
}>()

const handleSelect = (text: string) => {
  emit('exampleSelected', text)
}
</script>

<template>
  <section class="bg-gray-100/30 py-16">
    <div class="container mx-auto px-4">
      <h2 class="mb-12 text-center text-3xl font-bold text-gray-800">Experimente com Exemplos!</h2>
      <div class="grid gap-6 md:grid-cols-3">
        <div 
          v-for="(example, index) in examples" 
          :key="index"
          @click="handleSelect(example.content)"
          class="group cursor-pointer rounded-lg border bg-white p-4 shadow-sm transition transform hover:shadow-lg hover:-translate-y-1"
        >
          <h3 class="pb-3 text-lg font-semibold text-gray-700 group-hover:text-blue-500 transition">
            {{ example.title }}
          </h3>
          <p class="text-sm text-gray-500 leading-relaxed mb-4">{{ example.content }}</p>
          <button class="w-full border border-blue-200 text-blue-500 py-2 text-sm rounded transition hover:bg-blue-500 hover:text-white">
            Usar este exemplo
          </button>
        </div>
      </div>
    </div>
  </section>
</template>


