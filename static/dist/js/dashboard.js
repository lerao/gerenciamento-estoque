google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(drawCharts);

function drawCharts(){
  drawChart();
  drawChart2();
}
function drawChart() {

  var data = google.visualization.arrayToDataTable([
    ['Categorias', 'Quantidade'],
    ['Carnes',     4],
    ['Gelados',      2],
    ['Bebidas Alcoolicas',  15],
    ['Laticínios', 10],
    ['Queijos',    5]
  ]);

  var options = {
    title: 'Categorias No Estoque'
  };

  var chart = new google.visualization.PieChart(document.getElementById('piechart'));

  chart.draw(data, options);
}

function drawChart2() {

  var data = google.visualization.arrayToDataTable([
    ['Categorias', 'Quantidade'],
    ['Carnes',     4],
    ['Gelados',      2],
    ['Bebidas Alcoolicas',  15],
    ['Laticínios', 10],
    ['Queijos',    5]
  ]);

  var options = {
    title: 'Categorias No Estoque'
  };

  var chart = new google.visualization.BarChart(document.getElementById('piechart2'));

  chart.draw(data, options);
}