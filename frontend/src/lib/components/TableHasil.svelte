<table {...$$restProps}>
  <thead>
    <tr>
      <th>Skor</th>
      <th>Kalimat</th>
      <th>per-kata</th>
    </tr>
  </thead>
  <tbody>
    <slot />
  </tbody>
</table>

<style lang="scss">
  th {
    @apply border-2 border-white bg-blue-300;
  }
  tbody {
    @apply bg-blue-200;
  }
</style>
