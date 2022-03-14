<script lang="ts">
  import QuestionMarkFilled from "$lib/elements/QuestionMarkFilled.svelte";
  import Logo from "$lib/elements/Logo.svelte";
  import Modal from "$lib/elements/Modal.svelte";
  import Card from "$lib/elements/Card.svelte";
  import Info from "$lib/elements/Info.svelte";

  let mod = false;
</script>

<div class="navbar">
  <a class="logo" href="/">
    <Logo></Logo>
  </a>
  <QuestionMarkFilled on:clicked={() => (mod = !mod)} />
</div>

{#if mod}
  <Modal on:clicked={() => (mod = !mod)}>
    <Card>
      <Info></Info>
    </Card>
  </Modal>
{/if}

<style lang="scss">
  .navbar {
    @apply flex justify-between sticky p-2 bg-blue-500;
  }
  .logo {
    @apply text-white;
  }

</style>
