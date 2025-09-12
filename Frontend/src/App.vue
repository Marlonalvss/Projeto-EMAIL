<script setup lang="ts">
import Classifier from './components/Classifier.vue';
import ExamplesSection from './components/ExamplesSection.vue';
import HeroSection from './components/HeroSection.vue';
import InfoSection from './components/InfoSection.vue';

import { ref } from 'vue';

const exampleText = ref('');
</script>

<template>
  <div class="min-h-screen bg-background">
    <HeroSection />
    <Classifier :exampleText="exampleText" />
    <ExamplesSection @exampleSelected="text => exampleText = text" />
    <InfoSection />
  </div>
</template>
