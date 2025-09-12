<script setup lang="ts">
import { ref, watch, defineProps } from 'vue';

const props = defineProps<{
  exampleText?: string
}>()

watch(() => props.exampleText, (newText) => {
  if (newText) text.value = newText
})

const text = ref<string>('');
const isDragging = ref<boolean>(false);
const attachedFileName = ref<string | null>(null);
const attachedFile = ref<File | null>(null);
const isLoading = ref<boolean>(false);

const result = ref<{
  classification: string;
  suggestion: string;
} | null>(null);



//Função principal 
const classifyTextBackend = async () => {
  if (!text.value.trim() && !attachedFile.value) {
    result.value = null;
    return;
  }

  // Limpa o resultado antigo e inicia loader
  result.value = null;
  isLoading.value = true;

  let payload;
  let headers = {};
  let requestBody;

  if (attachedFile.value) {
    payload = new FormData();
    payload.append('file', attachedFile.value);
    requestBody = payload;
  } else {
    payload = { text: text.value };
    headers = { "Content-Type": "application/json" };
    requestBody = JSON.stringify(payload);
  }

  try {
    const res = await fetch("http://localhost:8000/classify", {
      method: "POST",
      headers: headers,
      body: requestBody
    });

    if (!res.ok) throw new Error("Erro na requisição ao backend");

    const data = await res.json();
    const classificationData = data.result || {};

    result.value = {
      classification: classificationData.classification || "Desconhecido",
      suggestion: classificationData.suggestion || "Sem sugestão"
    };
  } catch (error) {
    console.error(error);
    alert("Erro ao classificar o texto.");
  } finally {
    isLoading.value = false;
  }
};

//Função de copiar a mensagem que foi gerada
const copySuggestion = () => {
  if (result?.value?.suggestion) {
    navigator.clipboard.writeText(result.value.suggestion)
      .then(() => {
        alert("Sugestão copiada para a área de transferência!");
      })
      .catch(() => {
        alert("Não foi possível copiar o texto.");
      });
  }
};


// Funções de upload de arquivo
const handleFileSelect = (event: Event) => {
  const target = event.target as HTMLInputElement;
  const files = target.files;
  if (files && files.length > 0) {
    const file = files[0];
    if (file.type === 'text/plain' || file.type === 'application/pdf') {
      attachedFile.value = file;
      attachedFileName.value = file.name;

      // Para .txt, lê o conteúdo para a textarea. Para .pdf, deixa em branco.
      if (file.type === 'text/plain') {
        const reader = new FileReader();
        reader.onload = () => {
          text.value = reader.result as string || '';
        };
        reader.readAsText(file);
      } else {
        text.value = '';
      }
    } else {
      alert('Por favor, selecione um arquivo .txt ou .pdf válido.');
    }
  }
  target.value = '';
};

const handleDragOver = (event: DragEvent) => { event.preventDefault(); isDragging.value = true; };
const handleDragLeave = (event: DragEvent) => { event.preventDefault(); isDragging.value = false; };
const handleDrop = (event: DragEvent) => {
  event.preventDefault();
  isDragging.value = false;
  const files = event.dataTransfer?.files;
  if (files && files.length > 0) {
    const eventMock = { target: { files: files } } as unknown as Event;
    handleFileSelect(eventMock);
  }
};
const openFileSelector = () => {
  const fileInput = document.getElementById('file-upload-input');
  if (fileInput) fileInput.click();
};
const removeFile = () => {
  attachedFileName.value = null;
  attachedFile.value = null;
  text.value = '';
};

// Cor de badge de classificação
const getClassificationColor = (classification: string) => {
  switch (classification.toLowerCase()) {
    case 'produtivo': return 'bg-green-500 text-white';
    case 'improdutivo': return 'bg-red-500 text-white';
    default: return 'bg-gray-500 text-white';
  }
};
</script>


<template>
  <section class="container mx-auto px-4 py-16">
    <div class="mx-auto max-w-6xl">
      <div class="grid gap-8 md:grid-cols-2">
        <div
          class="rounded-lg border bg-white p-6 shadow-soft transition-shadow duration-300 hover:shadow-lg dark:bg-gray-800">
          <div class="border-b border-gray-200 pb-4 dark:border-gray-700">
            <h2 class="text-2xl font-bold text-gray-900 dark:text-gray-100">Insira seu Texto</h2>
          </div>
          <div class="space-y-4 pt-6">
            <textarea placeholder="Cole ou digite seu texto aqui para classificá-lo..." v-model="text"
              class="w-full min-h-[180px] resize-none rounded-md border border-gray-300 bg-gray-50 p-3 text-gray-900 transition-colors duration-300 focus:border-blue-500 focus:ring-2 focus:ring-blue-500 dark:border-gray-700 dark:bg-gray-900 dark:text-gray-100 dark:focus:border-blue-500"
              rows="7" :disabled="!!attachedFileName"></textarea>

            <div v-if="!attachedFileName"
              class="mt-4 cursor-pointer flex flex-col items-center justify-center rounded-lg border-2 border-dashed p-6 text-center transition-colors duration-300"
              :class="{
                'border-blue-400 bg-blue-50 dark:bg-blue-900 dark:border-blue-600': isDragging,
                'border-gray-300 bg-gray-50 dark:bg-gray-700 dark:border-gray-600': !isDragging
              }" @dragover="handleDragOver" @dragleave="handleDragLeave" @drop="handleDrop" @click="openFileSelector">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-10 w-10 text-gray-400" viewBox="0 0 24 24" fill="none"
                stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M4 14.899A7 7 0 1 1 15.71 8h1.79a4.5 4.5 0 0 1 2.5 8.242M12 18V9M12 18l-3 3M12 18l3 3" />
              </svg>
              <p class="mt-2 text-sm text-gray-600 dark:text-gray-400">
                Arraste e solte ou **clique aqui** para enviar
              </p>
              <p class="text-xs text-gray-400 dark:text-gray-500">
                (Apenas .txt e .pdf)
              </p>
            </div>

            <div v-if="attachedFileName"
              class="mt-4 flex items-center justify-between rounded-lg bg-gray-100 p-3 shadow-sm dark:bg-gray-700">
              <span class="text-sm font-medium text-gray-800 truncate dark:text-gray-200">
                Arquivo anexado: {{ attachedFileName }}
              </span>
              <button @click="removeFile" class="text-gray-500 hover:text-red-500 transition-colors duration-200"
                aria-label="Remover anexo">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 24 24" fill="none"
                  stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <line x1="18" y1="6" x2="6" y2="18"></line>
                  <line x1="6" y1="6" x2="18" y2="18"></line>
                </svg>
              </button>
            </div>

            <input type="file" id="file-upload-input" class="hidden" @change="handleFileSelect" accept=".txt,.pdf" />

            <button @click="classifyTextBackend" :disabled="(!text.trim() && !attachedFile) || isLoading"
              class="w-full rounded-md bg-blue-500 py-3 text-lg font-semibold text-white transition-colors duration-300 hover:bg-blue-600 disabled:bg-gray-400 dark:bg-blue-600 dark:hover:bg-blue-700 dark:disabled:bg-gray-700">
              Classificar Texto
            </button>
          </div>
        </div>

        <div
          class="rounded-lg border bg-white p-6 shadow-soft transition-shadow duration-300 hover:shadow-lg dark:bg-gray-800">
          <div class="border-b border-gray-200 pb-4 dark:border-gray-700">
            <h2 class="text-2xl font-bold text-gray-900 dark:text-gray-100">Resultados da Classificação</h2>
          </div>
          <div class="space-y-6 pt-6">
            <div v-if="result">
              <div>
                <div class="mb-2 flex items-center justify-between">
                  <span class="font-medium text-gray-700 dark:text-gray-300">Classificação:</span>
                  <span
                    :class="['rounded-full px-3 py-1 text-sm font-semibold', getClassificationColor(result.classification)]">
                    {{ result.classification }}
                  </span>
                </div>
              </div>

              <div
                class="rounded-lg bg-blue-50 p-4 border border-blue-200 dark:bg-blue-950 dark:border-blue-800 relative">
                <h4 class="mb-2 font-semibold text-blue-600 dark:text-blue-400">Sugestão de Resposta / Ação</h4>

                <!-- Ícone de copiar -->
                <button @click="copySuggestion"
                  class="absolute top-4 right-4 text-gray-500 hover:text-gray-800 dark:hover:text-gray-200"
                  aria-label="Copiar sugestão">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 24 24" fill="none"
                    stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect>
                    <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path>
                  </svg>
                </button>

                <p class="text-sm text-gray-600 leading-relaxed dark:text-gray-400">
                  {{ result.suggestion }}
                </p>
              </div>
            </div>

            <div class="flex h-[200px] items-center justify-center text-gray-500 dark:text-gray-400">
              <div v-if="isLoading" class="flex flex-col items-center">
                <div class="loader mb-2"></div>
                <span>Classificando...</span>
              </div>
              <p v-else>Digite um texto ou anexe um arquivo para ver os resultados.</p>
            </div>

          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.loader {
  width: 60px;
  aspect-ratio: 2;
  --_g: no-repeat radial-gradient(circle closest-side, #000 90%, #0000);
  background:
    var(--_g) 0% 50%,
    var(--_g) 50% 50%,
    var(--_g) 100% 50%;
  background-size: calc(100%/3) 50%;
  animation: l3 1s infinite linear;
}

@keyframes l3 {
  20% {
    background-position: 0% 0%, 50% 50%, 100% 50%
  }

  40% {
    background-position: 0% 100%, 50% 0%, 100% 50%
  }

  60% {
    background-position: 0% 50%, 50% 100%, 100% 0%
  }

  80% {
    background-position: 0% 50%, 50% 50%, 100% 100%
  }
}
</style>