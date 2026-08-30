/**
 * router.js — Hash-based SPA router
 * Maps location.hash → page key, delegates rendering to app.js
 */

export const ROUTE_MAP = {
  '': 'dashboard', '#/': 'dashboard', '#/dashboard': 'dashboard',
  '#/marketplace': 'marketplace',
  '#/marketplace/wheat': 'marketplace/wheat',
  '#/marketplace/listings': 'marketplace/listings',
  '#/marketplace/listings/new': 'marketplace/listings/new',
  '#/marketplace/buyer': 'marketplace/buyer',
  '#/financials': 'financials',
  '#/financials/new': 'financials/new',
  '#/logistics': 'logistics',
  '#/logistics/new': 'logistics/new',
  '#/analytics': 'analytics',
  '#/settings': 'settings',
  '#/help': 'help'
};

export const NAV_MAP = {
  'dashboard': 'dashboard',
  'marketplace': 'marketplace',
  'marketplace/wheat': 'marketplace',
  'marketplace/listings': 'marketplace',
  'marketplace/listings/new': 'marketplace',
  'marketplace/buyer': 'marketplace',
  'financials': 'financials',
  'financials/new': 'financials',
  'logistics': 'logistics',
  'logistics/new': 'logistics',
  'analytics': 'analytics',
  'settings': 'settings',
  'help': 'help'
};

const HASH_MAP = {
  'dashboard': '#/dashboard',
  'marketplace': '#/marketplace',
  'marketplace/wheat': '#/marketplace/wheat',
  'marketplace/listings': '#/marketplace/listings',
  'marketplace/listings/new': '#/marketplace/listings/new',
  'marketplace/buyer': '#/marketplace/buyer',
  'financials': '#/financials',
  'financials/new': '#/financials/new',
  'logistics': '#/logistics',
  'logistics/new': '#/logistics/new',
  'analytics': '#/analytics',
  'settings': '#/settings',
  'help': '#/help'
};

export const PAGE_TITLES = {
  'dashboard': 'Dashboard',
  'marketplace': 'Marketplace',
  'marketplace/wheat': 'Wheat Analysis',
  'marketplace/listings': 'Active Listings',
  'marketplace/listings/new': 'Create Listing',
  'marketplace/buyer': 'Buyer Details',
  'financials': 'Financials',
  'financials/new': 'New Entry',
  'logistics': 'Logistics',
  'logistics/new': 'New Shipment',
  'analytics': 'Analytics',
  'settings': 'Settings',
  'help': 'Help & Support'
};

/** Navigate to a page key */
export function navigate(page) {
  location.hash = HASH_MAP[page] || '#/dashboard';
}

/** Return the current page key from location.hash */
export function currentPage() {
  return ROUTE_MAP[location.hash] || 'dashboard';
}
