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
    <section class=" py-16 ">
        <div class="container mx-auto px-4">
            <h2 class="mb-12 text-center text-3xl font-bold text-[var(--chat-text)]">Experimente com
                Exemplos!</h2>
            <div class="grid gap-6 md:grid-cols-3">
                <div v-for="(example, index) in examples" :key="index" @click="handleSelect(example.content)"
                    class="group cursor-pointer rounded-lg border p-4 shadow-soft transition-shadow duration-300 hover:shadow-lg  bg-[var(--chat-card)] dark:border-gray-700">
                    <h3 class="pb-3 text-lg font-semibold text-[var(--chat-text)] group-hover:text-[var(--chat-accent)] text-[var(--chat-text)] group-hover:text-blue-500 transition">
                     {{ example.title }}
                    </h3>
                    <p class="text-sm text-[var(--chat-text)] leading-relaxed mb-4">
    {{ example.content }}
</p>
                    <button
                        class="w-full border border-blue-500 text-[var(--chat-text)] py-2 text-sm rounded transition hover:bg-[var(--chat-accent)]  hover:text-white">
                     Usar este exemplo
                    </button>
                </div>
            </div>
        </div>
    </section>
</template>