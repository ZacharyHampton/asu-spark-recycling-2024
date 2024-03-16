<script setup>
import { cn } from '@/shadcn/lib/utils'

import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from '../shadcn/components/ui/card'
import Container from "@/components/Container.vue";
</script>

<template>
<div class="flex flex-col items-center justify-center min-h-screen">
    <div class="w-full max-w-md">
      <img src="/logo.webp" alt="" class="mx-auto block" style="width: 100%; max-width: 300px;"> <!-- Adjust the max-width as needed -->
    </div>
</div>
</template>


<style scoped>
.search-font {
    font-family: geist, serif;
}
.card-font {
    font-family: geist, serif;
}

.search-font:focus, .search-font:focus-visible {
    outline:none !important;
    box-shadow: none !important; /* Remove any box-shadow if applied */
}
@font-face {
    font-family: geist;
    src:url("../../public/geist/geist-semibold.woff2")
}
</style>