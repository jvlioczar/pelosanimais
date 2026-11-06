"""Confere links internos, âncoras, SEO e referências proibidas. Uso: python tools/audit.py"""
import collections, json, os, re, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
erros = 0; n = 0; titulos = collections.defaultdict(list); paginas = set()
def falha(*m):
    global erros
    print(*m); erros += 1
for pasta, _, arqs in os.walk(ROOT):
    if os.path.basename(pasta) in ('tools', '.git'): continue
    for a in arqs:
        if not a.endswith('.html'): continue
        n += 1; p = os.path.join(pasta, a); t = open(p, encoding='utf-8').read()
        rel = os.path.relpath(p, ROOT).replace(os.sep, '/'); paginas.add(rel)
        if 'assuperlistas' in t.lower(): falha('assuperlistas em', rel)
        if re.search(r'citad[oa]s? de mem|documento do projeto|autor-data', t, re.I): falha('nota de rascunho em', rel)
        if len(re.findall(r'<h1[\s>]', t)) != 1: falha('h1 em', rel)
        m = re.search(r'<title>(.*?)</title>', t); titulos[m.group(1) if m else ''].append(rel)
        d = re.search(r'name="description" content="(.*?)"', t)
        if not d or len(d.group(1)) > 175: falha('descrição em', rel)
        ids = re.findall(r'\sid="([^"]+)"', re.sub(r'<svg\b.*?</svg>', '', t, flags=re.S))
        for i, c in collections.Counter(ids).items():
            if c > 1: falha('id repetido', i, 'em', rel)
        if a != '404.html':
            if 'rel="canonical"' not in t: falha('sem canonical', rel)
            bl = re.search(r'application/ld\+json">(.*?)</script>', t, re.S)
            try: json.loads(bl.group(1))
            except Exception: falha('JSON-LD inválido', rel)
        for h in re.findall(r'(?:href|src)="([^"]*)"', t):
            if re.match(r'https?:|mailto:|/|\?', h): continue
            arq, _, ancora = h.partition('#'); arq = arq.split('?')[0]
            alvo = os.path.normpath(os.path.join(pasta, arq)) if arq else p
            if a == '404.html': alvo = os.path.normpath(os.path.join(ROOT, arq)) if arq else p
            if not os.path.exists(alvo): falha('quebrado:', rel, '->', h)
            elif ancora and alvo.endswith('.html') and f'id="{ancora}"' not in open(alvo, encoding='utf-8').read(): falha('âncora:', rel, '->', h)
for k, v in titulos.items():
    if len(v) > 1: falha('título repetido', k, v[:3])
s = open(os.path.join(ROOT, 'sitemap.xml'), encoding='utf-8').read()
urls = {u.split('.org/')[1] or 'index.html' for u in re.findall(r'<loc>(.*?)</loc>', s)}
for f in sorted(paginas - urls - {'404.html'}): falha('fora do sitemap', f)
for f in sorted(urls - paginas): falha('sitemap sem página', f)
print(f'{n} páginas, {erros} problemas.')
sys.exit(1 if erros else 0)
