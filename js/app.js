
import { ROUTE_MAP, NAV_MAP, PAGE_TITLES, currentPage, navigate } from "./router.js";
import { renderSidebar } from "./components/sidebar.js";
import { renderHeader } from "./components/header.js";
import { renderMobileNav } from "./components/mobileNav.js";
import { showToast } from "./components/toast.js";

import * as DashboardPage from "./pages/dashboard.js";
import * as MarketplacePage from "./pages/marketplace.js";
import * as WheatAnalysisPage from "./pages/wheatAnalysis.js";
import * as ListingsPage from "./pages/listings.js";
import * as NewListingPage from "./pages/newListing.js";
import * as BuyerPage from "./pages/buyer.js";
import * as FinancialsPage from "./pages/financials.js";
import * as NewEntryPage from "./pages/newEntry.js";
import * as LogisticsPage from "./pages/logistics.js";
import * as NewShipmentPage from "./pages/newShipment.js";
import * as AnalyticsPage from "./pages/analytics.js";
import * as SettingsPage from "./pages/settings.js";
import * as HelpPage from "./pages/help.js";

const pages = {
  "dashboard": DashboardPage,
  "marketplace": MarketplacePage,
  "marketplace/wheat": WheatAnalysisPage,
  "marketplace/listings": ListingsPage,
  "marketplace/listings/new": NewListingPage,
  "marketplace/buyer": BuyerPage,
  "financials": FinancialsPage,
  "financials/new": NewEntryPage,
  "logistics": LogisticsPage,
  "logistics/new": NewShipmentPage,
  "analytics": AnalyticsPage,
  "settings": SettingsPage,
  "help": HelpPage
};

window.navigate = navigate;
window.showToast = showToast;

window.publishListing = function(e) {
  e.preventDefault();
  const crop = document.getElementById("new-crop").value || "Wheat";
  const qty = (document.getElementById("new-qty").value || "400") + " " + (document.getElementById("new-unit").value || "Qt");
  const price = "₹" + parseInt(document.getElementById("new-price").value || 3250).toLocaleString();
  const location = document.getElementById("new-location").value || "Indore, MP";

  showToast(`Listing for ${crop} (${qty}) published successfully!`);
  navigate("marketplace/listings");
};

window.saveFinancialEntry = function(e) {
  e.preventDefault();
  const desc = document.getElementById("fin-desc").value || "New Transaction";
  const amount = parseInt(document.getElementById("fin-amount").value || 50000).toLocaleString();
  showToast(`Financial entry "${desc}" (₹${amount}) saved!`);
  navigate("financials");
};

window.createShipment = function(e) {
  e.preventDefault();
  const id = document.getElementById("ship-id").value || "FF-1028";
  const crop = document.getElementById("ship-crop").value || "Wheat";
  showToast(`Shipment ${id} (${crop}) created successfully!`);
  navigate("logistics");
};

function renderCurrentPage() {
  const pageKey = currentPage();
  const pageModule = pages[pageKey] || DashboardPage;
  const view = document.getElementById("page-view");
  
  const navKey = NAV_MAP[pageKey] || pageKey;
  renderSidebar(navKey);
  renderHeader(PAGE_TITLES[pageKey] || "FarmForward");
  renderMobileNav(navKey);

  if (view && pageModule) {
    view.innerHTML = pageModule.render();
    view.scrollTop = 0;
    if (pageModule.initCharts) {
      pageModule.initCharts();
    }
  }
}

window.addEventListener("hashchange", renderCurrentPage);
window.addEventListener("DOMContentLoaded", () => {
  if (!location.hash) location.hash = "#/dashboard";
  else renderCurrentPage();
});
