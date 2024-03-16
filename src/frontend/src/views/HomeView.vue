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
  <div class="flex flex-col items-center justify-center min-h-screen">
    <div class="relative w-full max-w-md mb-4" style="transform: translateY(-18%);">
      <Input id="search" type="text" placeholder="Describe your product..."
             class="pl-8 rounded-2xl border-2 border-black search-font" />
      <span class="absolute start-0 inset-y-0 flex items-center justify-center" style="padding-left: 8px;">
        <Search class="size-5 text-muted-foreground" />
      </span>
    </div>
    <div class="w-full max-w-md">
      <div class="bg-gray-200 p-1 rounded-2xl"> <!-- Added div with gray background and slight padding -->
        <Card class="border-2 border-black rounded-2xl card-font">
          <CardHeader>
            <CardTitle>Card Title</CardTitle>
            <CardDescription>Card Description</CardDescription>
          </CardHeader>
          <CardContent>
            Card Content
          </CardContent>
          <CardFooter>
            Card Footer
          </CardFooter>
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
