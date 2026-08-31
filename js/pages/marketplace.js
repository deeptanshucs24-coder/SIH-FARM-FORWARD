export function render() {
  return `<div class="p-8 max-w-7xl mx-auto pb-24 md:pb-8">
  <div class="mb-6">
    <h2 class="text-3xl font-bold text-on-surface mb-2">Marketplace</h2>
    <p class="text-on-surface-variant text-base mb-6">Find the best prices and connect with verified buyers across India.</p>
    <div class="flex flex-wrap items-center gap-3">
      <button class="px-4 py-2 bg-white border border-outline rounded-xl text-on-surface font-medium hover:bg-surface flex items-center gap-2"><i class="fa-solid fa-filter text-on-surface-variant"></i>All Filters</button>
      <button class="px-4 py-2 bg-white border border-outline rounded-xl text-on-surface font-medium hover:bg-surface flex items-center gap-2">Crop: All <i class="fa-solid fa-chevron-down text-on-surface-variant text-xs"></i></button>
      <button class="px-4 py-2 bg-primary-light text-primary border border-primary/20 rounded-xl font-medium hover:bg-primary-light/80 flex items-center gap-2">Location: Near Me <i class="fa-solid fa-xmark ml-1"></i></button>
      <button class="px-4 py-2 bg-white border border-outline rounded-xl text-on-surface font-medium hover:bg-surface flex items-center gap-2 ml-auto">Sort: Highest Price <i class="fa-solid fa-chevron-down text-on-surface-variant text-xs"></i></button>
    </div>
  </div>
  <div class="grid grid-cols-1 xl:grid-cols-3 gap-6">
    <div class="xl:col-span-2 space-y-8">
      <!-- Best Prices Nearby -->
      <section>
        <h3 class="text-lg font-bold text-on-surface mb-4">Best Prices Nearby</h3>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
          <div class="bg-white p-5 rounded-2xl border border-outline hover:shadow-md transition-shadow cursor-pointer" onclick="navigate('marketplace/wheat')">
            <div class="flex justify-between items-start mb-4">
              <div class="w-10 h-10 rounded-xl bg-primary-light/50 flex items-center justify-center text-primary"><i class="fa-solid fa-wheat-awn"></i></div>
              <span class="inline-flex items-center px-2 py-1 rounded-md text-xs font-semibold bg-success-bg text-success"><i class="fa-solid fa-arrow-trend-up mr-1 text-[10px]"></i>+2.4%</span>
            </div>
            <h4 class="font-semibold text-on-surface mb-1">Wheat (Sharbati)</h4>
            <div class="flex items-baseline gap-1 mb-3"><span class="text-2xl font-bold text-on-surface">₹3,200</span><span class="text-sm text-on-surface-variant">/ Qt</span></div>
            <div class="text-xs text-on-surface-variant flex items-center gap-1.5"><i class="fa-solid fa-location-dot"></i>Delhi Mandi</div>
          </div>
          <div class="bg-white p-5 rounded-2xl border border-outline hover:shadow-md transition-shadow">
            <div class="flex justify-between items-start mb-4">
              <div class="w-10 h-10 rounded-xl bg-primary-light/50 flex items-center justify-center text-primary"><i class="fa-solid fa-seedling"></i></div>
              <span class="inline-flex items-center px-2 py-1 rounded-md text-xs font-semibold bg-danger-bg text-danger"><i class="fa-solid fa-arrow-trend-down mr-1 text-[10px]"></i>-1.2%</span>
            </div>
            <h4 class="font-semibold text-on-surface mb-1">Onion (Red)</h4>
            <div class="flex items-baseline gap-1 mb-3"><span class="text-2xl font-bold text-on-surface">₹1,850</span><span class="text-sm text-on-surface-variant">/ Qt</span></div>
            <div class="text-xs text-on-surface-variant flex items-center gap-1.5"><i class="fa-solid fa-location-dot"></i>Nashik Mandi</div>
          </div>
          <div class="bg-white p-5 rounded-2xl border border-outline hover:shadow-md transition-shadow">
            <div class="flex justify-between items-start mb-4">
              <div class="w-10 h-10 rounded-xl bg-primary-light/50 flex items-center justify-center text-primary"><i class="fa-solid fa-leaf"></i></div>
              <span class="inline-flex items-center px-2 py-1 rounded-md text-xs font-semibold bg-success-bg text-success"><i class="fa-solid fa-arrow-trend-up mr-1 text-[10px]"></i>+5.1%</span>
            </div>
            <h4 class="font-semibold text-on-surface mb-1">Tomato (Hybrid)</h4>
            <div class="flex items-baseline gap-1 mb-3"><span class="text-2xl font-bold text-on-surface">₹2,100</span><span class="text-sm text-on-surface-variant">/ Qt</span></div>
            <div class="text-xs text-on-surface-variant flex items-center gap-1.5"><i class="fa-solid fa-location-dot"></i>Pune Mandi</div>
          </div>
        </div>
      </section>
      <!-- Active Buy Leads -->
      <section>
        <h3 class="text-lg font-bold text-on-surface mb-4">Active Buy Leads</h3>
        <div class="bg-white rounded-2xl border border-outline overflow-hidden">
          <table class="w-full text-left border-collapse">
            <thead>
              <tr class="bg-surface/50 border-b border-outline text-xs uppercase tracking-wider text-on-surface-variant">
                <th class="px-6 py-4 font-medium">Buyer</th>
                <th class="px-6 py-4 font-medium">Requirement</th>
                <th class="px-6 py-4 font-medium">Location</th>
                <th class="px-6 py-4 font-medium">Target Price</th>
                <th class="px-6 py-4 font-medium text-right">Action</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-outline">
              <tr class="hover:bg-surface/30 transition-colors">
                <td class="px-6 py-4"><div class="flex items-center gap-3"><div class="w-8 h-8 rounded-lg bg-primary text-white flex items-center justify-center font-bold text-xs">AL</div><div><div class="font-semibold text-on-surface">AgriCorp Ltd</div><div class="text-xs text-on-surface-variant flex items-center gap-1 mt-0.5"><i class="fa-solid fa-circle-check text-success text-[10px]"></i>Verified Buyer</div></div></div></td>
                <td class="px-6 py-4 text-sm"><div class="text-on-surface font-medium">Soybean • 500 MT</div></td>
                <td class="px-6 py-4 text-sm text-on-surface-variant">Indore, MP</td>
                <td class="px-6 py-4 text-sm font-semibold text-on-surface">₹4,850 <span class="font-normal text-on-surface-variant text-xs">/ Qt</span></td>
                <td class="px-6 py-4 text-right"><button class="px-4 py-1.5 bg-primary-light text-primary font-medium rounded-lg hover:bg-primary-light/80 transition-colors text-sm" onclick="navigate('marketplace/buyer')">Negotiate</button></td>
              </tr>
              <tr class="hover:bg-surface/30 transition-colors">
                <td class="px-6 py-4"><div class="flex items-center gap-3"><div class="w-8 h-8 rounded-lg bg-primary/20 text-primary flex items-center justify-center font-bold text-xs">HF</div><div><div class="font-semibold text-on-surface">Heritage Foods</div><div class="text-xs text-on-surface-variant flex items-center gap-1 mt-0.5"><i class="fa-solid fa-circle-check text-success text-[10px]"></i>Verified Buyer</div></div></div></td>
                <td class="px-6 py-4 text-sm"><div class="text-on-surface font-medium">Maize • 200 MT</div></td>
                <td class="px-6 py-4 text-sm text-on-surface-variant">Jaipur, RJ</td>
                <td class="px-6 py-4 text-sm font-semibold text-on-surface">₹2,250 <span class="font-normal text-on-surface-variant text-xs">/ Qt</span></td>
                <td class="px-6 py-4 text-right"><button class="px-4 py-1.5 bg-primary-light text-primary font-medium rounded-lg hover:bg-primary-light/80 transition-colors text-sm" onclick="navigate('marketplace/buyer')">Negotiate</button></td>
              </tr>
              <tr class="hover:bg-surface/30 transition-colors">
                <td class="px-6 py-4"><div class="flex items-center gap-3"><div class="w-8 h-8 rounded-lg bg-primary text-white flex items-center justify-center font-bold text-xs">GM</div><div><div class="font-semibold text-on-surface">GreenLeaf Mills</div><div class="text-xs text-on-surface-variant mt-0.5">Standard Buyer</div></div></div></td>
                <td class="px-6 py-4 text-sm"><div class="text-on-surface font-medium">Cotton • 150 Bales</div></td>
                <td class="px-6 py-4 text-sm text-on-surface-variant">Ahmedabad, GJ</td>
                <td class="px-6 py-4 text-sm font-semibold text-on-surface">₹7,100 <span class="font-normal text-on-surface-variant text-xs">/ Qt</span></td>
                <td class="px-6 py-4 text-right"><button class="px-4 py-1.5 bg-primary-light text-primary font-medium rounded-lg hover:bg-primary-light/80 transition-colors text-sm" onclick="navigate('marketplace/buyer')">Negotiate</button></td>
              </tr>
            </tbody>
          </table>
        </div>
      </section>
    </div>
    <!-- Right Column -->
    <div class="space-y-6">
      <div class="bg-primary rounded-2xl p-6 text-white relative overflow-hidden" style="background:#1b4332">
        <div class="relative z-10">
          <div class="flex items-center gap-2 text-green-200 text-xs font-bold uppercase tracking-wider mb-3"><i class="fa-solid fa-bullhorn"></i>Opportunity Alert</div>
          <h4 class="text-xl font-bold mb-3 leading-tight">High Demand: Wheat in Delhi Mandi</h4>
          <p class="text-white/80 text-sm mb-6 leading-relaxed">Current prices are above the recent average and buyers are actively sourcing larger quantities.</p>
          <button class="w-full py-3 bg-primary-light text-primary font-bold rounded-xl hover:bg-white transition-colors shadow-sm" style="color:#1b4332" onclick="navigate('marketplace/listings/new')">List Produce</button>
        </div>
      </div>
      <div class="bg-white rounded-2xl border border-outline p-6">
        <div class="flex items-center justify-between mb-5">
          <h3 class="text-lg font-bold text-on-surface">Trending Upwards</h3>
          <a class="text-sm font-medium text-primary hover:underline" href="#/marketplace">View All</a>
        </div>
        <div class="space-y-4">
          <div class="flex items-center justify-between p-2 -mx-2 rounded-xl hover:bg-surface transition-colors">
            <div class="flex items-center gap-3"><div class="w-10 h-10 rounded-xl bg-primary-light/50 flex items-center justify-center text-primary"><i class="fa-solid fa-cloud"></i></div><div><div class="font-semibold text-on-surface">Cotton</div><div class="text-xs text-on-surface-variant">High Export Demand</div></div></div>
            <div class="text-right"><div class="font-bold text-on-surface">₹7,250</div><div class="text-xs font-semibold text-success flex items-center justify-end gap-1"><i class="fa-solid fa-arrow-up text-[10px]"></i>8.0%</div></div>
          </div>
          <div class="flex items-center justify-between p-2 -mx-2 rounded-xl hover:bg-surface transition-colors">
            <div class="flex items-center gap-3"><div class="w-10 h-10 rounded-xl bg-primary-light/50 flex items-center justify-center text-primary"><i class="fa-solid fa-seedling"></i></div><div><div class="font-semibold text-on-surface">Soybean</div><div class="text-xs text-on-surface-variant">Oil Extraction Surge</div></div></div>
            <div class="text-right"><div class="font-bold text-on-surface">₹4,900</div><div class="text-xs font-semibold text-success flex items-center justify-end gap-1"><i class="fa-solid fa-arrow-up text-[10px]"></i>4.5%</div></div>
          </div>
          <div class="flex items-center justify-between p-2 -mx-2 rounded-xl hover:bg-surface transition-colors">
            <div class="flex items-center gap-3"><div class="w-10 h-10 rounded-xl bg-primary-light/50 flex items-center justify-center text-primary"><i class="fa-solid fa-droplet"></i></div><div><div class="font-semibold text-on-surface">Mustard Seed</div><div class="text-xs text-on-surface-variant">Seasonal Shift</div></div></div>
            <div class="text-right"><div class="font-bold text-on-surface">₹5,400</div><div class="text-xs font-semibold text-success flex items-center justify-end gap-1"><i class="fa-solid fa-arrow-up text-[10px]"></i>3.2%</div></div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
`;
}

