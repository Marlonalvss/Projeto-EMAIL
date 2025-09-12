<script setup lang="ts">
import { ref } from 'vue';

// Estado reativo para o input do usuário
const text = ref<string>('');
const isDragging = ref<boolean>(false);
const attachedFileName = ref<string | null>(null); // Novo estado para o nome do arquivo anexado

// Estado reativo para o resultado da classificação
const result = ref<{
  classification: string;
  confidence: number;
  suggestion: string;
} | null>(null);

// Simulação das funções que você mencionou
const classifyText = () => {
  if (!text.value.trim() && !attachedFileName.value) {
    result.value = null;
    return;
  }
  
  result.value = {
    classification: 'Satisfação do Cliente',
    confidence: 95,
    suggestion: 'Responda com uma mensagem de agradecimento e ofereça um cupom de desconto para a próxima compra.'
  };
};

// Nova função para lidar com a seleção de arquivos, seja por clique ou drop
const handleFileSelect = (event: Event) => {
  const target = event.target as HTMLInputElement;
  const files = target.files;
  if (files && files.length > 0) {
    const file = files[0];
    if (file.type === 'text/plain' || file.type === 'application/pdf') {
      const reader = new FileReader();
      reader.onload = () => {
        // Atualiza a variável reativa com o nome do arquivo
        attachedFileName.value = file.name;
        // Limpa o textarea para focar no arquivo anexado
        text.value = '';
      };
      reader.readAsText(file);
    } else {
      alert('Por favor, selecione um arquivo .txt ou .pdf válido.');
    }
  }
  target.value = '';
};

// Funções para lidar com o Drag and Drop
const handleDragOver = (event: DragEvent) => {
  event.preventDefault();
  isDragging.value = true;
};

const handleDragLeave = (event: DragEvent) => {
  event.preventDefault();
  isDragging.value = false;
};

const handleDrop = (event: DragEvent) => {
  event.preventDefault();
  isDragging.value = false;
  const files = event.dataTransfer?.files;
  if (files && files.length > 0) {
    const eventMock = { target: { files: files } } as unknown as Event;
    handleFileSelect(eventMock);
  }
};

// Função para abrir o seletor de arquivos quando a área de drop é clicada
const openFileSelector = () => {
  const fileInput = document.getElementById('file-upload-input');
  if (fileInput) {
    fileInput.click();
  }
};

// Função para remover o arquivo anexado
const removeFile = () => {
  attachedFileName.value = null;
  text.value = '';
};

// Lógica para definir a cor do "badge" de classificação
const getClassificationColor = (classification: string) => {
  switch (classification) {
    case 'Satisfação do Cliente':
      return 'bg-green-500 text-white';
    case 'Reclamação':
      return 'bg-red-500 text-white';
    case 'Pergunta':
      return 'bg-blue-500 text-white';
    default:
      return 'bg-gray-500 text-white';
  }
};
</script>

<template>
  <section class="container mx-auto px-4 py-16">
    <div class="mx-auto max-w-6xl">
      <div class="grid gap-8 md:grid-cols-2">
        <div class="rounded-lg border bg-white p-6 shadow-soft transition-shadow duration-300 hover:shadow-lg dark:bg-gray-800">
          <div class="border-b border-gray-200 pb-4 dark:border-gray-700">
            <h2 class="text-2xl font-bold text-gray-900 dark:text-gray-100">Insira seu Texto</h2>
          </div>
          <div class="space-y-4 pt-6">
            <textarea
              placeholder="Cole ou digite seu texto aqui para classificá-lo..."
              v-model="text"
              class="w-full min-h-[180px] resize-none rounded-md border border-gray-300 bg-gray-50 p-3 text-gray-900 transition-colors duration-300 focus:border-blue-500 focus:ring-2 focus:ring-blue-500 dark:border-gray-700 dark:bg-gray-900 dark:text-gray-100 dark:focus:border-blue-500"
              rows="7"
              :disabled="!!attachedFileName"
            ></textarea>

            <div v-if="!attachedFileName"
              class="mt-4 cursor-pointer flex flex-col items-center justify-center rounded-lg border-2 border-dashed p-6 text-center transition-colors duration-300"
              :class="{
                'border-blue-400 bg-blue-50 dark:bg-blue-900 dark:border-blue-600': isDragging,
                'border-gray-300 bg-gray-50 dark:bg-gray-700 dark:border-gray-600': !isDragging
              }"
              @dragover="handleDragOver"
              @dragleave="handleDragLeave"
              @drop="handleDrop"
              @click="openFileSelector"
            >
              <svg xmlns="http://www.w3.org/2000/svg" class="h-10 w-10 text-gray-400" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M4 14.899A7 7 0 1 1 15.71 8h1.79a4.5 4.5 0 0 1 2.5 8.242M12 18V9M12 18l-3 3M12 18l3 3"/>
              </svg>
              <p class="mt-2 text-sm text-gray-600 dark:text-gray-400">
                Arraste e solte ou **clique aqui** para enviar
              </p>
              <p class="text-xs text-gray-400 dark:text-gray-500">
                (Apenas .txt e .pdf)
              </p>
            </div>
            
            <div v-if="attachedFileName" class="mt-4 flex items-center justify-between rounded-lg bg-gray-100 p-3 shadow-sm dark:bg-gray-700">
              <span class="text-sm font-medium text-gray-800 truncate dark:text-gray-200">
                Arquivo anexado: {{ attachedFileName }}
              </span>
              <button @click="removeFile" class="text-gray-500 hover:text-red-500 transition-colors duration-200" aria-label="Remover anexo">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <line x1="18" y1="6" x2="6" y2="18"></line>
                  <line x1="6" y1="6" x2="18" y2="18"></line>
                </svg>
              </button>
            </div>

            <input type="file" id="file-upload-input" class="hidden" @change="handleFileSelect" accept=".txt,.pdf" />

            <button
              @click="classifyText"
              :disabled="!text.trim() && !attachedFileName"
              class="w-full rounded-md bg-blue-500 py-3 text-lg font-semibold text-white transition-colors duration-300 hover:bg-blue-600 disabled:bg-gray-400 dark:bg-blue-600 dark:hover:bg-blue-700 dark:disabled:bg-gray-700"
            >
              Classificar Texto
            </button>
          </div>
        </div>

        <div class="rounded-lg border bg-white p-6 shadow-soft transition-shadow duration-300 hover:shadow-lg dark:bg-gray-800">
          <div class="border-b border-gray-200 pb-4 dark:border-gray-700">
            <h2 class="text-2xl font-bold text-gray-900 dark:text-gray-100">Resultados da Classificação</h2>
          </div>
          <div class="space-y-6 pt-6">
            <div v-if="result">
              <div>
                <div class="mb-2 flex items-center justify-between">
                  <span class="font-medium text-gray-700 dark:text-gray-300">Classificação:</span>
                  <span :class="['rounded-full px-3 py-1 text-sm font-semibold', getClassificationColor(result.classification)]">
                    {{ result.classification }}
                  </span>
                </div>
                <div class="flex items-center justify-between">
                  <span class="font-medium text-gray-700 dark:text-gray-300">Confiança:</span>
                  <span class="text-lg font-semibold text-blue-600 dark:text-blue-400">{{ result.confidence }}%</span>
                </div>
              </div>

              <div class="rounded-lg bg-blue-50 p-4 border border-blue-200 dark:bg-blue-950 dark:border-blue-800">
                <h4 class="mb-2 font-semibold text-blue-600 dark:text-blue-400">Sugestão de Resposta / Ação</h4>
                <p class="text-sm text-gray-600 leading-relaxed dark:text-gray-400">
                  {{ result.suggestion }}
                </p>
              </div>
            </div>

            <div v-else class="flex h-[200px] items-center justify-center text-gray-500 dark:text-gray-400">
              <p>Digite um texto ou anexe um arquivo para ver os resultados.</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>