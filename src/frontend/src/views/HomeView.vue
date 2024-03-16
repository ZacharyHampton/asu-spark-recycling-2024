<script setup>
  import { Button } from '../shadcn/components/ui/button/index.js'
  import { Input } from '../shadcn/components/ui/input/index.js'
  import { Search } from 'lucide-vue-next'
  import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from '../shadcn/components/ui/card/index.js'
</script>

<template>
  <div class="flex items-center justify-center min-h-screen" style="transform: translateY(-18%);"> <!-- Adjusted for vertical move -->
    <div class="relative w-full max-w-sm">
      <Input id="search" type="text" placeholder="Describe your product... "
             class="pl-8 rounded-2xl border-2 border-black search-font" /> <!-- Prevent additional border on focus -->
      <span class="absolute start-0 inset-y-0 flex items-center justify-center" style="padding-left: 8px;"> <!-- Adjusted for icon spacing -->
        <Search class="size-5 text-muted-foreground" />
      </span>
    </div>
  </div>

  <div>

  </div>
</template>

<style scoped>
.search-font {
    font-family: geist, serif
}
.search-font:focus {
    outline:none !important
}
@font-face {
    font-family: geist;
    src:url("../../public/geist/geist-semibold.woff2")
}
</style>
