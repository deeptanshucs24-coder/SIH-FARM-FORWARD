
export function showToast(msg) {
  let toast = document.getElementById("global-toast");
  if (!toast) {
    toast = document.createElement("div");
    toast.id = "global-toast";
    toast.className = "fixed top-4 right-4 z-50 bg-primary-container text-primary-fixed px-lg py-md rounded-xl shadow-lg border border-primary-fixed/30 font-label-md text-label-md flex items-center gap-sm transition-all duration-300";
    document.body.appendChild(toast);
  }
  toast.innerHTML = `<span class="material-symbols-outlined text-primary-fixed">check_circle</span><span>${msg}</span>`;
  toast.style.display = "flex";
  setTimeout(() => { toast.style.display = "none"; }, 3500);
}
