import html.parser
from html.parser import HTMLParser

class PrettyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.indent_level = 0
        self.output = []
        
    def handle_starttag(self, tag, attrs):
        attrs_str = ' '.join([f'{k}="{v}"' for k, v in attrs])
        if attrs_str:
            self.output.append(f"{'  ' * self.indent_level}<{tag} {attrs_str}>")
        else:
            self.output.append(f"{'  ' * self.indent_level}<{tag}>")
        if tag not in ['br', 'img', 'meta', 'link', 'input']:
            self.indent_level += 1
        
    def handle_endtag(self, tag):
        if tag not in ['br', 'img', 'meta', 'link', 'input']:
            self.indent_level -= 1
        self.output.append(f"{'  ' * self.indent_level}</{tag}>")
        
    def handle_data(self, data):
        if data.strip():
            self.output.append(f"{'  ' * self.indent_level}{data.strip()}")

with open('web.html', 'r', encoding='utf-8') as f:
    content = f.read()

parser = PrettyHTMLParser()
parser.feed(content)

with open('web.html', 'w', encoding='utf-8') as f:
    f.write('\n'.join(parser.output))

print('✓ Fichier web.html reformatté avec succès!')
