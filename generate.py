from jinja2 import Environment, FileSystemLoader
import json
import os

# Setup paths
env = Environment(loader=FileSystemLoader('templates'))
output_dir = '.'

# Load project data
with open('projects.json') as f:
    projects = json.load(f)

# Define pages and templates
pages = [
    {'template': 'index.html', 'output': 'index.html', 'context': {}},
    {'template': 'projects.html', 'output': 'projects.html', 'context': {'projects': projects}},
    {'template': 'about.html', 'output': 'about.html', 'context': {}}
]

# Render each page
for page in pages:
    template = env.get_template(page['template'])
    output_path = os.path.join(output_dir, page['output'])

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(template.render(page['context']))

print("✅ Portfolio generated successfully!")
