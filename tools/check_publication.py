"""Validate original public docs/assets; never invoke editing or native libraries."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
FORBIDDEN = {'.dll', '.dylib', '.exe', '.mp4', '.mov', '.wav', '.mp3', '.otf', '.ttf', '.zip'}
REQUIRED = ['README.md', 'README.en.md', 'LICENSE', 'index.html', 'docs/licensing.md',
            'docs/platforms.md', 'docs/roadmap.md', 'assets/hero-zh.svg', 'assets/hero-mobile.svg']
errors = []

def link(source, value):
    if value.startswith(('https://', 'http://', 'mailto:', '#')):
        return
    path = unquote(urlsplit(value).path)
    target = (source.parent / path).resolve()
    if not target.is_relative_to(ROOT) or not target.is_file():
        errors.append(f'{source.relative_to(ROOT)}: missing/escaping local link {value}')

class Links(HTMLParser):
    def __init__(self, source):
        super().__init__(); self.source = source
    def handle_starttag(self, tag, attrs):
        data = dict(attrs)
        if tag == 'img' and not data.get('alt'):
            errors.append(f'{self.source.name}: image missing alt')
        for key in ('href', 'src', 'srcset'):
            if key in data:
                link(self.source, data[key])

for rel in REQUIRED:
    if not (ROOT / rel).is_file(): errors.append('Missing required file: ' + rel)
count = 0
for p in sorted(ROOT.rglob('*')):
    parts = p.relative_to(ROOT).parts
    if any(x in {'.git', '__pycache__'} for x in parts) or not p.is_file(): continue
    count += 1
    if (p.suffix.lower() in FORBIDDEN and p.relative_to(ROOT).as_posix() not in {'downloads/LightCut-Mac-Windows-Preview-R81.zip', 'downloads/LightCut-Mac-Windows-R82.zip', 'downloads/LightCut-Mac-Windows-R84.zip'}) or parts[0] in {'upstream', 'work', 'local', 'research', 'results', 'dist'}:
        errors.append('Unexpected private/runtime payload: ' + str(p.relative_to(ROOT)))
    if p.suffix in {'.md', '.html', '.svg'}:
        text = p.read_text(encoding='utf-8')
        if re.search(r'/Users/|/home/|[A-Z]:\\Users\\|gh[pousr]_[A-Za-z0-9]{20,}|sk-[A-Za-z0-9]{20,}', text):
            errors.append('Possible private path/credential: ' + str(p.relative_to(ROOT)))
        if p.suffix in {'.md', '.html'}:
            Links(p).feed(text)
            for target in re.findall(r'\]\(([^\s)]+)\)', text): link(p, target)
        else:
            try:
                svg = ET.fromstring(text)
                if svg.find('{http://www.w3.org/2000/svg}title') is None:
                    errors.append('SVG missing title: ' + p.name)
                if any(e.tag.endswith(('script', 'foreignObject')) for e in svg.iter()):
                    errors.append('Active SVG content: ' + p.name)
            except ET.ParseError as exc: errors.append(f'{p.name}: {exc}')
if errors:
    raise SystemExit('\n'.join(errors))
print(f'PASS: {count} public files; local links, image alternatives, SVG and publication scope checked.')
