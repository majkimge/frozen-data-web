import requests

def load_addresses(mysql, userid):
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

  graphs = fetch_graphs_from_api(name, address, competitors)

  return (name, address,competitors)

def fetch_graphs_from_api(name, address, competitors):
  url = "http://18.130.124.104/getGraphs/"
  graphs = ["plot_eth_spent_graph_customers", "plot_customers_graph", "plot_eth_spent_graph_everyone"]

  for graph in graphs:
    print("Fetching graph...")
    data = {"address_name_tuple1" : address,"address_name_tuple2" : name, "competition_addresses_dict" : competitors, "func_to_run":"plot_eth_spent_graph_everyone"}
    x = requests.post(url, json=data)
    print(f"Size: {len(data)}")
