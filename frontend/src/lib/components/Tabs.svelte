<script lang="ts">
    import { createEventDispatcher } from 'svelte';
    const dispatch = createEventDispatcher();

    export let tabNames;
    export let activeTab;
</script>

<div class="tabs">
    <ul>
        {#each tabNames as item}
            <li on:click={()=>dispatch('tabChange', item)}>
                <div class:active={item === activeTab}>{item}</div>
            </li>
        {/each}
    </ul>
</div>

<style lang="scss">
    .tabs {
        @apply mb-4;
    }
    ul {
        @apply flex justify-center gap-2;
        li {
            @apply m-0 cursor-pointer text-gray-900;
            &:hover {
                @apply border-red-400 border-b-2 text-red-400;
            }
            .active {
                @apply font-semibold text-red-400 border-b-2 border-red-400;
            }
        }
    }
</style>