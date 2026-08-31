export function render() {
  return `<div class="p-6 max-w-7xl mx-auto pb-24 md:pb-6">
  <div class="mb-6">
    <a class="text-primary hover:underline text-sm font-medium flex items-center mb-2 cursor-pointer" onclick="navigate('marketplace')">
      <svg class="w-4 h-4 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path d="M10 19l-7-7m0 0l7-7m-7 7h18" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"/></svg>Back to Marketplace
    </a>
    <h2 class="text-3xl font-bold text-on-surface">Wheat â€” Price Analysis</h2>
    <p class="text-on-surface-variant mt-1">Track mandi prices, historical trends, and the best time to sell.</p>
  </div>
  <!-- Metric Cards -->
  <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 mb-6">
    <div class="bg-white rounded-lg border border-outline p-4"><div class="flex items-start"><div class="bg-primary-light/50 p-2 rounded-md mr-3"><svg class="w-6 h-6 text-primary" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path d="M5 3v4M3 5h4M6 17v4m-2-2h4m5-16l2.286 6.857L21 12l-5.714 2.143L13 21l-2.286-6.857L5 12l5.714-2.143L13 3z" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"/></svg></div><div><p class="text-sm font-medium text-on-surface-variant">Current Best Price</p><div class="flex items-baseline mt-1"><span class="text-2xl font-bold text-on-surface">â‚¹3,200</span><span class="text-sm text-on-surface-variant ml-1">/ Qt</span></div><p class="text-sm text-on-surface-variant">Delhi Mandi</p></div></div><div class="mt-4"><span class="inline-flex items-center px-2 py-0.5 rounded text-xs font-medium bg-success-bg text-success"><svg class="mr-1 h-3 w-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"/></svg>2.4% today</span></div></div>
    <div class="bg-white rounded-lg border border-outline p-4"><div class="flex items-start"><div class="bg-primary-light/50 p-2 rounded-md mr-3"><svg class="w-6 h-6 text-primary" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"/></svg></div><div><p class="text-sm font-medium text-on-surface-variant">7-Day Average</p><div class="flex items-baseline mt-1"><span class="text-2xl font-bold text-on-surface">â‚¹3,085</span><span class="text-sm text-on-surface-variant ml-1">/ Qt</span></div></div></div><div class="mt-4 text-right"><span class="inline-flex items-center px-2 py-0.5 rounded text-xs font-medium bg-success-bg text-success">3.7% vs last week</span></div></div>
    <div class="bg-white rounded-lg border border-outline p-4"><div class="flex items-start"><div class="bg-primary-light/50 p-2 rounded-md mr-3"><svg class="w-6 h-6 text-primary" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"/><path d="M15 11a3 3 0 11-6 0 3 3 0 016 0z" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"/></svg></div><div><p class="text-sm font-medium text-on-surface-variant">Highest Nearby</p><div class="flex items-baseline mt-1"><span class="text-2xl font-bold text-on-surface">â‚¹3,240</span><span class="text-sm text-on-surface-variant ml-1">/ Qt</span></div><p class="text-sm text-on-surface-variant">Jaipur Mandi</p></div></div><div class="mt-4 flex items-center text-xs text-on-surface-variant">240 km away</div></div>
    <div class="bg-white rounded-lg border border-outline p-4"><div class="flex items-start"><div class="bg-primary-light/50 p-2 rounded-md mr-3"><svg class="w-6 h-6 text-primary" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"/></svg></div><div><p class="text-sm font-medium text-on-surface-variant">Predicted Price</p><div class="flex items-baseline mt-1"><span class="text-2xl font-bold text-on-surface">â‚¹3,350</span><span class="text-sm text-on-surface-variant ml-1">/ Qt</span></div><p class="text-sm text-on-surface-variant">Expected in 7 days</p></div></div><div class="mt-4 text-right"><span class="inline-flex items-center px-2 py-0.5 rounded text-xs font-medium bg-success-bg text-success">Strong Buy Signal</span></div></div>
  </div>
  <!-- Chart + Right -->
  <div class="flex flex-col lg:flex-row gap-6">
    <div class="flex-1 flex flex-col gap-6">
      <!-- Price Chart -->
      <div class="bg-white p-6 rounded-lg border border-outline shadow-sm">
        <div class="flex justify-between items-center mb-6">
          <h3 class="text-lg font-bold text-on-surface">Wheat Price Trend â€” Last 30 Days</h3>
          <div class="flex items-center space-x-4 text-sm">
            <div class="flex items-center"><span class="w-3 h-1 bg-primary rounded mr-2 inline-block" style="background:#1b4332"></span><span class="text-on-surface-variant">Actual Price</span></div>
            <div class="flex items-center"><span class="w-3 h-1 border-t-2 border-dashed border-green-300 mr-2 inline-block"></span><span class="text-on-surface-variant">7-Day MA</span></div>
          </div>
        </div>
        <p class="text-xs text-on-surface-variant mb-2">Price (â‚¹ / Quintal)</p>
        <div class="h-[250px] w-full"><canvas id="wheatChart"></canvas></div>
      </div>
      <!-- Mandi Table -->
      <div class="bg-white rounded-lg border border-outline shadow-sm overflow-hidden">
        <div class="p-4 border-b border-outline"><h3 class="text-lg font-bold text-on-surface">Wheat Prices Across Mandis</h3></div>
        <table class="min-w-full divide-y divide-outline">
          <thead class="bg-gray-50"><tr>
            <th class="px-6 py-3 text-left text-xs font-medium text-on-surface-variant uppercase tracking-wider">Mandi</th>
            <th class="px-6 py-3 text-left text-xs font-medium text-on-surface-variant uppercase tracking-wider">Region</th>
            <th class="px-6 py-3 text-right text-xs font-medium text-on-surface-variant uppercase tracking-wider">Price (â‚¹/Qt)</th>
            <th class="px-6 py-3 text-right text-xs font-medium text-on-surface-variant uppercase tracking-wider">Trend</th>
          </tr></thead>
          <tbody class="bg-white divide-y divide-outline">
            <tr><td class="px-6 py-4 text-sm font-medium text-on-surface flex items-center"><svg class="w-4 h-4 text-gray-400 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"/><path d="M15 11a3 3 0 11-6 0 3 3 0 016 0z" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"/></svg>Delhi Mandi</td><td class="px-6 py-4 text-sm text-on-surface-variant">Delhi</td><td class="px-6 py-4 text-sm font-semibold text-on-surface text-right">â‚¹3,200</td><td class="px-6 py-4 text-sm text-right text-success font-medium">â†‘ 2.4%</td></tr>
            <tr><td class="px-6 py-4 text-sm font-medium text-on-surface flex items-center"><svg class="w-4 h-4 text-gray-400 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"/><path d="M15 11a3 3 0 11-6 0 3 3 0 016 0z" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"/></svg>Pune Mandi</td><td class="px-6 py-4 text-sm text-on-surface-variant">Maharashtra</td><td class="px-6 py-4 text-sm font-semibold text-on-surface text-right">â‚¹3,050</td><td class="px-6 py-4 text-sm text-right text-success font-medium">â†‘ 1.8%</td></tr>
            <tr class="bg-primary-light/20"><td class="px-6 py-4 text-sm font-medium text-on-surface flex items-center"><svg class="w-4 h-4 text-primary mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24" style="color:#1b4332"><path d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"/><path d="M15 11a3 3 0 11-6 0 3 3 0 016 0z" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"/></svg>Jaipur Mandi<span class="ml-2 text-white text-[10px] px-2 py-0.5 rounded font-bold tracking-wide" style="background:#1b4332">BEST PRICE</span></td><td class="px-6 py-4 text-sm text-on-surface-variant">Rajasthan</td><td class="px-6 py-4 text-sm font-semibold text-on-surface text-right">â‚¹3,240</td><td class="px-6 py-4 text-sm text-right text-success font-medium">â†‘ 3.1%</td></tr>
            <tr><td class="px-6 py-4 text-sm font-medium text-on-surface flex items-center"><svg class="w-4 h-4 text-gray-400 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"/><path d="M15 11a3 3 0 11-6 0 3 3 0 016 0z" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"/></svg>Indore Mandi</td><td class="px-6 py-4 text-sm text-on-surface-variant">Madhya Pradesh</td><td class="px-6 py-4 text-sm font-semibold text-on-surface text-right">â‚¹3,120</td><td class="px-6 py-4 text-sm text-right text-success font-medium">â†‘ 2.0%</td></tr>
            <tr><td class="px-6 py-4 text-sm font-medium text-on-surface flex items-center"><svg class="w-4 h-4 text-gray-400 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"/><path d="M15 11a3 3 0 11-6 0 3 3 0 016 0z" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"/></svg>Nashik Mandi</td><td class="px-6 py-4 text-sm text-on-surface-variant">Maharashtra</td><td class="px-6 py-4 text-sm font-semibold text-on-surface text-right">â‚¹2,980</td><td class="px-6 py-4 text-sm text-right text-danger font-medium">â†“ 0.6%</td></tr>
          </tbody>
        </table>
      </div>
    </div>
    <!-- Right Sidebar -->
    <div class="w-full lg:w-[320px] flex flex-col gap-6 shrink-0">
      <div class="bg-white rounded-lg border border-outline shadow-sm p-5">
        <h3 class="text-lg font-bold text-on-surface mb-4">7-Day Price Forecast</h3>
        <div class="space-y-3 mb-6">
          <div class="flex justify-between items-center text-sm"><span class="text-on-surface-variant">Tomorrow</span><div class="flex items-center font-semibold">â‚¹3,215<svg class="w-3 h-3 ml-1 text-success" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path d="M5 10l7-7m0 0l7 7m-7-7v18" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"/></svg></div></div>
          <div class="flex justify-between items-center text-sm"><span class="text-on-surface-variant">Day 3</span><div class="flex items-center font-semibold">â‚¹3,260<svg class="w-3 h-3 ml-1 text-success" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path d="M5 10l7-7m0 0l7 7m-7-7v18" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"/></svg></div></div>
          <div class="flex justify-between items-center text-sm"><span class="text-on-surface-variant">Day 5</span><div class="flex items-center font-semibold">â‚¹3,310<svg class="w-3 h-3 ml-1 text-success" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path d="M5 10l7-7m0 0l7 7m-7-7v18" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"/></svg></div></div>
          <div class="flex justify-between items-center text-sm"><span class="text-on-surface-variant">Day 7</span><div class="flex items-center font-semibold">â‚¹3,350<svg class="w-3 h-3 ml-1 text-success" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path d="M5 10l7-7m0 0l7 7m-7-7v18" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"/></svg></div></div>
        </div>
        <div class="h-16 w-full mb-4"><canvas id="wheatSparkline"></canvas></div>
        <div class="bg-gray-50 rounded p-3 text-sm text-on-surface-variant flex items-start border border-gray-100">
          <svg class="w-5 h-5 text-gray-500 mr-2 mt-0.5 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"/></svg>
          <p>Prices are trending upward. Holding wheat for several days may improve returns.</p>
        </div>
      </div>
      <div class="rounded-lg shadow-sm p-6 text-white relative overflow-hidden" style="background:#1b4332">
        <div class="flex items-center text-green-200 text-xs font-bold tracking-wider mb-2 uppercase"><svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path d="M11 5.882V19.24a1.76 1.76 0 01-3.417.592l-2.147-6.15M18 13a3 3 0 100-6M5.436 13.683A4.001 4.001 0 017 6h1.832c4.1 0 7.625-1.234 9.168-3v14c-1.543-1.766-5.067-3-9.168-3H7a3.988 3.988 0 01-1.564-.317z" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"/></svg>Recommended Action</div>
        <h3 class="text-3xl font-bold mb-2">Hold for 3â€“5 days</h3>
        <p class="text-green-100 text-sm mb-6">Expected upside: â‚¹120â€“â‚¹150 / Qt</p>
        <button class="w-full bg-primary-light text-primary font-semibold py-3 px-4 rounded hover:bg-white transition-colors flex items-center justify-center" style="color:#1b4332" onclick="navigate('marketplace/listings/new')">View Selling Options<svg class="w-4 h-4 ml-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path d="M14 5l7 7m0 0l-7 7m7-7H3" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"/></svg></button>
      </div>
    </div>
  </div>
</div>
`;
}

let wheatChartInstance = null, wheatSparkInstance = null;

export function initCharts() {
  if (wheatChartInstance) { wheatChartInstance.destroy(); wheatChartInstance = null; }
  if (wheatSparkInstance) { wheatSparkInstance.destroy(); wheatSparkInstance = null; }
  setTimeout(() => {
    const ctx = document.getElementById('wheatChart');
    if (ctx) {
      const grad = ctx.getContext('2d').createLinearGradient(0,0,0,250);
      grad.addColorStop(0,'rgba(27,67,50,0.2)'); grad.addColorStop(1,'rgba(27,67,50,0)');
      wheatChartInstance = new Chart(ctx, {
        type:'line',
        data:{
          labels:['Oct 1','Oct 8','Oct 15','Oct 22','Oct 29','Nov 5'],
          datasets:[
            {label:'Actual',data:[2930,3080,3160,3070,3190,3200],borderColor:'#1b4332',backgroundColor:grad,borderWidth:2,pointBackgroundColor:'#fff',pointBorderColor:'#1b4332',pointBorderWidth:2,pointRadius:4,fill:true,tension:0.4},
            {label:'7-Day MA',data:[2900,3020,3080,3080,3150,3180],borderColor:'#86efac',borderWidth:2,borderDash:[5,5],pointRadius:0,fill:false,tension:0.4}
          ]
        },
        options:{responsive:true,maintainAspectRatio:false,plugins:{legend:{display:false}},scales:{y:{min:2800,max:3300,ticks:{stepSize:100},grid:{color:'#f3f4f6'}},x:{grid:{display:false}}}}
      });
    }
    const spark = document.getElementById('wheatSparkline');
    if (spark) {
      const sg = spark.getContext('2d').createLinearGradient(0,0,0,60);
      sg.addColorStop(0,'rgba(27,67,50,0.3)'); sg.addColorStop(1,'rgba(27,67,50,0)');
      wheatSparkInstance = new Chart(spark, {
        type:'line',
        data:{labels:['1','2','3','4','5','6','7'],datasets:[{data:[10,15,20,18,25,22,35],borderColor:'#1b4332',borderWidth:2,backgroundColor:sg,fill:true,pointRadius:3,pointBackgroundColor:'#1b4332',tension:0.3}]},
        options:{responsive:true,maintainAspectRatio:false,plugins:{legend:{display:false},tooltip:{enabled:false}},scales:{x:{display:false},y:{display:false,min:0,max:40}}}
      });
    }
  }, 50);
}

