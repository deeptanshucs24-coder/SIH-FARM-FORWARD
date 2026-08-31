import { initialShipments } from "../data/mockData.js";

if (!window.shipments) {
  window.shipments = [...initialShipments];
}

export function render() {
  const activeCount = window.shipments.filter(item => item.status === "In Transit" || item.status === "Scheduled").length;
  
  const shipmentRows = window.shipments.map(item => {
    let statusClass = "bg-[#fff8e1] text-[#f57f17] border border-[#ffecb3]";
    let dotClass = "bg-[#f57f17]";
    if (item.status === "Delivered") {
      statusClass = "bg-success-bg text-success border border-success/20";
      dotClass = "bg-success";
    } else if (item.status === "Scheduled") {
      statusClass = "bg-surface-variant text-on-surface-variant border border-outline";
      dotClass = "bg-on-surface-variant";
    }
    
    const destination = item.route.includes("→") ? item.route.split("→")[1].trim() : item.route;

    return `
      <tr class="hover:bg-surface/30 transition-colors">
        <td class="px-6 py-4 font-semibold text-sm text-on-surface">${item.id}</td>
        <td class="px-6 py-4">
          <div class="font-semibold text-on-surface text-sm">${item.crop}</div>
          <div class="text-on-surface-variant text-xs">${item.qty}</div>
        </td>
        <td class="px-6 py-4 text-sm text-on-surface">
          <div class="flex items-center gap-1">
            <span>Indore</span>
            <span class="material-symbols-outlined text-outline text-[16px]">arrow_right_alt</span>
            <span>${destination}</span>
          </div>
        </td>
        <td class="px-6 py-4">
          <span class="${statusClass} px-2.5 py-1 rounded-full text-xs font-semibold uppercase tracking-wide inline-flex items-center gap-1">
            <span class="w-1.5 h-1.5 rounded-full ${dotClass}"></span>${item.status}
          </span>
        </td>
        <td class="px-6 py-4 text-sm text-on-surface-variant font-medium">${item.eta}</td>
        <td class="px-6 py-4 text-right">
          <button class="text-on-surface-variant hover:text-on-surface p-1 rounded transition-colors">
            <span class="material-symbols-outlined">more_vert</span>
          </button>
        </td>
      </tr>`;
  }).join("");

  return `<div class="p-margin max-w-7xl mx-auto pb-24 md:pb-margin">
  <div class="flex flex-col md:flex-row md:items-end justify-between gap-md mb-xl">
    <div>
      <h1 class="font-headline-lg text-headline-lg text-primary">Logistics</h1>
      <p class="font-body-md text-body-md text-on-surface-variant mt-xs">Track shipment dispatches, delivery routes, and transport costs.</p>
    </div>
    <div class="flex items-center gap-md shrink-0">
      <button class="bg-surface text-on-surface border border-outline-variant font-label-md text-label-md px-md py-sm rounded-lg hover:bg-surface-container-low transition-colors shadow-sm flex items-center gap-xs" onclick="alert('Downloading carrier list...')"><span class="material-symbols-outlined" style="font-size:18px">local_shipping</span>Carrier List</button>
      <button onclick="navigate('logistics/new')" class="bg-primary-container text-on-primary font-label-md text-label-md px-md py-sm rounded-lg hover:opacity-90 transition-opacity shadow-sm flex items-center gap-xs cursor-pointer"><span class="material-symbols-outlined" style="font-size:18px">add</span>New Shipment</button>
    </div>
  </div>
  <!-- KPI Summary -->
  <div class="grid grid-cols-2 md:grid-cols-4 gap-4 mb-xl">
    <div class="bg-white rounded-2xl border border-outline p-4">
      <p class="text-xs text-on-surface-variant font-medium uppercase tracking-wider mb-1">Active Shipments</p>
      <p class="text-2xl font-bold text-on-surface">${activeCount}</p>
      <p class="text-xs text-on-surface-variant mt-1">In transit / Scheduled</p>
    </div>
    <div class="bg-white rounded-2xl border border-outline p-4">
      <p class="text-xs text-on-surface-variant font-medium uppercase tracking-wider mb-1">Deliveries</p>
      <p class="text-2xl font-bold text-on-surface">38</p>
      <p class="text-xs text-success font-semibold mt-1">100% successful rate</p>
    </div>
    <div class="bg-white rounded-2xl border border-outline p-4">
      <p class="text-xs text-on-surface-variant font-medium uppercase tracking-wider mb-1">On-Time Delivery</p>
      <p class="text-2xl font-bold text-on-surface">94.2%</p>
      <p class="text-xs text-success font-semibold mt-1">↑ 1.5% vs last month</p>
    </div>
    <div class="bg-white rounded-2xl border border-outline p-4">
      <p class="text-xs text-on-surface-variant font-medium uppercase tracking-wider mb-1">Logistics Cost</p>
      <p class="text-2xl font-bold text-on-surface">₹2,84,500</p>
      <p class="text-xs text-on-surface-variant mt-1">Total this month</p>
    </div>
  </div>
  <!-- Content Area -->
  <div class="flex flex-col lg:flex-row gap-xl">
    <div class="flex-1 flex flex-col gap-xl">
      <!-- Shipment List -->
      <div class="bg-white rounded-2xl border border-outline overflow-hidden shadow-sm">
        <div class="p-4 border-b border-outline flex justify-between items-center bg-surface-bright">
          <h3 class="text-lg font-bold text-on-surface">Active Deliveries</h3>
          <div class="flex items-center gap-2">
            <button class="px-3 py-1.5 bg-white border border-outline rounded-lg text-sm font-medium hover:bg-surface">All Routes</button>
          </div>
        </div>
        <div class="overflow-x-auto">
          <table class="w-full text-left border-collapse">
            <thead>
              <tr class="bg-surface font-label-md text-label-md text-on-surface-variant uppercase border-b border-outline">
                <th class="px-6 py-4 font-semibold">Shipment ID</th>
                <th class="px-6 py-4 font-semibold">Commodity</th>
                <th class="px-6 py-4 font-semibold">Route</th>
                <th class="px-6 py-4 font-semibold">Status</th>
                <th class="px-6 py-4 font-semibold">ETA / Delivery Date</th>
                <th class="px-6 py-4 font-semibold text-right">Action</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-outline" id="logistics-tbl-body">
              ${shipmentRows}
            </tbody>
          </table>
        </div>
      </div>
    </div>
    <!-- Right Panel: Map & Logistics Cost -->
    <div class="w-full lg:w-[320px] flex flex-col gap-xl">
      <!-- Route Map -->
      <div class="bg-white rounded-2xl border border-outline p-4 shadow-sm flex flex-col">
        <h3 class="font-headline-md text-headline-md text-on-surface mb-md font-bold">Route Map</h3>
        <div class="bg-surface-container-low border border-outline rounded-xl h-52 relative overflow-hidden flex items-center justify-center">
          <!-- Route Map SVG with visually sensible coordinates -->
          <svg class="w-full h-full" viewBox="0 0 240 200">
            <!-- Background Grid/Decoration -->
            <ellipse cx="115" cy="95" fill="#e8f5e9" rx="105" ry="75" opacity="0.6"/>
            <!-- Indore (Central Origin) -->
            <circle cx="120" cy="115" fill="#1b4332" r="8"/><text fill="#1b4332" font-size="10" font-weight="bold" text-anchor="middle" x="120" y="133">Indore</text>
            <!-- Delhi (North of Indore) -->
            <circle cx="130" cy="30" fill="#1b4332" r="8"/><text fill="#1b4332" font-size="10" font-weight="bold" text-anchor="middle" x="130" y="20">Delhi</text>
            <!-- Jaipur (Northwest of Indore) -->
            <circle cx="70" cy="60" fill="#4c6452" r="6"/><text fill="#4c6452" font-size="9" font-weight="bold" text-anchor="end" x="62" y="64">Jaipur</text>
            <!-- Nashik (Southwest of Indore) -->
            <circle cx="85" cy="140" fill="#4c6452" r="6"/><text fill="#4c6452" font-size="9" text-anchor="end" x="77" y="144">Nashik</text>
            <!-- Pune (South of Nashik/Indore) -->
            <circle cx="95" cy="165" fill="#4c6452" r="6"/><text fill="#4c6452" font-size="9" text-anchor="middle" x="95" y="177">Pune</text>
            <!-- Routes -->
            <line stroke="#1b4332" stroke-dasharray="6,3" stroke-width="2" x1="120" x2="130" y1="115" y2="30"/>
            <line stroke="#1b4332" stroke-dasharray="6,3" stroke-width="2" x1="120" x2="70" y1="115" y2="60"/>
            <line stroke="#4c6452" stroke-dasharray="4,3" stroke-width="1.5" x1="120" x2="85" y1="115" y2="140"/>
            <line stroke="#4c6452" stroke-dasharray="4,3" stroke-width="1.5" x1="120" x2="95" y1="115" y2="165"/>
            <!-- Trucks -->
            <circle cx="125" cy="72" fill="#ffb300" r="5"/><text fill="#e65100" font-size="8" font-weight="bold" text-anchor="start" x="133" y="75">FF-1024</text>
            <circle cx="95" cy="87" fill="#ffb300" r="5"/><text fill="#e65100" font-size="8" font-weight="bold" text-anchor="end" x="88" y="90">FF-1025</text>
          </svg>
        </div>
        <div class="mt-md flex flex-col gap-sm">
          <div class="flex items-center justify-between py-sm border-b border-outline-variant/50">
            <span class="font-body-sm text-on-surface-variant">FF-1024 · Indore → Delhi</span>
            <span class="font-label-md font-bold text-[#f57f17]">In Transit</span>
          </div>
          <div class="flex items-center justify-between py-sm">
            <span class="font-body-sm text-on-surface-variant">FF-1025 · Indore → Jaipur</span>
            <span class="font-label-md font-bold text-[#f57f17]">In Transit</span>
          </div>
        </div>
      </div>
      <!-- Cost Breakdown -->
      <div class="bg-surface border border-outline-variant rounded-xl p-md shadow-[0_2px_4px_rgba(0,0,0,0.05)] flex-1">
        <h3 class="font-headline-md text-headline-md text-on-surface mb-md font-bold">Cost Breakdown</h3>
        <div class="flex flex-col gap-sm">
          <div class="flex justify-between items-center py-sm border-b border-outline-variant/50"><span class="font-body-sm text-on-surface-variant">Road Transport</span><span class="font-body-sm font-bold text-on-surface">₹1,42,000</span></div>
          <div class="flex justify-between items-center py-sm border-b border-outline-variant/50"><span class="font-body-sm text-on-surface-variant">Loading / Unloading</span><span class="font-body-sm font-bold text-on-surface">₹48,500</span></div>
          <div class="flex justify-between items-center py-sm border-b border-outline-variant/50"><span class="font-body-sm text-on-surface-variant">Packaging</span><span class="font-body-sm font-bold text-on-surface">₹62,000</span></div>
          <div class="flex justify-between items-center py-sm"><span class="font-body-sm text-on-surface-variant">Insurance</span><span class="font-body-sm font-bold text-on-surface">₹32,000</span></div>
        </div>
      </div>
    </div>
  </div>
</div>`;
}
