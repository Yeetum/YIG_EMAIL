from pathlib import Path
import pandas as pd
from jinja2 import Environment, FileSystemLoader, select_autoescape
from pretty_html_table import build_table

env = Environment(
    loader=FileSystemLoader(['./templates/', './templates/images/']),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('index.html')

def htmlify_csv(FILEPATH, SUBJECT):
    df_csv = pd.read_csv(FILEPATH)
    data = pd.DataFrame(df_csv)

    html_table_data = build_table(data, 'blue_light')
    print("Beautified csv table", html_table_data)
    prepped_html = template.render(subject=SUBJECT, df=data.to_html() )
    print(prepped_html)
    return prepped_html

def htmlify_cleanup():
    pass
