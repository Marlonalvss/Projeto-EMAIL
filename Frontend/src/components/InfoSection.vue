<script setup lang="ts">
import { ref } from 'vue';

const expandedCard = ref<number | null>(null);

const toggleExpand = (cardIndex: number) => {
    expandedCard.value = expandedCard.value === cardIndex ? null : cardIndex;
};
</script>

<template>
    <section class="container mx-auto px-4 py-16 ">
        <div class="mx-auto max-w-4xl">
            <div class="grid gap-8 md:grid-cols-2 items-start">
                <div
                    class="group rounded-2xl border p-8 shadow-md transition-shadow duration-300 hover:shadow-lg min-h-[20rem] bg-[var(--chat-card)] dark:border-gray-700">
                    <div class="cursor-pointer" @click="toggleExpand(1)">
                        <h3
                            class="mb-4 text-2xl font-bold text-[var(--chat-text)] group-hover:text-blue-500 transition-colors duration-300">
                            Olhe Mais a Fundo!
                        </h3>
                        <p class="mb-6 text-[var(--chat-text)] leading-relaxed">
                            Descubra insights avançados sobre seus E-mails com a classificação em tempo real.
                        </p>
                    </div>

                    <Transition name="expand">
                        <div v-if="expandedCard === 1" class="overflow-hidden">
                            <hr class="my-4 border-gray-200 dark:border-gray-700" />
                            <p class="text-sm text-[var(--chat-text)]">
                                Nossa análise aprofundada utiliza **tecnologia de ponta como o Gemini**, para
                                uma classificação rápida. Identificamos o proposito, extraímos as entidades e palavras-chave mais
                                relevantes, e detectamos a intenção por trás da mensagem. Isso permite que você automatize tarefas
                                complexas, como direcionar tickets de suporte, priorizar feedbacks de clientes e entender o sentimento
                                do mercado em tempo real.
                            </p>
                        </div>
                    </Transition>

                    <button @click.stop="toggleExpand(1)"
                        class="mt-4 w-full rounded-md border border-blue-500 py-2 text-sm text-[var(--chat-text)] transition-colors duration-300 hover:bg-[var(--chat-accent)] hover:text-white">
                        {{ expandedCard === 1 ? 'Ver Menos' : 'Saiba Mais' }}
                    </button>
                </div>

                <div
                    class="group rounded-2xl border min-h-80  p-8 shadow-soft transition-shadow duration-300 hover:shadow-lg bg-[var(--chat-card)] dark:border-gray-700">
                    <div class="cursor-pointer" @click="toggleExpand(2)">
                        <h3
                            class="mb-4 text-2xl font-bold text-[var(--chat-text)] group-hover:text-blue-500 transition-colors duration-300">
                            Descubra Como Funciona
                        </h3>
                        <p class="mb-6 text-[var(--chat-text)] leading-relaxed ">
                            Entenda a tecnologia por trás do nosso classificador inteligente e como ele pode otimizar
                            seus processos de análise.
                        </p>
                    </div>

                    <Transition name="expand">
                        <div v-if="expandedCard === 2" class="overflow-hidden">
                            <hr class="my-4 border-gray-200 dark:border-gray-700" />
                            <p class="text-sm text-[var(--chat-text)] mb-6">
                                A tecnologia central do nosso classificador é alimentada pelo **modelo de linguagem avançado do Gemini**.
                                O modelo do Google é treinado em um vasto conjunto de dados, o que lhe permite ler, entender e classificar
                                textos em português com alta precisão, reconhecendo padrões complexos e nuances da língua. Quando você
                                insere um texto ou arquivo, ele é processado em tempo real, gerando uma classificação e uma sugestão de
                                ação relevante.
                            </p>
                            <h3 class="text-xl font-bold text-[var(--chat-text)] mb-6">
                                Tecnologias Utilizadas
                            </h3>

                            <div class="flex flex-wrap justify-center items-center gap-8">
                                <div class="flex flex-col items-center">
                                    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vuejs/vuejs-original.svg"
                                        alt="Vue.js" class="h-10 w-10" />
                                    <span class="mt-2 text-sm text-[var(--chat-text)]">Vue.js</span>
                                </div>

                                <div class="flex flex-col items-center">
                                    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg"
                                        alt="TypeScript" class="h-10 w-10" />
                                    <span class="mt-2 text-sm text-[var(--chat-text)]">TypeScript</span>
                                </div>

                                <div class="flex flex-col items-center">
                                    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/tailwindcss/tailwindcss-plain.svg"
                                        alt="Tailwind CSS" class="h-10 w-10" />
                                    <span class="mt-2 text-sm text-[var(--chat-text)]">Tailwind</span>
                                </div>

                                <div class="flex flex-col items-center">
                                    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg"
                                        alt="Python" class="h-10 w-10" />
                                    <span class="mt-2 text-sm text-[var(--chat-text)]">Python</span>
                                </div>

                                <div class="flex flex-col items-center">
                                    <img src="https://cdn.jsdelivr.net/gh/simple-icons/simple-icons/icons/googlegemini.svg"
                                        alt="Gemini AI" class="h-10 w-10" />
                                    <span class="mt-2 text-sm text-[var(--chat-text)]">Gemini AI</span>
                                </div>
                            </div>
                        </div>
                    </Transition>

                    <button @click.stop="toggleExpand(2)"
                        class="mt-4 w-full rounded-md border border-blue-500 py-2 text-sm text-[var(--chat-text)] transition-colors duration-300 hover:bg-[var(--chat-accent)] hover:text-white"
                        :aria-expanded="expandedCard === 2">
                        {{ expandedCard === 2 ? 'Ver Menos' : 'Saiba mais' }}
                    </button>
                </div>
            </div>
        </div>
    </section>
</template>

<style scoped>
.expand-enter-active,
.expand-leave-active {
    transition: max-height 0.5s cubic-bezier(0.25, 0.46, 0.45, 0.94), opacity 0.5s ease-in-out;
}

.expand-enter-from,
.expand-leave-to {
    max-height: 0;
    opacity: 0;
}

.expand-enter-to,
.expand-leave-from {
    max-height: 500px;
    opacity: 1;
}
</style>