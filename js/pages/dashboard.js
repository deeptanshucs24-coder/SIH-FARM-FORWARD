export function render() {
  return `<div class="p-margin max-w-7xl mx-auto pb-24 md:pb-margin">
  <header class="mb-xl">
    <h1 class="font-headline-lg text-headline-lg text-primary">Dashboard</h1>
    <p class="font-body-md text-body-md text-on-surface-variant mt-xs">Welcome back, Rajesh. Here is your farm's overview.</p>
  </header>
  <!-- KPIs -->
  <div class="grid grid-cols-1 md:grid-cols-3 gap-lg mb-lg">
    <div class="bg-surface-container-lowest border border-outline-variant rounded-xl p-md flex flex-col gap-sm shadow-sm">
      <div class="flex items-center justify-between">
        <span class="font-label-md text-label-md text-on-surface-variant uppercase tracking-wider">Total Yield Value</span>
        <span class="material-symbols-outlined text-surface-tint">account_balance_wallet</span>
      </div>
      <div class="font-headline-xl text-headline-xl text-primary font-bold">₹24,50,000</div>
      <div class="font-body-sm text-body-sm text-surface-tint flex items-center gap-xs font-semibold">
        <span class="material-symbols-outlined text-[16px]">trending_up</span>+12% vs last month
      </div>
    </div>
    <div class="bg-surface-container-lowest border border-outline-variant rounded-xl p-md flex flex-col gap-sm shadow-sm">
      <div class="flex items-center justify-between">
        <span class="font-label-md text-label-md text-on-surface-variant uppercase tracking-wider">Active Contracts</span>
        <span class="material-symbols-outlined text-surface-tint">description</span>
      </div>
      <div class="font-headline-xl text-headline-xl text-primary font-bold">18</div>
      <div class="font-body-sm text-body-sm text-on-surface-variant">4 pending signature</div>
    </div>
    <div class="bg-surface-container-lowest border border-outline-variant rounded-xl p-md flex flex-col gap-sm shadow-sm">
      <div class="flex items-center justify-between">
        <span class="font-label-md text-label-md text-on-surface-variant uppercase tracking-wider">Pending Logistics</span>
        <span class="material-symbols-outlined text-surface-tint">local_shipping</span>
      </div>
      <div class="font-headline-xl text-headline-xl text-primary font-bold">5</div>
      <div class="font-body-sm text-body-sm text-on-surface-variant">Shipments scheduled</div>
    </div>
  </div>
  <!-- Chart + Right Rail -->
  <div class="grid grid-cols-1 lg:grid-cols-3 gap-lg">
    <div class="lg:col-span-2 flex flex-col gap-lg">
      <!-- Yield Chart SVG -->
      <div class="bg-surface-container-lowest border border-outline-variant rounded-xl p-md flex flex-col gap-md shadow-sm">
        <div class="flex items-center justify-between">
          <h3 class="font-headline-md text-headline-md text-primary font-bold">Yield Projection vs Actuals</h3>
          <div class="flex items-center gap-3 text-xs">
            <div class="flex items-center gap-1"><div class="w-3 h-3 bg-primary-fixed rounded-sm"></div><span class="text-on-surface-variant">Projected</span></div>
            <div class="flex items-center gap-1"><div class="w-3 h-3 bg-primary-container rounded-sm"></div><span class="text-on-surface-variant">Actual</span></div>
          </div>
        </div>
        <div class="w-full h-[280px]">
          <svg class="w-full h-full" preserveAspectRatio="none" viewBox="0 0 600 280">
            <line stroke="#e0e3e8" stroke-width="1" x1="40" x2="580" y1="240" y2="240"/>
            <line stroke="#e0e3e8" stroke-width="1" x1="40" x2="580" y1="190" y2="190"/>
            <line stroke="#e0e3e8" stroke-width="1" x1="40" x2="580" y1="140" y2="140"/>
            <line stroke="#e0e3e8" stroke-width="1" x1="40" x2="580" y1="90" y2="90"/>
            <line stroke="#e0e3e8" stroke-width="1" x1="40" x2="580" y1="40" y2="40"/>
            <text fill="#717973" font-size="11" text-anchor="end" x="35" y="244">0</text>
            <text fill="#717973" font-size="11" text-anchor="end" x="35" y="194">10</text>
            <text fill="#717973" font-size="11" text-anchor="end" x="35" y="144">20</text>
            <text fill="#717973" font-size="11" text-anchor="end" x="35" y="94">30</text>
            <text fill="#717973" font-size="11" text-anchor="end" x="35" y="44">40 Qt</text>
            <text fill="#717973" font-size="11" text-anchor="middle" x="100" y="262">Apr</text>
            <text fill="#717973" font-size="11" text-anchor="middle" x="210" y="262">May</text>
            <text fill="#717973" font-size="11" text-anchor="middle" x="320" y="262">Jun</text>
            <text fill="#717973" font-size="11" text-anchor="middle" x="430" y="262">Jul</text>
            <text fill="#717973" font-size="11" text-anchor="middle" x="540" y="262">Aug</text>
            <rect fill="#c1ecd4" height="108" rx="2" width="20" x="82" y="132"/>
            <rect fill="#c1ecd4" height="126" rx="2" width="20" x="192" y="114"/>
            <rect fill="#c1ecd4" height="144" rx="2" width="20" x="302" y="96"/>
            <rect fill="#c1ecd4" height="162" rx="2" width="20" x="412" y="78"/>
            <rect fill="#c1ecd4" height="180" rx="2" width="20" x="522" y="60"/>
            <rect fill="#1b4332" height="102" rx="2" width="20" x="106" y="138"/>
            <rect fill="#1b4332" height="132" rx="2" width="20" x="216" y="108"/>
            <rect fill="#1b4332" height="138" rx="2" width="20" x="326" y="102"/>
            <rect fill="#1b4332" height="168" rx="2" width="20" x="436" y="72"/>
            <rect fill="#1b4332" height="186" rx="2" width="20" x="546" y="54"/>
          </svg>
        </div>
      </div>
      <!-- Recent Sales -->
      <div class="bg-surface-container-lowest border border-outline-variant rounded-xl p-md flex flex-col gap-md shadow-sm">
        <div class="flex items-center justify-between">
          <h3 class="font-headline-md text-headline-md text-primary font-bold">Recent Sales</h3>
          <a class="font-label-md text-label-md text-surface-tint hover:underline" href="#/marketplace">View All</a>
        </div>
        <div class="overflow-x-auto">
          <table class="w-full text-left border-collapse">
            <thead>
              <tr class="border-b border-outline-variant/50">
                <th class="py-2 px-2 font-label-md text-on-surface-variant font-semibold">Crop</th>
                <th class="py-2 px-2 font-label-md text-on-surface-variant font-semibold">Mandi</th>
                <th class="py-2 px-2 font-label-md text-on-surface-variant font-semibold">Quantity</th>
                <th class="py-2 px-2 font-label-md text-on-surface-variant font-semibold text-right">Amount</th>
                <th class="py-2 px-2 font-label-md text-on-surface-variant font-semibold text-right">Status</th>
              </tr>
            </thead>
            <tbody>
              <tr class="border-b border-outline-variant/50 hover:bg-surface-container-low transition-colors">
                <td class="py-3 px-2 font-body-sm font-semibold text-on-surface">Wheat (Sharbati)</td>
                <td class="py-3 px-2 font-body-sm text-on-surface-variant">Delhi Mandi</td>
                <td class="py-3 px-2 font-body-sm text-on-surface-variant">500 Qt</td>
                <td class="py-3 px-2 font-body-sm font-bold text-primary text-right">₹16,00,000</td>
                <td class="py-3 px-2 text-right"><span class="inline-flex px-2 py-1 rounded-full text-xs font-semibold bg-secondary-container text-on-secondary-container">Completed</span></td>
              </tr>
              <tr class="border-b border-outline-variant/50 hover:bg-surface-container-low transition-colors">
                <td class="py-3 px-2 font-body-sm font-semibold text-on-surface">Tomato (Hybrid)</td>
                <td class="py-3 px-2 font-body-sm text-on-surface-variant">Pune Mandi</td>
                <td class="py-3 px-2 font-body-sm text-on-surface-variant">120 Qt</td>
                <td class="py-3 px-2 font-body-sm font-bold text-primary text-right">₹2,52,000</td>
                <td class="py-3 px-2 text-right"><span class="inline-flex px-2 py-1 rounded-full text-xs font-semibold bg-surface-variant text-on-surface-variant">In Transit</span></td>
              </tr>
              <tr class="hover:bg-surface-container-low transition-colors">
                <td class="py-3 px-2 font-body-sm font-semibold text-on-surface">Soybean</td>
                <td class="py-3 px-2 font-body-sm text-on-surface-variant">Indore Mandi</td>
                <td class="py-3 px-2 font-body-sm text-on-surface-variant">300 Qt</td>
                <td class="py-3 px-2 font-body-sm font-bold text-primary text-right">₹14,55,000</td>
                <td class="py-3 px-2 text-right"><span class="inline-flex px-2 py-1 rounded-full text-xs font-semibold bg-surface-variant text-on-surface-variant">Pending</span></td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
    <!-- Right Rail -->
    <div class="flex flex-col gap-lg">
      <div class="bg-primary-container text-on-primary-container border border-primary-fixed/20 rounded-xl p-md flex flex-col gap-md shadow-sm">
        <div class="flex items-center gap-sm">
          <span class="material-symbols-outlined text-primary-fixed">lightbulb</span>
          <h3 class="font-headline-md text-headline-md font-bold text-primary-fixed">Recommendation</h3>
        </div>
        <p class="font-body-md text-body-md text-primary-fixed-dim">Sell <strong class="text-primary-fixed">Wheat</strong> now in Delhi for peak price. Expected upside ₹120–150/Qt.</p>
        <button class="mt-xs bg-primary-fixed text-on-primary-fixed font-label-md text-label-md py-sm px-md rounded-lg self-start hover:bg-primary-fixed-dim transition-colors" onclick="navigate('marketplace')">Take Action</button>
      </div>
      <div class="bg-surface-container-lowest border border-outline-variant rounded-xl p-md flex flex-col gap-md shadow-sm flex-1">
        <div class="flex items-center justify-between">
          <h3 class="font-headline-md text-headline-md text-primary font-bold">Market Prices</h3>
          <a class="font-label-md text-label-md text-surface-tint hover:underline" href="#/marketplace">View All</a>
        </div>
        <div class="flex flex-col">
          <div class="flex justify-between items-center py-md border-b border-outline-variant/50">
            <div>
              <div class="font-body-md font-semibold text-on-surface">Wheat (Qt)</div>
              <div class="font-label-md text-label-md text-on-surface-variant mt-xs">Delhi Mandi</div>
            </div>
            <div>
              <div class="font-body-md font-bold text-primary text-right">₹3,200</div>
              <div class="text-xs font-semibold text-green-600 text-right">↑ 2.4%</div>
            </div>
          </div>
          <div class="flex justify-between items-center py-md border-b border-outline-variant/50">
            <div>
              <div class="font-body-md font-semibold text-on-surface">Onion (Qt)</div>
              <div class="font-label-md text-label-md text-on-surface-variant mt-xs">Nashik Mandi</div>
            </div>
            <div>
              <div class="font-body-md font-bold text-primary text-right">₹1,850</div>
              <div class="text-xs font-semibold text-red-500 text-right">↓ 1.2%</div>
            </div>
          </div>
          <div class="flex justify-between items-center py-md">
            <div>
              <div class="font-body-md font-semibold text-on-surface">Tomato (Qt)</div>
              <div class="font-label-md text-label-md text-on-surface-variant mt-xs">Pune Mandi</div>
            </div>
            <div>
              <div class="font-body-md font-bold text-primary text-right">₹2,100</div>
              <div class="text-xs font-semibold text-green-600 text-right">↑ 5.1%</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
`;
}

