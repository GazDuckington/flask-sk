<script lang="ts">
  import Btn from "$lib/elements/Btn.svelte";
  import { createEventDispatcher } from "svelte";

  let artikel, wrg: string;
  let min = 4;
  const dispatch = createEventDispatcher();

  function handleSubmit() {
    if (artikel) {
      let isnum = /^\d+$/.test(artikel);
      if (artikel.length < min) {
        wrg = "Peringatan! jumlah minimum karakter: " + min;
      } else if (isnum) {
        wrg = "tolong gunakan karakter alpha-numeric";
      } else {
        dispatch("submit", artikel);
      }
    } else {
      wrg = "Tolong masukan input";
    }
  }
</script>

<div class="container min-h-[20rem]">
  <div class="form">
    <form on:submit|preventDefault={handleSubmit} method="post">
      {#if wrg}
        <div class="warning">{wrg}</div>
      {/if}

      <textarea
        name="data"
        id="data"
        cols="30"
        rows="10"
        bind:value={artikel}
      />
      <Btn type="submit">Submit</Btn>
    </form>
  </div>
</div>

<style lang="scss">
  .container {
    @apply flex flex-col gap-y-2 p-2 border-2;
    @apply justify-center;
  }
  form {
    @apply flex flex-col gap-1;
    @apply text-center;
    @apply shadow-md;
    textarea {
      @apply bg-gray-300 shadow-sm p-1 rounded;
    }
  }
  .warning {
    @apply bg-yellow-500 text-white text-left;
    @apply rounded font-semibold px-1;
  }
</style>
