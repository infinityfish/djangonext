import argparse
import glob
import os
from bs4 import BeautifulSoup


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-d',
        '--dir',
        type=str,
        required=True)
    args = parser.parse_args()
    return args


def inspect_parser(soup, tag):
    for x in soup.find_all(tag):
        if x.get('src') and x['src'].startswith('/_next/'):
            x['src'] = "{% static \"" + x['src'] + "\" %}"
        if x.get('href') and x['href'].startswith('/_next/'):
            x['href'] = "{% static \"" + x['href'] + "\" %}"


def render_html_static():
    args = parse_args()
    for html_file in glob.glob(os.path.join(args.dir, '*html')):
        soup = BeautifulSoup(open(html_file), 'html.parser')
        soup.insert(0, '{% load static %}')
        inspect_parser(soup, 'link')
        inspect_parser(soup, 'script')
        fout = open(html_file, 'wb')
        fout.write(soup.prettify('utf-8'))
        fout.close()


render_html_static()


# ##### After completing the nextjs project, do the following
# 1. npm build
# 2. npx next export -o output
# Make sure you delete the old static folder in your route directory before you continue
# 3. mv output static
# 4. python djangonext.py -d static
# 5. python manage.py runserver


# npx next export -o output && mv output static && python app.py -d static && python manage.py runserver

# ln -s ../static/index.html index.html

# rm -rf output static && next export -o output && mv output static && python app.py -d static
