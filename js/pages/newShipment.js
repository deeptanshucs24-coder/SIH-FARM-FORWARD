export function render() {
  const nextId = "FF-" + (1024 + (window.shipments ? window.shipments.length : 4));
  return `<div class="p-margin max-w-4xl mx-auto pb-24 md:pb-margin">
  <a class="text-primary hover:underline text-sm font-medium flex items-center mb-md cursor-pointer" onclick="navigate('logistics')">
    <svg class="w-4 h-4 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path d="M10 19l-7-7m0 0l7-7m-7 7h18" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"/></svg>Back to Logistics
  </a>
  <div class="mb-xl">
    <h1 class="font-headline-lg text-headline-lg text-primary font-bold">Create New Shipment</h1>
    <p class="font-body-md text-body-md text-on-surface-variant mt-xs">Schedule dispatch and assign transport for harvested produce delivery.</p>
  </div>
  <form onsubmit="createShipment(event)" class="bg-surface-container-lowest border border-outline-variant rounded-xl p-lg flex flex-col gap-lg shadow-sm">
    <div class="grid grid-cols-1 sm:grid-cols-2 gap-md">
      <div class="flex flex-col gap-xs">
        <label class="font-label-md text-label-md text-on-surface-variant uppercase font-semibold">Shipment ID</label>
        <input id="ship-id" type="text" value="${nextId}" readonly class="px-md py-sm bg-surface-container border border-outline-variant rounded-lg font-body-sm font-bold text-primary">
      </div>
      <div class="flex flex-col gap-xs">
        <label class="font-label-md text-label-md text-on-surface-variant uppercase font-semibold">Crop / Commodity *</label>
        <select id="ship-crop" required class="px-md py-sm bg-surface border border-outline-variant rounded-lg font-body-sm focus:outline-none focus:border-primary-container">
          <option value="Wheat">Wheat</option>
          <option value="Soybean">Soybean</option>
          <option value="Onion">Onion</option>
          <option value="Tomato">Tomato</option>
          <option value="Cotton">Cotton</option>
        </select>
      </div>
      <div class="flex flex-col gap-xs">
        <label class="font-label-md text-label-md text-on-surface-variant uppercase font-semibold">Quantity *</label>
        <input id="ship-qty" type="text" required placeholder="e.g. 450 Qt" class="px-md py-sm bg-surface border border-outline-variant rounded-lg font-body-sm focus:outline-none focus:border-primary-container">
      </div>
      <div class="flex flex-col gap-xs">
        <label class="font-label-md text-label-md text-on-surface-variant uppercase font-semibold">Transporter / Carrier *</label>
        <input id="ship-carrier" type="text" required placeholder="e.g. Kisan Agri Logistics" class="px-md py-sm bg-surface border border-outline-variant rounded-lg font-body-sm focus:outline-none focus:border-primary-container">
      </div>
      <div class="flex flex-col gap-xs">
        <label class="font-label-md text-label-md text-on-surface-variant uppercase font-semibold">Source Location *</label>
        <input id="ship-source" type="text" required placeholder="e.g. Indore Farm Warehouse, MP" class="px-md py-sm bg-surface border border-outline-variant rounded-lg font-body-sm focus:outline-none focus:border-primary-container">
      </div>
      <div class="flex flex-col gap-xs">
        <label class="font-label-md text-label-md text-on-surface-variant uppercase font-semibold">Destination Mandi / Buyer *</label>
        <input id="ship-dest" type="text" required placeholder="e.g. Azadpur Mandi, Delhi" class="px-md py-sm bg-surface border border-outline-variant rounded-lg font-body-sm focus:outline-none focus:border-primary-container">
      </div>
      <div class="flex flex-col gap-xs">
        <label class="font-label-md text-label-md text-on-surface-variant uppercase font-semibold">Dispatch Date *</label>
        <input id="ship-dispatch" type="date" value="2024-09-01" required class="px-md py-sm bg-surface border border-outline-variant rounded-lg font-body-sm focus:outline-none focus:border-primary-container">
      </div>
      <div class="flex flex-col gap-xs">
        <label class="font-label-md text-label-md text-on-surface-variant uppercase font-semibold">Expected Delivery Date *</label>
        <input id="ship-eta" type="date" value="2024-09-03" required class="px-md py-sm bg-surface border border-outline-variant rounded-lg font-body-sm focus:outline-none focus:border-primary-container">
      </div>
      <div class="flex flex-col gap-xs sm:col-span-2">
        <label class="font-label-md text-label-md text-on-surface-variant uppercase font-semibold">Vehicle &amp; Transport Details</label>
        <input id="ship-vehicle" type="text" placeholder="e.g. 10-Ton Truck MP-09-AB-4567 · Driver: Suresh Sharma (+91 98260 11223)" class="px-md py-sm bg-surface border border-outline-variant rounded-lg font-body-sm focus:outline-none focus:border-primary-container">
      </div>
    </div>
    <div class="flex items-center justify-end gap-md border-t border-outline-variant/40 pt-md mt-sm">
      <button type="button" onclick="navigate('logistics')" class="px-lg py-md border border-outline-variant text-on-surface font-label-md text-label-md rounded-xl hover:bg-surface-container transition-colors">Cancel</button>
      <button type="submit" class="px-lg py-md text-white font-label-md text-label-md rounded-xl hover:opacity-90 transition-opacity shadow-sm" style="background:#1b4332">Create Shipment</button>
    </div>
  </form>
</div>
`;
}

