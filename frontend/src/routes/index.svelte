<script lang="ts">
  import FormArtikel from "$lib/components/FormArtikel.svelte";
  import TableHasil from "$lib/components/TableHasil.svelte";
  import { predictText } from "$lib/db";
  import Btn from "$lib/elements/Btn.svelte";

  let data: string;
  let load = false;
  let raw = false;
  let promise = Promise.all([]);

  function handleSubmit(e: any) {
    //! delete address:port before build
    const url = "/api/1/predict/";
    data = e.detail;
    if (data) {
      promise = predictText(url, data);
      load = !load;
    }
  }

  function copyHasil() {
    var copyText = document.getElementById("hasil-analisa").innerText;
    navigator.clipboard.writeText(copyText);
    alert("Hasil analisis telah tersimpan dalam clipboard");
  }
</script>

<div class="container lg:flex gap-2">
  <div class=" lg:min-w-[50%]">

    <p class="text-left">input teks yang ingin di-analisis:</p>
    <div class="form-berita">
      <FormArtikel on:submit={handleSubmit} />
    </div>

  </div>

  <div class="lg:min-w-[50%]">

    <p class="text-left">hasil anailsis:</p>
    <div class="hasil min-h-[20rem]">
      {#await promise}
      {#if load}
        ..loading
      {/if}
    {:then promise}
      {#if raw}
        <div class="flex gap-1">
            <Btn color="blue" on:click={() => (raw = !raw)}>Tabel</Btn>
          
            <p class="text-blue-800">
              klik text untuk meng-copy hasil ke <i>clipboard</i>.
            </p>
        </div>

        <div id="hasil-analisa" on:click={() => copyHasil()}>
          {JSON.stringify(promise)}
        </div>
      {:else}
        <div class="flex gap-1">
          <Btn color="blue" on:click={() => (raw = !raw)}>Json</Btn>
          <p class="text-blue-800">klik untuk melihat versi mentah.</p>
        </div>

        <TableHasil>
          {#each promise["perkalimat"] as kt}
            <tr>
              <td class="skor">
                <div class={kt.label == "1" ? "blue" : "red"}>
                  {kt.skor}
                </div>
              </td>
              <td class="perkalimat">{kt.kalimat}</td>
              <td class="perkata">
                {#each kt["perkata"] as tt}
                  <div class={tt.label == "1" ? "blue" : "red"}>
                    <p>{tt.freq}({tt.kata})</p>
                  </div>
                {/each}
              </td>
            </tr>
          {/each}
        </TableHasil>
      {/if}
    {:catch error}
      <p style="color: red">{error.message}</p>
    {/await}
  </div>
</div>
</div>

<style lang="scss">
  td,
  tr {
    @apply border-2 border-white px-1;
  }

  .hasil {
    @apply flex p-2;
    @apply flex-col gap-y-2 border-2;
  }

  #hasil-analisa {
    @apply bg-gray-300 p-2 rounded-md;
  }

  .perkata {
    @apply border-0 flex flex-wrap max-w-sm;
    font-style: none;
  }
  .perkalimat {
    @apply max-w-md;
  }

  .blue {
    @apply bg-blue-400 rounded p-1 m-1 shadow-md w-max;
  }
  .red {
    @apply bg-red-400 rounded p-1 m-1 shadow-md w-max;
  }
</style>
