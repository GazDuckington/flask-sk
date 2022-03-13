<script lang="ts">
  export let color = "green";
</script>

<button class={color} on:click {...$$restProps}>
  <slot />
</button>

<style lang="scss">
  button {
    @apply rounded px-1 border-2;

    &:disabled {
      @apply bg-gray-400;
    }

    &.green {
      @apply bg-green-500 text-white border-green-400;
      &:hover {
        @apply bg-green-300;
      }
    }

    &.red {
      @apply bg-red-500 text-white;
      &:hover {
        @apply bg-red-300;
      }
    }

    &.blue {
      @apply bg-blue-500 border-blue-500 text-white;
      &:hover {
        @apply bg-blue-300;
      }
    }
  }
</style>
