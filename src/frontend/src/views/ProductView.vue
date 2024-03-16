<script setup>
import { cn } from '@/shadcn/lib/utils'

import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from '@/shadcn/lib/registry/new-york/ui/card'
</script>

<template>
<div class="hidden items-start justify-center gap-6 rounded-lg p-8 md:grid lg:grid-cols-2 xl:grid-cols-3">
    <div class="col-span-2 grid items-start gap-6 lg:col-span-1">
      <Container>
        <Card>
          <CardContent class="pt-6">
            <div class="space-y-2">
              <Label for="date" class="shrink-0">
                Pick a date
              </Label>
            </div>
          </CardContent>
        </Card>
      </Container>
    </div>
</div>
</template>


<style scoped>

</style>