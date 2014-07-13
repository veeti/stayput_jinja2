from jinja2 import Environment, FileSystemLoader

from stayput import Templater


class Jinja2Templater(Templater):

    def __init__(self, site, *args, **kwargs):
        self.site = site
        self.env = Environment(loader=FileSystemLoader(site.templates_path))

    def template(self, item, site, *args, **kwargs):
        return self.env.from_string(item.contents).render(site=self.site, item=item)
