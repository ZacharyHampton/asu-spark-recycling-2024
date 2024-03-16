<script setup>
  import {
    NavigationMenu,
    NavigationMenuContent,
    NavigationMenuItem,
    NavigationMenuLink,
    NavigationMenuList,
    NavigationMenuTrigger,
  } from '@/shadcn/components/ui/navigation-menu/index.js'
</script>

<template>
  <nav class="bg-gray-800 p-4 flex justify-between items-center">
    <!-- Logo container -->
    <div class="flex items-center">
      <img src="" alt="Logo" class="h-8 mr-4">
      <span class="text-white text-lg font-semibold">Your Brand</span>
    </div>

    <!-- Search bar container -->
    <div class="flex-1 max-w-xl mx-auto">
      <div class="relative">
        <input type="search" class="w-full px-4 py-2 rounded-md" placeholder="Search...">
        <button type="submit" class="absolute right-2 top-1/2 transform -translate-y-1/2">
          <i class="fa fa-search text-gray-500"></i>
        </button>
      </div>
    </div>

    <!-- Additional navbar items could go here -->
  </nav>
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