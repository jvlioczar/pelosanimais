"""Livro em PDF com o essencial de cada argumento do catálogo, um argumento por página, na estética do site.
Uso: python tools/livro.py  ->  _livro/guia-de-argumentacao-pelos-animais.pdf (pasta fora do site, no .gitignore)

Reaproveita os dados do site importando build.py (que reconstrói o site em português no caminho).
Os textos pessoais (sobre o autor, dedicatória, agradecimentos, ficha catalográfica, contracapa) ficam em tools/livro_textos.py.
Estrutura de livro impresso: capa, falso rosto, folha de rosto, créditos e ficha, dedicatória, agradecimentos, sumário,
sobre o projeto, como usar, as famílias (cada uma abrindo numa página ímpar) e, no fim, sobre o autor, continue no site e contracapa.
Reúne só os argumentos do catálogo; outros conteúdos do site podem seguir o mesmo molde."""
import html, os, pathlib, re, sys, tempfile

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(AQUI)
sys.argv = [sys.argv[0]]  # build em português
sys.path.insert(0, AQUI)
import build as B  # noqa: E402
import livro_textos as T  # noqa: E402

e = lambda s: html.escape(str(s), quote=True)
FONTES = os.path.join(AQUI, 'fontes')
uri = lambda *p: pathlib.Path(os.path.join(FONTES, *p)).as_uri()

# Fontes estáticas: o Chrome converte fontes variáveis em Type 3 no PDF, que muitas gráficas recusam.
# Por isso cada peso usado no livro vira um arquivo TrueType comum (instância da fonte variável), guardado em _livro/fontes.
PESOS = [('Mozilla Headline', 'mozillaheadline', 'MozillaHeadline[wdth,wght].ttf', 'normal', {'wdth': 100}, (600, 650, 700)),
         ('Inter', 'inter', 'Inter[opsz,wght].ttf', 'normal', {'opsz': 14}, (400, 500, 600, 700)),
         ('Inter', 'inter', 'Inter-Italic[opsz,wght].ttf', 'italic', {'opsz': 14}, (400, 500)),
         ('JetBrains Mono', 'jetbrainsmono', 'JetBrainsMono[wght].ttf', 'normal', {}, (500,))]

def fontes_estaticas():
    from fontTools.ttLib import TTFont
    from fontTools.varLib import instancer
    pasta = os.path.join(RAIZ, '_livro', 'fontes'); os.makedirs(pasta, exist_ok=True)
    faces = []
    for fam, dir_, arq, estilo, fixos, pesos in PESOS:
        for w in pesos:
            nome = f'{fam.replace(" ", "")}-{w}{"Italic" if estilo == "italic" else ""}'
            dest = os.path.join(pasta, nome + '.ttf')
            if not os.path.exists(dest):
                f = instancer.instantiateVariableFont(TTFont(os.path.join(FONTES, dir_, arq)), dict(fixos, wght=w))
                for r in f['name'].names:
                    if r.nameID in (4, 6): r.string = nome
                f.save(dest)
            faces.append(f"@font-face{{font-family:'{fam}';src:url('{pathlib.Path(dest).as_uri()}');font-weight:{w};font-style:{estilo}}}")
    return '\n'.join(faces)

N15 = len(B.ARGS) // 10 * 10
TITULO = 'Guia de Argumentação Pelos Animais'
SUB = f'Respostas a mais de {N15} argumentos contra o veganismo e o antiespecismo'
SITE = B.SITE_PT.replace('https://', '')
ANO = B.ATUALIZADO[:4]

def plano(no):
    return re.sub(r'\s+', ' ', B.texto(no)).strip()

def paragrafos(t):
    """Parágrafos separados por linha em branco; [texto](https://...) vira link clicável no PDF."""
    def fmt(h):
        h = re.sub(r'\[([^\]]+)\]\((https?://[^)\s]+)\)', r'<a href="\2">\1</a>', e(h))
        return re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', h)
    out = ''
    for bloco in (b.strip() for b in t.strip().split('\n\n')):
        if not bloco: continue
        linhas = bloco.split('\n')
        if all(l.startswith('- ') for l in linhas): out += '<ul>' + ''.join(f'<li>{fmt(l[2:])}</li>' for l in linhas) + '</ul>'
        else: out += f'<p>{fmt(bloco).replace(chr(10), "<br/>")}</p>'
    return out

def vazio(rotulo):
    return f'<div class="vazio">{e(rotulo)}</div>'

def chave_pix():
    """A chave Pix fica fora do código, como no site: variável de ambiente GUIA_PIX ou o arquivo pessoal ~/.guia-doacoes."""
    v = os.environ.get('GUIA_PIX', '').strip()
    arq = os.path.join(os.path.expanduser('~'), '.guia-doacoes')
    if not v and os.path.exists(arq):
        for ln in open(arq, encoding='utf-8'):
            k, _, val = ln.partition('=')
            if k.strip() == 'GUIA_PIX': v = val.strip()
    return v

def essencial(c):
    """Resposta curta e pergunta de retorno, em texto simples (seção 4 do capítulo)."""
    if c not in B.CAPS: return [], ''
    ps, ret = [], ''
    for no in B.secao_cap(c, 4):
        if no.tag != 'paragraph': continue
        t = plano(no)
        if not t: continue
        if t.startswith('Pergunta de retorno'): ret = re.sub(r'^Pergunta de retorno:?\s*', '', t)
        else: ps.append(t)
    return ps, ret

CSS = """
{FACES}
@page{size:420pt 594pt;margin:0}  /* A5 arredondado para um número inteiro de pixels (560 x 792): com outras medidas o Chrome deixa um filete branco nas páginas coloridas */
:root{--papel:#fcfaf5;--areia:#f4f1e3;--tinta:#0a3703;--texto:#173300;--suave:#4f6346;--linha:#dcdac6;--amarelo:#ffeb5b;
  --serif:'Mozilla Headline',sans-serif;--sans:'Inter',sans-serif;--mono:'JetBrains Mono',monospace}
*{box-sizing:border-box}
html,body{margin:0;padding:0;background:var(--papel);color:var(--texto);font:400 10pt/1.5 var(--sans);-webkit-print-color-adjust:exact;print-color-adjust:exact}
a{color:inherit}
.pag{width:420pt;height:594pt;position:relative;overflow:hidden;background:var(--papel);page-break-after:always;break-after:page;padding:14mm 14mm 16mm}
.pag:last-child{page-break-after:auto;break-after:auto}
.rodape{position:absolute;left:14mm;right:14mm;bottom:7mm;display:flex;justify-content:space-between;font:500 7pt var(--mono);color:var(--suave);letter-spacing:.02em}
.par .rodape{flex-direction:row-reverse}
h1,h2,h3{font-family:var(--serif);color:var(--tinta);margin:0;line-height:1.08;letter-spacing:-.01em}
.ti{font:700 6.8pt var(--sans);text-transform:uppercase;letter-spacing:.11em;color:var(--suave);margin:0 0 2.2mm}
.vazio{border:1.2px dashed var(--linha);border-radius:3mm;color:var(--suave);font:500 8pt var(--mono);display:flex;align-items:center;justify-content:center;text-align:center;padding:6mm;min-height:40mm}
/* capa e contracapa */
.capa,.contra{--bg:var(--tinta);color:#fff;padding:18mm 15mm;display:flex;flex-direction:column}
.capa,.contra,.fam{background:var(--bg)}
.capa .selo{align-self:flex-start;background:var(--amarelo);color:var(--tinta);font:700 7.5pt var(--sans);letter-spacing:.1em;text-transform:uppercase;padding:1.6mm 4mm;border-radius:99px}
.capa{padding:15mm 15mm 14mm;align-items:center;text-align:center}
.capa .sub{margin-left:auto!important;margin-right:auto!important}
.capa .logo{width:88mm;height:88mm;background:var(--amarelo);border-radius:18mm;padding:13mm;margin:0}
.capa .logo svg{display:block}
.capa h1{color:#fff;font-size:40pt;font-weight:700;margin:10mm 0 6mm;line-height:1.0;white-space:nowrap}
.capa h1 span,.contra h2 span{color:var(--amarelo)}
.capa .sub{font:500 15pt/1.35 var(--sans);color:#d8e8cf;margin:0;max-width:112mm}
.capa .autor{font:600 14pt var(--sans);color:#fff;margin:auto 0 0}
.faixa{margin-top:auto;display:flex;gap:1.6mm;flex-wrap:wrap}
.faixa i{width:7.2mm;height:7.2mm;border-radius:50%;display:inline-flex;align-items:center;justify-content:center;font:700 8pt var(--sans);font-style:normal;color:#fff}
.capa .pe,.contra .pe{margin-top:8mm;font:500 8pt var(--mono);color:#c6dcd3;display:flex;justify-content:space-between}
.contra{align-items:center;text-align:center;justify-content:center}
.contra p{max-width:108mm;text-wrap:balance}
.contra .pe{justify-content:center;margin-top:24mm;font-size:11pt}
.contra .pe a{color:#c6dcd3;text-decoration:none}
.contra h2{color:#fff;font-size:20pt;margin:0 0 7mm}
.contra p{font:400 10.5pt/1.55 var(--sans);color:#e6efe0;margin:0 0 3.6mm}
.contra p:first-of-type{font:600 13pt/1.35 var(--serif);color:var(--amarelo)}
/* falso rosto, rosto, créditos, dedicatória */
.falso{display:flex;align-items:center;justify-content:center;text-align:center}
.falso h1{font-size:17pt}
.rosto{display:flex;flex-direction:column;text-align:center;padding-top:40mm}
.rosto h1{font-size:26pt;font-weight:700}
.rosto .sub{font:500 11pt/1.4 var(--sans);color:var(--suave);margin:6mm auto 0;max-width:100mm}
.rosto .vol{font:700 7.5pt var(--sans);letter-spacing:.11em;text-transform:uppercase;color:var(--suave);margin:10mm 0 0}
.rosto .autor{font:600 12pt var(--sans);color:var(--tinta);margin:auto 0 0}
.rosto .ed{font:500 8pt var(--mono);color:var(--suave);margin:3mm 0 0}
.creditos{display:flex;flex-direction:column;justify-content:flex-end;font-size:7.8pt;line-height:1.5;color:var(--suave)}
.creditos p{margin:0 0 2.6mm}
.creditos .ficha{margin:5mm 0 0}
.creditos .ficha pre{font:400 7.4pt/1.45 var(--mono);white-space:pre-wrap;border:1px solid var(--texto);padding:4mm;margin:0;color:var(--texto)}
.ded{display:flex;align-items:center;justify-content:flex-end;flex-direction:column;padding-bottom:60mm}
.ded .txt{font:italic 400 11pt/1.6 var(--sans);text-align:right;align-self:flex-end;max-width:85mm}
.ded .vazio{width:100%}
/* textos corridos */
.texto h2{font-size:20pt;margin:0 0 6mm}
.texto p{margin:0 0 3.2mm}
.texto .caixa{background:var(--areia);border-radius:4mm;padding:4mm 5mm;margin:4mm 0}
.texto .caixa p:last-child{margin:0}
.texto ul{margin:0 0 3mm;padding-left:5mm}
.texto li{margin:0 0 1.6mm}
/* sumário */
.sum li{display:flex;align-items:baseline;gap:2mm;list-style:none;margin:0 0 2.1mm}
.sum ol{padding:0;margin:0}
.fams h2{margin-bottom:3.5mm}
.fams ul{list-style:none;padding:0;margin:0}
.fams li{display:flex;gap:2.6mm;margin:0 0 1.5mm;align-items:flex-start}
.fams .l{flex:none;width:5.6mm;height:5.6mm;border-radius:50%;color:#fff;font:700 7pt/5.6mm var(--sans);text-align:center;margin-top:.3mm}
.fams strong{font-size:8pt;color:var(--tinta);line-height:1.25}
.fams p{margin:.2mm 0 0;font-size:7.5pt;line-height:1.32;color:var(--texto)}
.sum .l{flex:none;width:6mm;height:6mm;border-radius:50%;color:#fff;font:700 7.5pt/6mm var(--sans);text-align:center;align-self:center}
.sum a{text-decoration:none;flex:1;display:flex;gap:2mm}
.sum a span{flex:1;border-bottom:1px dotted var(--linha)}
.sum small{font:500 7.5pt var(--mono);color:var(--suave)}
/* família */
.fam{color:#fff;display:flex;flex-direction:column;justify-content:center}
.fam .letra{font:700 92pt/1 var(--serif);margin:0 0 4mm}
.fam h2{color:#fff;font-size:24pt;margin:0 0 5mm}
.fam .perg{font:500 13pt/1.35 var(--sans);margin:0 0 9mm;color:#fff}
.fam .parte{font:600 8.5pt/1.5 var(--sans);background:rgba(255,255,255,.16);border-radius:3mm;padding:3.5mm 4.5mm;margin:0}
.fam .parte b{display:block;font-weight:700;margin-top:1.2mm}
.fam .rodape{color:rgba(255,255,255,.75)}
/* argumento */
.arg{padding-bottom:30mm}
.arg .topo{display:flex;align-items:center;justify-content:space-between;gap:3mm;margin:0 0 6mm}
.arg .fam-n{font:700 7pt var(--sans);text-transform:uppercase;letter-spacing:.09em;color:var(--c)}
.arg .parte-n{font:700 6.5pt var(--sans);text-transform:uppercase;letter-spacing:.08em;color:var(--suave);border:1px solid var(--linha);border-radius:99px;padding:.7mm 2.4mm;white-space:nowrap}
.arg .barra{position:absolute;top:0;bottom:0;width:4mm;background:var(--c);right:0}
.arg.par .barra{right:auto;left:0}  /* na borda externa: direita nas ímpares, esquerda nas pares */
.arg .cod{display:inline-block;background:var(--c);color:#fff;font:700 9pt var(--sans);border-radius:99px;padding:1mm 3.6mm;margin:0 0 3mm}
.arg h2{font-size:19pt;font-weight:650;margin:0 0 6mm;text-wrap:balance}
.corpo{font-size:var(--fs,10pt)}
.falha{background:var(--areia);border-radius:3mm;padding:3mm 4mm;margin:0 0 5mm}
.falha .txt{margin:0;font-weight:600;color:var(--tinta);line-height:1.4}
.curta p{margin:0 0 2.6mm}
.doacao{margin-top:4mm}.doacao code{font:500 0.95em var(--mono)}
.retorno{background:var(--tinta);color:#fff;border-radius:3.5mm;padding:3.4mm 4.5mm;margin:4mm 0 0}
.retorno .ti{color:var(--amarelo);margin-bottom:1.4mm}
.retorno .txt{margin:0;font-weight:600;line-height:1.4}
.ind{font:italic 500 .86em/1.4 var(--sans);color:var(--suave);margin:4mm 0 0}
.botao{position:absolute;left:14mm;right:14mm;bottom:14mm;display:flex;align-items:center;justify-content:center;gap:2mm;text-decoration:none;text-align:center;
  background:var(--amarelo);color:var(--tinta);border-radius:99px;padding:2.8mm 5mm;font:700 9pt var(--sans)}
.botao .seta{font-size:1.1em;line-height:1}
"""

class Livro:
    """Páginas do miolo numeradas a partir de 1 (a primeira depois da capa é ímpar, à direita)."""
    def __init__(self): self.pags = []
    @property
    def prox(self): return len(self.pags) + 1
    def add(self, conteudo, classe='', estilo='', num=True, ancora=''):
        self.pags.append(dict(c=conteudo, classe=classe, estilo=estilo, num=num, ancora=ancora)); return len(self.pags)
    def branco(self): return self.add('', 'branco', num=False)
    def impar(self):
        if self.prox % 2 == 0: self.branco()
    def html(self):
        out = []
        for n, p in enumerate(self.pags, 1):
            par = ' par' if n % 2 == 0 else ''
            pe = f'<div class="rodape"><span>{e(TITULO)}</span><span>{n}</span></div>' if p['num'] else ''
            ida = f' id="{p["ancora"]}"' if p['ancora'] else ''
            out.append(f'<section class="pag {p["classe"]}{par}"{ida} style="{p["estilo"]}">{p["c"]}{pe}</section>')
        return ''.join(out)

def gera():
    fams = [B.FAMILIAS[f] for f in sorted({B.ARGS[c]['fam'] for c in B.ORDEM}, key=lambda f: B.ORDEM.index(next(c for c in B.ORDEM if B.ARGS[c]['fam'] == f)))]
    por_fam = {f['c']: [c for c in B.ORDEM if B.ARGS[c]['fam'] == f['c']] for f in fams}
    faixa = '<div class="faixa">' + ''.join(f'<i style="background:{f["cor"]}">{f["c"]}</i>' for f in fams) + '</div>'

    # primeira passada só para descobrir os números das páginas do sumário; a segunda escreve o sumário com eles
    def monta(numeros):
        L = Livro()
        L.add(f'<h1>{e(TITULO)}</h1>', 'falso', num=False)
        L.branco()
        L.add(f'<h1>Guia de Argumentação Pelos Animais</h1><p class="sub">{e(SUB)}</p>'
              f'<p class="autor">{e(T.AUTOR)}</p><p class="ed">{e(T.EDITORA) + " · " if T.EDITORA else ""}{ANO}</p>', 'rosto', num=False)
        ficha = f'<pre>{e(T.FICHA.strip())}</pre>' if T.FICHA.strip() else vazio('Ficha catalográfica (a inserir)')
        L.add(f'<p><strong>{e(TITULO)}</strong></p>'
              f'<p>© {ANO} {e(T.AUTOR)}<br/>{"Publicado por " + e(T.EDITORA) + ". " if T.EDITORA else ""}Edição digital de {B.ATUALIZADO[8:10]}/{B.ATUALIZADO[5:7]}/{ANO}.</p>'
              f'<p>O conteúdo completo e atualizado deste livro está disponível gratuitamente em <a href="{B.SITE_PT}">{e(SITE)}</a>.</p>'
              '<p>Texto sob a licença <a href="https://creativecommons.org/licenses/by/4.0/deed.pt-br">Creative Commons Atribuição 4.0 Internacional (CC BY 4.0)</a>: pode ser copiado, compartilhado e adaptado, inclusive para fins comerciais, desde que a fonte seja citada. Materiais de terceiros citados seguem as licenças de origem.</p>'
              f'<p>Fontes tipográficas: Mozilla Headline, Inter e JetBrains Mono, sob a licença SIL Open Font License.</p>'
              f'<div class="ficha">{ficha}</div>', 'creditos', num=False)
        L.add(f'<div class="txt">{paragrafos(T.DEDICATORIA)}</div>' if T.DEDICATORIA.strip() else vazio('Dedicatória (opcional)'), 'ded', num=False)
        L.branco()
        L.add('<div class="texto"><h2>Agradecimentos</h2>' + (paragrafos(T.AGRADECIMENTOS) if T.AGRADECIMENTOS.strip() else vazio('Agradecimentos (a escrever)')) + '</div>')
        L.branco()
        itens = [('+', 'var(--tinta)', 'Sobre o projeto', 'projeto', ''), ('+', 'var(--tinta)', 'Como usar este livro', 'como', ''), ('+', 'var(--tinta)', 'As famílias', 'familias', '')]
        itens += [(f['c'], f['cor'], f['nome'], f'fam-{f["c"]}', f' <small>· {len(por_fam[f["c"]])}</small>') for f in fams]
        itens += [('+', 'var(--tinta)', 'Sobre o autor', 'autor', ''), ('+', 'var(--tinta)', 'Continue no site', 'fim', '')]
        sumario = '<h2>Sumário</h2><ol>' + ''.join(
            f'<li><span class="l" style="background:{cor}">{l}</span><a href="#{a}"><span>{e(nome)}{extra}</span><small>{numeros.get(a, "")}</small></a></li>'
            for l, cor, nome, a, extra in itens) + '</ol>'
        L.add(f'<div class="texto sum">{sumario}</div>')
        L.branco()
        num = {}
        num['projeto'] = L.add(f'<div class="texto"><h2>Sobre o projeto</h2>{paragrafos(T.SOBRE_PROJETO)}</div>', ancora='projeto')
        L.impar()
        como = (f'<h2>Como usar este livro</h2>'
                f'<p>Este livro reúne o essencial de {len(B.ARGS)} argumentos usados contra o veganismo e o antiespecismo, um por página, organizados em {len(fams)} famílias. '
                'Cada argumento aparece na forma em que costuma ser dito, com uma réplica direta, do jeito que se diria à pessoa. O que ele acerta, a versão mais forte e a desmontagem completa ficam no capítulo do site.</p>'
                '<p>Em cada página você encontra:</p><ul>'
                '<li><strong>A frase</strong>, como ela costuma aparecer numa conversa;</li>'
                '<li><strong>A falha principal</strong>, em uma linha;</li>'
                '<li><strong>Uma réplica</strong>, para usar na hora;</li>'
                '<li><strong>Uma pergunta</strong> para devolver e manter a conversa aberta;</li>'
                '<li><strong>Um botão</strong>, “Veja o argumento completo”, que abre o capítulo no site, com a versão mais forte do argumento, a desmontagem passo a passo, os erros e vieses, as conexões e as fontes.</li></ul>'
                '<div class="caixa"><p><strong>Argumentos diretos e indiretos.</strong> Os argumentos da Parte DIR discutem se é certo explorar os animais. '
                'Os da Parte IND discutem saúde, ambiente, economia ou quem defende o veganismo. Nesses, vale corrigir os fatos e depois voltar à pergunta de fundo: '
                'os interesses dos animais contam?</p></div>')
        pix = chave_pix()
        if pix:
            como += (f'<p class="doacao"><strong>Gostou do livro?</strong> Uma doação ajuda a manter o site no ar e a fazer mais projetos para ajudar os animais. '
                     f'Pix: <code>{e(pix)}</code></p>')
        num['como'] = L.add(f'<div class="texto">{como}</div>', ancora='como')
        lista = ''.join(f'<li><span class="l" style="background:{f["cor"]}">{f["c"]}</span><div><strong>{e(f["nome"])}</strong>'
                        f'<p>{e(T.FAMILIAS.get(f["c"], f["perg"]))}</p></div></li>' for f in fams)
        num['familias'] = L.add(f'<div class="texto fams"><h2>As famílias</h2><ul>{lista}</ul></div>', ancora='familias')
        for f in fams:
            L.impar()
            dir_ = f['parte'] == 'DIR'
            parte = ('Parte DIR · argumentos diretos: discutem se é certo usar os animais.' if dir_ else
                     'Parte IND · argumentos indiretos: discutem saúde, ambiente, economia ou quem defende os animais. Corrija os fatos e volte à pergunta moral.')
            num[f'fam-{f["c"]}'] = L.add(f'<p class="letra">{f["c"]}</p><h2>{e(f["nome"])}</h2><p class="perg">{e(f["perg"])}</p>'
                                         f'<p class="parte">{e(parte)}<b>{len(por_fam[f["c"]])} argumentos</b></p>', 'fam', f'--bg:{f["cor"]}', ancora=f'fam-{f["c"]}')
            for c in por_fam[f['c']]:
                a = B.ARGS[c]
                ps, ret = essencial(c)
                url = f'{B.SITE_PT}/argumentos/{a["slug"]}.html'
                corpo = (f'<div class="falha"><p class="ti">A falha principal</p><p class="txt">{e(a["falha"])}</p></div>'
                         + (f'<div class="curta">' + ''.join(f'<p>{e(p)}</p>' for p in ps) + '</div>' if ps else '')
                         + (f'<div class="retorno"><p class="ti">Devolva com uma pergunta</p><p class="txt">{e(ret)}</p></div>' if ret else '')
                         + ('' if dir_ else '<p class="ind">Argumento indireto: corrija os fatos, mas lembre que a questão de fundo é se os interesses dos animais contam.</p>'))
                L.add(f'<div class="barra"></div><div class="topo"><span class="fam-n">{f["c"]} · {e(f["nome"])}</span><span class="parte-n">{"Direto" if dir_ else "Indireto"}</span></div>'
                      f'<span class="cod">{c}</span><h2>“{e(a["frase"].rstrip("."))}”</h2><div class="corpo">{corpo}</div>'
                      f'<a class="botao" href="{e(url)}">Veja o argumento completo <span class="seta">↗</span></a>',
                      'arg', f'--c:{f["cor"]}')
        L.impar()
        num['autor'] = L.add(f'<div class="texto"><h2>Sobre o autor</h2>{paragrafos(T.SOBRE_AUTOR)}</div>', ancora='autor')
        L.impar()
        num['fim'] = L.add('<div class="texto"><h2>Continue no site</h2>'
                           '<p>Este livro traz só o essencial de cada argumento. No site, cada um tem um capítulo completo: a versão mais forte da objeção, o que ela acerta, '
                           'a resposta passo a passo, a melhor réplica e por que ela também falha, os erros de raciocínio, os vieses, as contradições e as fontes.</p>'
                           '<p>Lá também estão o mapa de conexões entre os argumentos, um debate simulado para treinar, os argumentos que veganos deveriam parar de usar, '
                           'as objeções políticas e éticas, a biblioteca e o glossário.</p>'
                           f'<div class="caixa"><p><strong><a href="{B.SITE_PT}">{e(SITE)}</a></strong><br/>Gratuito, sem cadastro, revisado e atualizado.</p></div></div>', ancora='fim')
        if len(L.pags) % 2: L.branco()  # miolo com número par de páginas, como num caderno impresso
        return L, num
    _, num = monta({})
    L, num2 = monta(num)
    assert num == num2
    logo = re.sub(r'width="\d+" height="\d+"', 'width="100%" height="100%"', B.LOGO)
    capa = (f'<div class="logo">{logo}</div><h1>Guia de<br/>Argumentação<br/><span>Pelos Animais</span></h1><p class="sub">{e(SUB)}</p>'
            f'<p class="autor">{e(T.AUTOR)}</p>')
    contra = (f'<h2>Guia de Argumentação<br/><span>Pelos Animais</span></h2>{paragrafos(T.CONTRACAPA.format(n=N15))}'
              f'<div class="pe"><a href="{B.SITE_PT}">{e(SITE)}</a></div>')
    corpo = f'<section class="pag capa">{capa}</section>{L.html()}<section class="pag contra">{contra}</section>'
    return f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"/><title>{e(TITULO)}</title><style>{CSS.replace('{FACES}', fontes_estaticas())}</style></head><body>{corpo}</body></html>', len(L.pags)

AJUSTA = """() => {
  const ajustes = [];
  for (const p of document.querySelectorAll('.pag.arg')) {
    const corpo = p.querySelector('.corpo'), botao = p.querySelector('.botao');
    const limite = () => botao.getBoundingClientRect().top - 4;
    let fs = 10;
    while (corpo.getBoundingClientRect().bottom > limite() && fs > 7.6) { fs -= 0.2; corpo.style.setProperty('--fs', fs + 'pt'); }
    if (corpo.getBoundingClientRect().bottom > limite()) { p.querySelector('h2').style.fontSize = '16pt'; }
    const cod = p.querySelector('.cod').textContent;
    if (corpo.getBoundingClientRect().bottom > limite()) ajustes.push(cod + ': ESTOURA');
    else if (fs < 10) ajustes.push(cod + ':' + fs.toFixed(1));
  }
  for (const p of document.querySelectorAll('.pag:not(.arg)')) if (p.scrollHeight > p.clientHeight + 1) ajustes.push('estoura: ' + (p.id || p.className));
  return ajustes;
}"""

if __name__ == '__main__':
    doc, n = gera()
    tmp = os.path.join(tempfile.gettempdir(), 'guia_livro.html')
    open(tmp, 'w', encoding='utf-8').write(doc)
    saida = os.path.join(RAIZ, '_livro'); os.makedirs(saida, exist_ok=True)
    pdf = os.path.join(saida, 'guia-de-argumentacao-pelos-animais.pdf')
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        nav = None
        for canal in ('chrome', 'msedge', None):
            try: nav = p.chromium.launch(channel=canal) if canal else p.chromium.launch(); break
            except Exception: continue
        pg = nav.new_page()
        pg.goto(pathlib.Path(tmp).as_uri()); pg.wait_for_load_state('networkidle'); pg.evaluate('document.fonts.ready')
        ajustes = pg.evaluate(AJUSTA)
        pg.pdf(path=pdf, prefer_css_page_size=True, print_background=True)
        nav.close()
    print(f'miolo: {n} páginas, mais capa e contracapa ->', pdf)
    print('ajustes:', ajustes)
