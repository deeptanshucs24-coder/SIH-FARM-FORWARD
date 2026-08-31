import { initialTransactions } from "../data/mockData.js";

if (!window.transactions) {
  window.transactions = [...initialTransactions];
}
if (window.extraRevenue === undefined) window.extraRevenue = 0;
if (window.extraExpenses === undefined) window.extraExpenses = 0;

export function render() {
  const currentRevenue = 2450000 + window.extraRevenue;
  const currentExpenses = 872500 + window.extraExpenses;
  const currentProfit = currentRevenue - currentExpenses;

  const transactionRows = window.transactions.map(item => {
    const amountColor = item.isIncome ? "text-primary-container font-semibold" : "text-on-surface font-medium";
    const statusBg = (item.status === "Received" || item.status === "Paid") 
      ? "bg-secondary-container text-on-secondary-container" 
      : "bg-surface-variant text-on-surface-variant";
    
    const amountDisplay = item.amount;
    const statusDisplay = item.status;
    
    return `
      <tr class="border-b border-outline-variant/50 hover:bg-surface-container-lowest transition-colors">
        <td class="p-4 text-on-surface-variant">${item.date}</td>
        <td class="p-4 font-medium">${item.desc}</td>
        <td class="p-4">${item.cat}</td>
        <td class="p-4 text-right ${amountColor}">${amountDisplay}</td>
        <td class="p-4 text-center">
          <span class="inline-block px-2 py-1 ${statusBg} rounded-full font-label-md text-[10px] uppercase tracking-wider">${statusDisplay}</span>
        </td>
      </tr>`;
  }).join("");

  return `<div class="p-margin max-w-7xl mx-auto pb-24 md:pb-margin">
  <div class="flex flex-col md:flex-row md:items-end justify-between gap-md mb-xl">
    <div>
      <h1 class="font-headline-lg text-headline-lg text-primary">Financials</h1>
      <p class="font-body-md text-body-md text-on-surface-variant mt-xs">Track revenue, expenses, and cash flow for your farm.</p>
    </div>
    <div class="flex items-center gap-md shrink-0">
      <button class="bg-surface text-on-surface border border-outline-variant font-label-md text-label-md px-md py-sm rounded-lg hover:bg-surface-container-low transition-colors shadow-sm flex items-center gap-xs" onclick="alert('Exporting Financial Report CSV...')"><span class="material-symbols-outlined" style="font-size:18px">download</span>Export</button>
      <button onclick="navigate('financials/new')" class="bg-primary-container text-on-primary font-label-md text-label-md px-md py-sm rounded-lg hover:opacity-90 transition-opacity shadow-sm flex items-center gap-xs cursor-pointer"><span class="material-symbols-outlined" style="font-size:18px">add</span>New Entry</button>
    </div>
  </div>
  <!-- KPI Cards -->
  <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-md mb-xl">
    <div class="bg-surface-container-lowest border border-outline-variant p-md rounded-[12px] shadow-[0_2px_4px_rgba(0,0,0,0.05)]">
      <div class="flex justify-between items-start mb-sm"><span class="font-label-md text-label-md text-on-surface-variant uppercase">Total Revenue</span><div class="p-1.5 bg-secondary-container rounded-lg"><span class="material-symbols-outlined text-tertiary-container text-[20px]">trending_up</span></div></div>
      <div class="font-headline-lg text-headline-lg text-on-surface font-semibold mb-xs">₹${currentRevenue.toLocaleString('en-IN')}</div>
      <div class="flex items-center gap-1 font-body-sm text-body-sm text-primary-container"><span class="material-symbols-outlined text-[16px]">arrow_upward</span><span>+12.4% vs last year</span></div>
    </div>
    <div class="bg-surface-container-lowest border border-outline-variant p-md rounded-[12px] shadow-[0_2px_4px_rgba(0,0,0,0.05)]">
      <div class="flex justify-between items-start mb-sm"><span class="font-label-md text-label-md text-on-surface-variant uppercase">Total Expenses</span><div class="p-1.5 bg-surface-container-highest rounded-lg"><span class="material-symbols-outlined text-on-surface-variant text-[20px]">trending_down</span></div></div>
      <div class="font-headline-lg text-headline-lg text-on-surface font-semibold mb-xs">₹${currentExpenses.toLocaleString('en-IN')}</div>
      <div class="flex items-center gap-1 font-body-sm text-body-sm text-on-surface-variant"><span class="material-symbols-outlined text-[16px]">arrow_downward</span><span>-3.2% vs last year</span></div>
    </div>
    <div class="bg-surface-container-lowest border border-outline-variant p-md rounded-[12px] shadow-[0_2px_4px_rgba(0,0,0,0.05)] relative overflow-hidden">
      <div class="absolute right-0 top-0 w-24 h-24 bg-secondary-fixed-dim/20 rounded-full blur-xl -mr-8 -mt-8 pointer-events-none"></div>
      <div class="flex justify-between items-start mb-sm relative z-10"><span class="font-label-md text-label-md text-on-surface-variant uppercase">Net Profit</span><div class="p-1.5 bg-tertiary-fixed rounded-lg"><span class="material-symbols-outlined text-tertiary-fixed-variant text-[20px]">account_balance_wallet</span></div></div>
      <div class="font-headline-lg text-headline-lg text-primary font-bold mb-xs relative z-10">₹${currentProfit.toLocaleString('en-IN')}</div>
      <div class="flex items-center gap-1 font-body-sm text-body-sm text-primary-container relative z-10"><span class="material-symbols-outlined text-[16px]">arrow_upward</span><span>+18.1% vs last year</span></div>
    </div>
    <div class="bg-surface-container-lowest border border-outline-variant p-md rounded-[12px] shadow-[0_2px_4px_rgba(0,0,0,0.05)]">
      <div class="flex justify-between items-start mb-sm"><span class="font-label-md text-label-md text-on-surface-variant uppercase">Pending Payments</span><div class="p-1.5 bg-error-container rounded-lg"><span class="material-symbols-outlined text-error text-[20px]">pending_actions</span></div></div>
      <div class="font-headline-lg text-headline-lg text-on-surface font-semibold mb-xs">₹3,45,000</div>
      <div class="flex items-center gap-1 font-body-sm text-body-sm text-on-surface-variant"><span>2 Invoices due this week</span></div>
    </div>
  </div>
  <!-- Chart + Right Rail -->
  <div class="flex flex-col lg:flex-row gap-xl">
    <div class="flex-1 flex flex-col gap-xl">
      <!-- Cash Flow Chart -->
      <div class="bg-surface-container-lowest border border-outline-variant rounded-[12px] p-md shadow-[0_2px_4px_rgba(0,0,0,0.05)]">
        <div class="flex justify-between items-center mb-md">
          <h3 class="font-headline-md text-headline-md text-on-surface font-bold">Cash Flow Overview</h3>
          <select class="bg-surface-container-low border border-outline-variant rounded-lg px-3 py-1.5 text-body-sm font-body-sm text-on-surface-variant focus:border-primary focus:ring-0">
            <option>Last 6 Months</option><option>This Year</option>
          </select>
        </div>
        <div class="flex gap-4 text-xs mb-3">
          <div class="flex items-center gap-1"><div class="w-3 h-3 rounded-sm" style="background:#1b4332"></div><span class="text-on-surface-variant">Inflow</span></div>
          <div class="flex items-center gap-1"><div class="w-3 h-3 rounded-sm" style="background:#b3cdb7"></div><span class="text-on-surface-variant">Outflow</span></div>
        </div>
        <div class="w-full h-[260px]">
          <svg class="w-full h-full" preserveAspectRatio="none" viewBox="0 0 600 260">
            <line stroke="#e0e3e8" stroke-width="1" x1="40" x2="580" y1="220" y2="220"/>
            <line stroke="#e0e3e8" stroke-width="1" x1="40" x2="580" y1="170" y2="170"/>
            <line stroke="#e0e3e8" stroke-width="1" x1="40" x2="580" y1="120" y2="120"/>
            <line stroke="#e0e3e8" stroke-width="1" x1="40" x2="580" y1="70" y2="70"/>
            <line stroke="#e0e3e8" stroke-width="1" x1="40" x2="580" y1="20" y2="20"/>
            <text fill="#717973" font-size="11" text-anchor="end" x="35" y="224">₹0</text>
            <text fill="#717973" font-size="11" text-anchor="end" x="35" y="174">₹1L</text>
            <text fill="#717973" font-size="11" text-anchor="end" x="35" y="124">₹2L</text>
            <text fill="#717973" font-size="11" text-anchor="end" x="35" y="74">₹3L</text>
            <text fill="#717973" font-size="11" text-anchor="end" x="35" y="24">₹4L</text>
            <text fill="#717973" font-size="11" text-anchor="middle" x="100" y="244">Mar</text>
            <text fill="#717973" font-size="11" text-anchor="middle" x="190" y="244">Apr</text>
            <text fill="#717973" font-size="11" text-anchor="middle" x="280" y="244">May</text>
            <text fill="#717973" font-size="11" text-anchor="middle" x="370" y="244">Jun</text>
            <text fill="#717973" font-size="11" text-anchor="middle" x="460" y="244">Jul</text>
            <text fill="#717973" font-size="11" text-anchor="middle" x="550" y="244">Aug</text>
            <rect fill="#1b4332" height="160" rx="2" width="15" x="85" y="60"/><rect fill="#b3cdb7" height="72" rx="2" width="15" x="105" y="148"/>
            <rect fill="#1b4332" height="190" rx="2" width="15" x="175" y="30"/><rect fill="#b3cdb7" height="84" rx="2" width="15" x="195" y="136"/>
            <rect fill="#1b4332" height="200" rx="2" width="15" x="265" y="20"/><rect fill="#b3cdb7" height="96" rx="2" width="15" x="285" y="124"/>
            <rect fill="#1b4332" height="210" rx="2" width="15" x="355" y="10"/><rect fill="#b3cdb7" height="100" rx="2" width="15" x="375" y="120"/>
            <rect fill="#1b4332" height="205" rx="2" width="15" x="445" y="15"/><rect fill="#b3cdb7" height="90" rx="2" width="15" x="465" y="130"/>
            <rect fill="#1b4332" height="215" rx="2" width="15" x="535" y="5"/><rect fill="#b3cdb7" height="108" rx="2" width="15" x="555" y="112"/>
          </svg>
        </div>
      </div>
      <!-- Transactions Table -->
      <div class="bg-surface-container-lowest border border-outline-variant rounded-[12px] shadow-[0_2px_4px_rgba(0,0,0,0.05)] overflow-hidden">
        <div class="p-md border-b border-outline-variant flex justify-between items-center bg-surface-bright">
          <h3 class="font-headline-md text-headline-md text-on-surface">Recent Transactions</h3>
          <a class="font-label-md text-label-md text-primary-container hover:underline" href="#/financials">View All</a>
        </div>
        <div class="overflow-x-auto">
          <table class="w-full text-left border-collapse">
            <thead><tr class="bg-surface font-label-md text-label-md text-on-surface-variant uppercase border-b border-outline-variant">
              <th class="p-4 font-semibold">Date</th><th class="p-4 font-semibold">Description</th><th class="p-4 font-semibold">Category</th><th class="p-4 font-semibold text-right">Amount</th><th class="p-4 font-semibold text-center">Status</th>
            </tr></thead>
            <tbody class="font-body-sm text-body-sm text-on-surface" id="fin-tbl-body">
              ${transactionRows}
            </tbody>
          </table>
        </div>
      </div>
    </div>
    <!-- Right Rail -->
    <div class="w-full lg:w-[320px] flex flex-col gap-xl">
      <div class="bg-primary-container text-on-primary-container rounded-[12px] p-md shadow-lg relative overflow-hidden">
        <div class="absolute inset-0 opacity-10 pointer-events-none" style="background-image:radial-gradient(circle at 100% 0%,#ffffff 0%,transparent 50%)"></div>
        <div class="flex items-center gap-3 mb-md relative z-10">
          <div class="p-2 bg-on-primary-fixed-variant rounded-lg"><span class="material-symbols-outlined text-tertiary-fixed">health_and_safety</span></div>
          <h3 class="font-headline-md text-headline-md text-on-primary">Financial Health</h3>
        </div>
        <div class="mb-4 relative z-10">
          <div class="flex justify-between items-end mb-1"><span class="font-label-md text-label-md opacity-80 uppercase tracking-wider">Status</span><span class="font-headline-md text-headline-md text-on-primary font-bold">Strong</span></div>
          <div class="w-full bg-on-primary-fixed-variant rounded-full h-2"><div class="bg-tertiary-fixed h-2 rounded-full" style="width:85%"></div></div>
        </div>
        <div class="grid grid-cols-2 gap-4 mt-6 relative z-10">
          <div><div class="font-label-md text-label-md opacity-80 mb-1">Profit Margin</div><div class="font-headline-md text-headline-md text-on-primary font-semibold">64.4%</div></div>
          <div><div class="font-label-md text-label-md opacity-80 mb-1">Rev Growth</div><div class="font-headline-md text-headline-md text-tertiary-fixed font-semibold">+12.8%</div></div>
        </div>
      </div>
      <div class="bg-surface-container-lowest border border-outline-variant rounded-[12px] p-md shadow-[0_2px_4px_rgba(0,0,0,0.05)]">
        <h4 class="font-headline-md text-headline-md text-on-surface mb-md font-bold">Upcoming Payments</h4>
        <div class="flex flex-col gap-sm">
          <div class="flex justify-between items-center py-sm border-b border-outline-variant/50">
            <div><div class="font-body-sm font-medium text-on-surface">Tractor Service</div><div class="font-label-md text-label-md text-on-surface-variant">Sep 1, 2024</div></div>
            <div class="font-body-sm font-bold text-error">₹18,000</div>
          </div>
          <div class="flex justify-between items-center py-sm border-b border-outline-variant/50">
            <div><div class="font-body-sm font-medium text-on-surface">Irrigation Loan EMI</div><div class="font-label-md text-label-md text-on-surface-variant">Sep 5, 2024</div></div>
            <div class="font-body-sm font-bold text-error">₹3,27,000</div>
          </div>
          <div class="flex justify-between items-center py-sm">
            <div><div class="font-body-sm font-medium text-on-surface">Seed Purchase</div><div class="font-label-md text-label-md text-on-surface-variant">Sep 12, 2024</div></div>
            <div class="font-body-sm font-bold text-on-surface">₹42,000</div>
          </div>
        </div>
      </div>
      <div class="bg-surface-container-lowest border border-outline-variant rounded-[12px] p-md shadow-[0_2px_4px_rgba(0,0,0,0.05)]">
        <h4 class="font-headline-md text-headline-md text-on-surface mb-md font-bold">Quick Actions</h4>
        <div class="flex flex-col gap-sm">
          <button onclick="alert('Invoice generator modal opened.')" class="w-full py-sm px-md bg-secondary-container text-on-secondary-container font-label-md text-label-md rounded-lg hover:bg-secondary-fixed transition-colors flex items-center gap-sm"><span class="material-symbols-outlined text-[18px]">receipt_long</span>Generate Invoice</button>
          <button onclick="alert('Bank Linking portal opened.')" class="w-full py-sm px-md bg-surface-container border border-outline-variant text-on-surface font-label-md text-label-md rounded-lg hover:bg-surface-container-high transition-colors flex items-center gap-sm"><span class="material-symbols-outlined text-[18px]">account_balance</span>Link Bank Account</button>
          <button onclick="alert('Tax Summary downloaded.')" class="w-full py-sm px-md bg-surface-container border border-outline-variant text-on-surface font-label-md text-label-md rounded-lg hover:bg-surface-container-high transition-colors flex items-center gap-sm"><span class="material-symbols-outlined text-[18px]">bar_chart</span>View Tax Summary</button>
        </div>
      </div>
    </div>
  </div>
</div>`;
}
