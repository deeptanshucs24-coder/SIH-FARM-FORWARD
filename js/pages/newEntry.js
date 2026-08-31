export function render() {
  return `<div class="p-margin max-w-4xl mx-auto pb-24 md:pb-margin">
  <a class="text-primary hover:underline text-sm font-medium flex items-center mb-md cursor-pointer" onclick="navigate('financials')">
    <svg class="w-4 h-4 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path d="M10 19l-7-7m0 0l7-7m-7 7h18" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"/></svg>Back to Financials
  </a>
  <div class="mb-xl">
    <h1 class="font-headline-lg text-headline-lg text-primary font-bold">New Financial Entry</h1>
    <p class="font-body-md text-body-md text-on-surface-variant mt-xs">Record a farm income or expense transaction to keep your financial ledger up to date.</p>
  </div>
  <form onsubmit="saveFinancialEntry(event)" class="bg-surface-container-lowest border border-outline-variant rounded-xl p-lg flex flex-col gap-lg shadow-sm">
    <div class="grid grid-cols-1 sm:grid-cols-2 gap-md">
      <div class="flex flex-col gap-xs sm:col-span-2">
        <label class="font-label-md text-label-md text-on-surface-variant uppercase font-semibold">Entry Type *</label>
        <div class="flex gap-md">
          <label class="flex-1 flex items-center justify-center gap-2 p-md border border-outline-variant rounded-xl cursor-pointer hover:bg-surface-container-low"><input type="radio" name="entry_type" value="Income" checked class="text-primary focus:ring-primary"><span class="font-label-md text-primary font-bold">Income (Sale / Receivables)</span></label>
          <label class="flex-1 flex items-center justify-center gap-2 p-md border border-outline-variant rounded-xl cursor-pointer hover:bg-surface-container-low"><input type="radio" name="entry_type" value="Expense" class="text-primary focus:ring-primary"><span class="font-label-md text-error font-bold">Expense (Input / Transport)</span></label>
        </div>
      </div>
      <div class="flex flex-col gap-xs">
        <label class="font-label-md text-label-md text-on-surface-variant uppercase font-semibold">Category *</label>
        <select id="fin-cat" required class="px-md py-sm bg-surface border border-outline-variant rounded-lg font-body-sm focus:outline-none focus:border-primary-container">
          <option value="Crop Sales">Crop Sales</option>
          <option value="Input Purchase">Inputs (Fertilizer / Seeds)</option>
          <option value="Transport">Transport &amp; Logistics</option>
          <option value="Equipment">Equipment Maintenance</option>
          <option value="Labor">Labor &amp; Wages</option>
          <option value="Utilities">Irrigation &amp; Power</option>
        </select>
      </div>
      <div class="flex flex-col gap-xs">
        <label class="font-label-md text-label-md text-on-surface-variant uppercase font-semibold">Amount (â‚¹) *</label>
        <input id="fin-amount" type="number" required placeholder="e.g. 85000" class="px-md py-sm bg-surface border border-outline-variant rounded-lg font-body-sm focus:outline-none focus:border-primary-container">
      </div>
      <div class="flex flex-col gap-xs sm:col-span-2">
        <label class="font-label-md text-label-md text-on-surface-variant uppercase font-semibold">Description *</label>
        <input id="fin-desc" type="text" required placeholder="e.g. Soybean sale at Indore Spot Market" class="px-md py-sm bg-surface border border-outline-variant rounded-lg font-body-sm focus:outline-none focus:border-primary-container">
      </div>
      <div class="flex flex-col gap-xs">
        <label class="font-label-md text-label-md text-on-surface-variant uppercase font-semibold">Date *</label>
        <input id="fin-date" type="date" value="2024-08-30" required class="px-md py-sm bg-surface border border-outline-variant rounded-lg font-body-sm focus:outline-none focus:border-primary-container">
      </div>
      <div class="flex flex-col gap-xs">
        <label class="font-label-md text-label-md text-on-surface-variant uppercase font-semibold">Payment Method</label>
        <select id="fin-method" class="px-md py-sm bg-surface border border-outline-variant rounded-lg font-body-sm focus:outline-none focus:border-primary-container">
          <option value="Bank Transfer (NEFT)">Bank Transfer (NEFT/RTGS)</option>
          <option value="UPI / Instant">UPI / Instant Pay</option>
          <option value="Cash">Cash Transaction</option>
          <option value="Cheque">Cheque</option>
        </select>
      </div>
      <div class="flex flex-col gap-xs sm:col-span-2">
        <label class="font-label-md text-label-md text-on-surface-variant uppercase font-semibold">Notes &amp; Reference No.</label>
        <textarea id="fin-notes" rows="2" placeholder="Invoice #, Mandi receipt number or additional transaction details..." class="px-md py-sm bg-surface border border-outline-variant rounded-lg font-body-sm focus:outline-none focus:border-primary-container"></textarea>
      </div>
    </div>
    <div class="flex items-center justify-end gap-md border-t border-outline-variant/40 pt-md mt-sm">
      <button type="button" onclick="navigate('financials')" class="px-lg py-md border border-outline-variant text-on-surface font-label-md text-label-md rounded-xl hover:bg-surface-container transition-colors">Cancel</button>
      <button type="submit" class="px-lg py-md text-white font-label-md text-label-md rounded-xl hover:opacity-90 transition-opacity shadow-sm" style="background:#1b4332">Save Entry</button>
    </div>
  </form>
</div>
`;
}

