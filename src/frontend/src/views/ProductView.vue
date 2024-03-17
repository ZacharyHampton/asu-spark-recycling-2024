<script setup>
import { cn } from '../shadcn/lib/utils'
import { h } from 'vue'
import * as z from 'zod'

import { Button } from '../shadcn/components/ui/button/index.js'
import {
  FormControl,
  FormDescription,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from '../shadcn/components/ui/form/index.js'
import {
  Select,
  SelectContent,
  SelectGroup,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from '../shadcn/components/ui/select/index.js'
import { toast } from '../shadcn/components/ui/toast/index.js'

import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from '../shadcn/components/ui/card'
import Container from "@/components/Container.vue";
import {Input} from "@/shadcn/components/ui/input/index.js";
import {Search} from "lucide-vue-next";
</script>

<template>
  <div class="flex-1 h-screen flex-col items-center justify-start min-h-screen pt-8 pb-8">
    <div class="mx-auto max-w-md bg-shadcngray bg-opacity-65 rounded-2xl p-3 h-full ">
      <!-- Large Card -->
      <Card class="h-full border-2 border-black rounded-2xl card-font mb-2 w-full h-screen-3/4">
        <!-- Large card almost full screen size -->
        <CardHeader class="p-2 flex flex-col">
          <!-- Top Left Title inside a Rounded Box -->
          <div class="bg-white border-2 border-shadcngray rounded-md p-2 text-shadcnblack">
            <CardTitle>iPhone 65 Plus Pro Max</CardTitle>
          </div>
          <!-- Large Image below the title -->
          <div class="my-4">
            <img src="" alt="Large Image" class="w-full rounded-md">
            <!-- Large image here -->
          </div>
          <!-- Another Card below the image -->
          <Card class="border-2 border-shadcngray rounded-2xl card-font">
            <CardHeader class="p-2">
              <CardTitle>Condition</CardTitle>
              <CardContent>
                <form class="w-2/3 space-y-6" @submit="onSubmit">
                  <FormField v-slot="{ componentField }" name="email">
                    <FormItem>
                      <Select v-bind="componentField">
                        <FormControl>
                          <SelectTrigger>
                            <SelectValue class="cursor-pointer hover:border-shadcnblack transition-all duration-300" placeholder="Select the condition" />
                          </SelectTrigger>
                        </FormControl>
                        <SelectContent>
                          <SelectGroup>
                            <SelectItem class="cursor-pointer" value="m@example.com"> Working </SelectItem>
                            <SelectItem class="cursor-pointer" value="m@google.com"> Broken </SelectItem>
                            <SelectItem class="cursor-pointer" value="m@support.com"> Refurbished </SelectItem>
                          </SelectGroup>
                        </SelectContent>
                      </Select>
                      <FormDescription> Select the condition of your device. </FormDescription>
                      <FormMessage />
                    </FormItem>
                  </FormField>
                  <Button type="submit"> Submit </Button>
                </form>
              </CardContent>
            </CardHeader>
          </Card>
          <Card class="border-2 border-shadcngray rounded-2xl card-font">
            <CardHeader>
            <CardTitle>Best Buy</CardTitle>
            </CardHeader>
              <CardContent>$100.50</CardContent>

  </Card>
        </CardHeader>
      </Card>
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