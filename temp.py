import plotly.express as px
df = px.data.iris()
plot = px.scatter(data_frame=df, x="petal_width", y="petal_length", color='species', title="My Graph")
div = plot.write_html("temp2.html",full_html=True, include_plotlyjs="cdn")
