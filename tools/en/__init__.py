"""English version of the guide (fortheanimals.biblioverse.org).

build.py imports this package in both languages: the Portuguese site needs the English slugs for the language toggle,
and `python tools/build.py en` uses it to swap every text for its translation. Content that has no translation yet
falls back to Portuguese and is listed by relatorio() at the end of the build, so nothing slips through unnoticed.

Translations are adapted for an international reader: where the Portuguese text uses a Brazilian example only as an
illustration, the English text uses an international equivalent with a checked source; Brazilian facts stay when they
are the evidence itself."""
import os, re, shutil

from .catalogo import ARGS, FAMILIAS, FALACIAS, VIESES, CADEIAS, CADEIAS_LONGAS
from .ruins import RUINS, TIPOS
from .motivos import MOTIVOS
from .paginas import POLITICAS, POL_INTRO, ALEM, LIVROS, FOCOS, SITES, SITES_URL, TEXTOS, ARVORE
from .debate import PESSOAS, OP
from .ui import UI, JS

NOME = 'For the Animals: An Argument Guide'
CURTO = 'For the Animals'
MARCA = 'For the Animals<br/>An Argument Guide'
SITE_PT = 'https://pelosanimais.biblioverse.org'

FALTAM = {}
def falta(tipo, chave):
    FALTAM.setdefault(tipo, []).append(chave)

# ---------- paths ----------
PASTAS = {'argumentos': 'arguments', 'ruins': 'stop-saying', 'familias': 'families', 'politicas': 'political', 'alem': 'beyond'}
PAGS = {'comece-aqui': 'start-here', 'argumentos-ruins': 'stop-saying', 'alem-do-veganismo': 'beyond-veganism',
        'objecoes-politicas': 'political-objections', 'raciocinio': 'reasoning', 'mapa': 'map', 'falacias': 'fallacies',
        'vieses': 'biases', 'biblioteca': 'library', 'sobre': 'about', 'treino': 'practice', 'familias': 'families', 'debate': 'debate'}
SUB = {'politicas': {k: v['s'] for k, v in POLITICAS.items()}, 'alem': {k: v['s'] for k, v in ALEM.items()}}

_PASTA_RE = re.compile(r'(?<![\w-])(argumentos|ruins|familias|politicas|alem)/([\w-]+)\.html')
_PAG_RE = re.compile(r'(?<![\w/-])((?:\.\./)*)(' + '|'.join(sorted(PAGS, key=len, reverse=True)) + r')\.html')
_PAG_RAIZ_RE = re.compile(r'(?<=biblioverse\.org/)(' + '|'.join(sorted(PAGS, key=len, reverse=True)) + r')\.html')

_IRMAOS = {**SUB['politicas'], **SUB['alem']}
_IRMAO_RE = re.compile(r'(?<=href=")(' + '|'.join(sorted(_IRMAOS, key=len, reverse=True)) + r')\.html')

def caminho(s):
    """Portuguese paths (folders, page names, theory and topic slugs) to their English form, anywhere in a string.
    Bare slugs cover links between pages of the same folder (previous/next theory, the Beyond veganism side menu)."""
    s = _IRMAO_RE.sub(lambda m: f'{_IRMAOS[m[1]]}.html', s)
    s = _PASTA_RE.sub(lambda m: f'{PASTAS[m[1]]}/{SUB.get(m[1], {}).get(m[2], m[2])}.html', s)
    s = _PAG_RE.sub(lambda m: f'{m[1]}{PAGS[m[2]]}.html', s)
    return _PAG_RAIZ_RE.sub(lambda m: f'{PAGS[m[1]]}.html', s)

# ---------- text ----------
_UI = sorted(UI, key=lambda x: -len(x[0]))
_JS = sorted(JS + UI, key=lambda x: -len(x[0]))

def traduz_html(doc, links=None):
    """Interface strings, then argument links (build.py's nova_url), then paths. Links to the Portuguese site are protected."""
    guardados = []
    def guarda(m):
        guardados.append(m[0]); return f'\0{len(guardados) - 1}\0'
    doc = re.sub(re.escape(SITE_PT) + r'[^"\s<]*', guarda, doc)
    for pt, en in _UI: doc = doc.replace(pt, en)
    if links: doc = links(doc)
    doc = caminho(doc)
    return re.sub(r'\0(\d+)\0', lambda m: guardados[int(m[1])], doc)

def motivo(s):
    if s in MOTIVOS: return MOTIVOS[s]
    falta('motivo', s); return s

def copia_assets(src, dst):
    os.makedirs(dst, exist_ok=True)
    for n in os.listdir(src):
        a = os.path.join(src, n)
        if not os.path.isfile(a) or n in ('busca.json', 'share.png'): continue
        if n.endswith('.js'):
            t = open(a, encoding='utf-8').read()
            for pt, en in _JS: t = t.replace(pt, en)
            t = caminho(t)
            open(os.path.join(dst, n), 'w', encoding='utf-8', newline='\n').write(t)
        else: shutil.copyfile(a, os.path.join(dst, n))

def llms(site, nome, desc):
    ls = [('Start here', 'start-here.html'), ('All arguments', '#arguments'), ('Simulated debate', 'debate.html'), ('Practice answers', 'practice.html'),
          ('Stop saying this: weak vegan arguments and better ways to say them', 'stop-saying.html'), ('Political objections', 'political-objections.html'),
          ('Beyond veganism', 'beyond-veganism.html'), ('The 13 families', 'families.html'), ('The anti-vegan line of reasoning', 'reasoning.html'),
          ('Map of connections', 'map.html'), ('Fallacies', 'fallacies.html'), ('Biases', 'biases.html'), ('Library', 'library.html')]
    return f'# {nome}\n\n> {desc}\n\n## Main pages\n' + ''.join(f'- [{t}]({site}/{u})\n' for t, u in ls) + f'\nPortuguese version: {SITE_PT}/\n'

# ---------- Questão de Ética in English ----------
_QE_LOCAL = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))), 'jornadaeticaanimal', 'en')
def qe(vol, cap):
    """(title, url) of a chapter of the English edition of Questão de Ética, or None if it can't be found locally."""
    import glob, html as _h
    achados = glob.glob(os.path.join(_QE_LOCAL, f'v{vol}', f'{cap:02d}-*.html'))
    if not achados: return None
    t = re.search(r'<title>(.*?)</title>', open(achados[0], encoding='utf-8').read())
    titulo = _h.unescape(t[1]).split(' · ')[0] if t else os.path.basename(achados[0])
    return titulo, f'https://questaodeetica.biblioverse.org/en/v{vol}/{os.path.basename(achados[0])}'

# ---------- data swap ----------
def aplica(g):
    """Replace the Portuguese texts loaded by build.py with their English versions, in place."""
    for c, a in g['ARGS'].items():
        if c in ARGS: a['frase'], a['formas'], a['falha'] = ARGS[c][0], list(ARGS[c][1]), ARGS[c][2]
        else: falta('argumento', c)
    for c, f in g['FAMILIAS'].items():
        if c in FAMILIAS: f['nome'], f['perg'], f['erro'] = FAMILIAS[c]
        else: falta('família', c)
    for lista, dic, tipo in ((g['FALACIAS'], FALACIAS, 'falácia'), (g['VIESES'], VIESES, 'viés')):
        for x in lista:
            if x['n'] in dic: x['n'], x['d'], x['aparece'] = dic[x['n']][0], dic[x['n']][1], ''
            else: falta(tipo, x['n'])
    for x in g['CADEIAS']:
        if x['n'] in CADEIAS: x['n'], x['fim'] = CADEIAS[x['n']]
        else: falta('cadeia', x['n'])
    g['CADEIAS_LONGAS'][:] = [(CADEIAS_LONGAS.get(n, (n, d))[0], CADEIAS_LONGAS.get(n, (n, d))[1], cs) for n, d, cs in g['CADEIAS_LONGAS']]
    for k in list(g['TIPOS']):
        if k in TIPOS: g['TIPOS'][k] = TIPOS[k]
        else: falta('tipo', k)
    cod_pt = {r['frase']: r['c'] for r in g['RUINS']}
    for r in g['RUINS']:
        t = RUINS.get(r['frase'])
        if not t: falta('ruim', r['frase']); continue
        r['frase_pt'] = r['frase']
        for campo in ('frase', 'por', 'lugar', 'nota', 'fontes'):
            if campo in t: r[campo] = t[campo]
        r['lugar'] = r['lugar'].replace('{V12}', cod_pt.get('Ser vegano exige ser anticapitalista.', ''))
    pol = g['politicas']
    pol.INTRO = POL_INTRO or pol.INTRO
    for t in pol.TEORIAS:
        x = POLITICAS.get(t['s'])
        if not x: falta('política', t['s']); continue
        for campo in ('t', 'frase', 'principio', 'quebra', 'replica', 'resposta', 'fontes'):
            if campo in x: t[campo] = x[campo]
    for p in g['alem'].PAGINAS:
        x = ALEM.get(p['s'])
        if not x: falta('além', p['s']); continue
        for campo in ('t', 'res', 'selo', 'corpo', 'fontes'):
            if campo in x: p[campo] = x[campo]
    bib = g['biblioteca']
    bib.FOCOS.update(FOCOS)
    for b in bib.LIVROS:
        x = LIVROS.get(b['t'])
        if not x: falta('livro', b['t']); continue
        b.update(x)
    novos = []
    for n, d, u in bib.SITES:
        if u in SITES: novos.append((SITES[u][0], SITES[u][1], SITES_URL.get(u, u)))
        else: falta('site', n); novos.append((n, d, u))
    bib.SITES[:] = novos
    deb = g['debate']
    deb.PESSOAS[:] = PESSOAS or deb.PESSOAS
    for c in list(deb.OP):
        if c in OP: deb.OP[c] = OP[c]
        else: falta('debate', c)
    for k, v in TEXTOS.items():
        if k in g: g[k] = v
    for k in ('DESCRICAO', 'IND_TEXTO', 'IND_TEMA', 'IND_EXEMPLO', 'EQUILIBRIO'):
        if k not in TEXTOS: falta('texto', k)

# ---------- report ----------
_PT = re.compile(r"[^<>\"{}]*(?:\b(?:não|você|são|também|então|porque|até|já|está|isso|esse|essa|uma|pelo|pela|nos|das|dos|com|para|mas|ou|o|a|os|as|de|do|da|em|que|é)\b[^<>\"{}]*){3,}")
_SEM_PT = re.compile(r'[A-Za-z]')

def relatorio(out):
    """List what is still in Portuguese: missing data entries and interface strings found in the built pages."""
    for tipo, ls in FALTAM.items():
        print(f'  missing {tipo}: {len(ls)}', '' if len(ls) > 8 else ls)
    achados = {}
    for pasta, _, arqs in os.walk(out):
        for a in arqs:
            if not a.endswith(('.html', '.js', '.json')): continue
            t = open(os.path.join(pasta, a), encoding='utf-8').read()
            t = re.sub(r'<script type="application/ld\+json">.*?</script>', '', t, flags=re.S)
            for m in re.finditer(r'>([^<]{6,})<|"([^"]{12,})"', t):
                s = (m[1] or m[2]).strip()
                if re.search(r'[ãõçêâ]|\b(não|você|são|também|então|porque|está|isso|esse|essa|uma|pelo|pela|para|mas|que)\b', s) and not s.startswith(('http', 'data:')):
                    achados[s[:140]] = achados.get(s[:140], 0) + 1
    print(f'  Portuguese strings left in the English pages: {len(achados)}')
    for s, n in sorted(achados.items(), key=lambda x: -x[1])[:60]:
        print(f'   {n:4} {s}')
