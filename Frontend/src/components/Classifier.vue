<script setup lang="ts">
// Props recebidas do componente pai (exemplo de texto)
import { ref, watch, defineProps } from 'vue';

const props = defineProps<{
    exampleText?: string
}>()

// Atualiza o campo de texto quando um exemplo é selecionado
watch(() => props.exampleText, (newText) => {
    if (newText) text.value = newText
})

// Variaveis reativas
const text = ref<string>('');
const isDragging = ref<boolean>(false);
const attachedFileName = ref<string | null>(null);
const attachedFile = ref<File | null>(null);
const isLoading = ref<boolean>(false);
const isSuggestionLoading = ref<boolean>(false);
const result = ref<{
    classification: string;
    suggestion: string;
} | null>(null);

// Função para enviar texto ou arquivo para o backend e obter classificação
const classifyTextBackend = async () => {
    if (!text.value.trim() && !attachedFile.value) {
        result.value = null;
        return;
    }

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

// Função para copiar a sugestão gerada para a área de transferência
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

// Função para solicitar uma nova sugestão ao backend, mantendo a classificação
const regenerateSuggestion = async () => {
    if (!result.value) return;

    // Usa a sugestão atual como texto base para regenerar
    const textToSend = result.value.suggestion;

    isSuggestionLoading.value = true;

    try {
        const res = await fetch("http://localhost:8000/regenerate-suggestion", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                text: textToSend,
                classification: result.value.classification
            })
        });

        if (!res.ok) throw new Error("Erro na requisição ao backend");

        const data = await res.json();
        const newSuggestion = data.result.suggestion || "Sem sugestão";

        result.value.suggestion = newSuggestion;
    } catch (error) {
        console.error(error);
        alert("Erro ao gerar uma nova sugestão.");
    } finally {
        isSuggestionLoading.value = false;
    }
};

// Função para tratar seleção de arquivo pelo usuário
const handleFileSelect = (event: Event) => {
    const target = event.target as HTMLInputElement;
    const files = target.files;
    if (files && files.length > 0) {
        const file = files[0];
        if (file.type === 'text/plain' || file.type === 'application/pdf') {
            attachedFile.value = file;
            attachedFileName.value = file.name;

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

// Função para tratar evento de arrastar arquivo sobre a área de upload
const handleDragOver = (event: DragEvent) => { event.preventDefault(); isDragging.value = true; };

// Função para tratar evento de sair da área de upload
const handleDragLeave = (event: DragEvent) => { event.preventDefault(); isDragging.value = false; };

// Função para tratar evento de soltar arquivo na área de upload
const handleDrop = (event: DragEvent) => {
    event.preventDefault();
    isDragging.value = false;
    const files = event.dataTransfer?.files;
    if (files && files.length > 0) {
        const eventMock = { target: { files: files } } as unknown as Event;
        handleFileSelect(eventMock);
    }
};

// Função para abrir seletor de arquivo manualmente
const openFileSelector = () => {
    const fileInput = document.getElementById('file-upload-input');
    if (fileInput) fileInput.click();
};

// Função para remover arquivo anexado e limpar campo de texto
const removeFile = () => {
    attachedFileName.value = null;
    attachedFile.value = null;
    text.value = '';
};

// Função para definir cor do badge de classificação
const getClassificationColor = (classification: string) => {
    switch (classification.toLowerCase()) {
        case 'produtivo': return 'bg-green-500 text-white';
        case 'improdutivo': return 'bg-red-500 text-white';
        default: return 'bg-gray-500 text-white';
    }
};
</script>

<template>
  <section class="container mx-auto px-4 py-16 bg-[var(--chat-bg)]">
    <div class="mx-auto max-w-full md:max-w-6xl">
      <div class="grid grid-cols-1 md:grid-cols-2 gap-8">

        <div class="rounded-lg border p-6 shadow-md transition-shadow duration-300 hover:shadow-lg bg-[var(--chat-card)] border-[var(--chat-text)] hover:border-blue-500">
          <div class="border-b pb-4 border-[var(--chat-text)]">
            <h2 class="text-2xl font-bold text-[var(--chat-text)]">Insira seu Texto</h2>
          </div>
          <div class="space-y-4 pt-6">
            <textarea 
              placeholder="Cole ou digite seu texto aqui para classificá-lo..." 
              v-model="text"
              :disabled="!!attachedFileName"
              class="w-full min-h-[180px] resize-none rounded-md border p-3 bg-[var(--chat-card)] text-[var(--chat-text)] focus:border-[var(--chat-accent] focus:ring-2 focus:ring-[var(--chat-accent)] transition-colors duration-300  hover:border-blue-500"
            ></textarea>
            <div v-if="!attachedFileName"
              class="mt-4 cursor-pointer flex flex-col items-center justify-center rounded-lg border-2 border-dashed p-6 text-center transition-colors duration-300 hover:border-blue-500"
              :class="{
                'border-[var(--chat-accent)] bg-[var(--chat-accent)]/10': isDragging,
                'border-[var(--chat-text)] bg-[var(--chat-card)]': !isDragging
              }"
              @dragover="handleDragOver" 
              @dragleave="handleDragLeave" 
              @drop="handleDrop"
              @click="openFileSelector"
            >
              <svg xmlns="http://www.w3.org/2000/svg" class="h-10 w-10 text-[var(--chat-text)]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M4 14.899A7 7 1 1 1 15.71 8h1.79a4.5 4.5 0 0 1 2.5 8.242M12 18V9M12 18l-3 3M12 18l3 3"/>
              </svg>
              <p class="mt-2 text-sm text-[var(--chat-text)]">Arraste e solte ou **clique aqui** para enviar</p>
              <p class="text-xs text-[var(--chat-text)]">(Apenas .txt e .pdf)</p>
            </div>

            <div v-if="attachedFileName"
              class="mt-4 flex items-center justify-between rounded-lg p-3 shadow-sm bg-[var(--chat-card)] border border-[var(--chat-text)] overflow-auto">
              <span class="text-sm font-medium text-[var(--chat-text)] truncate break-all">
                Arquivo anexado: {{ attachedFileName }}
              </span>
              <button @click="removeFile"
                class="text-red-500 hover:text-red-700 transition-colors duration-200"
                :class="{ 'cursor-pointer': attachedFileName }"
                aria-label="Remover anexo">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <line x1="18" y1="6" x2="6" y2="18"></line>
                  <line x1="6" y1="6" x2="18" y2="18"></line>
                </svg>
              </button>
            </div>

            <input type="file" id="file-upload-input" class="hidden" @change="handleFileSelect" accept=".txt,.pdf" />

            <button
  @click="classifyTextBackend"
  :disabled="(!text.trim() && !attachedFile) || isLoading"
  class="w-full rounded-md py-3 text-lg font-semibold transition-colors duration-300
         bg-[var(--chat-accent)] text-white hover:bg-[var(--chat-accent)]/90 disabled:bg-gray-400"
  :class="{ 'cursor-pointer': text.trim() || attachedFile }"
>
  Classificar Texto
</button>

          </div>
        </div>

        <div class="rounded-lg border p-6 shadow-md transition-shadow duration-300 hover:shadow-lg bg-[var(--chat-card)] border-[var(--chat-text)]   hover:border-blue-500">
          <div class="border-b pb-4 border-[var(--chat-text)]">
            <h2 class="text-2xl font-bold text-[var(--chat-text)]">Resultados da Classificação</h2>
          </div>

          <div class="space-y-6 pt-6">
            <div v-if="result">
              <div class="mb-2 flex items-center justify-between">
                <span class="font-medium text-[var(--chat-text)]">Classificação:</span>
                <span :class="['rounded-full px-3 py-1 text-sm font-semibold', getClassificationColor(result.classification)]">
                  {{ result.classification }}
                </span>
              </div>

              <div class="rounded-lg p-4 border bg-[var(--chat-card)] border-[var(--chat-text)] relative hover:border-blue-500 transition-colors duration-200 flex flex-col">
                <h4 class="mb-2 font-semibold text-[var(--chat-text)]">Sugestão de Resposta / Ação</h4>
                <button @click="copySuggestion" class="absolute top-4 right-4 text-[var(--chat-text)] hover:text-[var(--chat-accent)] cursor-pointer" aria-label="Copiar sugestão">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect>
                    <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path>
                  </svg>
                </button>
                <p class="text-sm text-[var(--chat-text)] leading-relaxed">{{ result.suggestion }}</p>
                
                <button
                  @click="regenerateSuggestion"
                  :disabled="isSuggestionLoading"
                  class="mt-8 w-full rounded-md py-2 text-sm font-semibold transition-colors duration-300
                         bg-[var(--chat-accent)] text-white hover:bg-[var(--chat-accent)]/90 disabled:bg-gray-400 cursor-pointer"
                  :class="{ 'cursor-pointer': !isSuggestionLoading }"
                  style="align-self: flex-end;"
                >
                  {{ isSuggestionLoading ? 'Gerando...' : 'Gerar Nova Sugestão' }}
                </button>
              </div>
            </div>

            <div class="flex h-[200px] items-center justify-center text-[var(--chat-text)]">
              <div v-if="isLoading" class="flex flex-col items-center">
                <div class="loader mb-2"></div>
                <span>Classificando...</span>
              </div>
              <p v-else-if="!result">Digite um texto ou anexe um arquivo para ver os resultados.</p>
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
    --_g: no-repeat radial-gradient(circle closest-side, var(--chat-text) 90%, #0000);
    background:
        var(--_g) 0% 50%,
        var(--_g) 50% 50%,
        var(--_g) 100% 50%;
    background-size: calc(100%/3) 50%;
    animation: l3 1s infinite linear;
}

@media (prefers-color-scheme: dark) {
  .loader {
    --_g: no-repeat radial-gradient(circle closest-side, #fff 90%, #0000);
  }
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