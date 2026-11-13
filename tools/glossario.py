"""Glossário: lê data/glossario.md (rascunho do Dicionário-Guia de Ética e Defesa Animal, 2026-11-13) e devolve seções e verbetes.
Fica de fora a seção de organizações (bibliotecas e organizações já têm página própria) e os verbetes marcados com ⚠️ (definição incerta, a revisar)."""
import os, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECOES, VERBETES, PENDENTES = [], [], []
_sec = None
_atual = None
for linha in open(os.path.join(ROOT, 'data', 'glossario.md'), encoding='utf-8').read().split('\n'):
    m = re.match(r'## (\d+)\. (.*)', linha)
    if m:
        _atual = None
        if 'Organizações' in m[2]: _sec = None; continue
        _sec = (int(m[1]), m[2].strip()); SECOES.append(_sec); continue
    if re.match(r'## ', linha): _sec = None; continue
    if _sec is None: continue
    if re.match(r'\*\*[^*]+\*\*\s*\*\(ver ', linha): continue  # remissivas soltas, sem definição
    m = re.match(r'\*\*(.+?)\*\*\s*(⚠️)?\s*—\s*(.*)', linha)
    if m:
        _atual = dict(termo=m[1].strip(), sec=_sec[0], dubio=bool(m[2]), texto=m[3].strip(), links=[])
        VERBETES.append(_atual); continue
    if _atual is None: continue
    l = linha.strip()
    if l.startswith('- http'): _atual['links'].append(l[2:].strip())
    elif l and l != '---' and not l.startswith('*Para entender mais'): _atual['texto'] += ' ' + l
for v in VERBETES:
    t = v['texto']
    m = re.search(r'\s\*([^*]+)\*\s*$', t)
    v['def'], v['com'] = (t[:m.start()].strip(), m[1].strip()) if m else (t, '')
    del v['texto']
PENDENTES = [v['termo'] for v in VERBETES if v['dubio']]
VERBETES = [v for v in VERBETES if not v['dubio']]

# termos que o glossário original de Julio tinha e o rascunho não (2026-11-13), com definição reescrita; veja data/novos/glossario_extra.json
import json as _json
VERBETES += [dict(v, dubio=False) for v in _json.load(open(os.path.join(ROOT, 'data', 'novos', 'glossario_extra.json'), encoding='utf-8'))]
VERBETES.sort(key=lambda v: __import__('unicodedata').normalize('NFD', v['termo'].lower()).encode('ascii', 'ignore').decode())
for _i, _v in enumerate(VERBETES): _v['i'] = _i; _v['pt'] = _v['termo']

SECOES_EN = {1: 'Sentience, Consciousness and Cognition', 2: 'Technical Fields Related to Animals', 3: 'Criteria and Moral Status', 4: 'Normative Ethical Theories',
    5: 'Currents of Animal Ethics', 6: 'Biases, Fallacies and Rhetoric', 7: 'Animal Law and Legislation', 8: 'Livestock, Exploitation and Related Practices',
    9: 'Animal-Derived Products', 10: 'Plant-Derived Products', 11: 'Reducing and Ending the Use of Animals', 12: 'Experiences (Welfare, Pain and Affective States)',
    13: 'Activism and the Movement', 14: 'Movement Strategy: Reformism, Abolitionism and Ethical Washing', 15: 'Diet and Vegetarianism: Variants',
    16: 'Intersectionality and Social Justice', 17: 'Applied Ethics, the Future and Technology'}
def traduz():
    """Troca termo, definição e comentário pelas versões em inglês (data/novos/glos_en_*.json, por posição na lista) e reordena."""
    import glob, unicodedata
    en = {}
    for f in glob.glob(os.path.join(ROOT, 'data', 'novos', 'glos_en_*.json')):
        for x in _json.load(open(f, encoding='utf-8')): en[x['pt']] = x
    for v in VERBETES:
        x = en.get(v['pt'])
        if not x or not x['def'].strip(): print('glossário sem tradução:', v['termo']); continue
        v['termo'], v['def'], v['com'] = x['termo'].strip(), x['def'].strip(), (x.get('com') or '').strip()
    VERBETES.sort(key=lambda v: unicodedata.normalize('NFD', v['termo'].lower()).encode('ascii', 'ignore').decode())
    SECOES[:] = [(n, SECOES_EN[n]) for n, _ in SECOES]
