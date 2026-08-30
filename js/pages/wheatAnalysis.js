
export function render() {
  return ``;
}

let wheatChartInstance = null, wheatSparkInstance = null;

export function initCharts() {
  if (wheatChartInstance) { wheatChartInstance.destroy(); wheatChartInstance = null; }
  if (wheatSparkInstance) { wheatSparkInstance.destroy(); wheatSparkInstance = null; }
  
  setTimeout(() => {
    const ctx = document.getElementById("wheatChart");
    if (ctx) {
      const grad = ctx.getContext("2d").createLinearGradient(0,0,0,250);
      grad.addColorStop(0,"rgba(27,67,50,0.2)"); grad.addColorStop(1,"rgba(27,67,50,0)");
      wheatChartInstance = new Chart(ctx, {
        type:"line",
        data:{
          labels:["Oct 1","Oct 8","Oct 15","Oct 22","Oct 29","Nov 5"],
          datasets:[
            {label:"Actual",data:[2930,3080,3160,3070,3190,3200],borderColor:"#1b4332",backgroundColor:grad,borderWidth:2,pointBackgroundColor:"#fff",pointBorderColor:"#1b4332",pointBorderWidth:2,pointRadius:4,fill:true,tension:0.4},
            {label:"7-Day MA",data:[2900,3020,3080,3080,3150,3180],borderColor:"#86efac",borderWidth:2,borderDash:[5,5],pointRadius:0,fill:false,tension:0.4}
          ]
        },
        options:{responsive:true,maintainAspectRatio:false,plugins:{legend:{display:false}},scales:{y:{min:2800,max:3300,ticks:{stepSize:100},grid:{color:"#f3f4f6"}},x:{grid:{display:false}}}}
      });
    }
    const spark = document.getElementById("wheatSparkline");
    if (spark) {
      const sg = spark.getContext("2d").createLinearGradient(0,0,0,60);
      sg.addColorStop(0,"rgba(27,67,50,0.3)"); sg.addColorStop(1,"rgba(27,67,50,0)");
      wheatSparkInstance = new Chart(spark, {
        type:"line",
        data:{labels:["1","2","3","4","5","6","7"],datasets:[{data:[10,15,20,18,25,22,35],borderColor:"#1b4332",borderWidth:2,backgroundColor:sg,fill:true,pointRadius:3,pointBackgroundColor:"#1b4332",tension:0.3}]},
        options:{responsive:true,maintainAspectRatio:false,plugins:{legend:{display:false},tooltip:{enabled:false}},scales:{x:{display:false},y:{display:false,min:0,max:40}}}
      });
    }
  }, 50);
}
