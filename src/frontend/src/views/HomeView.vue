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
<div class="relative w-full max-w-sm items-center" style="margin:auto">
    <Input id="search" type="text" placeholder="Search..." class="pl-10" />
    <span class="absolute start-0 inset-y-0 flex items-center justify-center px-2">
      <Search class="size-6 text-muted-foreground" />
    </span>
  </div>
  <div>
    <Button variant="outline">Click me</Button>
  </div>
</template>

<style scoped>

</style>
