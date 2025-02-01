# 1. Run this script
# 2. Copy the terminal output and paste it in the correct place in index.html
# 3. Format index.html

import json
import requests

response = requests.get(
    'https://raw.githubusercontent.com/libredirect/browser_extension/refs/heads/master/src/config.json'
)
data = response.json()

html_output = ""
for service in data["services"].values():
    html_output += f'<li>\n{service['name']} <span>&#8594;</span>\n'

    frontend_links = []
    for service in service["frontends"].values():
        name = service["name"]
        url = service["url"]
        frontend_links.append(f'<a href="{url}">{name}</a>')

    html_output += ',\n'.join(frontend_links)
    html_output += '\n</li>'

print(html_output)
