from stayput import simple_router
from stayput.jinja2 import Jinja2Templater

def configure(site):
    site.router = simple_router
    site.templater = Jinja2Templater(site)
    site.title = 'Stayput Jinja2 Example'

