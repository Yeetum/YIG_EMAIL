import sys
from pathlib import Path
import pandas as pd
from jinja2 import Environment, FileSystemLoader, select_autoescape
from pretty_html_table import build_table

# Import web assets config
import config

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

def stock_reports(MARKET_STRENGTH_FILEPATH, SECTOR_REPORT_FILEPATH, STOCK_SIGNAL_FILEPATH, SUBJECT):

    # Prep csv dataframs
    df_marketStrength = pd.read_csv(MARKET_STRENGTH_FILEPATH)
    df_sectorReport = pd.read_csv(SECTOR_REPORT_FILEPATH)
    df_stockSignal = pd.read_csv(STOCK_SIGNAL_FILEPATH)

    ms_data = pd.DataFrame(df_marketStrength)
    sector_data = pd.DataFrame(df_sectorReport)
    signal_data = pd.DataFrame(df_stockSignal)

    # Prep html tables of dataframes
    ms_html_table= build_table(ms_data, 'grey_dark')
    sector_html_table = build_table(sector_data, 'grey_dark')
    signal_html_table = signal_data.to_html()
    
    prepped_html = stock_template.render(subject=SUBJECT, marketScore=ms_html_table, sectorSummary=sector_html_table, signalsReport=signal_html_table, yeetumLogo=yeetumLogo, atlasURI=atlasURI )
    print('HTML size in bytes', sys.getsizeof(prepped_html))
    return prepped_html


def htmlify_cleanup():
    pass
