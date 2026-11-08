"""Converte os capítulos escritos aqui (data/capitulos_md/*.md) para o mesmo XML que os exportados do doc original.

O Markdown aceito é o mínimo que os capítulos usam: # e ## e ### títulos, parágrafos, listas com - ou 1.,
tabelas com | e, dentro do texto, **negrito**, *itálico* e [link](url).
"""
import glob, html, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
e = lambda s: html.escape(s, quote=True)
INLINE = re.compile(r'\*\*(.+?)\*\*|\*(.+?)\*|\[(.+?)\]\((\S+?)\)')

def runs(s):
    """Texto em <text>, um por trecho com a mesma marcação."""
    out, pos = [], 0
    for m in INLINE.finditer(s):
        if m.start() > pos: out.append(f'<text>{e(s[pos:m.start()])}</text>')
        if m[1] is not None: out.append(f'<text><bold>{e(m[1])}</bold></text>')
        elif m[2] is not None: out.append(f'<text><italic>{e(m[2])}</italic></text>')
        else:
            dentro = re.sub(r'^\*(.+)\*$', r'<italic>\1</italic>', e(m[3]))
            out.append(f'<text><link href="{e(m[4])}">{dentro}</link></text>')
        pos = m.end()
    if pos < len(s): out.append(f'<text>{e(s[pos:])}</text>')
    return ''.join(out)

def par(s, nivel=None):
    return f'<paragraph{f" heading={chr(39)}{nivel}{chr(39)}" if nivel else ""}>{runs(s)}</paragraph>'

def converte(md):
    o, linhas, i = [], md.splitlines(), 0
    while i < len(linhas):
        l = linhas[i].rstrip()
        if not l: i += 1; continue
        if l == '[[ARVORE]]': o.append('<codeBlock/>'); i += 1; continue  # árvore de decisão (A1, A10)
        m = re.match(r'(#{1,3}) (.*)', l)
        if m: o.append(par(m[2], len(m[1]))); i += 1; continue
        if l.startswith('|'):
            rows = []
            while i < len(linhas) and linhas[i].startswith('|'):
                cels = [c.strip() for c in linhas[i].strip().strip('|').split('|')]
                if not all(re.fullmatch(r':?-{3,}:?', c) for c in cels): rows.append(cels)
                i += 1
            t = ''.join('<row>' + ''.join(f'<cell{" header=" + chr(39) + "true" + chr(39) if n == 0 else ""}>{par(c)}</cell>' for c in r) + '</row>' for n, r in enumerate(rows))
            o.append(f'<table>{t}</table>'); continue
        m = re.match(r'(-|\d+\.) ', l)
        if m:
            kind = 'bullet' if m[1] == '-' else 'ordered'
            itens = []
            while i < len(linhas) and re.match(r'(-|\d+\.) ', linhas[i]):
                itens.append(f'<listItem>{par(re.sub(r"^(-|\d+\.) ", "", linhas[i].rstrip()))}</listItem>'); i += 1
            o.append(f"<list kind='{kind}'>{''.join(itens)}</list>"); continue
        txt = [l]
        i += 1
        while i < len(linhas) and linhas[i].strip() and not re.match(r'(#{1,3} |\||-|\d+\. )', linhas[i]):
            txt.append(linhas[i].strip()); i += 1
        o.append(par(' '.join(txt)))
    return '<doc>' + ''.join(o) + '</doc>'

def todos(base=None):
    base = base or os.path.join(ROOT, 'data')
    saida = os.path.join(base, 'capitulos')
    os.makedirs(saida, exist_ok=True)
    for f in glob.glob(os.path.join(base, 'capitulos_md', '*.md')):
        cod = os.path.basename(f)[:-3]
        open(os.path.join(saida, cod + '.xml'), 'w', encoding='utf-8').write(converte(open(f, encoding='utf-8').read()))

if __name__ == '__main__':
    todos()
