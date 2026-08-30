
export function renderHeader(title) {
  const container = document.getElementById("header-root");
  if (!container) return;
  container.innerHTML = `<header class="sticky top-0 w-full z-40 bg-surface border-b border-outline-variant h-16 px-gutter flex justify-between items-center shrink-0">
    <div class="flex items-center gap-md lg:w-1/3">
      <button class="md:hidden text-primary p-sm rounded-full">
        <span class="material-symbols-outlined">menu</span>
      </button>
      <span class="font-headline-md text-headline-md font-bold text-primary md:hidden" id="mobile-page-title">Dashboard</span>
      <div class="hidden md:flex relative w-full max-w-md">
        <span class="material-symbols-outlined absolute left-3 top-1/2 -translate-y-1/2 text-on-surface-variant">search</span>
        <input class="w-full pl-10 pr-4 py-2 bg-surface-container-lowest border border-outline-variant rounded-full font-body-sm focus:outline-none focus:border-primary-container transition-all" placeholder="Search crops, financials..." type="text">
      </div>
    </div>
    <div class="flex items-center gap-md">
      <button class="text-on-surface-variant p-sm rounded-full relative" onclick="alert('You have 2 pending notifications.')">
        <span class="material-symbols-outlined">notifications</span>
        <span class="absolute top-1 right-1 w-2 h-2 bg-error rounded-full"></span>
      </button>
      <button class="flex items-center gap-sm p-xs rounded-full pr-sm" onclick="navigate('settings')">
        <img alt="User" class="w-8 h-8 rounded-full object-cover border border-outline-variant" src="https://lh3.googleusercontent.com/aida-public/AB6AXuC-7FwkDGstTpuUtE5TO8-6f7EOphQXja3rWXpnlMVzs4d2sas2O4ZR_QpjfgUOxQ00-pUurm0Y1QbdaAm2GTghN72jQ2rvgf2cOJmeiN5wiSzWYlal9CH5BH-shfpWuWyaWfgeZK-WTjLF6tzIMWPgpfhhP3-2YJ-QIwUaI_8u_qyaHBim05vW3E1Fawl1c0lBkG19jd9UoIOMchDLEVcKenGbjO5p_liPPsvXmTfafOiZl3p_y6-lRw">
      </button>
    </div>
  </header>`;
  const titleEl = document.getElementById("mobile-page-title");
  if (titleEl && title) titleEl.textContent = title;
}
