<script lang="ts">
  import "../app.css";
  import "../app.scss";
  import Navbar from "$lib/components/Navbar.svelte";
</script>

<svelte:head>
  <title>Home</title>
</svelte:head>

<div class="body">
  <Navbar></Navbar>
  <div class="content">
    <slot />
  </div>
</div>

<style lang="scss">
  .content {
    @apply items-center p-10;
  }
</style>
