export function render() {
  return `<div class="p-6 max-w-7xl mx-auto pb-24 md:pb-6">
  <a class="text-primary hover:underline text-sm font-medium flex items-center mb-4 cursor-pointer" onclick="navigate('marketplace/listings')">
    <svg class="w-4 h-4 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path d="M10 19l-7-7m0 0l7-7m-7 7h18" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"/></svg>Back to Active Listings
  </a>
  <div class="flex flex-col lg:flex-row gap-6">
    <!-- Left: Buyer Profile -->
    <div class="flex-1 space-y-6">
      <div class="bg-white rounded-2xl border border-outline p-6">
        <div class="flex items-start gap-4 mb-6">
          <div class="w-16 h-16 rounded-2xl flex items-center justify-center text-white text-2xl font-bold shrink-0" style="background:#1b4332">AL</div>
          <div class="flex-1">
            <div class="flex items-center gap-2 flex-wrap">
              <h2 class="text-2xl font-bold text-on-surface">AgriCorp Ltd</h2>
              <span class="inline-flex items-center px-2.5 py-1 rounded-full text-xs font-semibold bg-success-bg text-success"><i class="fa-solid fa-circle-check mr-1 text-[10px]"></i>Verified Buyer</span>
            </div>
            <p class="text-on-surface-variant mt-1">Established 2008 Â· Indore, Madhya Pradesh</p>
            <div class="flex items-center gap-4 mt-3 text-sm text-on-surface-variant">
              <span><i class="fa-regular fa-star text-yellow-400 mr-1"></i><strong class="text-on-surface">4.8</strong> / 5 rating</span>
              <span>â€¢</span>
              <span><strong class="text-on-surface">120+</strong> transactions</span>
              <span>â€¢</span>
              <span>Member since <strong class="text-on-surface">2019</strong></span>
            </div>
          </div>
        </div>
        <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
          <div class="bg-surface rounded-xl p-3"><p class="text-xs text-on-surface-variant uppercase font-medium tracking-wider mb-1">Crop Needed</p><p class="font-bold text-on-surface">Soybean</p></div>
          <div class="bg-surface rounded-xl p-3"><p class="text-xs text-on-surface-variant uppercase font-medium tracking-wider mb-1">Quantity</p><p class="font-bold text-on-surface">500 MT</p></div>
          <div class="bg-surface rounded-xl p-3"><p class="text-xs text-on-surface-variant uppercase font-medium tracking-wider mb-1">Target Price</p><p class="font-bold text-on-surface">â‚¹4,850/Qt</p></div>
          <div class="bg-surface rounded-xl p-3"><p class="text-xs text-on-surface-variant uppercase font-medium tracking-wider mb-1">Delivery</p><p class="font-bold text-on-surface">Within 15 days</p></div>
        </div>
      </div>
      <!-- Transaction History -->
      <div class="bg-white rounded-2xl border border-outline overflow-hidden">
        <div class="p-4 border-b border-outline"><h3 class="text-lg font-bold text-on-surface">Transaction History with AgriCorp</h3></div>
        <table class="w-full text-left">
          <thead><tr class="bg-surface/50 border-b border-outline text-xs uppercase tracking-wider text-on-surface-variant">
            <th class="px-6 py-3 font-medium">Date</th><th class="px-6 py-3 font-medium">Crop</th><th class="px-6 py-3 font-medium">Quantity</th><th class="px-6 py-3 font-medium">Amount</th><th class="px-6 py-3 font-medium">Status</th>
          </tr></thead>
          <tbody class="divide-y divide-outline">
            <tr class="hover:bg-surface/30"><td class="px-6 py-4 text-sm text-on-surface-variant">Jun 12, 2024</td><td class="px-6 py-4 text-sm font-medium text-on-surface">Wheat</td><td class="px-6 py-4 text-sm text-on-surface">320 Qt</td><td class="px-6 py-4 text-sm font-bold text-on-surface">â‚¹9,92,000</td><td class="px-6 py-4"><span class="inline-flex px-2 py-1 rounded-full text-xs font-semibold bg-success-bg text-success">Completed</span></td></tr>
            <tr class="hover:bg-surface/30"><td class="px-6 py-4 text-sm text-on-surface-variant">Mar 5, 2024</td><td class="px-6 py-4 text-sm font-medium text-on-surface">Soybean</td><td class="px-6 py-4 text-sm text-on-surface">480 Qt</td><td class="px-6 py-4 text-sm font-bold text-on-surface">â‚¹22,08,000</td><td class="px-6 py-4"><span class="inline-flex px-2 py-1 rounded-full text-xs font-semibold bg-success-bg text-success">Completed</span></td></tr>
            <tr class="hover:bg-surface/30"><td class="px-6 py-4 text-sm text-on-surface-variant">Nov 18, 2023</td><td class="px-6 py-4 text-sm font-medium text-on-surface">Maize</td><td class="px-6 py-4 text-sm text-on-surface">200 Qt</td><td class="px-6 py-4 text-sm font-bold text-on-surface">â‚¹4,20,000</td><td class="px-6 py-4"><span class="inline-flex px-2 py-1 rounded-full text-xs font-semibold bg-success-bg text-success">Completed</span></td></tr>
          </tbody>
        </table>
      </div>
    </div>
    <!-- Right: Negotiation Panel -->
    <div class="w-full lg:w-[340px] space-y-4 shrink-0">
      <div class="rounded-2xl p-6 text-white" style="background:#1b4332">
        <h3 class="text-lg font-bold mb-1">Start Negotiation</h3>
        <p class="text-green-200 text-sm mb-5">AgriCorp Ltd is ready to discuss pricing</p>
        <div class="space-y-3 mb-5">
          <div class="bg-white/10 rounded-xl p-3"><p class="text-xs text-green-200 uppercase font-medium mb-1">Their Offer</p><p class="text-2xl font-bold">â‚¹4,850 / Qt</p></div>
          <div class="bg-white/10 rounded-xl p-3"><p class="text-xs text-green-200 uppercase font-medium mb-1">Your Listed Price</p><p class="text-2xl font-bold">â‚¹4,800 / Qt</p></div>
        </div>
        <div class="space-y-2">
          <button class="w-full py-3 bg-primary-light font-bold rounded-xl hover:bg-white transition-colors" style="color:#1b4332" onclick="alert('Offer â‚¹4,850/Qt accepted! Contract generated.')">Accept â‚¹4,850/Qt</button>
          <button class="w-full py-3 bg-white/10 border border-white/20 font-semibold rounded-xl hover:bg-white/20 transition-colors" onclick="alert('Counter offer sent to buyer.')">Counter Offer</button>
        </div>
      </div>
      <div class="bg-white rounded-2xl border border-outline p-5">
        <h4 class="font-bold text-on-surface mb-3">Buyer Contact</h4>
        <div class="space-y-2 text-sm">
          <div class="flex items-center gap-2 text-on-surface-variant"><i class="fa-solid fa-user w-4 text-center"></i><span>Ramesh Gupta (Procurement Head)</span></div>
          <div class="flex items-center gap-2 text-on-surface-variant"><i class="fa-solid fa-phone w-4 text-center"></i><span>+91 98100 45678</span></div>
          <div class="flex items-center gap-2 text-on-surface-variant"><i class="fa-solid fa-envelope w-4 text-center"></i><span>ramesh@agricorp.in</span></div>
        </div>
      </div>
    </div>
  </div>
</div>
`;
}

