export function render() {
  return `<div class="p-margin max-w-4xl mx-auto pb-24 md:pb-margin">
  <a class="text-primary hover:underline text-sm font-medium flex items-center mb-md cursor-pointer" onclick="navigate('marketplace/listings')">
    <svg class="w-4 h-4 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path d="M10 19l-7-7m0 0l7-7m-7 7h18" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"/></svg>Back to Active Listings
  </a>
  <div class="mb-xl">
    <h1 class="font-headline-lg text-headline-lg text-primary font-bold">Create New Produce Listing</h1>
    <p class="font-body-md text-body-md text-on-surface-variant mt-xs">Post your crop details to receive direct buy offers from verified buyers across mandis.</p>
  </div>
  <form onsubmit="publishListing(event)" class="bg-surface-container-lowest border border-outline-variant rounded-xl p-lg flex flex-col gap-lg shadow-sm">
    <div class="grid grid-cols-1 sm:grid-cols-2 gap-md">
      <div class="flex flex-col gap-xs">
        <label class="font-label-md text-label-md text-on-surface-variant uppercase font-semibold">Produce / Crop *</label>
        <select id="new-crop" required class="px-md py-sm bg-surface border border-outline-variant rounded-lg font-body-sm focus:outline-none focus:border-primary-container">
          <option value="Wheat">Wheat</option>
          <option value="Soybean">Soybean</option>
          <option value="Onion">Onion</option>
          <option value="Tomato">Tomato</option>
          <option value="Maize">Maize</option>
          <option value="Cotton">Cotton</option>
        </select>
      </div>
      <div class="flex flex-col gap-xs">
        <label class="font-label-md text-label-md text-on-surface-variant uppercase font-semibold">Variety</label>
        <input id="new-variety" type="text" placeholder="e.g. Sharbati, Lok-1, Hybrid" class="px-md py-sm bg-surface border border-outline-variant rounded-lg font-body-sm focus:outline-none focus:border-primary-container">
      </div>
      <div class="flex flex-col gap-xs">
        <label class="font-label-md text-label-md text-on-surface-variant uppercase font-semibold">Quantity *</label>
        <div class="flex gap-2">
          <input id="new-qty" type="number" required placeholder="e.g. 400" class="flex-1 px-md py-sm bg-surface border border-outline-variant rounded-lg font-body-sm focus:outline-none focus:border-primary-container">
          <select id="new-unit" class="w-28 px-md py-sm bg-surface border border-outline-variant rounded-lg font-body-sm focus:outline-none focus:border-primary-container">
            <option value="Qt">Qt (Quintal)</option>
            <option value="MT">MT (Metric Ton)</option>
            <option value="Bales">Bales</option>
            <option value="Kg">Kg</option>
          </select>
        </div>
      </div>
      <div class="flex flex-col gap-xs">
        <label class="font-label-md text-label-md text-on-surface-variant uppercase font-semibold">Asking Price (₹ / Unit) *</label>
        <input id="new-price" type="number" required placeholder="e.g. 3250" class="px-md py-sm bg-surface border border-outline-variant rounded-lg font-body-sm focus:outline-none focus:border-primary-container">
      </div>
      <div class="flex flex-col gap-xs">
        <label class="font-label-md text-label-md text-on-surface-variant uppercase font-semibold">Location / Mandi *</label>
        <input id="new-location" type="text" required placeholder="e.g. Indore Mandi, MP" class="px-md py-sm bg-surface border border-outline-variant rounded-lg font-body-sm focus:outline-none focus:border-primary-container">
      </div>
      <div class="flex flex-col gap-xs">
        <label class="font-label-md text-label-md text-on-surface-variant uppercase font-semibold">Availability / Harvest Date</label>
        <input id="new-date" type="date" value="2024-09-02" class="px-md py-sm bg-surface border border-outline-variant rounded-lg font-body-sm focus:outline-none focus:border-primary-container">
      </div>
      <div class="flex flex-col gap-xs sm:col-span-2">
        <label class="font-label-md text-label-md text-on-surface-variant uppercase font-semibold">Quality / Grade</label>
        <select id="new-grade" class="px-md py-sm bg-surface border border-outline-variant rounded-lg font-body-sm focus:outline-none focus:border-primary-container">
          <option value="Grade A (Premium)">Grade A (Premium Quality)</option>
          <option value="Grade B (Standard)">Grade B (Standard Quality)</option>
          <option value="Organic Certified">Organic Certified</option>
        </select>
      </div>
      <div class="flex flex-col gap-xs sm:col-span-2">
        <label class="font-label-md text-label-md text-on-surface-variant uppercase font-semibold">Description &amp; Notes</label>
        <textarea id="new-desc" rows="3" placeholder="Describe moisture level, packaging, storage conditions..." class="px-md py-sm bg-surface border border-outline-variant rounded-lg font-body-sm focus:outline-none focus:border-primary-container"></textarea>
      </div>
    </div>
    <div class="flex items-center justify-end gap-md border-t border-outline-variant/40 pt-md mt-sm">
      <button type="button" onclick="navigate('marketplace/listings')" class="px-lg py-md border border-outline-variant text-on-surface font-label-md text-label-md rounded-xl hover:bg-surface-container transition-colors">Cancel</button>
      <button type="submit" class="px-lg py-md text-white font-label-md text-label-md rounded-xl hover:opacity-90 transition-opacity shadow-sm" style="background:#1b4332">Publish Listing</button>
    </div>
  </form>
</div>
`;
}

