<script>
  import "../app.css";
  import "../app.scss";
</script>

<svelte:head>
  <title>Home</title>
</svelte:head>

<div class="body">
  <div class="navbar">
    <h2 class="header">Demo</h2>
  </div>
  <div class="content">
    <slot />
  </div>
</div>

<style lang="scss">
  .navbar {
    @apply sticky p-2 bg-blue-300 text-center;
  }
  .content {
    @apply items-center p-10;
  }
</style>
