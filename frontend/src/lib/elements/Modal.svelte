<script lang="ts">
    import {createEventDispatcher} from "svelte";
    const dispatch = createEventDispatcher();

    function handleClick(){
        dispatch("clicked");
    }
</script>

<div class="modal" on:click={handleClick}>
    <slot />
</div>

<style lang="scss">
    .modal {
        @apply fixed top-0 left-0 h-full w-full grid place-items-center;
        @apply text-black backdrop-blur-3xl bg-blue-100/50;
    }
</style>