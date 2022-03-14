<div class="backdrop">
  <div class="modal">
    <slot />
  </div>
</div>

<style lang="scss">
  .backdrop {
    @apply w-full h-full fixed bg-gray-100/80;
  }
  .modal {
    @apply grid place-items-center;
  }
</style>
