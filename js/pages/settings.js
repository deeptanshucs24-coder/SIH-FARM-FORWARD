export function render() {
  return `<div class="p-margin max-w-4xl mx-auto pb-24 md:pb-margin">
  <div class="mb-xl">
    <h1 class="font-headline-lg text-headline-lg text-primary font-bold">Settings</h1>
    <p class="font-body-md text-body-md text-on-surface-variant mt-xs">Manage your FarmForward account preferences and configurations.</p>
  </div>
  <div class="grid grid-cols-1 md:grid-cols-3 gap-lg">
    <div class="md:col-span-2 space-y-lg">
      <div class="bg-surface-container-lowest border border-outline-variant rounded-xl p-md flex flex-col gap-md shadow-sm">
        <h3 class="font-headline-md text-headline-md text-primary font-bold">Profile Details</h3>
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-md">
          <div class="flex flex-col gap-xs"><label class="font-label-md text-label-md text-on-surface-variant uppercase">Full Name</label><input class="px-md py-sm bg-surface border border-outline-variant rounded-lg font-body-sm focus:outline-none focus:border-primary-container" type="text" value="Rajesh Kumar"></div>
          <div class="flex flex-col gap-xs"><label class="font-label-md text-label-md text-on-surface-variant uppercase">Phone Number</label><input class="px-md py-sm bg-surface border border-outline-variant rounded-lg font-body-sm focus:outline-none focus:border-primary-container" type="tel" value="+91 98765 43210"></div>
          <div class="flex flex-col gap-xs"><label class="font-label-md text-label-md text-on-surface-variant uppercase">Farm Location</label><input class="px-md py-sm bg-surface border border-outline-variant rounded-lg font-body-sm focus:outline-none focus:border-primary-container" type="text" value="Indore, Madhya Pradesh"></div>
          <div class="flex flex-col gap-xs"><label class="font-label-md text-label-md text-on-surface-variant uppercase">Farm Size (Acres)</label><input class="px-md py-sm bg-surface border border-outline-variant rounded-lg font-body-sm focus:outline-none focus:border-primary-container" type="number" value="15"></div>
        </div>
      </div>
      <div class="bg-surface-container-lowest border border-outline-variant rounded-xl p-md flex flex-col gap-md shadow-sm">
        <h3 class="font-headline-md text-headline-md text-primary font-bold">Crop Preferences</h3>
        <p class="font-body-sm text-body-sm text-on-surface-variant">Select your primary crops to customize dashboard feeds and price recommendations.</p>
        <div class="flex flex-wrap gap-sm">
          <span class="px-md py-sm bg-secondary-container text-on-secondary-container font-label-md text-label-md rounded-full flex items-center gap-xs">Wheat <span class="material-symbols-outlined text-xs cursor-pointer">close</span></span>
          <span class="px-md py-sm bg-secondary-container text-on-secondary-container font-label-md text-label-md rounded-full flex items-center gap-xs">Soybean <span class="material-symbols-outlined text-xs cursor-pointer">close</span></span>
          <span class="px-md py-sm bg-secondary-container text-on-secondary-container font-label-md text-label-md rounded-full flex items-center gap-xs">Onion <span class="material-symbols-outlined text-xs cursor-pointer">close</span></span>
          <button class="px-md py-sm border border-dashed border-outline-variant text-on-surface-variant font-label-md text-label-md rounded-full flex items-center gap-xs hover:bg-surface-container-low transition-colors">+ Add Crop</button>
        </div>
      </div>
      <div class="bg-surface-container-lowest border border-outline-variant rounded-xl p-md flex flex-col gap-md shadow-sm">
        <h3 class="font-headline-md text-headline-md text-primary font-bold">Farm Details</h3>
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-md">
          <div class="flex flex-col gap-xs"><label class="font-label-md text-label-md text-on-surface-variant uppercase">Soil Type</label><select class="px-md py-sm bg-surface border border-outline-variant rounded-lg font-body-sm focus:outline-none"><option>Black Cotton Soil</option><option>Red Laterite</option><option>Alluvial Soil</option></select></div>
          <div class="flex flex-col gap-xs"><label class="font-label-md text-label-md text-on-surface-variant uppercase">Irrigation Type</label><select class="px-md py-sm bg-surface border border-outline-variant rounded-lg font-body-sm focus:outline-none"><option>Drip Irrigation</option><option>Flood Irrigation</option><option>Rain-fed</option></select></div>
        </div>
      </div>
    </div>
    <div class="space-y-lg">
      <div class="bg-surface-container-lowest border border-outline-variant rounded-xl p-md flex flex-col gap-md shadow-sm">
        <h3 class="font-headline-md text-headline-md text-primary font-bold">App Settings</h3>
        <div class="flex flex-col gap-xs"><label class="font-label-md text-label-md text-on-surface-variant uppercase">Language</label><select class="px-md py-sm bg-surface border border-outline-variant rounded-lg font-body-sm focus:outline-none"><option selected>English</option><option>à¤¹à¤¿à¤¨à¥à¤¦à¥€</option><option>à¤®à¤°à¤¾à¤ à¥€</option></select></div>
        <div class="flex flex-col gap-xs pt-sm border-t border-outline-variant/30">
          <label class="font-label-md text-label-md text-on-surface-variant uppercase mb-xs">Notifications</label>
          <div class="flex items-center justify-between py-xs"><span class="font-body-sm text-on-surface">SMS Price Alerts</span><input checked class="rounded text-primary w-4 h-4" type="checkbox"></div>
          <div class="flex items-center justify-between py-xs"><span class="font-body-sm text-on-surface">Logistics Updates</span><input checked class="rounded text-primary w-4 h-4" type="checkbox"></div>
          <div class="flex items-center justify-between py-xs"><span class="font-body-sm text-on-surface">Payment Alerts</span><input checked class="rounded text-primary w-4 h-4" type="checkbox"></div>
          <div class="flex items-center justify-between py-xs"><span class="font-body-sm text-on-surface">Market Insights</span><input class="rounded text-primary w-4 h-4" type="checkbox"></div>
        </div>
      </div>
      <button onclick="showToast('Profile settings saved successfully!')" class="w-full py-md bg-primary-container text-white font-label-md text-label-md rounded-xl hover:opacity-90 transition-opacity flex items-center justify-center gap-sm shadow-sm">
        <span class="material-symbols-outlined">save</span>Save Changes
      </button>
      <button onclick="alert('Password reset link sent to your registered mobile.')" class="w-full py-md bg-surface border border-outline-variant text-on-surface font-label-md text-label-md rounded-xl hover:bg-surface-container transition-colors flex items-center justify-center gap-sm">
        <span class="material-symbols-outlined">lock_reset</span>Change Password
      </button>
    </div>
  </div>
</div>
`;
}

