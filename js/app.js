import { ROUTE_MAP, NAV_MAP, PAGE_TITLES, currentPage, navigate } from "./router.js";
import { renderSidebar } from "./components/sidebar.js";
import { renderHeader } from "./components/header.js";
import { renderMobileNav } from "./components/mobileNav.js";
import { showToast } from "./components/toast.js";
import { initialListings, initialTransactions, initialShipments } from "./data/mockData.js";

if (!window.listings) window.listings = [...initialListings];
if (!window.transactions) window.transactions = [...initialTransactions];
if (!window.shipments) window.shipments = [...initialShipments];
if (window.extraRevenue === undefined) window.extraRevenue = 0;
if (window.extraExpenses === undefined) window.extraExpenses = 0;

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
  const variety = document.getElementById("new-variety").value || "";
  const qtyVal = document.getElementById("new-qty").value || "400";
  const unit = document.getElementById("new-unit").value || "Qt";
  const priceVal = document.getElementById("new-price").value || "3250";
  const location = document.getElementById("new-location").value || "Indore, MP";

  const formattedCrop = variety ? `${crop} (${variety})` : crop;
  const formattedQty = `${qtyVal} ${unit}`;
  const formattedPrice = `₹${parseInt(priceVal).toLocaleString()} / ${unit}`;

  const newListing = {
    crop: formattedCrop,
    date: new Date().toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' }),
    qty: formattedQty,
    price: formattedPrice,
    location: location,
    status: "Active",
    responses: "0 buyers",
    icon: "fa-seedling"
  };

  if (window.listings) {
    window.listings.unshift(newListing);
  }

  showToast(`Listing for ${formattedCrop} (${formattedQty}) published successfully!`);
  navigate("marketplace/listings");
};

window.saveFinancialEntry = function(e) {
  e.preventDefault();
  const entryTypeEl = document.querySelector('input[name="entry_type"]:checked');
  const entryType = entryTypeEl ? entryTypeEl.value : "Income";
  const desc = document.getElementById("fin-desc").value || "New Entry";
  const amountVal = document.getElementById("fin-amount").value || "5000";
  const cat = document.getElementById("fin-cat").value || "Crop Sales";
  const dateVal = document.getElementById("fin-date").value || new Date().toISOString().split('T')[0];

  const parsedDate = new Date(dateVal);
  const formattedDate = parsedDate.toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' });
  const isIncome = entryType === "Income";
  const amountStr = (isIncome ? "+" : "-") + "₹" + parseInt(amountVal).toLocaleString();

  const newTx = {
    date: formattedDate,
    desc: desc,
    cat: cat,
    amount: amountStr,
    status: isIncome ? "Received" : "Paid",
    isIncome: isIncome
  };

  if (window.transactions) {
    window.transactions.unshift(newTx);
  }

  const amountInt = parseInt(amountVal);
  if (isIncome) {
    window.extraRevenue += amountInt;
  } else {
    window.extraExpenses += amountInt;
  }

  showToast(`Financial entry "${desc}" (${amountStr}) saved!`);
  navigate("financials");
};

window.createShipment = function(e) {
  e.preventDefault();
  const id = document.getElementById("ship-id").value || "FF-1028";
  const crop = document.getElementById("ship-crop").value || "Wheat";
  const qty = document.getElementById("ship-qty").value || "400 Qt";
  const source = document.getElementById("ship-source").value || "Indore";
  const destVal = document.getElementById("ship-dest").value || "Delhi";
  const etaVal = document.getElementById("ship-eta").value || "Tomorrow";

  const destClean = destVal.split(',')[0].trim();
  const routeStr = `Indore → ${destClean}`;

  let etaStr = etaVal;
  try {
    const d = new Date(etaVal);
    etaStr = d.toLocaleDateString('en-US', { month: 'short', day: 'numeric' });
  } catch (err) {}

  const newShipment = {
    id: id,
    crop: crop,
    qty: qty,
    route: routeStr,
    status: "Scheduled",
    eta: etaStr
  };

  if (window.shipments) {
    window.shipments.unshift(newShipment);
  }

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
