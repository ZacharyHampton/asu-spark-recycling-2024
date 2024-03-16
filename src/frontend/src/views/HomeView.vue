<script>
  import { Input } from '../shadcn/components/ui/input/index.js'
  import { Search } from 'lucide-vue-next'
  import {
  Card,
  CardHeader,
  CardTitle,
} from '../shadcn/components/ui/card/index.js'
  import _ from "lodash";

  export default {
      name: "HomeView",
      components: {
          Card,
          CardHeader,
          CardTitle,
          Search,
          Input
      },
      data() {
          return {
              items: []
          }
      },
      methods: {
        search(query) {
          fetch(`http://localhost:8000/api/v1/search?query=${query}`)
            .then(response => response.json())
            .then(data => {
              this.items = data['products'];
            })
        },
        searchInput: _.debounce(function (event) {
          let query = event.target.value;

          if (query.length > 0) {
            this.search(query);
          } else {
            this.items = [];
          }
        }, 500),
      }
  }
</script>

<template>
  <div class="flex flex-col items-center justify-center min-h-screen">
      <!-- Logo Section -->
    <div class="w-full max-w-md">
      <img src="/logo.webp" alt="" class="mx-auto block" style="width: 100%; max-width: 300px;"> <!-- Adjust the max-width as needed -->
    </div>
    <div class="relative mb-2 max-w-md w-full">
      <Input id="search" type="text" placeholder="Describe your product..."
             class="pl-8 rounded-2xl border-2 border-shadcngray hover:border-shadcnblack transition-all duration-300 search-font w-full" @input="searchInput($event)" />
      <span class="absolute start-0 inset-y-0 flex items-center justify-center" style="padding-left: 8px;">
        <Search class="size-5 text-muted-foreground" />
      </span>
    </div>
    <div class="w-full max-w-md bg-shadcngray rounded-2xl p-2" v-if="items.length !== 0">
      <div>
  <Card
          class="border-2 border-white rounded-2xl card-font mb-2 hover:border-shadcnblack cursor-pointer transition-all duration-300"
          v-for="item in items"
          :key="item.id"
  >
    <CardHeader class="p-2">
      <div class="flex items-center">
        <img :src="item.image_url" alt="" class="w-10 h-10 mr-2 rounded-full">
        <CardTitle>{{ item.title }}</CardTitle>
      </div>
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
