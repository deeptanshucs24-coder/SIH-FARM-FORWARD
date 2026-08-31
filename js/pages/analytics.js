export function render() {
  return `<div class="p-margin max-w-7xl mx-auto pb-24 md:pb-margin">
  <div class="mb-xl">
    <h1 class="font-headline-xl text-headline-xl text-on-surface mb-sm">Analytics</h1>
    <p class="font-body-lg text-body-lg text-on-surface-variant">Understand your farm performance, market trends and selling opportunities.</p>
  </div>
  <!-- KPI Cards -->
  <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-gutter mb-xl">
    <div class="bg-surface-container-lowest border border-outline-variant rounded-[12px] p-md flex flex-col gap-sm shadow-[0_2px_4px_rgba(0,0,0,0.05)]"><span class="font-label-md text-label-md text-on-surface-variant uppercase">Total Yield</span><div class="flex items-end justify-between"><span class="font-headline-lg text-headline-lg text-on-surface">1,840 Qt</span><div class="flex items-center gap-xs text-primary bg-secondary-container px-2 py-1 rounded-sm font-label-md"><span class="material-symbols-outlined text-[16px]">arrow_upward</span><span>8.6%</span></div></div><span class="font-body-sm text-body-sm text-on-surface-variant">vs last season</span></div>
    <div class="bg-surface-container-lowest border border-outline-variant rounded-[12px] p-md flex flex-col gap-sm shadow-[0_2px_4px_rgba(0,0,0,0.05)]"><span class="font-label-md text-label-md text-on-surface-variant uppercase">Avg Selling Price</span><div class="flex items-end justify-between"><span class="font-headline-lg text-headline-lg text-on-surface">â‚¹3,420 / Qt</span><div class="flex items-center gap-xs text-primary bg-secondary-container px-2 py-1 rounded-sm font-label-md"><span class="material-symbols-outlined text-[16px]">arrow_upward</span><span>11.2%</span></div></div><span class="font-body-sm text-body-sm text-on-surface-variant">vs last season</span></div>
    <div class="bg-surface-container-lowest border border-outline-variant rounded-[12px] p-md flex flex-col gap-sm shadow-[0_2px_4px_rgba(0,0,0,0.05)]"><span class="font-label-md text-label-md text-on-surface-variant uppercase">Net Profit</span><div class="flex items-end justify-between"><span class="font-headline-lg text-headline-lg text-on-surface">â‚¹15,77,500</span><div class="flex items-center gap-xs text-primary bg-secondary-container px-2 py-1 rounded-sm font-label-md"><span class="material-symbols-outlined text-[16px]">arrow_upward</span><span>18.1%</span></div></div><span class="font-body-sm text-body-sm text-on-surface-variant">vs last season</span></div>
    <div class="bg-surface-container-lowest border border-outline-variant rounded-[12px] p-md flex flex-col gap-sm shadow-[0_2px_4px_rgba(0,0,0,0.05)]"><span class="font-label-md text-label-md text-on-surface-variant uppercase">Best Performing Crop</span><div class="flex items-end justify-between"><span class="font-headline-lg text-headline-lg text-on-surface">Wheat</span></div><span class="font-body-sm text-body-sm text-primary font-medium">â‚¹7,85,000 profit</span></div>
  </div>
  <!-- Bento Grid -->
  <div class="grid grid-cols-1 lg:grid-cols-3 gap-gutter mb-xl">
    <!-- Crop Performance Chart -->
    <div class="lg:col-span-2 bg-surface-container-lowest border border-outline-variant rounded-[12px] p-lg shadow-[0_2px_4px_rgba(0,0,0,0.05)] flex flex-col">
      <div class="flex items-center justify-between mb-md">
        <h2 class="font-headline-md text-headline-md text-on-surface">Crop Performance (Qt &amp; â‚¹ Lakhs)</h2>
        <div class="flex gap-md font-label-md text-label-md">
          <div class="flex items-center gap-xs"><div class="w-3 h-3 bg-secondary-fixed"></div>Yield</div>
          <div class="flex items-center gap-xs"><div class="w-3 h-3 bg-tertiary-container"></div>Revenue</div>
          <div class="flex items-center gap-xs"><div class="w-3 h-3 bg-primary-container"></div>Profit</div>
        </div>
      </div>
      <div class="relative w-full flex justify-around items-end h-[260px] pt-xl">
        <div class="absolute inset-0 flex flex-col justify-between pointer-events-none pb-8">
          <div class="border-b border-outline-variant border-dashed w-full flex-1"></div>
          <div class="border-b border-outline-variant border-dashed w-full flex-1"></div>
          <div class="border-b border-outline-variant border-dashed w-full flex-1"></div>
          <div class="border-b border-outline-variant border-dashed w-full flex-1"></div>
          <div class="border-b border-outline-variant border-solid w-full"></div>
        </div>
        <!-- Wheat -->
        <div class="flex flex-col items-center gap-2 w-1/4 z-10">
          <div class="flex items-end gap-1 w-full justify-center" style="height:200px">
            <div class="w-6 bg-secondary-fixed rounded-t-sm" style="height:100%" title="Yield 620 Qt"></div>
            <div class="w-6 bg-tertiary-container rounded-t-sm" style="height:80%" title="Revenue â‚¹6.8L"></div>
            <div class="w-6 bg-primary-container rounded-t-sm" style="height:60%" title="Profit â‚¹4.1L"></div>
          </div>
          <span class="font-label-md text-label-md text-on-surface">Wheat</span>
        </div>
        <!-- Soybean -->
        <div class="flex flex-col items-center gap-2 w-1/4 z-10">
          <div class="flex items-end gap-1 w-full justify-center" style="height:200px">
            <div class="w-6 bg-secondary-fixed rounded-t-sm" style="height:77%"></div>
            <div class="w-6 bg-tertiary-container rounded-t-sm" style="height:65%"></div>
            <div class="w-6 bg-primary-container rounded-t-sm" style="height:45%"></div>
          </div>
          <span class="font-label-md text-label-md text-on-surface">Soybean</span>
        </div>
        <!-- Onion -->
        <div class="flex flex-col items-center gap-2 w-1/4 z-10">
          <div class="flex items-end gap-1 w-full justify-center" style="height:200px">
            <div class="w-6 bg-secondary-fixed rounded-t-sm" style="height:62%"></div>
            <div class="w-6 bg-tertiary-container rounded-t-sm" style="height:50%"></div>
            <div class="w-6 bg-primary-container rounded-t-sm" style="height:35%"></div>
          </div>
          <span class="font-label-md text-label-md text-on-surface">Onion</span>
        </div>
        <!-- Tomato -->
        <div class="flex flex-col items-center gap-2 w-1/4 z-10">
          <div class="flex items-end gap-1 w-full justify-center" style="height:200px">
            <div class="w-6 bg-secondary-fixed rounded-t-sm" style="height:56%"></div>
            <div class="w-6 bg-tertiary-container rounded-t-sm" style="height:45%"></div>
            <div class="w-6 bg-primary-container rounded-t-sm" style="height:30%"></div>
          </div>
          <span class="font-label-md text-label-md text-on-surface">Tomato</span>
        </div>
      </div>
    </div>
    <!-- AI Insight + Farm Performance -->
    <div class="flex flex-col gap-gutter">
      <div class="bg-primary-container text-on-primary-container p-lg rounded-[12px] flex flex-col gap-md shadow-[0_2px_4px_rgba(0,0,0,0.05)] relative overflow-hidden">
        <div class="absolute -right-10 -top-10 text-tertiary-container opacity-20 pointer-events-none"><span class="material-symbols-outlined text-[120px]">smart_toy</span></div>
        <div class="flex items-center gap-sm relative z-10"><span class="material-symbols-outlined text-secondary-fixed">tips_and_updates</span><h3 class="font-headline-md text-headline-md font-bold text-on-primary">AI Market Insight</h3></div>
        <p class="font-body-md text-body-md text-on-primary-container relative z-10 leading-relaxed">"Wheat prices are trending upward across Delhi and Indore mandis. Selling within the next 5â€“7 days may improve expected returns."</p>
        <button class="bg-secondary-fixed text-primary font-label-md text-label-md py-sm px-md rounded-md hover:bg-secondary-fixed-dim transition-colors w-fit mt-sm relative z-10 font-bold uppercase tracking-wider" onclick="navigate('marketplace/wheat')">View Recommendation</button>
      </div>
      <div class="bg-surface-container-lowest border border-outline-variant rounded-[12px] p-lg flex-1 flex flex-col gap-md shadow-[0_2px_4px_rgba(0,0,0,0.05)]">
        <h3 class="font-headline-md text-headline-md text-on-surface">Farm Performance</h3>
        <div class="flex flex-col gap-sm"><div class="flex justify-between font-body-sm text-on-surface-variant"><span>Yield Efficiency</span><span class="font-medium text-on-surface">92%</span></div><div class="w-full bg-surface-container-high rounded-full h-2"><div class="bg-primary-container h-2 rounded-full" style="width:92%"></div></div></div>
        <div class="flex flex-col gap-sm"><div class="flex justify-between font-body-sm text-on-surface-variant"><span>Revenue Growth</span><span class="font-medium text-primary">+12.4%</span></div><div class="w-full bg-surface-container-high rounded-full h-2"><div class="bg-tertiary-container h-2 rounded-full" style="width:75%"></div></div></div>
        <div class="flex flex-col gap-sm"><div class="flex justify-between font-body-sm text-on-surface-variant"><span>Profit Margin</span><span class="font-medium text-on-surface">64.4%</span></div><div class="w-full bg-surface-container-high rounded-full h-2"><div class="bg-primary-container h-2 rounded-full" style="width:64.4%"></div></div></div>
        <div class="flex flex-col gap-sm"><div class="flex justify-between font-body-sm text-on-surface-variant"><span>On-Time Deliveries</span><span class="font-medium text-on-surface">94.2%</span></div><div class="w-full bg-surface-container-high rounded-full h-2"><div class="bg-secondary h-2 rounded-full" style="width:94.2%"></div></div></div>
      </div>
    </div>
  </div>
  <!-- Bottom Row -->
  <div class="grid grid-cols-1 lg:grid-cols-2 gap-gutter">
    <!-- Market Price Trends SVG -->
    <div class="bg-surface-container-lowest border border-outline-variant rounded-[12px] p-lg shadow-[0_2px_4px_rgba(0,0,0,0.05)] flex flex-col">
      <div class="flex items-center justify-between mb-md">
        <h2 class="font-headline-md text-headline-md text-on-surface">Market Price Trends (Jan â€“ Jun)</h2>
        <div class="flex gap-md font-label-md text-label-md">
          <div class="flex items-center gap-xs"><div class="w-3 h-1 bg-primary-container rounded-sm"></div>Wheat</div>
          <div class="flex items-center gap-xs"><div class="w-3 h-1 bg-tertiary-container rounded-sm"></div>Soybean</div>
          <div class="flex items-center gap-xs"><div class="w-3 h-1 bg-secondary rounded-sm"></div>Onion</div>
        </div>
      </div>
      <div class="relative w-full h-[200px]">
        <div class="absolute bottom-6 w-full flex justify-between px-2 font-label-md text-[10px] text-on-surface-variant"><span>Jan</span><span>Feb</span><span>Mar</span><span>Apr</span><span>May</span><span>Jun</span></div>
        <svg class="absolute inset-0 w-full pb-6" style="height:100%" preserveAspectRatio="none" viewBox="0 0 100 90">
          <line stroke="#e0e3e8" stroke-width="0.5" x1="0" x2="100" y1="20" y2="20"/>
          <line stroke="#e0e3e8" stroke-width="0.5" x1="0" x2="100" y1="40" y2="40"/>
          <line stroke="#e0e3e8" stroke-width="0.5" x1="0" x2="100" y1="60" y2="60"/>
          <polyline fill="none" points="0,60 20,58 40,55 60,50 80,45 100,40" stroke="#1b4332" stroke-width="1.5" vector-effect="non-scaling-stroke"/>
          <polyline fill="none" points="0,20 20,18 40,15 60,10 80,5 100,2" stroke="#00452e" stroke-width="1.5" vector-effect="non-scaling-stroke"/>
          <polyline fill="none" points="0,75 20,74 40,70 60,66 80,64 100,58" stroke="#4c6452" stroke-width="1.5" vector-effect="non-scaling-stroke"/>
          <circle cx="0" cy="60" fill="#1b4332" r="1.5"/><circle cx="20" cy="58" fill="#1b4332" r="1.5"/><circle cx="40" cy="55" fill="#1b4332" r="1.5"/><circle cx="60" cy="50" fill="#1b4332" r="1.5"/><circle cx="80" cy="45" fill="#1b4332" r="1.5"/><circle cx="100" cy="40" fill="#1b4332" r="1.5"/>
          <circle cx="0" cy="20" fill="#00452e" r="1.5"/><circle cx="20" cy="18" fill="#00452e" r="1.5"/><circle cx="40" cy="15" fill="#00452e" r="1.5"/><circle cx="60" cy="10" fill="#00452e" r="1.5"/><circle cx="80" cy="5" fill="#00452e" r="1.5"/><circle cx="100" cy="2" fill="#00452e" r="1.5"/>
          <circle cx="0" cy="75" fill="#4c6452" r="1.5"/><circle cx="20" cy="74" fill="#4c6452" r="1.5"/><circle cx="40" cy="70" fill="#4c6452" r="1.5"/><circle cx="60" cy="66" fill="#4c6452" r="1.5"/><circle cx="80" cy="64" fill="#4c6452" r="1.5"/><circle cx="100" cy="58" fill="#4c6452" r="1.5"/>
        </svg>
      </div>
    </div>
    <!-- Recent Insights -->
    <div class="bg-surface-container-lowest border border-outline-variant rounded-[12px] p-lg shadow-[0_2px_4px_rgba(0,0,0,0.05)] flex flex-col">
      <h2 class="font-headline-md text-headline-md text-on-surface mb-md">Recent Insights</h2>
      <div class="flex flex-col gap-sm">
        <div class="flex items-start gap-md p-md bg-surface border border-outline-variant rounded-lg"><div class="bg-error-container text-on-error-container p-sm rounded-full flex shrink-0"><span class="material-symbols-outlined text-[20px]">water_drop</span></div><div class="flex flex-col gap-xs"><span class="font-label-md text-label-md text-on-surface font-bold uppercase">Irrigation Alert</span><p class="font-body-sm text-body-sm text-on-surface-variant">Soil moisture levels in Sector B dropping below optimal.</p></div></div>
        <div class="flex items-start gap-md p-md bg-surface border border-outline-variant rounded-lg"><div class="bg-secondary-fixed text-on-secondary-fixed p-sm rounded-full flex shrink-0"><span class="material-symbols-outlined text-[20px]">eco</span></div><div class="flex flex-col gap-xs"><span class="font-label-md text-label-md text-on-surface font-bold uppercase">Fertilizer Efficiency</span><p class="font-body-sm text-body-sm text-on-surface-variant">New organic mix increased yield density by 4% over last cycle.</p></div></div>
        <div class="flex items-start gap-md p-md bg-surface border border-outline-variant rounded-lg"><div class="bg-tertiary-fixed text-on-tertiary-fixed p-sm rounded-full flex shrink-0"><span class="material-symbols-outlined text-[20px]">trending_up</span></div><div class="flex flex-col gap-xs"><span class="font-label-md text-label-md text-on-surface font-bold uppercase">Soybean Demand</span><p class="font-body-sm text-body-sm text-on-surface-variant">Increased demand in Indore mandi for export.</p></div></div>
        <div class="flex items-start gap-md p-md bg-surface border border-outline-variant rounded-lg"><div class="bg-primary-fixed text-on-primary-fixed p-sm rounded-full flex shrink-0"><span class="material-symbols-outlined text-[20px]">insights</span></div><div class="flex flex-col gap-xs"><span class="font-label-md text-label-md text-on-surface font-bold uppercase">Wheat Price Increase</span><p class="font-body-sm text-body-sm text-on-surface-variant">Mandi prices surged 4% this week.</p></div></div>
      </div>
    </div>
  </div>
</div>
`;
}

