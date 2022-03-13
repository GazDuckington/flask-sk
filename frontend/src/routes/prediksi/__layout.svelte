<svelte:head>
    <title>Analisis Sentimen</title>
</svelte:head>
<div class="container">
    <slot/>
</div>

<style lang="scss">
    div {
        @apply p-2;
    }
    .container {
        @apply items-center px-10;
    }
</style>