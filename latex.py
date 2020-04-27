from jinja2.loaders import FileSystemLoader
from latex.jinja2 import make_env

env = make_env(loader=FileSystemLoader('.'))
tpl = env.get_template('doc.latex')

print(tpl.render(name="Alice"))