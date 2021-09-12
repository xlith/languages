import pandas as pd
import requests
import string
from bs4 import BeautifulSoup
import sqlite3
import os
from pathlib import Path


def _to_xml(df, filename=None, mode='w'):
    def row_to_xml(row):
        xml = ['<item>']
        for i, col_name in enumerate(row.index):
            xml.append('  <field name="{0}">{1}</field>'.format(col_name, row.iloc[i]))
        xml.append('</item>')
        return '\n'.join(xml)

    res = '<root>\n' + '\n'.join(df.apply(row_to_xml, axis=1)) + '\n</root>'

    if filename is None:
        return res
    with open(filename, mode) as f:
        f.write(res)


def prep_data():
    result = pd.DataFrame()
    for character in string.ascii_lowercase:
        print(f'\nLanguages table index: {character}')
        url = f'https://en.wikipedia.org/wiki/ISO_639:{character}'
        response = requests.get(url)
        if response.status_code == 200:
            print(f'{character} table imported')

        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find('table', {'class': "wikitable"})

        df = pd.read_html(str(table))
        df = pd.DataFrame(df[0])

        df = df.dropna(subset=["639-1"])
        df = df.drop(["Scope/Type"], axis=1)

        print(f'{len(df.index)} line processed')

        result = pd.concat([result, df])

    result.reset_index(drop=True, inplace=True)
    return result


def export_data(data):
    path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'output'))
    Path(path).mkdir(parents=True, exist_ok=True)

    print(f'output path: {path}')
    data.to_json(os.path.join(path, 'languages.json'), orient='records')
    print("Json file exported")
    data.to_csv(os.path.join(path, 'languages.csv'))
    print("csv file exported")
    data.to_xml(os.path.join(path, 'languages.xml'))
    print("xml file exported")

    database = sqlite3.connect(os.path.join(path, 'languages.sqlite3.db'))
    data.to_sql('languages', con=database, if_exists='replace')
    print("sqlite3 database exported")

    with open(os.path.join(path, 'languages.sql'), 'w') as f:
        for line in database.iterdump():
            if line.startswith('INSERT INTO'):
                f.write('%s\n' % line)
    print("sql file exported")


def process():
    print("Process Started")
    pd.DataFrame.to_xml = _to_xml
    data = prep_data()
    export_data(data)


if __name__ == '__main__':
    process()


