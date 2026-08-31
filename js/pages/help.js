export function render() {
  return `<div class="p-margin max-w-7xl mx-auto pb-24 md:pb-margin">
  <div class="mb-xl">
    <h1 class="font-headline-lg text-headline-lg text-primary font-bold">Help &amp; Support</h1>
    <p class="font-body-md text-body-md text-on-surface-variant mt-xs">Find answers to questions, learn how to use FarmForward, or contact our agricultural support specialists.</p>
  </div>
  
  <!-- Search Bar -->
  <div class="bg-surface-container-lowest border border-outline-variant rounded-xl p-lg shadow-sm mb-xl">
    <div class="relative w-full max-w-2xl mx-auto">
      <span class="material-symbols-outlined absolute left-4 top-1/2 -translate-y-1/2 text-on-surface-variant text-2xl">search</span>
      <input type="text" placeholder="Search guides, FAQs, mandi pricing help..." class="w-full pl-12 pr-4 py-3 bg-surface border border-outline-variant rounded-full font-body-md focus:outline-none focus:border-primary-container">
    </div>
  </div>

  <!-- Categories -->
  <div class="grid grid-cols-1 md:grid-cols-3 gap-lg mb-xl">
    <div class="bg-surface-container-lowest border border-outline-variant rounded-xl p-md flex flex-col gap-sm shadow-sm hover:border-primary transition-colors cursor-pointer" onclick="alert('Viewing Getting Started Guide')">
      <div class="p-2 bg-secondary-container w-fit rounded-lg text-primary"><span class="material-symbols-outlined">rocket_launch</span></div>
      <h3 class="font-headline-md text-headline-md text-primary font-bold">Getting Started</h3>
      <p class="font-body-sm text-body-sm text-on-surface-variant">Setup your farm profile, crop preferences, and mandi alerts.</p>
    </div>
    <div class="bg-surface-container-lowest border border-outline-variant rounded-xl p-md flex flex-col gap-sm shadow-sm hover:border-primary transition-colors cursor-pointer" onclick="navigate('marketplace')">
      <div class="p-2 bg-secondary-container w-fit rounded-lg text-primary"><span class="material-symbols-outlined">storefront</span></div>
      <h3 class="font-headline-md text-headline-md text-primary font-bold">Marketplace &amp; Listings</h3>
      <p class="font-body-sm text-body-sm text-on-surface-variant">Post produce listings, negotiate with verified buyers, and lock in best mandi prices.</p>
    </div>
    <div class="bg-surface-container-lowest border border-outline-variant rounded-xl p-md flex flex-col gap-sm shadow-sm hover:border-primary transition-colors cursor-pointer" onclick="navigate('financials')">
      <div class="p-2 bg-secondary-container w-fit rounded-lg text-primary"><span class="material-symbols-outlined">payments</span></div>
      <h3 class="font-headline-md text-headline-md text-primary font-bold">Financials &amp; Payments</h3>
      <p class="font-body-sm text-body-sm text-on-surface-variant">Track revenue, manage farm expenses, and link bank accounts for direct payout.</p>
    </div>
  </div>

  <!-- FAQ & Contact Support -->
  <div class="grid grid-cols-1 lg:grid-cols-3 gap-xl">
    <div class="lg:col-span-2 space-y-md">
      <h3 class="font-headline-md text-headline-md text-primary font-bold mb-md">Frequently Asked Questions</h3>
      
      <div class="bg-surface-container-lowest border border-outline-variant rounded-xl p-md shadow-sm">
        <h4 class="font-body-md font-bold text-on-surface mb-xs">How do I list my produce on FarmForward Marketplace?</h4>
        <p class="font-body-sm text-on-surface-variant leading-relaxed">Navigate to Marketplace → Active Listings and click "New Listing". Enter your crop variety, quantity, asking price, and location. Verified buyers across nearby mandis will be notified instantly.</p>
      </div>

      <div class="bg-surface-container-lowest border border-outline-variant rounded-xl p-md shadow-sm">
        <h4 class="font-body-md font-bold text-on-surface mb-xs">How are payment transactions secured?</h4>
        <p class="font-body-sm text-on-surface-variant leading-relaxed">All payments through FarmForward are held in secure escrow accounts until harvest dispatch and quality verification are confirmed by both farmer and buyer.</p>
      </div>

      <div class="bg-surface-container-lowest border border-outline-variant rounded-xl p-md shadow-sm">
        <h4 class="font-body-md font-bold text-on-surface mb-xs">How do I track my active logistics shipments?</h4>
        <p class="font-body-sm text-on-surface-variant leading-relaxed">Visit the Logistics dashboard to view real-time GPS progress, ETA updates, and transporter contact details for all dispatches.</p>
      </div>
    </div>

    <div class="space-y-lg">
      <div class="bg-primary-container text-white rounded-xl p-lg shadow-md flex flex-col gap-md">
        <div class="flex items-center gap-sm">
          <span class="material-symbols-outlined text-primary-fixed text-3xl">headset_mic</span>
          <div>
            <h3 class="font-headline-md font-bold text-white">Contact Support</h3>
            <p class="text-xs text-primary-fixed-dim">Dedicated Farmer Support Team</p>
          </div>
        </div>
        <p class="text-sm text-primary-fixed-dim leading-relaxed">Need help with a trade or payment issue? Our agricultural specialists are available 24/7.</p>
        <div class="space-y-xs pt-xs text-xs border-t border-primary-fixed/20">
          <div class="flex items-center gap-2 text-primary-fixed"><span class="material-symbols-outlined text-base">call</span><span>Toll Free: 1800-123-4567</span></div>
          <div class="flex items-center gap-2 text-primary-fixed"><span class="material-symbols-outlined text-base">mail</span><span>support@farmforward.in</span></div>
          <div class="flex items-center gap-2 text-primary-fixed"><span class="material-symbols-outlined text-base">schedule</span><span>Mon - Sun: 6:00 AM - 10:00 PM</span></div>
        </div>
        <button onclick="alert('Connecting to FarmForward Live Support...')" class="w-full py-md bg-secondary-fixed text-primary-container font-label-md text-label-md rounded-xl hover:bg-primary-fixed transition-colors font-bold mt-xs">Start a Conversation</button>
      </div>
    </div>
  </div>
</div>`;
}
