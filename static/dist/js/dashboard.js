google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(drawChart);

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