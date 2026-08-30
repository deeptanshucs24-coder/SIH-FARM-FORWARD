
export const initialListings = [
  { crop: "Wheat (Sharbati)", date: "Aug 22, 2024", qty: "500 Qt", price: "₹3,150 / Qt", location: "Indore, MP", status: "Active", responses: "6 buyers", icon: "fa-wheat-awn" },
  { crop: "Soybean", date: "Aug 20, 2024", qty: "300 Qt", price: "₹4,800 / Qt", location: "Indore, MP", status: "Active", responses: "3 buyers", icon: "fa-seedling" },
  { crop: "Tomato (Hybrid)", date: "Aug 18, 2024", qty: "120 Qt", price: "₹2,050 / Qt", location: "Pune, MH", status: "Active", responses: "2 buyers", icon: "fa-leaf" }
];

export const initialTransactions = [
  { date: "Aug 24, 2024", desc: "Wheat sale (Contract #A24)", cat: "Crop Sales", amount: "+₹4,50,000", status: "Received", isIncome: true },
  { date: "Aug 22, 2024", desc: "Soybean sale (Spot Market)", cat: "Crop Sales", amount: "+₹1,20,000", status: "Pending", isIncome: true },
  { date: "Aug 18, 2024", desc: "Fertilizer purchase (DAP)", cat: "Inputs", amount: "-₹85,000", status: "Paid", isIncome: false },
  { date: "Aug 15, 2024", desc: "Logistics — Harvest Transport", cat: "Transport", amount: "-₹32,000", status: "Paid", isIncome: false }
];

export const initialShipments = [
  { id: "FF-1024", crop: "Wheat", qty: "500 Qt", route: "Indore → Delhi", status: "In Transit", eta: "Today, 6:30 PM" },
  { id: "FF-1025", crop: "Soybean", qty: "300 Qt", route: "Indore → Jaipur", status: "In Transit", eta: "Tomorrow" },
  { id: "FF-1026", crop: "Tomato", qty: "120 Qt", route: "Pune → Mumbai", status: "Scheduled", eta: "Aug 30" },
  { id: "FF-1027", crop: "Onion", qty: "200 Qt", route: "Nashik → Hyderabad", status: "Delivered", eta: "Aug 26" }
];
