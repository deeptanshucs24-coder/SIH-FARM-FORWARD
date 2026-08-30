
export function renderSidebar(activeKey) {
  const container = document.getElementById("sidebar-root");
  if (!container) return;
  container.innerHTML = `<aside class="w-[240px] flex-shrink-0 h-screen hidden md:flex flex-col bg-primary-container border-r border-outline-variant z-50 p-lg justify-between overflow-y-auto">
  <div class="flex flex-col gap-md">
    <div class="mb-lg">
      <h1 class="font-headline-xl text-[28px] font-bold text-primary-fixed leading-none">FarmForward</h1>
      <p class="font-label-md text-label-md text-primary-fixed-dim uppercase tracking-wider mt-xs">Agri-FinTech Hub</p>
    </div>
    <nav class="flex flex-col gap-sm" id="desktop-nav">
      <a class="nav-link flex items-center gap-md px-md py-sm rounded-xl transition-colors" data-page="dashboard" href="#/dashboard">
        <span class="material-symbols-outlined">dashboard</span>
        <span class="font-label-md text-label-md">Dashboard</span>
      </a>
      <a class="nav-link flex items-center gap-md px-md py-sm rounded-xl transition-colors" data-page="marketplace" href="#/marketplace">
        <span class="material-symbols-outlined">storefront</span>
        <span class="font-label-md text-label-md">Marketplace</span>
      </a>
      <a class="nav-link flex items-center gap-md px-md py-sm rounded-xl transition-colors" data-page="financials" href="#/financials">
        <span class="material-symbols-outlined">payments</span>
        <span class="font-label-md text-label-md">Financials</span>
      </a>
      <a class="nav-link flex items-center gap-md px-md py-sm rounded-xl transition-colors" data-page="logistics" href="#/logistics">
        <span class="material-symbols-outlined">local_shipping</span>
        <span class="font-label-md text-label-md">Logistics</span>
      </a>
      <a class="nav-link flex items-center gap-md px-md py-sm rounded-xl transition-colors" data-page="analytics" href="#/analytics">
        <span class="material-symbols-outlined">analytics</span>
        <span class="font-label-md text-label-md">Analytics</span>
      </a>
      <a class="nav-link flex items-center gap-md px-md py-sm rounded-xl transition-colors" data-page="settings" href="#/settings">
        <span class="material-symbols-outlined">settings</span>
        <span class="font-label-md text-label-md">Settings</span>
      </a>
    </nav>
    <button onclick="navigate('marketplace/listings/new')" class="mt-lg w-full py-md bg-secondary-fixed text-primary-container font-label-md text-label-md rounded-xl hover:bg-primary-fixed transition-colors flex items-center justify-center gap-sm shadow-sm">
      <span class="material-symbols-outlined" style="font-variation-settings:'FILL' 1">add_circle</span>Add Produce
    </button>
  </div>
  <div class="flex flex-col gap-sm border-t border-primary-fixed/20 pt-md mt-auto">
    <a class="nav-link flex items-center gap-md px-md py-sm text-primary-fixed-dim hover:text-primary-fixed hover:bg-white/10 transition-colors rounded-xl" data-page="help" href="#/help">
      <span class="material-symbols-outlined">help</span>
      <span class="font-label-md text-label-md">Help &amp; Support</span>
    </a>
    <a class="flex items-center gap-md px-md py-sm text-primary-fixed-dim hover:text-primary-fixed hover:bg-white/10 transition-colors rounded-xl" href="#" onclick="alert('Logged out successfully.')">
      <span class="material-symbols-outlined">logout</span>
      <span class="font-label-md text-label-md">Logout</span>
    </a>
  </div>
</aside>`;
  
  container.querySelectorAll(".nav-link").forEach(el => {
    const isActive = el.dataset.page === activeKey;
    el.className = isActive
      ? "nav-link flex items-center gap-md px-md py-sm bg-surface-container-highest text-on-primary-container rounded-xl font-bold scale-95 duration-100"
      : "nav-link flex items-center gap-md px-md py-sm text-primary-fixed-dim hover:text-primary-fixed hover:bg-white/10 transition-colors rounded-xl";
  });
}
