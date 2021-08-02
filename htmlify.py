import sys
import io
from base64 import b64encode
from pathlib import Path
from numpy import sign
import pandas as pd
from jinja2 import Environment, FileSystemLoader, select_autoescape
from pretty_html_table import build_table
import plotly.express as px
#import dash
#import dash_core_components as dcc
#import dash_html_components as html
#from dash.dependencies import Input, Output

# Import web assets config
import config

buffer = io.StringIO()
html_bytes = buffer.getvalue().encode()
encoded = b64encode(html_bytes).decode()

#app = dash.Dash(__name__)

env = Environment(
    loader=FileSystemLoader(['./templates/', './templates/images/']),
    autoescape=select_autoescape(['html', 'xml'])
)

# Static web asset URIs
yeetumLogo=config.yeetumWhiteURI
atlasURI=config.aiPngURI

template = env.get_template('index.html')
stock_template = env.get_template('stock_report.html')

def standard_csv(FILEPATH, SUBJECT):

    df_csv = pd.read_csv(FILEPATH)
    data = pd.DataFrame(df_csv)

    html_table_data = build_table(data, 'grey_dark')
    prepped_html = template.render(subject=SUBJECT, df=html_table_data, yeetumLogo=yeetumLogo, atlasURI=atlasURI )

    return prepped_html

# def stock_reports(MARKET_STRENGTH_FILEPATH, SECTOR_REPORT_FILEPATH, STOCK_SIGNAL_FILEPATH, SUBJECT):

#     # Prep csv dataframs
#     df_marketStrength = pd.read_csv(MARKET_STRENGTH_FILEPATH)
#     df_sectorReport = pd.read_csv(SECTOR_REPORT_FILEPATH)
#     df_stockSignal = pd.read_csv(STOCK_SIGNAL_FILEPATH)

#     ms_data = pd.DataFrame(df_marketStrength)
#     sector_data = pd.DataFrame(df_sectorReport)
#     signal_data = pd.DataFrame(df_stockSignal)
#     signal_data.drop(signal_data.columns[[0,12,13, 14, 15, 16, 17]], axis=1, inplace=True)


#     ms_fig = px.line(ms_data, x=ms_data[ms_data.columns[0]], y=ms_data[ms_data.columns[1]])

#     # Prep html tables of dataframes
#     app.layout = html.Div([
#         dcc.Graph(id="graph", figure=ms_fig)
#     ])
#     ms_html_table = ms_fig.to_html()
#     sector_html_table = build_table(sector_data, 'grey_dark')
#     signal_html_table = None #signal_data.to_html()
    
#     prepped_html = stock_template.render(subject=SUBJECT, marketScore=ms_html_table, sectorSummary=sector_html_table, signalsReport=signal_html_table, yeetumLogo=yeetumLogo, atlasURI=atlasURI )
#     print('HTML size in bytes', sys.getsizeof(prepped_html))
#     return prepped_html

def htmlify_cleanup():
    pass
