'''
Flask app for Juncture site.
Dependencies: bs4 Flask Flask-Cors html5lib requests
'''

import os, logging

from flask import Flask, request, send_from_directory
from flask_cors import CORS

import requests
logging.getLogger('requests').setLevel(logging.WARNING)

app = Flask(__name__)
CORS(app)

from bs4 import BeautifulSoup

# Prefix for site content
prefix = 'kent-map/kent'
default_ref = None

def _add_tag(soup, tag, attrs):
  el = soup.new_tag(tag)
  el.attrs = attrs
  if tag in ('script',):
    soup.body.append(el)
  else:
    soup.head.append(el)

def _remove_tags(soup, tag, attrs):
  for el in soup.find_all(tag, attrs): el.decompose()

def _customize_response(html):
  '''Perform any post-processing of API-generated HTML.'''
  # parse API-generated HTML with BeautifulSoup
  #   https://beautiful-soup-4.readthedocs.io/en/latest/
  soup = BeautifulSoup(html, 'html5lib')
  
  # Custom favicon
  _remove_tags(soup, 'link', {'rel':'icon'})
  _add_tag(soup, 'link', {'href': '/static/images/favicon.png', 'rel':'icon', 'type':'image/png'})
  
  # Custom stylesheet
  #_remove_tags(soup, 'style', {'data-id':'default'})
  #_add_tag(soup, 'link', {'href': '/static/css/custom.css', 'rel':'stylesheet'})

  return str(soup)

def _get_html(path, base_url, ref=default_ref, **kwargs):
  api_url = f'https://api.juncture-digital.org/html{path}?prefix={prefix}&base={base_url}'
  if ref: api_url += f'&ref={ref}'
  resp = requests.get(api_url)
  return resp.status_code, resp.text if resp.status_code == 200 else ''

@app.route('/favicon.ico')
def favicon():
  # return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')
  return send_from_directory(os.path.join(app.root_path, 'static', 'images'), 'favicon.png', mimetype='image/png')

@app.route('/robots.txt')
def robots_txt():
  return send_from_directory(os.path.join(app.root_path, 'static'), 'robots.txt', mimetype='text/plain')

@app.route('/sitemap.txt')
def sitemap_txt():
  return send_from_directory(os.path.join(app.root_path, 'static'), 'sitemap.txt', mimetype='text/plain')

@app.route('/<path:path>')
@app.route('/')
def render_html(path=None):
  base_url = f'/{"/".join(request.base_url.split("/")[3:])}'
  if base_url != '/' and not base_url.endswith('/'): base_url += '/'
  path = f'/{path}' if path else '/'
  status, html = _get_html(path, base_url, **dict(request.args))
  if status == 200:
    html = _customize_response(html)
  return html, status

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=7777)
