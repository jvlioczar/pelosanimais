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
from .paginas import POLITICAS, POL_CURTAS, POL_INTRO, POL_ESPECTRO, ALEM, LIVROS, FOCOS, SITES, SITES_URL, TEXTOS, ARVORE
from .debate import PESSOAS, OP
from .ui import UI, JS

NOME = 'For the Animals: An Argument Guide'
CURTO = 'For the Animals'
MARCA = 'For the Animals<br/>An Argument Guide'
SITE_PT = 'https://pelosanimais.biblioverse.org'

# Formal fallacies added on 2026-11-20 (Nobis, Animals & Ethics 101, pp. 41 and 98)
FALACIAS.update({
 'Negação do antecedente': ('Denying the antecedent', '"If A, then B; not A; so, not B". E.g. "if a person studies medicine, they are at university; they do not study medicine; so, they are not at university". They may be on another course'),
 'Afirmação do consequente': ('Affirming the consequent', '"If A, then B; B; so, A". E.g. "if it rained, the street is wet; the street is wet; so, it rained". Someone may have hosed down the pavement'),
})

import novos as _novos_lotes  # argumentos acrescentados em 2026-11-13
ARGS.update(_novos_lotes.EN); MOTIVOS.update(_novos_lotes.MOTIVOS)

_EXTRA_EN = {'A12': ["We're all naturally biased: we protect our family, our species, our nation, and veganism is an illusion"], 'E3': ['We have to respect different views'], 'A7': ['Vegans treat animals like humans'],
    'D7': ['Vegans want to impose veganism on Indigenous peoples'], 'C2': ['Our bodies are designed to eat meat'], 'J2': ["Veganism is classist and elitist, it isn't accessible to poorer people"],
    'C1': ['We have canine teeth, so we were made to eat meat', "If we weren't meant to eat meat, we wouldn't have canines", 'Humans are carnivores by nature'],
    'I11': ['Silk is a natural, noble fabric, better than synthetics', 'Nobody kills anything to make silk'], 'I12': ["Honey is healthy and natural; there's nothing wrong with it"],
    'N26': ['Sentientists discuss impossible or very distant scenarios'], 'N10': ['Sentientists want to play God'], 'L21': ['Vegans prefer animals to people']}
for _c, _fs in {  # phrasings gathered from lists of anti-vegan myths (2026-11-15)
    'A1': ["You can't know what goes on in an animal's head", "An animal is a machine; it feels nothing", 'Animals are like robots; they just react', 'I can only be sure that I feel'], 'A4': ["Plants have it worse, they can't even run away", 'If you defend life, why do you kill plants?', 'Plants defend themselves, so they want to live'],
    'A7': ["It's just pity for cute animals", 'Veganism is more emotion than reason'], 'A9': ['Animals are less evolved than us'],     'A20': ["Slaughter isn't murder"], 'A21': ['A cow would kill you if it had the chance'], 'A22': ['Ethics is for humans, not animals'],
    'B1': ['Almost every slaughterhouse is clean and painless'], 'B3': ['Animals live better on the farm than in the wild'], 'B8': ['On the farm the animals are treated like royalty'],
    'C1': ['Being vegetarian goes against our biology'], 'C2': ["We can't even digest cellulose"], 'C4': ['Without meat, evolution would have stopped', 'Eating meat is the peak of evolution'],
    'C9': ["If we don't kill, we die"], 'C10': ['These animals were born to die anyway'], 'C12': ['There will be cattle running loose all over nature'], 'C13': ['We have great respect for farm animals'],
    'D10': ['Animals exist to serve us'], 'D12': ["It's not what goes into the mouth that defiles a person"],
    'E1': ["Eating meat doesn't hurt anyone"], 'E3': ["It's just one ethics among many"], 'E4': ['Food is food; it has nothing to do with ethics'], 'E9': ["A little egg in a cake doesn't hurt"],
    'G4': ['Vegans live on supplements', 'B12 only exists in meat'], 'G6': ["Without milk, vegans' bones will break"], 'G10': ['It was in the news: a vegan couple\'s baby died of malnutrition'],
    'G12': ["Vegans are all skinny and can't gain weight"], 'G16': ['Cavemen ate meat'], 'G18': ["Without soy and fake meat, vegans can't get enough nutrients"],
    'H7': ["Cow burps don't warm the planet", 'If cattle pollute, just eat the cattle'], 'H15': ['With good management, livestock farming becomes sustainable', 'Modern livestock farming is more efficient and emits less per kilo'],
    'H19': ["If nobody fishes, the sea will be overrun with fish"], 'I1': ["Livestock and animal testing brought progress; we can't abolish them"],
    'J1': ['Vegans have to buy everything at health-food stores'], 'J5': ["Vegans can't go to barbecues"], 'J7': ['Vegan food is all foreign stuff', "Vegans can't even have a little treat"],
    'J22': ["It's lobbying by people who profit from ending livestock farming"], 'K1': ['One swallow does not make a summer'],
    'J8': ["I'm flexitarian and spare the animals", "I'm reducetarian; I eat less meat and already spare lots of animals", "I'm vegan at home and eat everything when I'm out"],
    'L2': ['Veganism is for people with nothing better to do'], 'L11': ["Vegans take long showers and don't even recycle"], 'L12': ['Even the water you drink kills fish'], 'L25': ["It's a 1960s hippie fad"],
}.items(): _EXTRA_EN.setdefault(_c, []).extend(_fs)
_EXTRA_EN.setdefault('F6', []).extend(['Killing insects protects us', "I kill mosquitoes, it's a health issue", 'A scorpion in the house has to be killed', 'Insects are pests; spray everything'])  # antigo F7 unido ao F6
_EXTRA_EN.setdefault('E1', []).append('We have the right to eat animals')
_EXTRA_EN.setdefault('J19', []).append('The vegan industry is trying to manipulate you')
for _c, _fs in _EXTRA_EN.items(): ARGS[_c] = (ARGS[_c][0], list(ARGS[_c][1]) + _fs, ARGS[_c][2])

FALTAM = {}
def falta(tipo, chave):
    FALTAM.setdefault(tipo, []).append(chave)

# ---------- paths ----------
PASTAS = {'argumentos': 'arguments', 'ruins': 'stop-saying', 'familias': 'families', 'politicas': 'political', 'alem': 'beyond'}
PAGS = {'comece-aqui': 'start-here', 'argumentos-ruins': 'stop-saying', 'alem-do-veganismo': 'beyond-veganism',
        'objecoes-politicas': 'political-objections', 'raciocinio': 'reasoning', 'mapa': 'map', 'falacias': 'fallacies',
        'vieses': 'biases', 'biblioteca': 'library', 'sobre': 'about', 'glossario': 'glossary', 'treino': 'practice', 'familias': 'families', 'debate': 'debate', 'exploracao': 'exploitation'}
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
    # the catalogue section is #arguments in English (links to the Portuguese site stay protected above)
    doc = doc.replace('#argumentos"', '#arguments"').replace('id="argumentos"', 'id="arguments"')
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
            # Apostrophes between letters (today's, don't) become typographic: a straight ' would close the JS string it lands in.
            for pt, en in _JS: t = t.replace(pt, re.sub(r"(?<=[A-Za-z])'(?=[A-Za-z])", '’', en))
            t = caminho(t)
            open(os.path.join(dst, n), 'w', encoding='utf-8', newline='\n').write(t)
        else: shutil.copyfile(a, os.path.join(dst, n))

def llms(site, nome, desc):
    ls = [('Start here', 'start-here.html'), ('All arguments', '#arguments'), ('Simulated debate', 'debate.html'), ('Practice answers', 'practice.html'),
          ('Stop saying this: weak vegan arguments and better ways to say them', 'stop-saying.html'), ('Political objections', 'political-objections.html'),
          ('Beyond veganism', 'beyond-veganism.html'), ('The 14 families', 'families.html'), ('Types of exploitation', 'exploitation.html'), ('The anti-vegan line of reasoning', 'reasoning.html'),
          ('Map of connections', 'map.html'), ('Fallacies', 'fallacies.html'), ('Biases', 'biases.html'), ('Glossary', 'glossary.html'), ('Library', 'library.html')]
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
        for campo in ('frase', 'por', 'lugar', 'nota', 'fontes', 'formas'):
            if campo in t: r[campo] = t[campo]
        r['lugar'] = r['lugar'].replace('{V12}', cod_pt.get('Ser vegano exige ser anticapitalista.', ''))
    pol = g['politicas']
    pol.INTRO = POL_INTRO or pol.INTRO
    pol.ESPECTRO = POL_ESPECTRO
    for t in pol.TEORIAS:
        x = POLITICAS.get(t['s'])
        if not x: falta('política', t['s']); continue
        for campo in ('t', 'frase', 'principio', 'quebra', 'replica', 'resposta', 'fontes', 'mais', 'nomes'):
            if campo in x: t[campo] = x[campo]
        if t['s'] in POL_CURTAS: t['curta'], t['pergunta'] = POL_CURTAS[t['s']]
        else: falta('política curta', t['s'])
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
    novos = []
    for n, d, u in bib.ORGS:
        if u in SITES: novos.append((SITES[u][0], SITES[u][1], SITES_URL.get(u, u)))
        else: falta('organização', n); novos.append((n, d, u))
    bib.ORGS[:] = novos
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
# Absorvidos na revisão de 2026-11-20: A20 em B2, J24 (hoje J99) em K10
_EXTRA_EN.setdefault('B2', []).extend(["Animals don't know they're going to die, so killing them is fine", "They don't suffer over the idea of death", 'Animals live in the present; they make no plans', 'It has no sense of the future, so it loses nothing', 'For a cow, being alive or dead makes no difference'])
_EXTRA_EN.setdefault('K10', []).extend(['A vegan world is utopian', 'That will never happen', "It's a hippie dream", 'Humans are cruel by nature; that will never change'])
