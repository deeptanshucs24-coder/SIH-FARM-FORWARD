
export function renderMobileNav(activeKey) {
  const container = document.getElementById("mobile-nav-root");
  if (!container) return;
  container.innerHTML = `<nav class="md:hidden fixed bottom-0 left-0 right-0 z-50 bg-surface border-t border-outline-variant flex h-16 shrink-0" id="mobile-nav">
    <a class="mob-link flex flex-col items-center justify-center flex-1 gap-0.5" data-page="dashboard" href="#/dashboard">
      <span class="material-symbols-outlined text-xl">dashboard</span>
      <span style="font-size:10px;font-weight:600">Dashboard</span>
    </a>
    <a class="mob-link flex flex-col items-center justify-center flex-1 gap-0.5" data-page="marketplace" href="#/marketplace">
      <span class="material-symbols-outlined text-xl">storefront</span>
      <span style="font-size:10px;font-weight:600">Market</span>
    </a>
    <a class="mob-link flex flex-col items-center justify-center flex-1 gap-0.5" data-page="financials" href="#/financials">
      <span class="material-symbols-outlined text-xl">payments</span>
      <span style="font-size:10px;font-weight:600">Finance</span>
    </a>
    <a class="mob-link flex flex-col items-center justify-center flex-1 gap-0.5" data-page="logistics" href="#/logistics">
      <span class="material-symbols-outlined text-xl">local_shipping</span>
      <span style="font-size:10px;font-weight:600">Logistics</span>
    </a>
    <a class="mob-link flex flex-col items-center justify-center flex-1 gap-0.5" data-page="settings" href="#/settings">
      <span class="material-symbols-outlined text-xl">person</span>
      <span style="font-size:10px;font-weight:600">Profile</span>
    </a>
  </nav>`;
  container.querySelectorAll(".mob-link").forEach(el => {
    const isActive = el.dataset.page === activeKey;
    el.style.color = isActive ? "#1b4332" : "#717973";
    el.style.fontWeight = isActive ? "700" : "400";
  });
}
