<script setup>
  import { Button } from '@/shadcn/components/ui/button'
  import {
    NavigationMenu,
    NavigationMenuContent,
    NavigationMenuItem,
    NavigationMenuLink,
    NavigationMenuList,
    NavigationMenuTrigger,
  } from '@/shadcn/components/ui/navigation-menu'
</script>

<template>
  <div>
    <NavigationMenu>
  <NavigationMenuList>
    <NavigationMenuItem>
      <NavigationMenuTrigger>Item One</NavigationMenuTrigger>
      <NavigationMenuContent>
        <NavigationMenuLink>Link</NavigationMenuLink>
      </NavigationMenuContent>
    </NavigationMenuItem>
  </NavigationMenuList>
</NavigationMenu>

  </div>
  <div>
    <Button variant="outline">Click me</Button>
  </div>
</template>

<style scoped>

</style>
