<script lang="ts"></script>

<div class="card">
    <slot />
</div>

<style lang="scss">
    .card {
        @apply rounded-md max-w-[60%] p-5 overflow-x-scroll; 
        @apply bg-white shadow-md border-4 border-gray-100;
    }
</style>