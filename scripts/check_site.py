"""Dependency-free structural/link checks for the static site; no network access."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote

ROOT = Path(__file__).resolve().parents[1] / 'dist'
VOID = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param', 'source', 'track', 'wbr'}
class Document(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack, self.ids, self.links, self.resources = [], [], [], []
        self.h1 = self.main = self.title = 0
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        assert tag not in {'script', 'iframe', 'form', 'object', 'embed', 'base'}, tag
        assert not any(k.startswith('on') for k in a), 'inline event handler'
        if tag not in VOID: self.stack.append(tag)
        self.h1 += tag == 'h1'
        self.main += tag == 'main'
        self.title += tag == 'title'
        if 'id' in a: self.ids.append(a['id'])
        if tag == 'html': assert a.get('lang') == 'en-GB'
        if 'href' in a: self.links.append(a['href'])
        if 'src' in a: self.resources.append(a['src'])
        if tag == 'link': self.resources.append(a['href'])
    def handle_endtag(self, tag):
        assert self.stack and self.stack.pop() == tag, f'unbalanced {tag}'

def parse(path):
    doc = Document(); doc.feed(path.read_text()); doc.close()
    assert not doc.stack and doc.h1 == 1 and doc.main == 1 and doc.title == 1
    assert len(doc.ids) == len(set(doc.ids))
    return doc

pages = list(ROOT.rglob('*.html'))
assert len(pages) >= 4 and (ROOT / '.nojekyll').is_file()
for page in pages:
    doc = parse(page)
    for resource in doc.resources:
        assert not urlsplit(resource).scheme and not resource.startswith('//'), resource
    for link in doc.links + doc.resources:
        u = urlsplit(link)
        if u.scheme:
            assert u.scheme in {'https', 'mailto'}, link
            if u.scheme == 'mailto': assert u.path == 'stephencurtisapps@gmail.com'
            continue
        assert not u.netloc
        target = (page.parent / unquote(u.path)).resolve() if u.path else page
        if target.is_dir(): target /= 'index.html'
        assert target.is_relative_to(ROOT.resolve()) and target.is_file(), (page, link)
        if u.fragment: assert u.fragment in parse(target).ids, (page, link)
    print('PASS', page.relative_to(ROOT))
css = (ROOT / 'assets/styles.css').read_text()
assert '@import' not in css and 'url(' not in css
assert ':focus-visible' in css and 'prefers-reduced-motion' in css
assert not any(p.is_symlink() for p in ROOT.rglob('*'))
print('PASS structure, links, anchors, local resources and dependency-free Pages layout')
