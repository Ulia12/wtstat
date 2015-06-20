# -*- coding: utf-8
"""
Построение гистограммы по входным параметрам
"""
import sys
import datetime
from jinja2 import Environment
HTML = u'''\
<html>
 <head>
  <meta charset="utf-8">
  <title>{{ title }}</title>
  <script src="https://www.google.com/jsapi"></script>
  <script>
   google.load("visualization", "1", {packages:["corechart"]});
   google.setOnLoadCallback(drawChart);
   function drawChart() {
    var data = google.visualization.arrayToDataTable([
     ['Время', 'Процент'],
     ['02:00', {{ p1 }}],
     ['06:00', {{ p2 }}],
     ['10:00', {{ p3 }}],
     ['14:00', {{ p4 }}],
     ['18:00', {{ p5 }}],
     ['22:00', {{ p6 }}]
    ]);
    var options = {
     title: '{{ title }}',
     hAxis: {title: 'Время'},
     vAxis: {title: 'Процент'}
    };
    var chart = new google.visualization.ColumnChart(document.getElementById('oil'));
    chart.draw(data, options);
   }
  </script>
 </head>
 <body>
  <div id="oil" style="width: 500px; height: 400px;"></div>
 </body>
 </html>'''

now_time = datetime.datetime.utcnow()
y = [sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6]]

def print_html_doc():
    return Environment().from_string(HTML).render(title = u'Статистика '+str(now_time.strftime("%d.%m.%Y")),p1=y[0],p2=y[1],p3=y[2],p4=y[3],p5=y[4],p6=y[5])

f = open('gist.html', 'w')
f.write(str(print_html_doc().encode('utf-8')))