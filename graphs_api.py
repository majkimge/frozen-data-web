import requests
from plotly.io import from_json
from plotly.offline import plot
import plotly as py
import json

def load_competitors(mysql, userid):
  with mysql.connect() as conn:
    with conn.cursor() as cursor:
      cursor.execute("SELECT address FROM addresses WHERE userid=%(userid)s", {"userid":userid})
      data = cursor.fetchall()
  if len(data) != 1:
    return None
  address = data[0][0]

  with mysql.connect() as conn:
    with conn.cursor() as cursor:
      cursor.execute("SELECT name FROM users WHERE id=%(userid)s", {"userid":userid})
      data = cursor.fetchall()
  if len(data) != 1:
    return None
  name = data[0][0]

  with mysql.connect() as conn:
    with conn.cursor() as cursor:
      cursor.execute("SELECT address,competition_name FROM competition_addresses WHERE userid=%(userid)s", {"userid":userid})
      data = cursor.fetchall()

  competitors = {d[0]: d[1] for d in data}

  return (name, address,competitors)

def fetch_graphs_from_api(name, address, competitors):
  url = "http://18.130.124.104/getGraphs/"
  graphs = ["plot_eth_spent_graph_customers", "plot_customers_graph", "plot_eth_spent_graph_everyone", "create_distribution_plot", "get_pie_competition"]

  figs = []
  for graph in graphs:
    print("Fetching graph...")
    data = {"address_name_tuple1" : address,"address_name_tuple2" : name, "competition_addresses_dict" : competitors, "func_to_run":graph}
    x = requests.post(url, json=data)
    data = json.loads(x.text)
    fig = from_json(data)
    layout = py.graph_objects.Layout(paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)')
    fig.update_layout(layout, template="plotly_dark")
    #fig_div = fig.to_html(full_html=False, include_plotlyjs=False, default_height="10rem")
    fig_div = plot(fig, include_plotlyjs=False, output_type='div')
    figs.append(fig_div)
  
  return figs
