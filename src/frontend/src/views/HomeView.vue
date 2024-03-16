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
  <div class="flex flex-col items-center justify-center min-h-screen ">
      <div class="relative mb-2 ">
        <Input id="search" type="text" placeholder="Describe your product..."
               class="pl-8 rounded-3xl border-2 border-shadcnblack search-font w-full" />
        <span class="absolute start-0 inset-y-0 flex items-center justify-center" style="padding-left: 8px;">
          <Search class="size-5 text-muted-foreground" />
        </span>
      </div>
          <div class="w-full max-w-md bg-shadcnblack rounded-3xl p-2">
      <div>
        <Card class="border-2 border-shadcngray rounded-3xl card-font mb-2">
          <CardHeader class="flex items-center p-2">
            <CardTitle>Product</CardTitle>
          </CardHeader>
        </Card>
        <Card class="border-2 border-shadcngray rounded-3xl card-font">
          <CardHeader class="flex items-center p-2">
            <CardTitle>Product 2</CardTitle>
          </CardHeader>
        </Card>
      </div>
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
