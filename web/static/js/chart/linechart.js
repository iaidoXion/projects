function lineChart() {
  var ctx = document.getElementById('lineChart');
  var lineChart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
      datasets: [{
        color: app.color.theme,
        backgroundColor: 'rgba('+ app.color.themeRgb +', .2)',
        borderColor: app.color.theme,
        borderWidth: 1.5,
        pointBackgroundColor: app.color.white,
        pointBorderWidth: 1.5,
        pointRadius: 4,
        pointHoverBackgroundColor: app.color.theme,
        pointHoverBorderColor: app.color.white,
        pointHoverRadius: 7,
        label: 'Total Sales',
        data: [12, 19, 4, 5, 2, 3]
      }]
    }
  });
};