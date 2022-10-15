import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
from pandas import ExcelWriter
import requests
from bs4 import BeautifulSoup

#----------- Make Graph Function -------------------------

def make_graph(stock_data, revenue_data, stock):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("Historical Share Price", "Historical Revenue"), vertical_spacing = .3)
    stock_data_specific = stock_data[stock_data.Date <= '2021--06-14']
    revenue_data_specific = revenue_data[revenue_data.Date <= '2021-04-30']
    fig.add_trace(go.Scatter(x=pd.to_datetime(stock_data_specific.Date, infer_datetime_format=True), y=stock_data_specific.Close.astype("float"), name="Share Price"), row=1, col=1)
    fig.add_trace(go.Scatter(x=pd.to_datetime(revenue_data_specific.Date, infer_datetime_format=True), y=revenue_data_specific.Revenue.astype("float"), name="Revenue"), row=2, col=1)
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)
    fig.update_layout(showlegend=False,
    height=900,
    title=stock,
    xaxis_rangeslider_visible=True)
    fig.show()

#------------------- TESLA ---------------------------------------
# Tesla Stock Data
tesla = yf.Ticker('TSLA')
tesla_data = tesla.history(period='max')
tesla_data.reset_index(inplace=True)
# Tesla Revenue Data
url = "https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10"
html_data = requests.get(url).text
soup = BeautifulSoup(html_data, 'html5lib')
tables = pd.read_html(html_data)
tesla_revenue = tables[1].rename(columns={'Tesla Quarterly Revenue(Millions of US $)':'Date', 'Tesla Quarterly Revenue(Millions of US $).1':'Revenue'})
tesla_revenue["Revenue"] = tesla_revenue['Revenue'].str.replace(',|\$',"")
tesla_revenue.dropna(inplace=True)
tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""]

writer = ExcelWriter('Tesla.xlsx')
tesla_data.to_excel(writer, 'Tesla Stock Data')
tesla_revenue.to_excel(writer, 'Tesla Revenue Data')
writer.save()
make_graph(tesla_data, tesla_revenue, 'TESLA')

#------------------- GameStop ---------------------------------------
# GameStop Stock Data
gme = yf.Ticker('GME')
gme_data = gme.history(period='max')
gme_data.reset_index(inplace=True)
# GameStop Revenue Data
url = "https://www.macrotrends.net/stocks/charts/GME/gamestop/revenue?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkPY0220ENSkillsNetwork23455606-2021-01-01"
html_data = requests.get(url).text
soup = BeautifulSoup(html_data, 'html5lib')
tables = pd.read_html(html_data)
gme_revenue = tables[1].rename(columns={'GameStop Quarterly Revenue(Millions of US $)':'Date', 'GameStop Quarterly Revenue(Millions of US $).1':'Revenue'})
gme_revenue["Revenue"] = gme_revenue['Revenue'].str.replace(',|\$',"")
gme_revenue.dropna(inplace=True)
gme_revenue = gme_revenue[gme_revenue['Revenue'] != ""]

writer = ExcelWriter('GameStop.xlsx')
tesla_data.to_excel(writer, 'GameStop Stock Data')
tesla_revenue.to_excel(writer, 'GameStop Revenue Data')
writer.save()
make_graph(gme_data, gme_revenue, 'GameStop')
