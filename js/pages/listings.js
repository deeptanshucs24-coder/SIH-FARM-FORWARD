import { initialListings } from "../data/mockData.js";

if (!window.listings) {
  window.listings = [...initialListings];
}

export function render() {
  const activeCount = window.listings.filter(item => item.status === "Active").length;
  const totalQty = window.listings.reduce((sum, item) => {
    const val = parseInt(item.qty);
    return sum + (isNaN(val) ? 0 : val);
  }, 0);
  
  const rows = window.listings.map(item => {
    let iconClass = item.icon || "fa-seedling";
    if (item.crop.toLowerCase().includes("wheat")) {
      iconClass = "fa-wheat-awn";
    } else if (item.crop.toLowerCase().includes("soybean")) {
      iconClass = "fa-seedling";
    } else if (item.crop.toLowerCase().includes("tomato")) {
      iconClass = "fa-leaf";
    }
    
    const statusBg = item.status === "Active" ? "bg-success-bg text-success" : "bg-surface-variant text-on-surface-variant";
    const priceStr = item.price.includes('/') ? item.price.split('/')[0].trim() : item.price;
    const isOwner = true; // Prototype assumption
    
    return `
      <tr class="hover:bg-surface/30 transition-colors">
        <td class="px-6 py-4">
          <div class="flex items-center gap-3">
            <div class="w-9 h-9 rounded-xl flex items-center justify-center" style="background:#d8f3dc">
              <i class="fa-solid ${iconClass}" style="color:#1b4332"></i>
            </div>
            <div>
              <div class="font-semibold text-on-surface">${item.crop}</div>
              <div class="text-xs text-on-surface-variant mt-0.5">Listed ${item.date}</div>
            </div>
          </div>
        </td>
        <td class="px-6 py-4 text-sm font-medium text-on-surface">${item.qty}</td>
        <td class="px-6 py-4 text-sm font-bold text-on-surface">${priceStr} <span class="font-normal text-on-surface-variant text-xs">/ Qt</span></td>
        <td class="px-6 py-4 text-sm text-on-surface-variant">${item.location}</td>
        <td class="px-6 py-4"><span class="inline-flex items-center px-2.5 py-1 rounded-full text-xs font-semibold ${statusBg}">${item.status}</span></td>
        <td class="px-6 py-4 text-sm font-semibold text-on-surface">${item.responses}</td>
        <td class="px-6 py-4 text-right">
          <button class="px-4 py-1.5 bg-primary-light text-primary font-medium rounded-lg hover:bg-primary-light/80 text-sm" style="color:#1b4332" onclick="navigate('marketplace/buyer')">View Leads</button>
        </td>
      </tr>`;
  }).join("");

  return `<div class="p-6 max-w-7xl mx-auto pb-24 md:pb-6">
  <div class="mb-6">
    <a class="text-primary hover:underline text-sm font-medium flex items-center mb-2 cursor-pointer" onclick="navigate('marketplace')">
      <svg class="w-4 h-4 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path d="M10 19l-7-7m0 0l7-7m-7 7h18" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"/></svg>Back to Marketplace
    </a>
    <div class="flex items-center justify-between">
      <div>
        <h2 class="text-3xl font-bold text-on-surface">Active Listings</h2>
        <p class="text-on-surface-variant mt-1">Manage your produce listings and track responses from buyers.</p>
      </div>
      <button onclick="navigate('marketplace/listings/new')" class="px-5 py-2.5 font-semibold rounded-xl text-white shadow-sm hover:opacity-90 transition flex items-center gap-2 cursor-pointer" style="background:#1b4332">
        <i class="fa-solid fa-plus"></i>New Listing
      </button>
    </div>
  </div>
  <!-- Summary Cards -->
  <div class="grid grid-cols-2 md:grid-cols-4 gap-4 mb-6">
    <div class="bg-white rounded-2xl border border-outline p-4">
      <p class="text-xs text-on-surface-variant font-medium uppercase tracking-wider mb-1">Active</p>
      <p class="text-2xl font-bold text-on-surface" id="stat-active-count">${activeCount}</p>
      <p class="text-xs text-success font-semibold mt-1">↑ 1 new this week</p>
    </div>
    <div class="bg-white rounded-2xl border border-outline p-4">
      <p class="text-xs text-on-surface-variant font-medium uppercase tracking-wider mb-1">Responses</p>
      <p class="text-2xl font-bold text-on-surface">11</p>
      <p class="text-xs text-on-surface-variant mt-1">From verified buyers</p>
    </div>
    <div class="bg-white rounded-2xl border border-outline p-4">
      <p class="text-xs text-on-surface-variant font-medium uppercase tracking-wider mb-1">Qty Listed</p>
      <p class="text-2xl font-bold text-on-surface">${totalQty} Qt</p>
      <p class="text-xs text-on-surface-variant mt-1">Across all listings</p>
    </div>
    <div class="bg-white rounded-2xl border border-outline p-4">
      <p class="text-xs text-on-surface-variant font-medium uppercase tracking-wider mb-1">Avg Price</p>
      <p class="text-2xl font-bold text-on-surface">₹3,140</p>
      <p class="text-xs text-on-surface-variant mt-1">Per quintal</p>
    </div>
  </div>
  <!-- Listings Table -->
  <div class="bg-white rounded-2xl border border-outline overflow-hidden">
    <div class="p-4 border-b border-outline flex items-center justify-between">
      <h3 class="text-lg font-bold text-on-surface">Your Produce Listings</h3>
      <div class="flex items-center gap-2">
        <button class="px-3 py-1.5 bg-white border border-outline rounded-lg text-sm font-medium hover:bg-surface">All Status</button>
      </div>
    </div>
    <table class="w-full text-left border-collapse">
      <thead>
        <tr class="bg-surface/50 border-b border-outline text-xs uppercase tracking-wider text-on-surface-variant">
          <th class="px-6 py-4 font-medium">Produce</th>
          <th class="px-6 py-4 font-medium">Quantity</th>
          <th class="px-6 py-4 font-medium">Listed Price</th>
          <th class="px-6 py-4 font-medium">Location</th>
          <th class="px-6 py-4 font-medium">Status</th>
          <th class="px-6 py-4 font-medium">Responses</th>
          <th class="px-6 py-4 font-medium text-right">Action</th>
        </tr>
      </thead>
      <tbody class="divide-y divide-outline" id="listings-tbl-body">
        ${rows}
      </tbody>
    </table>
  </div>
</div>`;
}
