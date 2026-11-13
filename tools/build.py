"""Gera o site a partir de data/catalogo.xml e data/capitulos/*.xml (exportados do doc original). Uso: python tools/build.py"""
import collections, glob, html, json, os, re
import sys
import xml.etree.ElementTree as ET

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import alem
import md2xml
import biblioteca
import politicas
import debate
from ruins import RUINS, TIPOS
from conexoes import DEPOIS, MOTIVOS

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Versão em inglês: `python tools/build.py en` gera o site em ../fortheanimals (fortheanimals.biblioverse.org).
# Os textos traduzidos ficam em tools/en/; o que ainda não foi traduzido aparece no relatório do fim do build.
import en
EN = 'en' in sys.argv[1:]
OUT = os.path.join(os.path.dirname(ROOT), 'fortheanimals') if EN else ROOT
SITE_PT, SITE_EN = 'https://pelosanimais.biblioverse.org', 'https://fortheanimals.biblioverse.org'
SITE = SITE_EN if EN else SITE_PT
EN_NO_AR = True  # vira True quando fortheanimals.biblioverse.org estiver publicado: só então o site em português mostra o botão EN e o hreflang
BILINGUE = EN or EN_NO_AR
NOME = en.NOME if EN else 'Guia de Argumentação Pelos Animais'
CURTO = en.CURTO if EN else 'Guia de Argumentação'
def _ultima_mudanca():
    """Data da última alteração no conteúdo (capítulos, catálogo, ferramentas, estilo), para o sitemap."""
    import datetime, glob as _g
    r = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    arqs = _g.glob(os.path.join(r, 'data', '**', '*.*'), recursive=True) + _g.glob(os.path.join(r, 'tools', '*.py')) + [os.path.join(r, 'assets', n) for n in ('style.css', 'app.js')]
    return datetime.date.fromtimestamp(max(os.path.getmtime(a) for a in arqs if os.path.exists(a))).isoformat()
ATUALIZADO = _ultima_mudanca()
def _data_fonte(k):
    """Data da última alteração da fonte de uma página, para o lastmod do sitemap: o capítulo (nos dois idiomas, no site em inglês),
    o arquivo de dados da seção, ou a data geral do conteúdo."""
    import datetime
    r = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    pasta, x = k
    if pasta == 'argumentos':
        c = x.upper()
        arqs = [os.path.join(r, 'data', 'capitulos_md', c + '.md'), os.path.join(r, 'data', 'capitulos', c + '.xml')]
        if EN: arqs.append(os.path.join(r, 'data', 'en', 'capitulos_md', c + '.md'))
    else:
        fonte = {'ruins': 'ruins.py', 'alem': 'alem.py', 'politicas': 'politicas.py'}.get((pasta or x).split('/')[0])
        if not fonte: return ATUALIZADO
        arqs = [os.path.join(r, 'tools', fonte)] + ([os.path.join(r, 'tools', 'en', 'ruins.py' if fonte == 'ruins.py' else 'paginas.py')] if EN else [])
    arqs = [a for a in arqs if os.path.exists(a)]
    return datetime.date.fromtimestamp(max(os.path.getmtime(a) for a in arqs)).isoformat() if arqs else ATUALIZADO
LASTMOD, ALTERNA = {}, {}
EXT = 'target="_blank" rel="noopener"'
PT_ONLY = set()  # páginas ainda sem versão em inglês: sem botão EN, sem hreflang e fora do site em inglês (nenhuma por enquanto)
IND_AVISO = ('Este é um argumento indireto: discute saúde, ambiente, economia, praticidade ou quem defende o veganismo, e não se os animais merecem respeito. '
    'Muitos ativistas contestam o uso desse tipo de argumento na defesa dos animais, porque ele escapa do que importa. '
    'Outros movimentos sociais não fazem isso: ninguém defende os direitos de pessoas discriminadas dizendo que tratá-las com justiça faz bem ao meio ambiente. '
    'Aqui, os fatos servem para corrigir o que está errado; a justificativa moral vem do respeito aos animais.')
import hashlib as _h
VER_CSS = _h.md5(open(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'assets', 'style.css'), 'rb').read()).hexdigest()[:8]
VER_DEB = _h.md5(open(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'assets', 'debate.js'), 'rb').read()).hexdigest()[:8]
VER_JS = _h.md5(open(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'assets', 'app.js'), 'rb').read()).hexdigest()[:8]
if EN:  # no site em inglês os scripts passam pela tradução; a versão muda também quando ela muda, para o navegador baixar o arquivo novo
    _trad = b''.join(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'en', n), 'rb').read() for n in ('ui.py', '__init__.py'))
    VER_JS = _h.md5(bytes.fromhex(VER_JS) + _trad).hexdigest()[:8]
    VER_DEB = _h.md5(bytes.fromhex(VER_DEB) + _trad).hexdigest()[:8]
IND_TEMA = {'G': 'saúde e nutrição', 'H': 'ambiente e agricultura', 'I': 'a utilidade de testes, roupas, lazer e companhia',
    'J': 'custo, praticidade e economia', 'K': 'eficácia e responsabilidade individual', 'L': 'quem defende o veganismo', 'N': 'a experiência de quem tentou ser vegano e desistiu'}
IND_EXEMPLO = {
    'G': 'Se o veganismo fosse defendido pela saúde, quem consegue ser saudável comendo animais, e muita gente consegue, não teria razão para mudar. E, se surgisse um produto animal comprovadamente mais saudável, o mesmo argumento passaria a defender a exploração. A saúde de quem come não diz se é justo o que se faz ao animal.',
    'H': 'Se o veganismo fosse defendido pelo ambiente, uma exploração de baixo impacto seria aceitável, mesmo que matasse mais seres sencientes. E ela já é promovida: criação de insetos, caça "sustentável", couro "sustentável". É possível reduzir o impacto ambiental e aumentar a exploração ao mesmo tempo.',
    'I': 'Se a defesa dos animais dependesse de mostrar que testes, roupas ou diversão com animais são inúteis, bastaria um uso útil para justificá-los. Mas a utilidade não decide a questão: nenhum benefício justifica usar pessoas que não consentiram, e o mesmo vale para os animais.',
    'J': 'Se o veganismo fosse defendido por ser barato, prático ou bom para a economia, bastaria uma situação em que a exploração fosse mais barata ou gerasse mais empregos para justificá-la. Ninguém aceita esse raciocínio quando as vítimas são humanas: explorar pessoas também já foi lucrativo.',
    'K': 'Se o veganismo fosse defendido só pelo impacto de cada pessoa, quem provasse que sua compra não muda nada estaria liberado. Mas ninguém aceita isso para outros danos: participar de uma injustiça continua errado mesmo quando a parte de cada um é pequena.',
    'N': 'Se o veganismo dependesse de ser fácil para todos, bastaria alguém ter dificuldade para que ele deixasse de valer. Mas a dificuldade de uma pessoa, que merece ser ouvida e ajudada, não muda o que acontece com os animais: ela pede apoio prático, e não uma nova conclusão moral.',
    'L': 'Se a questão dependesse de quem defende os animais, bastaria os veganos serem simpáticos e coerentes para o argumento valer, ou chatos e incoerentes para deixar de valer. Mas os animais sofrem do mesmo jeito, seja quem for o mensageiro.',
}
def aviso_ind(fc, rot, pre='../'):
    """Aviso no alto de cada capítulo e de cada família da Parte IND. O exemplo muda com a família (IND_EXEMPLO)."""
    fund = f'{pre}alem/fundamentos.html'
    return (f'<aside class="aviso-ind"><span>{rot}</span>'
        + L(f'<p><strong>Este é um argumento indireto, e a resposta a ele também é indireta.</strong> Ele discute {IND_TEMA[fc]}, e não se os animais merecem respeito. '
            f'A questão de fundo da defesa dos animais corre em paralelo a esta: é a senciência, a capacidade que os animais têm de ser prejudicados e beneficiados (<a href="{fund}">veja o que sustenta a ética animal</a>).</p>'
            '<p>Muitos ativistas contestam o uso desse tipo de argumento na defesa dos animais, porque ele escapa do que importa. Outros movimentos não se defendem assim: '
            'ninguém sustenta o antirracismo dizendo que ele faz bem ao meio ambiente, à saúde dos brancos ou à economia. O dano causado às vítimas já é a razão.</p>',
            f'<p><strong>This is an indirect argument, and the answer to it is indirect too.</strong> It is about {IND_TEMA[fc]}, not about whether animals deserve respect. '
            f'The underlying question in the defense of animals runs in parallel to this one: it is sentience, the capacity animals have to be harmed and benefited (<a href="{fund}">see what supports animal ethics</a>).</p>'
            '<p>Many activists question using this kind of argument to defend animals, because it sidesteps what matters. Other movements are not defended this way: '
            'no one makes the case for anti-racism by saying it is good for the environment, for the health of white people or for the economy. The harm done to the victims is already the reason.</p>')
        + f'<p><strong>Por que não é bom usá-lo, ou por que sempre complementá-lo com um argumento ético:</strong> {IND_EXEMPLO[fc]}</p>'
        + L('<p>Argumentos indiretos também não levam, sozinhos, ao veganismo. Muitas vezes sustentam, no máximo, o vegetarianismo, a redução do consumo ou o ambientalismo, '
            'que aceitam os usos de animais considerados saudáveis, baratos ou de baixo impacto.</p>'
            '<p>Por isso, discuta os fatos como fatos: corrija o que estiver errado e reconheça o que for verdade. Mas não trate a resposta como fundamento moral, '
            'porque do que <em>é</em> não se chega, sozinho, ao que <em>deve ser</em>: mesmo um benefício real não mostraria que é justo fazer alguém sofrer e morrer para obtê-lo. '
            'Para responder de verdade, mostre que o debate moral é outro: o especismo e o que acontece com os animais como indivíduos. ',
            '<p>Indirect arguments also do not lead to veganism on their own. Often they support, at most, vegetarianism, eating less or environmentalism, '
            'which accept the uses of animals seen as healthy, cheap or low-impact.</p>'
            '<p>So discuss the facts as facts: correct what is wrong and acknowledge what is true. But do not treat the answer as a moral foundation, '
            'because what <em>is</em> does not, on its own, get you to what <em>ought to be</em>: even a real benefit would not show it is just to make someone suffer and die to obtain it. '
            'To really answer, show that the moral debate is a different one: speciesism and what happens to animals as individuals. ')
        + f'<a href="{pre}comece-aqui.html#indiretos">Entenda por quê</a></p></aside>')
IND_TEXTO = ('<p>Os argumentos <strong>indiretos</strong> não discutem se é certo explorar os animais. Discutem saúde, ambiente, economia, praticidade ou a credibilidade de quem defende o veganismo. '
    'Muitos ativistas e filósofos dos direitos animais contestam o uso desse tipo de argumento na defesa dos animais, porque ele escapa do que é importante: o respeito aos próprios animais.</p>'
    '<p>Outros movimentos sociais não se apoiam em argumentos indiretos para defender humanos. Ninguém sustenta o antirracismo dizendo que ele faz bem ao meio ambiente, à saúde dos brancos ou à economia, '
    'e quem luta pelos direitos de minorias e de pessoas prejudicadas não precisa provar nada disso: o fato de serem prejudicadas já basta como razão. Mesmo assim, o veganismo é muitas vezes defendido com argumentos de saúde ou de ambiente, '
    'como se o fim da exploração animal não fosse razão suficiente por si.</p>'
    '<p>O argumento indireto corre em paralelo à questão de fundo, que é a senciência: a capacidade dos animais de serem prejudicados e beneficiados (<a href="alem/fundamentos.html">veja o que sustenta a ética animal</a>). '
    'Por isso ele também não leva, sozinho, ao veganismo. Muitas vezes sustenta, no máximo, o vegetarianismo, a redução do consumo ou o ambientalismo, que aceitam os usos de animais considerados saudáveis, baratos ou de baixo impacto.</p>'
    '<p>Os argumentos indiretos são úteis no plano dos fatos: mostram que uma objeção prática é falsa, que a vida vegana é saudável e possível, que a pecuária causa danos. '
    'Mas não justificam, sozinhos, a moralidade de respeitar os animais. E podem até puxar para o lado oposto: couro "sustentável", caça "sustentável", carne orgânica, criação de insetos e '
    'animais geneticamente modificados são defendidos em nome do ambiente e mantêm ou aumentam a exploração (<a href="argumentos/h13.html">H13</a>). '
    'Por isso, cada capítulo da Parte IND responde no terreno do argumento, corrige os fatos e devolve a conversa à pergunta moral.</p>'
    '<p>Quando saúde, proteína ou ambiente são usados para justificar comer animais, o raciocínio costuma falhar em dois planos. No dos fatos, porque as premissas muitas vezes são falsas: '
    'uma alimentação vegetal bem planejada supre as necessidades e causa menos dano ambiental. No moral, porque dá um salto do que <em>é</em> para o que <em>deve ser</em>, '
    'a passagem que os filósofos chamam de falácia do é-deve: mesmo que comer animais trouxesse algum benefício, isso não mostraria que é justo fazê-los sofrer e morrer para obtê-lo. '
    'Mostrar os fatos é sempre necessário; parar neles, nunca é suficiente.</p>')
DESCRICAO = 'O guia de argumentação para defensores dos animais cataloga de forma sistemática todas as ideias usadas para explorar, causar danos, matar animais ou evitar ajudá-los, fornecendo uma explicação abrangente sobre todos os questionamentos e vieses das pessoas que se opõem ao veganismo e ao antiespecismo.'
e = lambda s: html.escape(str(s), quote=True)
def L(pt, en):
    """Texto com variáveis nos dois idiomas; os textos fixos são traduzidos por tools/en/ui.py."""
    return en if EN else pt
PAGINAS = []
BUSCA = []

# ---------- leitura do catálogo ----------
CORES = {'A': '#b8460f', 'B': '#7b3fa0', 'C': '#2f7d12', 'D': '#1d63b8', 'E': '#b0306e', 'F': '#0b7268', 'G': '#8a6100', 'H': '#4a46c2', 'I': '#c22f2f', 'J': '#5e6c0e', 'K': '#0a6f8f', 'L': '#8a4d2c', 'M': '#46607a', 'N': '#7a4a6e'}  # uma cor forte por família; a versão pastel sai do CSS (color-mix)

def texto(el): return ''.join(el.itertext()).strip()
def linhas(tab): return [[texto(c) for c in r.findall('cell')] for r in tab.findall('row')]
# Argumentos iguais vivem na mesma página: código absorvido -> (código que fica, falha que junta os dois).
UNIDOS = {
    'B3': ('B2', 'Ainda são mortos jovens; rótulos têm pouca relação com a prática, e mudar a escala não muda a natureza do ato'),
    'K3': ('B4', 'A indústria existe para atender o consumo: sistema e consumidor se sustentam mutuamente'),
    'F5': ('D3', 'Usa quem não tem alternativa para justificar quem tem; o veganismo já inclui "na medida do possível e praticável"'),
    'E3': ('E2', 'Autorrefutante e aplicado seletivamente; confunde gosto com afirmação sobre dano a terceiros'),
    'J8': ('J2', 'Barreira real para alguns, que não se aplica a quem faz a objeção; e muitas culturas têm tradições vegetarianas antigas'),
    'K8': ('K1', 'Raciocínio de expectativa: a elasticidade é menor que 1, mas positiva, e menos compra gera menos produção'),
}

def codigos(s):
    """'C1 a C11, G3' vira a lista de códigos, expandindo os intervalos e trocando os unidos pelo código que ficou."""
    out = []
    for m in re.finditer(r'([A-N])(\d{1,2})(?: a \1(\d{1,2}))?', s):
        ini, fim = int(m[2]), int(m[3] or m[2])
        out += [f'{m[1]}{n}' for n in range(ini, fim + 1)]
    return list(dict.fromkeys(UNIDOS[c][0] if c in UNIDOS else c for c in out))

cat = ET.parse(os.path.join(ROOT, 'data', 'catalogo.xml')).getroot()
FAMILIAS, ARGS, FALACIAS, VIESES, CADEIAS = {}, {}, [], [], []
atual = None
for no in cat:
    if no.tag == 'paragraph' and no.get('heading'):
        atual = texto(no)
    elif no.tag == 'table':
        ls = linhas(no)
        cab = ls[0]
        if cab[:3] == ['Parte', 'Código', 'Família']:
            for p, c, nome, perg, n, erro in [l for l in ls[1:] if l[1]]:
                FAMILIAS[c] = dict(c=c, parte=p, nome=nome, perg=perg, n=int(n), erro=erro, args=[], cor=CORES[c])
        elif cab[0] == 'Código':
            for c, arg, formas, falha in ls[1:]:
                fam = c[0]
                d = dict(c=c, frase=arg.strip('"“”'), formas=[f.strip().strip('"“”') for f in formas.split(';')], falha=falha, fam=fam, slug=c.lower())
                ARGS[c] = d; FAMILIAS[fam]['args'].append(d)
        elif cab[0] == 'Falácia':
            FALACIAS = [dict(n=l[0], d=l[1], aparece=l[2], cods=codigos(l[2])) for l in ls[1:]]
        elif cab[0] == 'Viés':
            VIESES = [dict(n=l[0], d=l[1], aparece=l[2], cods=codigos(l[2])) for l in ls[1:]]
        elif cab[0] == 'Cadeia':
            CADEIAS = [dict(n=l[0], cods=codigos(l[1]), fim=l[2]) for l in ls[1:]]
assert len(ARGS) == 150 and all(len(f['args']) == f['n'] for f in FAMILIAS.values())
for velho, (novo, falha) in UNIDOS.items():
    v, n = ARGS.pop(velho), ARGS[novo]
    n['formas'] += [v['frase']] + v['formas']
    n['falha'] = falha
    FAMILIAS[v['fam']]['args'].remove(v)
    FAMILIAS[v['fam']]['n'] -= 1
# Famílias acrescentadas depois do doc original. M: o critério da senciência além da exploração (animais selvagens, novas mentes, futuro).
FAMILIAS_NOVAS = [
    ('N', 'IND', 'Ex-veganos: por que desisti', 'Ter desistido muda o que é certo?', 'Lógico e moral (da experiência pessoal à conclusão moral)'),
    ('M', 'DIR', 'Animais selvagens, novas mentes e o futuro', 'Devemos ajudar, e não só deixar de prejudicar?', 'Moral (viés de omissão e apelo à natureza)'),
]
for c, p, nome, perg, erro in FAMILIAS_NOVAS:
    FAMILIAS[c] = dict(c=c, parte=p, nome=nome, perg=perg, n=0, erro=erro, args=[], cor=CORES[c])
# Frases que o público usa para argumentos que já têm capítulo: entram como formas, sem duplicar a página.
FORMAS_EXTRA = {'A13': ['Somos todos naturalmente enviesados: protegemos nossa família, nossa espécie, nossa nação, e o veganismo é uma ilusão'], 'E2': ['Temos que respeitar as diferentes visões'], 'A19': ['Veganos tratam animais como humanos'], 'D3': ['Veganos querem impor o veganismo aos indígenas'], 'C3': ['Nosso corpo é desenhado para comer carne'], 'J2': ['Veganismo é classista e elitista, não é acessível para a população mais pobre'], 'M12': ['Sencientistas discutem cenários impossíveis ou muito distantes'], 'M10': ['Sencientistas querem brincar de Deus'], 'L6': ['Veganos preferem animais a pessoas'], 'J3': ['Acabar com a pecuária seria ruim para a economia, muita gente perderia emprego'], 'L2': ['Veganismo é lavagem cerebral'], 'J7': ['Não existe vegano de direita'], 'F8': ['Os freegans comem carne do lixo, e isso não financia ninguém'], 'F9': ['E os piolhos, as pulgas e os carrapatos?', 'Onde você traça a linha?'], 'H2': ['Plantações também matam animais'], 'L9': ['Para cada vegano que não comer, eu vou comer o dobro']}
_feitas = set()
for c, fs in FORMAS_EXTRA.items():
    if c in ARGS: ARGS[c]['formas'] += fs; _feitas.add(c)
# Argumentos acrescentados depois do doc original, a partir das objeções da coleção Uma Jornada pela Ética Animal (site Questão de Ética).
NOVOS = [
    ('A21', 'Eu respeito os animais, mas os humanos vêm primeiro', ['Humanos têm dignidade, animais não', 'A vida humana vale mais', 'Animais importam, mas menos'], 'Um status especial que ninguém explica e que não passaria no véu da ignorância: o peso deve depender do tamanho do dano, não da espécie'),
    ('A22', 'Humanos sofrem mais que os animais', ['Humanos sofrem mais porque entendem o que acontece', 'O sofrimento humano é mais profundo'], 'Sofrer mais em alguns casos não autoriza desconsiderar quem sofre menos; e menos cognição muitas vezes significa mais sofrimento e mais vulnerabilidade'),
    ('A23', 'A moral existe para nos proteger uns dos outros', ['A ética foi inventada para autoproteção', 'Animais não podem nos ameaçar, então não entram no acordo'], 'Excluiria também bebês e pessoas vulneráveis; e explicar a origem de uma prática não justifica a prática'),
    ('A24', 'Espécie é biologia, raça é construção social', ['Especismo não é como racismo', 'Raça não existe, espécie existe'], 'Um critério biológico pode ser tão injusto quanto um social: o que torna uma discriminação injusta é tratar de forma tendenciosa os interesses de alguém'),
    ('E13', 'Defender os animais é coisa de utilitarista', ['Isso é Peter Singer, e o utilitarismo está errado', 'Só faz sentido numa ética utilitarista'], 'A igual consideração é um princípio formal aceito por teorias rivais; derrubar o utilitarismo não salva o especismo'),
    ('H14', 'Comer insetos é a proteína sustentável do futuro', ['Farinha de grilo é ecológica', 'Inseto não sente, pode criar à vontade'], 'Troca o impacto ambiental por trilhões de vítimas prováveis; há proteínas vegetais igualmente eficientes e sem ninguém para sofrer'),
    ('A25', 'Os animais não sabem que vão morrer, então não tem problema matá-los', ['Eles não sofrem com a ideia da morte', 'O animal vive o presente, não faz planos', 'Não tem noção de futuro, então não perde nada'], 'O mal da morte é o que ela tira, não o medo dela: o mesmo raciocínio autorizaria matar bebês, pessoas com demência ou quem está dormindo'),
    ('F11', 'E se descobrirem que as plantas sentem?', ['Aí vocês vão comer o quê, pedra?', 'Se tudo sente, por que não comer carne?'], 'Mesmo nesse cenário, comer plantas causaria menos dano, porque os animais comem muito mais plantas; não poder zerar o dano não torna tudo equivalente'),
    ('F10', 'Você comeria um animal que morreu de causas naturais?', ['E se o boi morreu de velhice?', 'Então come o cachorro atropelado na rua também', 'Se não comeria, é frescura'], 'Ninguém foi morto, por isso o problema moral é bem menor; mas essa carne não chega ao mercado, e recusar comer um corpo pode ser respeito, como fazemos com humanos'),
    ('G18', 'Frugivorismo não é saudável, então o veganismo também não é', ['Quem só come fruta fica doente', 'Veganismo é comer fruta e salada'], 'Veganismo não é frugivorismo: a dieta só de frutas é arriscada, mas uma alimentação vegana variada e planejada, com B12, é considerada adequada'),
    ('G19', 'Veganismo é transtorno alimentar disfarçado', ['Veganismo é anorexia com desculpa', 'Viu aquela vegana que morreu?', 'Ortorexia é a doença dos veganos'], 'A associação existe, mas o transtorno costuma vir antes da dieta; veganos da comunidade não têm mais sinais de transtorno, e a causa de uma tragédia é a doença'),
    ('L14', 'Vegano é tudo hippie', ['Bicho-grilo, natureba, paz e amor', 'Vai abraçar uma árvore'], 'Estereótipo e ataque à pessoa: o sofrimento dos animais não depende do estilo de vida de quem o aponta'),
    ('E14', 'Ele come carne, mas é uma pessoa boa', ['Conheço gente ótima que come carne', 'Minha avó come carne e é a pessoa mais bondosa do mundo', 'Você está chamando todo mundo de mau?'], 'Confunde julgar a pessoa com julgar o ato: gente boa também participa de injustiças aceitas pelo costume'),
    ('J16', 'Minha comida caga na sua', ['Meu churrasco humilha sua salada', 'Comida de verdade é a minha'], 'Provocação, não argumento: prazer de paladar não pesa contra a vida de alguém, e muita comida vegana é a mesma comida de sempre'),
    ('J17', 'Olha o que você está perdendo', ['Foto de churrasco nos comentários de um post vegano', 'Hmm, picanha. Tá com inveja?'], 'Mostrar o prato não responde à pergunta sobre quem virou o prato; a tentação não torna o ato justo'),
    ('D11', 'Minha religião aprova o consumo de animais', ['Minha religião permite', 'Se Deus não quisesse, não teria feito os animais de carne', 'Veganismo vai contra a Bíblia'], 'Permitir não é obrigar, e as próprias tradições religiosas proíbem o sofrimento desnecessário, que a produção atual causa em massa'),
    ('D12', 'Vou pagar pelos meus erros na próxima vida', ['Vou pagar na próxima encarnação', 'Isso é entre mim e o meu carma', 'Deus vai me julgar, não você'], 'A frase admite o erro e adia a conta, mas quem paga agora é o animal; as tradições do carma ensinam a não violência'),
    ('J18', 'Eu vivo disso, é o sustento da minha família', ['Você vai pagar as minhas contas?', 'Meu pai e meu avô criaram gado'], 'A dependência econômica explica a dificuldade de mudar, mas não torna a atividade justa; a saída é uma transição planejada e com apoio'),
    ('N1', 'Deixei de ser vegano porque comecei a me sentir mal', ['Meu corpo sente falta de carne, me sinto mal', 'Deixei de ser vegano por causa da energia', 'Voltei a comer carne e melhorei'], 'O mal-estar é real, mas raramente investigado: costuma vir de comer pouco, de falta de B12 ou de planejamento, e tem solução sem produtos animais'),
    ('N2', 'Deixei de ser vegano porque estou em outro momento da vida', ['Era uma fase', 'Hoje tenho outras prioridades'], 'A fase da vida muda o que é fácil, e não o que acontece com os animais; uma fase difícil pede ajustes, e não desistir'),
    ('N3', 'Ser vegano me limitava comer na casa dos meus familiares', ['Na casa da minha avó, não tinha o que comer', 'Minha mãe ficava magoada quando eu recusava a comida'], 'O custo social é real, mas tem saídas: conversar antes, levar um prato para dividir, comer o que já é vegano na mesa'),
    ('N4', 'Ser vegano é difícil para quem viaja muito', ['Na estrada, não tem o que comer', 'Em viagem de trabalho, não dá para escolher'], 'A dificuldade de algumas refeições justifica, no máximo, uma exceção real, e não abandonar o veganismo em casa'),
    ('E15', 'Te admiro, mas não consigo', ['Queria ter a sua força de vontade', 'Admiro os veganos, mas não é pra mim'], 'Admirar já é concordar com o ponto moral; difícil não é impossível, e mudar aos poucos, com apoio, funciona'),
    ('N6', 'Eu já fui vegano, sei do que estou falando', ['Também passei por essa fase', 'Fui vegano por anos e não recomendo'], 'Ter sido vegano dá experiência sobre como foi para a pessoa, e não autoridade sobre a questão moral'),
    ('K10', 'Veganos vão ser sempre minoria', ['O mundo nunca vai virar vegano', 'Para que insistir, se ninguém vai mudar?'], 'Ser minoria não torna algo errado nem inútil: mudanças começam com poucos, cada pessoa reduz a demanda, e leis de proteção animal mudam sem maioria vegana'),
    ('L15', 'Veganos são malucos, têm problemas mentais', ['Vegano é tudo maluco', 'Tem que ser doido para chorar por galinha'], 'Ataque à pessoa: a saúde de quem pergunta não muda a resposta, a associação com depressão não mostra causa, e usar transtorno mental como xingamento reforça o estigma'),
    ('L16', 'Criar filhos veganos é impor uma ideologia', ['Impor o veganismo a uma criança é lavagem cerebral', 'Deixa ele escolher quando crescer'], 'Toda família passa valores aos filhos, e servir carne também é escolha dos pais; o que importa é cuidar da saúde da criança e explicar as razões'),
    ('L13', 'Veganismo é só uma dieta da moda', ['Veganismo é modinha', 'É só mais uma dieta, logo passa'], 'Confunde uma posição ética sobre não prejudicar animais com um cardápio escolhido por saúde ou estética'),
    # Família M: o critério da senciência aplicado a quem ninguém explora (animais selvagens), a novas mentes e ao futuro.
    ('M1', 'Os animais selvagens vivem livres e felizes', ['A natureza é um paraíso para os bichos', 'Bicho solto é bicho feliz'], 'Os adultos que vemos são exceção: na maioria das espécies, quase todos os filhotes morrem pouco depois de nascer, de fome, frio, doença ou predação'),
    ('M2', 'Sofrimento e morte fazem parte da natureza', ['A natureza é cruel mesmo, faz parte', 'A natureza não é boa nem má'], 'Doenças também fazem parte da vida humana, e nunca foi motivo para não tratá-las; o dano não fica menor para a vítima porque ninguém teve culpa'),
    ('M3', 'Não fomos nós que causamos, então não temos obrigação de ajudar', ['Temos dever de não prejudicar, não de ajudar', 'Problema da natureza não é problema meu'], 'Viés de omissão: ninguém aceitaria esse raciocínio diante de uma criança se afogando ou de vítimas de uma enchente'),
    ('M4', 'É impossível resolver o sofrimento na natureza, é grande e complexo demais', ['São trilhões de animais, não adianta', 'Nunca vamos acabar com a predação'], 'Não poder resolver tudo não é razão para não fazer nada: já vacinamos raposas, resgatamos animais em desastres e podemos pesquisar para fazer mais'),
    ('M5', 'Mexer na natureza é errado, podemos piorar tudo', ['Toda intervenção humana dá errado', 'Deixe a natureza se cuidar'], 'O risco pede estudo e cautela, como na medicina, e não omissão: é a proposta da biologia do bem-estar'),
    ('M6', 'Quem somos nós para interferir na natureza?', ['Bicho selvagem tem que ser livre', 'Ajudar é humanizar os animais', 'Eles vão ficar dependentes'], 'Interferimos o tempo todo, com cidades, agricultura e medicina; e ninguém chama de arrogância socorrer uma pessoa ferida'),
    ('M7', 'Natureza equilibrada é natureza boa para os bichos', ['Espécie invasora tem que ser eliminada', 'Proteger a floresta é proteger os animais'], 'Equilíbrio mede números, não bem-estar; e programas ambientais matam milhares de animais por metas que nunca aceitaríamos para humanos'),
    ('M8', 'Ajudar animais selvagens não é veganismo, é outra pauta', ['Veganismo é só não explorar', 'Primeiro acabe com a pecuária, depois falamos de bicho do mato'], 'Se o que importa é a senciência, o sofrimento não deixa de contar porque não foi causado por nós; e uma causa não impede pesquisar a outra'),
    ('M9', 'Máquinas nunca vão sentir, robôs e IAs não precisam de direitos', ['É só um programa', 'Computador não sofre'], 'Se uma mente artificial um dia sentir, o substrato não importa mais que a espécie; e a incerteza pede precaução antes de criar mentes em massa'),
    ('M10', 'Usar remédios e genética para acabar com o sofrimento é brincar de Deus', ['Isso é eugenia', 'O sofrimento faz parte da condição humana e animal'], 'Já usamos anestesia, vacinas e analgésicos sem chamar isso de brincar de Deus; a questão é segurança e consentimento, não a origem natural da dor'),
    ('M11', 'Quem ainda não nasceu não importa', ['Seres futuros são só possibilidades', 'O futuro que se resolva'], 'Quem nascer vai sentir o que deixarmos: é por isso que enterrar lixo tóxico é errado, mesmo que as vítimas ainda não existam'),
    ('M12', 'Isso é ficção científica, temos problemas reais agora', ['Riscos de sofrimento futuro são paranoia', 'Primeiro os problemas de hoje'], 'Um risco incerto mas imenso pode merecer atenção, e muito do que reduz sofrimento futuro, como ampliar o círculo moral, também ajuda agora'),
]
import novos as _novos_lotes  # lotes de 2026-11-13: dados em data/novos/*.json
NOVOS += _novos_lotes.PT
for c, frase, formas, falha in NOVOS:
    d = dict(c=c, frase=frase, formas=formas, falha=falha, fam=c[0], slug=c.lower())
    ARGS[c] = d; FAMILIAS[c[0]]['args'].append(d); FAMILIAS[c[0]]['n'] += 1
_FAM_ORD = list(FAMILIAS)  # a ordem das famílias no site: N (ex-veganos) vem antes de M (animais selvagens e futuro)
for c, fs in FORMAS_EXTRA.items():  # formas de argumentos acrescentados depois (família M, N, lotes novos)
    if c not in _feitas: ARGS[c]['formas'] += fs
ORDEM = sorted(ARGS, key=lambda c: (_FAM_ORD.index(c[0]), int(c[1:])))
ARGS = {c: ARGS[c] for c in ORDEM}
for f in FAMILIAS.values(): f['args'].sort(key=lambda d: int(d['c'][1:]))

# Endereços legíveis: cada argumento e cada argumento ruim tem a URL da própria frase (melhor no Google).
# Os endereços antigos por código (argumentos/a10.html, ruins/v29.html) viram redirecionamentos no fim do build.
def _slug_frase(s, usados):
    import unicodedata
    base = re.sub(r'[^a-z0-9]+', '-', unicodedata.normalize('NFD', s.lower()).encode('ascii', 'ignore').decode()).strip('-')
    if len(base) > 70: base = base[:70].rsplit('-', 1)[0]
    x, k = base, 2
    while x in usados: x, k = f'{base}-{k}', k + 1
    usados.add(x)
    return x
_usados = set()
SLUG_ARG_PT = {c.lower(): _slug_frase(a['frase'], _usados) for c, a in ARGS.items()}
_usados = set()
SLUG_RUIM_PT = {r['c'].lower(): _slug_frase(r['frase'], _usados) for r in RUINS}
_usados = set()
_sem_ap = lambda s: s.replace("'", '').replace('’', '')  # they're -> theyre, can't -> cant
SLUG_ARG_EN = {c.lower(): _slug_frase(_sem_ap(en.ARGS[c][0]) if c in en.ARGS else c, _usados) for c in ARGS}
_usados = set()
SLUG_RUIM_EN = {r['c'].lower(): _slug_frase(_sem_ap(en.RUINS[r['frase']]['frase']) if r['frase'] in en.RUINS else r['c'], _usados) for r in RUINS}
SLUG_ARG, SLUG_RUIM = (SLUG_ARG_EN, SLUG_RUIM_EN) if EN else (SLUG_ARG_PT, SLUG_RUIM_PT)
for _a in ARGS.values(): _a['slug'] = SLUG_ARG[_a['c'].lower()]
REV_ARG = {v: k for k, v in SLUG_ARG.items()}
REV_RUIM = {v: k for k, v in SLUG_RUIM.items()}
def nova_url(s):
    s = re.sub(r'\bargumentos/([a-n]\d{1,2})\.html', lambda m: f'argumentos/{SLUG_ARG.get(m[1], m[1])}.html', s)
    return re.sub(r'\bruins/(v\d{1,2})\.html', lambda m: f'ruins/{SLUG_RUIM.get(m[1], m[1])}.html', s)

# Capítulos do site Questão de Ética (coleção de Luciano Carlos Cunha) que aprofundam cada argumento.
QE_URL = 'https://questaodeetica.biblioverse.org/'
from qe_caps import QE_CAPS
QE = {
    'M1': [(7, 3), (7, 1)],
    'M2': [(7, 15), (7, 16), (7, 13)],
    'M3': [(7, 5), (7, 21), (7, 4)],
    'M4': [(7, 25), (7, 26), (7, 28)],
    'M5': [(7, 24), (7, 19), (7, 27)],
    'M6': [(7, 6), (7, 7), (7, 10), (7, 11), (7, 12)],
    'M7': [(5, 5), (5, 8), (5, 9)],
    'M8': [(7, 9), (7, 22), (7, 35)],
    'M9': [(9, 12), (6, 3)],
    'M10': [(7, 28), (7, 31)],
    'M11': [(9, 2), (9, 3)],
    'M12': [(9, 1), (9, 5), (9, 7)],
    'A1': [(1, 4)], 'A2': [(1, 14)], 'A3': [(1, 4)], 'A4': [(1, 3)], 'A5': [(2, 3), (2, 4)], 'A6': [(2, 4), (2, 13), (6, 8)],
    'A7': [(1, 10)], 'A8': [(1, 4)], 'A9': [(1, 10), (1, 11)], 'A10': [(1, 2), (2, 2)], 'A11': [(1, 6), (2, 2)], 'A12': [(1, 5)],
    'A13': [(1, 8)], 'A14': [(4, 4), (6, 21)], 'A15': [(6, 6), (2, 13)], 'A16': [(3, 1), (3, 2), (3, 4), (3, 10), (3, 13)],
    'A17': [(4, 17)], 'A18': [(6, 13), (5, 10)], 'A19': [(6, 2)], 'A20': [(1, 14), (6, 16)],
    'A25': [(3, 10), (3, 1), (3, 4)],
    'A21': [(1, 14), (1, 1)], 'A22': [(2, 9)], 'A23': [(1, 12)], 'A24': [(1, 7)],
    'B1': [(4, 1), (4, 2)], 'B2': [(4, 1)], 'B5': [(4, 6)], 'B6': [(3, 8), (4, 7)], 'B8': [(4, 17), (8, 11)],
    'C1': [(4, 5), (1, 8)], 'C2': [(4, 5)], 'C6': [(1, 8)], 'C7': [(1, 8)],
    'D1': [(1, 9)], 'D2': [(1, 9)], 'D4': [(1, 13), (1, 3)], 'D7': [(4, 17)], 'D10': [(1, 13)],
    'E1': [(4, 18)], 'E2': [(1, 15), (1, 11)], 'E10': [(1, 15)], 'E11': [(2, 7), (11, 6)], 'E13': [(2, 7), (11, 6)],
    'F9': [(7, 30)],
    'F11': [(6, 21), (4, 4)],
    'F1': [(4, 8)], 'F2': [(4, 8), (2, 8)], 'F3': [(7, 1)], 'F7': [(2, 13)],
    'G1': [(4, 9)], 'G8': [(4, 9)], 'H2': [(4, 14)], 'H11': [(5, 8)], 'H13': [(5, 1)], 'H14': [(4, 19)],
    'I1': [(4, 20)], 'I2': [(4, 20)], 'I5': [(4, 19)],
    'J1': [(4, 10)], 'J2': [(4, 10)], 'J3': [(4, 12)], 'J4': [(4, 12)], 'J5': [(4, 11)], 'J6': [(4, 16)],
    'K1': [(4, 13)], 'K5': [(8, 12)], 'K9': [(8, 11)], 'L6': [(4, 16)], 'L13': [(4, 3)],
}
ROMANOS = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII']
def qe_bloco(c):
    if c not in QE: return ''
    def item(k):
        t, u = (en.qe(*k) if EN else None) or (QE_CAPS[k][0] + L('', ' (in Portuguese)'), QE_URL + QE_CAPS[k][1])
        return f'<li><a href="{u}" {EXT}>{e(t)}</a> <small>Vol. {ROMANOS[k[0] - 1]}, cap. {k[1]}</small></li>'
    itens = ''.join(item(k) for k in QE[c])
    return f'<div class="qe"><h2 id="aprofunde">Aprofunde no Questão de Ética</h2><p>Capítulos da coleção <em>Uma Jornada pela Ética Animal</em>, em acesso aberto, que discutem este argumento com mais detalhe:</p><ul>{itens}</ul></div>'
CADEIAS_LONGAS = [('Conversa informal', 'Começa na Parte DIR, foge para a IND e volta à DIR.', ['C1', 'C2', 'G1', 'G3', 'H1', 'H2', 'L5', 'K1', 'E1']),
                  ('Debate filosófico', 'Fica toda na Parte DIR.', ['B1', 'A16', 'A1', 'A11'])]
RAIZES = ['A10', 'J11', 'E12']

# ---------- leitura dos capítulos ----------
def limpa(s):
    """Tira do texto público as notas de rascunho do doc original."""
    s = re.sub(r'Formato autor-data provisório[^.]*\.\s*', '', s)
    s = re.sub(r'Provisional author-date format[^.]*\.\s*', '', s)
    s = s.replace('Os links indicam as fontes conferidas na redação deste capítulo.', 'Os links levam às fontes conferidas na redação deste capítulo.')
    s = re.sub(r'\b[Cc]itad[oa]s? de memória(, sem consulta à fonte)?', 'fonte ainda não conferida', s)
    s = s.replace(' (Documento do projeto.)', '').replace('. (Documento do projeto.)', '.')
    s = s.replace('Documento do projeto', 'Livro de referência deste guia')
    s = re.sub(r'\b([Uu]m|[Ee]ste|o|do) livro (que acusa|honesto|não|faz)', lambda m: f'{m[1]} guia {m[2]}', s)
    s = s.replace('enfraqueceria o livro', 'enfraqueceria o guia').replace(' do livro: escolhe-se', ' do guia: escolhe-se')
    if s[:1] == 'f' and s.startswith('fonte ainda'): s = 'F' + s[1:]
    return s

COD_RE = re.compile(r'(?<![\w.-])([A-N]\d{1,2})(?![\w-])')
def liga(s, ctx):
    def f(m):
        c = UNIDOS[m[1]][0] if m[1] in UNIDOS else m[1]
        if c not in ARGS or c == ctx.get('c') or c in ctx.get('fora', ()): return m[0]
        return f'<a class="ref" href="{ctx["pre"]}argumentos/{c.lower()}.html">{c}</a>'
    return COD_RE.sub(f, s)

def runs(el, ctx, em_link=False):
    out = e(limpa(el.text)) if el.text else ''
    if el.text and not em_link and el.tag != 'codeBlock': out = liga(out, ctx)
    for f in el:
        if f.tag == 'link':
            href = f.get('href', '')
            miolo = runs(f, ctx, True)
            out += miolo if href.startswith('#') else f'<a href="{e(href)}" {EXT}>{miolo}</a>'
        else:
            miolo = runs(f, ctx, em_link)
            tag = {'bold': 'strong', 'italic': 'em'}.get(f.tag)
            out += f'<{tag}>{miolo}</{tag}>' if tag else miolo
        if f.tail:
            t = e(limpa(f.tail))
            out += t if em_link else liga(t, ctx)
    return out

def junta_links(h):
    """Âncoras vizinhas para o mesmo destino viram uma só."""
    while True:
        n = re.sub(r'(<a href="([^"]+)"[^>]*>)((?:(?!</a>).)*)</a><a href="\2"[^>]*>', r'\1\3', h)
        if n == h: return h
        h = n

SEM_AUTOR = re.compile(r"^(<a [^>]+>)?(?!Corte|Brasil|Alemanha|ONU|Reino|Nonhuman|Te Awa|<em>)((?:[^<(]|<em>[^<]*</em>)*?\((?:c\. )?\d{4}[a-z]?\)\.\s*)")
PESSOA = re.compile(r"^(<a [^>]+>)?(?:[A-ZÀ-Ú][\w'À-ú-]+, [A-Z]\.(?: ?[A-Z]\.)* |(?:Aristóteles|Platão|Descartes|Tomás de Aquino|Agostinho|Kant|Bentham|Plutarco|Porfírio)\. )")
def sem_autor(h):
    """Listas de fontes mostram só o título da obra."""
    h = SEM_AUTOR.sub(lambda m: m[1] or '', h, 1)
    h = PESSOA.sub(lambda m: m[1] or '', h, 1)
    h = h.replace('&amp;', '\0')
    h = re.sub(r';\s*(?:[^;<]*?)\(\d{4}\)\.\s*', '; ', h)
    return h.replace('\0', '&amp;')

def tabela(t, ctx):
    ls = t.findall('row'); o = ['<div class="tabela"><table>']
    for i, r in enumerate(ls):
        tag = 'th' if r.find('cell').get('header') == 'true' else 'td'
        cels = ''.join(f'<{tag}{" scope=col" if tag == "th" else ""}>{junta_links("".join(runs(x, ctx) for x in c.findall("paragraph")))}</{tag}>' for c in r.findall('cell'))
        o.append(f'<tr>{cels}</tr>')
    return ''.join(o) + '</table></div>'

def lista(l, ctx, refs=False):
    tag = 'ol' if l.get('kind') == 'ordered' else 'ul'
    itens = []
    for li in l.findall('listItem'):
        h = junta_links(''.join(runs(p, ctx) for p in li.findall('paragraph')))
        itens.append(f'<li>{sem_autor(h) if refs else h}</li>')
    return f'<{tag}>' + ''.join(itens) + f'</{tag}>'

ARVORE = {
    'A1': '''<div class="arvore"><p class="q">Racional em qual sentido?</p><ul><li><span class="r">Forte: raciocínio abstrato</span>P2 fica verdadeira, <span class="f">mas P1 exclui bebês e pessoas com deficiência intelectual profunda</span></li><li><span class="r">Fraco: aprender, inferir, resolver problemas</span>P1 passa a incluir esses humanos, <span class="f">mas P2 fica falsa para muitos animais</span></li></ul></div>''',
    'A10': '''<div class="arvore"><p class="q">Existe uma característica C?</p><ul><li><span class="r">Não, é só a espécie</span><span class="f">Especismo nu: preconceito sem critério</span></li><li><span class="r">Sim, C é um traço específico</span>Todo humano tem C?<ul><li><span class="r">Não</span><span class="f">Sobreposição de espécies: exclui humanos protegidos</span></li><li><span class="r">Sim</span>C é relevante para dor e morte?<ul><li><span class="r">Não</span><span class="f">Critério irrelevante, como saber álgebra</span></li><li><span class="r">Sim</span><span class="f">Então o critério é a senciência, que os animais têm</span></li></ul></li></ul></li></ul></div>''',
}

CAPS = {}
md2xml.todos()
for arq in glob.glob(os.path.join(ROOT, 'data', 'capitulos', '*.xml')):
    c = os.path.basename(arq)[:-4]
    CAPS[c] = ET.parse(arq).getroot()
assert set(CAPS) <= set(ARGS) | set(UNIDOS) and {f'A{i}' for i in range(1, 13)} <= set(CAPS)
CAPS_PT = CAPS
if EN:  # capítulos traduzidos (data/en/capitulos_md); os demais aparecem como verbete
    CAPS = {}
    md2xml.todos(os.path.join(ROOT, 'data', 'en'))
    for arq in glob.glob(os.path.join(ROOT, 'data', 'en', 'capitulos', '*.xml')):
        CAPS[os.path.basename(arq)[:-4]] = ET.parse(arq).getroot()

def celulas(t, ctx):
    """Linhas de uma tabela como listas de HTML, sem o cabeçalho."""
    rs = []
    for r in t.findall('row'):
        if r.find('cell').get('header') == 'true': continue
        rs.append([junta_links(''.join(runs(p, ctx) for p in c.findall('paragraph'))) for c in r.findall('cell')])
    return rs

def itens_lista(l, ctx):
    return [junta_links(''.join(runs(p, ctx) for p in li.findall('paragraph'))) for li in l.findall('listItem')]

def separa(h):
    """Divide '<strong>Título.</strong> resto' em (título, resto)."""
    m = re.match(r'\s*<strong>(.*?)</strong>\s*(.*)$', h, re.S)
    return (m[1], m[2]) if m else ('', h)

def acordeao(titulo, miolo, aberto=False):
    return f'<details class="dobra"{" open" if aberto else ""}><summary>{titulo}</summary><div>{miolo}</div></details>'

def baloes(rs):
    return '<div class="baloes">' + ''.join(f'<figure class="balao"><blockquote>{r[1]}</blockquote><figcaption>{r[0]}</figcaption></figure>' for r in rs) + '</div>'

def silogismo(itens):
    o = ''
    for h in itens:
        t, resto = separa(h)
        conc = t.startswith('C')
        o += f'<li class="{"conc" if conc else "prem"}"><b>{t.rstrip(".")}</b><span>{resto}</span></li>'
    return f'<ol class="silogismo">{o}</ol>'

_ESPELHO = {}
def espelho():
    """As conexões dos capítulos acrescentados (NOVOS) aparecem também, invertidas, nos capítulos a que apontam."""
    if not _ESPELHO:
        for n, *_ in NOVOS:
            for t in secao_cap(n, 6, CAPS_PT):
                if t.tag != 'table': continue
                for r in t.findall('row')[1:]:
                    cels = [texto(x) for x in r.findall('cell')]
                    if len(cels) < 3: continue
                    volta = {'Vem antes': 'Vem depois', 'Vem depois': 'Vem antes'}.get(cels[0])
                    for x in codigos(cels[1]):
                        if volta and x in ARGS: _ESPELHO.setdefault(x, []).append([volta, n, e(en.motivo(cels[2]) if EN else cels[2])])
        _ESPELHO.setdefault('', [])
    return _ESPELHO

def rede(rs, c, ctx):
    """Conexões: o que vem antes, este argumento, o que vem depois."""
    rs = [[{'Comes before': 'Vem antes', 'Comes after': 'Vem depois'}.get(re.sub('<[^>]+>', '', r[0]), r[0])] + r[1:] for r in rs]
    ja = {x for r in rs for x in codigos(re.sub('<[^>]+>', '', r[1]))}
    rs = rs + [r for r in espelho().get(c, []) if r[1] not in ja]
    def nos(dir_):
        o = ''
        for r in rs:
            if r[0] != dir_: continue
            cods = [x for x in codigos(re.sub('<[^>]+>', '', r[1])) if x in ARGS]
            alvo = ''.join(f'<a class="no" style="--c:{FAMILIAS[x[0]]["cor"]}" href="{ARGS[x]["slug"]}.html"><b>{x}</b> {e(ARGS[x]["frase"])}</a>' for x in cods)
            o += f'<div class="elo">{alvo}<small>{r[2]}</small></div>'
        return o
    return f'<div class="rede"><div><p class="ti">Costuma vir antes</p>{nos("Vem antes")}</div><div class="centro"><span>{c}</span><small>este argumento</small></div><div><p class="ti">Costuma vir depois</p>{nos("Vem depois")}</div></div>'

def por_plano(rs):
    cols = {}
    for r in rs: cols.setdefault(re.sub('<[^>]+>', '', r[0]), []).append(r)
    expl = {'Lógico': 'A forma é válida?', 'Epistemológico': 'A evidência sustenta?', 'Moral': 'O critério é coerente?',
            'Logical': 'Is the form valid?', 'Epistemological': 'Does the evidence support it?'}
    if EN: expl['Moral'] = 'Is the criterion coherent?'
    return '<div class="planos">' + ''.join(f'<div class="plano p-{slug(p)}"><h4>{e(p)}</h4><p class="ti2">{expl.get(p, {"pre": "../"})}</p>' + ''.join(acordeao(r[1], r[2]) for r in ls) + '</div>' for p, ls in cols.items()) + '</div>'

def cartoes_vies(rs):
    return '<div class="grade-v">' + ''.join(f'<div class="cartao vies"><h4>{r[0]}</h4><p>{r[1]}</p><p class="ev">{r[2]}</p></div>' for r in rs) + '</div>'

def revelar(rs):
    return '<div class="revelar">' + ''.join(f'<details class="carta"><summary><small>Se valesse para…</small><b>{r[0]}</b><i>Toque para ver</i></summary><div><p>{r[1]}</p><p class="ev">{r[2]}</p></div></details>' for r in rs) + '</div>'

def capitulo(c):
    """Devolve (tese, notas, abas) de um capítulo, com cada bloco na sua forma visual."""
    raiz = CAPS[c]
    fora = set(re.findall(r'^(C\d)\.$', '\n'.join(texto(b) for b in raiz.iter('bold')), re.M))
    ctx = dict(c=c, pre='../', fora=fora)
    tese, notas, secoes, sec = '', [], {}, None
    for no in raiz:
        h = no.get('heading') if no.tag == 'paragraph' else None
        if h == '1': continue
        if h == '2':
            m = re.match(r'(\d+)\.', texto(no))
            sec = secoes.setdefault(int(m[1]) if m else 0, [])
            continue
        if sec is None:
            if no.tag == 'paragraph':
                t = texto(no)
                if t in ('Índice', 'Contents'): continue
                if t.startswith(('Tese:', 'Thesis:')):
                    tese = re.sub(r'<strong>(Tese|Thesis):</strong>', '', junta_links(runs(no, ctx))).strip()
                elif t.startswith(('Família:', 'Family:')):
                    m = re.sub(r'^<strong>(Família|Family):</strong>.*?<strong>(Parte|Part):</strong>\s*(DIR|IND)\s*(·\s*)?', '', junta_links(runs(no, ctx))).strip()
                    if m: notas.append(m)
                else:
                    notas.append(junta_links(runs(no, ctx)))
            continue
        sec.append(no)
    P = lambda no, cx=ctx: junta_links(runs(no, cx))
    # 1. formulação
    b1 = ''
    for no in secoes[1]:
        if no.tag == 'list': b1 += silogismo(itens_lista(no, ctx))
        elif no.tag == 'paragraph':
            t = texto(no)
            b1 += f'<div class="dita"><span>Como se diz</span><p>{separa(P(no))[1]}</p></div>' if t.startswith(('Versão cotidiana', 'Everyday version')) else f'<p>{P(no)}</p>'
    b2 = next((baloes(celulas(no, ctx)) for no in secoes[2] if no.tag == 'table'), '')
    b3 = ''.join(f'<p>{P(no)}</p>' for no in secoes[3] if no.tag == 'paragraph')
    curta, retorno = '', ''
    for no in secoes[4]:
        if texto(no).startswith(('Pergunta de retorno', 'Question to ask back')): retorno = separa(P(no))[1]
        else: curta += f'<p>{P(no)}</p>'
    # 5. resposta completa
    b5, atual = {}, None
    for no in secoes[5]:
        if no.tag == 'paragraph' and no.get('heading') == '3':
            atual = texto(no)[1]; b5[atual] = dict(t=texto(no), n=[])
        else: b5[atual]['n'].append(no)
    def bloco5(k):
        o = ''
        for no in b5[k]['n']:
            if no.tag == 'paragraph':
                h = P(no); ti, resto = separa(h)
                if k == 'b' and ti: o += acordeao(ti, f'<p>{resto}</p>', not o)
                else: o += f'<p>{h}</p>'
            elif no.tag == 'list':
                its = itens_lista(no, ctx)
                if k == 'e' and all(separa(i)[0] for i in its): o += ''.join(acordeao(separa(i)[0], f'<p>{separa(i)[1]}</p>') for i in its)
                else: o += lista(no, ctx)
            elif no.tag == 'table': o += tabela(no, ctx)
            elif no.tag == 'codeBlock': o += (en.ARVORE if EN else ARVORE)[c]
        return o
    rot = {'a': 'Diagnóstico', 'b': 'Onde quebra', 'c': 'Dados e fontes', 'd': 'A melhor réplica', 'e': 'Por que ela falha'}
    passos5 = ''.join(f'<li id="b5{k}"><span class="num">{k}</span><div><h3>{liga(e(re.sub(r"^\(.\)\s*", "", b5[k]["t"])), ctx)}</h3>{bloco5(k)}</div></li>' for k in b5)
    # 6 a 11
    t6 = next((no for no in secoes[6] if no.tag == 'table'), None)
    cx6 = dict(ctx, fora=set())
    b6 = ''.join(f'<p>{P(no, cx6)}</p>' for no in secoes[6] if no.tag == 'paragraph') + rede(celulas(t6, cx6), c, cx6)
    b7 = por_plano(celulas(next(no for no in secoes[7] if no.tag == 'table'), ctx))
    its8 = itens_lista(next(no for no in secoes[8] if no.tag == 'list'), ctx)
    b8 = '<div class="choques">' + ''.join(f'<div class="choque"><b>{separa(h)[0]}</b><p>{separa(h)[1]}</p></div>' for h in its8) + '</div>'
    b9 = cartoes_vies(celulas(next(no for no in secoes[9] if no.tag == 'table'), ctx))
    princ = next((texto(no) for no in secoes[10] if no.tag == 'paragraph'), '')
    b10 = f'<p class="principio">{e(limpa(princ))}</p>' + revelar(celulas(next(no for no in secoes[10] if no.tag == 'table'), ctx))
    ps11 = [P(no) for no in secoes[11] if no.tag == 'paragraph']
    b11 = f'<div class="balanca"><div class="acerta"><p class="ti">O que é verdade</p>{"".join(f"<p>{x}</p>" for x in ps11[:-1] or ps11)}</div>' + (f'<div class="mas"><p class="ti">Mas</p><p>{ps11[-1]}</p></div>' if len(ps11) > 1 else '') + '</div>'
    # referências
    refs = ''
    for no in secoes[0]:
        if no.tag == 'list': refs += lista(no, ctx, True)
        elif no.tag == 'paragraph':
            t = texto(no); h = P(no)
            if re.fullmatch(r'<strong>[^<]+</strong>', h): refs += f'<h4>{e(t)}</h4>'
            elif t: refs += f'<p>{h}</p>'
    abas = [
        ('responder', 'Responder', 'Para usar agora', f'<div class="duas"><section><h2 id="b4">Resposta curta</h2><div class="bloco curta" id="curta-txt">{curta}</div><p><button class="copiar" type="button" data-alvo="curta-txt">Copiar resposta</button></p></section><section><h2 id="b3">Para crianças</h2><div class="bloco crianca">{b3}</div></section></div>' + (f'<div class="retorno"><span>Devolva com uma pergunta</span><p>{retorno}</p></div>' if retorno else '')),
        ('argumento', 'O argumento', 'Formas e premissas', f'<h2 id="b2">Como pode aparecer</h2>{b2}<h2 id="b1">A versão mais forte</h2>{b1}'),
        ('desmontar', 'Desmontar', 'Passo a passo', f'<h2 id="b5">Resposta completa</h2><ol class="trilha5">{passos5}</ol>'),
        ('erros', 'Erros e vieses', 'O que faz parecer certo', f'<h2 id="b7">Erros de raciocínio</h2>{b7}<h2 id="b9">Vieses</h2>{b9}'),
        ('testar', 'Testar', 'Coerência e concessões', f'<h2 id="b10">Extrapolações</h2>{b10}<h2 id="b8">Contradições</h2>{b8}<h2 id="b11">O que o argumento acerta</h2>{b11}'),
        ('conexoes', 'Conexões', 'O que vem antes e depois', f'<h2 id="b6">Conexões</h2>{b6}{qe_bloco(c)}<h2 id="referencias">Referências</h2><div class="fontes">{refs}</div>'),
    ]
    return tese, notas, abas

# ---------- página ----------
def desc_seo(d):
    d = re.sub(r'\s+', ' ', html.unescape(re.sub('<[^>]+>', '', d))).strip()  # o texto pode chegar já escapado; page() escapa de novo
    if d and d[-1] not in '.!?…': d += '.'
    if d[:1].islower(): d = d[0].upper() + d[1:]  # as teses começam em minúscula depois de "Tese:"
    if len(d) < 70: d += ' Resposta com fontes, no guia para defensores dos animais.'
    if len(d) > 160: d = d[:157].rsplit(' ', 1)[0].rstrip(' ,;:') + '…'
    return d

LOGO = '<svg width="36" height="36" viewBox="0 0 40 40" aria-hidden="true"><path d="M6 2h28a4 4 0 0 1 4 4v22a4 4 0 0 1-4 4H19l-8 6v-6H6a4 4 0 0 1-4-4V6a4 4 0 0 1 4-4z" fill="#0a3703"/><g fill="#ffeb5b"><ellipse cx="15.500" cy="11.500" rx="2.700" ry="6.800" transform="rotate(-10 15.500 11.500)"/><ellipse cx="24.500" cy="11.500" rx="2.700" ry="6.800" transform="rotate(10 24.500 11.500)"/><ellipse cx="20" cy="22" rx="8" ry="6.800"/></g><g fill="#0a3703"><circle cx="17" cy="21" r="1.100"/><circle cx="23" cy="21" r="1.100"/><circle cx="20" cy="24.200" r="1"/></g></svg>'
TODOS = 'index.html#argumentos'
# Menu principal: links diretos e dois grupos (Praticar e Aprofundar), que abrem como lista no computador e no celular.
MENU = [(TODOS, 'Argumentos'), ('objecoes-politicas.html', 'Objeções políticas'), ('argumentos-ruins.html', 'Pare de dizer isso'),
        ('Praticar', [('debate.html', 'Debate simulado'), ('treino.html', 'Treinar respostas')]),
        ('Aprofundar', [('glossario.html', 'Glossário'), ('raciocinio.html', 'O raciocínio antivegano'), ('mapa.html', 'Mapa de conexões'), ('familias.html', 'As 14 famílias'),
                        ('falacias.html', 'Falácias'), ('vieses.html', 'Vieses'), ('alem-do-veganismo.html', 'Além do veganismo')]),
        ('biblioteca.html', 'Biblioteca'), ('sobre.html', L('Sobre', 'About'))]
def monta_menu(pre, atual):
    h = ''
    for u, t in MENU:
        if isinstance(t, list):
            t = [x for x in t if not (EN and x[0] in PT_ONLY)]
            dentro = any(x == atual for x, _ in t)
            itens = ''.join(f'<a href="{pre}{x}"{" aria-current=page" if x == atual else ""}>{e(n)}</a>' for x, n in t)
            h += f'<details class="sub"><summary{" class=aqui" if dentro else ""}>{e(u)}</summary><div class="sub-l">{itens}</div></details>'
        else:
            h += f'<a href="{pre}{u}"{" aria-current=page" if u == atual else ""}>{e(t)}</a>'
    return h

def dados(path, title, desc, url, tipo, trilha):
    org = {'@type': 'Organization', 'name': 'BiblioVerse', 'url': 'https://biblioverse.org'}
    site = {'@type': 'WebSite', '@id': SITE + '/#site', 'name': NOME, 'url': SITE + '/', 'inLanguage': 'pt-BR', 'publisher': org}
    if path == 'index.html': grafo = [site]
    else:
        pg = {'@type': tipo, 'name': title, 'description': desc, 'url': url, 'inLanguage': 'pt-BR', 'isPartOf': {'@id': SITE + '/#site'}, 'dateModified': ATUALIZADO}
        if tipo == 'Article': pg.update(headline=title[:110], datePublished=ATUALIZADO, author={'@type': 'Organization', 'name': NOME, 'url': SITE + '/sobre.html'}, publisher=org, mainEntityOfPage=url)
        mig = [('Início', SITE + '/')] + [(n, f'{SITE}/{u.replace("index.html", "")}') for n, u in trilha] + [(title, url)]
        grafo = [site, pg, {'@type': 'BreadcrumbList', 'itemListElement': [{'@type': 'ListItem', 'position': i + 1, 'name': n, 'item': u} for i, (n, u) in enumerate(mig)]}]
    return '<script type="application/ld+json">' + json.dumps({'@context': 'https://schema.org', '@graph': grafo}, ensure_ascii=False).replace('</', '<\\/') + '</script>'

def chave(path):
    """Identificador neutro de uma página, igual nos dois idiomas: pasta + código (argumentos e argumentos ruins) ou o caminho em português."""
    m = re.match(r'(argumentos|ruins)/([^/]+)\.html$', path)
    if m: return m[1], (REV_ARG if m[1] == 'argumentos' else REV_RUIM).get(m[2], m[2])
    return '', path
def url_lingua(k, lg):
    pasta, x = k
    if pasta: x = f'{pasta}/{(SLUG_ARG_EN if pasta == "argumentos" else SLUG_RUIM_EN)[x] if lg == "en" else (SLUG_ARG_PT if pasta == "argumentos" else SLUG_RUIM_PT)[x]}.html'
    if lg == 'en': x = en.caminho(x)
    return (SITE_EN if lg == 'en' else SITE_PT) + '/' + ('' if x == 'index.html' else x)

def page(path, title, desc, corpo, atual='', tipo='WebPage', trilha=()):
    path = nova_url(path)
    k = chave(path)
    if EN: path = en.caminho(path)
    PAGINAS.append(path)
    erro = path == '404.html'
    home = path == 'index.html'
    desc = desc_seo(desc)
    pre = '../' * path.count('/')
    url = SITE + '/' + ('' if home else path)
    u_pt, u_en = url_lingua(k, 'pt'), url_lingua(k, 'en')
    outra = u_pt if EN else u_en
    LASTMOD[path], ALTERNA[path] = _data_fonte(k), (u_pt, u_en)
    alterna = '' if not BILINGUE or path in PT_ONLY else f'<link rel="alternate" hreflang="pt-BR" href="{u_pt}"/>\n<link rel="alternate" hreflang="en" href="{u_en}"/>\n<link rel="alternate" hreflang="x-default" href="{u_pt}"/>\n'
    full = NOME if home else f'{title} | {NOME}'
    if len(full) > 60 and not home: full = title
    indexa = '<meta name="robots" content="noindex"/>\n' if erro else f'<link rel="canonical" href="{url}"/>\n' + alterna + dados(path, title, desc, url, tipo, trilha) + '\n'
    base = '<base href="/"/>\n' if erro else ''
    menu = monta_menu(pre, atual)
    l = lambda u, t: f'<li><a href="{pre}{u}">{e(t)}</a></li>'
    idioma = '' if erro or not BILINGUE or path in PT_ONLY else f'<a class="idioma" href="{outra}" hreflang="{"pt-BR" if EN else "en"}" lang="{"pt-BR" if EN else "en"}" title="{"Ler em português" if EN else "Read in English"}">{"PT" if EN else "EN"}</a>' + chr(10)
    doc = f'''<!doctype html>
<html lang="{"en" if EN else "pt-BR"}">
<head>
<meta charset="utf-8"/>
{base}<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>{e(full)}</title>
<meta name="description" content="{e(desc)}"/>
{indexa}<meta property="og:type" content="{'article' if tipo == 'Article' else 'website'}"/>
<meta property="og:site_name" content="{NOME}"/>
<meta property="og:title" content="{e(full)}"/>
<meta property="og:description" content="{e(desc)}"/>
<meta property="og:url" content="{url}"/>
<meta property="og:locale" content="{"en_US" if EN else "pt_BR"}"/>
<meta property="og:image" content="{SITE}/assets/share.png"/>
<meta property="og:image:width" content="1200"/>
<meta property="og:image:height" content="630"/>
<meta property="og:image:alt" content="{e(NOME)}: {"every objection has an answer." if EN else "toda objeção tem uma resposta."}"/>
<meta name="twitter:card" content="summary_large_image"/>
<meta name="twitter:image" content="{SITE}/assets/share.png"/>
<meta name="theme-color" content="#0a3703"/>
<link rel="icon" href="{pre}assets/icon.svg" type="image/svg+xml"/>
<link rel="apple-touch-icon" href="{pre}assets/apple-touch-icon.png"/>
<link rel="manifest" href="{pre}manifest.webmanifest"/>
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Mozilla+Headline:wght@500;600;700&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@500;700&display=swap"/>
<link rel="stylesheet" href="{pre}assets/style.css?v={VER_CSS}"/>
<script>try{{if(!localStorage.getItem("gv-visto")){{document.documentElement.classList.add("chegada");localStorage.setItem("gv-visto","1")}}}}catch(e){{}}</script>
<script src="https://biblioverse.org/superbar.js" async></script>
</head>
<body data-base="{pre}">
<nav id="bvbar" class="bvbar" data-current="{"fortheanimals" if EN else "pelosanimais"}" data-offset="none" aria-label="BiblioVerse" style="position:relative;height:36px;background:linear-gradient(90deg,#4f7cff,#7a5cff)"><a href="https://biblioverse.org" style="color:#fff;line-height:36px;padding:0 14px;font-weight:700;text-decoration:none">BiblioVerse</a></nav>
<a class="skip" href="#main">Pular para o conteúdo</a>
<header class="topo"><div class="wrap topo-in">
<a class="marca" href="{pre}index.html">{LOGO}<span>{en.MARCA if EN else "Guia de Argumentação<br/>Pelos Animais"}</span></a>
<nav class="menu" aria-label="Principal">{menu}</nav>
<button class="bbusca" type="button" aria-label="Buscar um argumento">🔍<span> Buscar</span> <kbd>Ctrl K</kbd></button>
{idioma}<button class="hamb" type="button" aria-label="Abrir menu" aria-expanded="false">☰</button>
</div></header>
<div id="busca" hidden><div class="bcx" role="dialog" aria-label="Buscar um argumento"><input id="q" type="search" placeholder="Digite a frase que você ouviu" autocomplete="off"/><div class="res" id="res"></div></div></div>
<main id="main">{corpo}</main>
<footer class="rodape"><div class="wrap rodape-in">
<div><strong>{NOME}</strong><p>Os argumentos usados para justificar a exploração animal, na sua versão mais forte, com o que acertam e onde falham.</p><p>Parte da <a href="https://biblioverse.org">BiblioVerse</a>.</p></div>
<div><p class="ti">Argumentos</p><ul>{l('comece-aqui.html', 'Como usar o guia')}{l(TODOS, 'Todos os argumentos')}{l('treino.html', 'Treinar respostas')}{l('debate.html', 'Debate simulado')}{l('familias.html', 'As 14 famílias')}{l('argumentos-ruins.html', 'Argumentos ruins de veganos')}{l('raciocinio.html', 'O raciocínio antivegano')}{l('mapa.html', 'Mapa de conexões')}</ul></div>
<div><p class="ti">Aprofundar</p><ul>{l('alem-do-veganismo.html', 'Além do veganismo')}{l('objecoes-politicas.html', 'Objeções políticas')}{l('biblioteca.html', 'Biblioteca')}{l('glossario.html', 'Glossário')}{l('falacias.html', 'Falácias')}{l('vieses.html', 'Vieses')}{l('sobre.html', 'Sobre o guia')}</ul></div>
</div></footer>
<script src="{pre}assets/app.js?v={VER_JS}" defer></script>
</body></html>
'''
    doc = en.traduz_html(doc, nova_url) if EN else nova_url(doc)  # em inglês, a tabela de interface vem antes de converter os links
    doc = doc.replace('href="index.html"', 'href="./"').replace('href="../index.html"', 'href="../"')
    alvo = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(alvo), exist_ok=True)
    open(alvo, 'w', encoding='utf-8', newline='\n').write(doc)
    if not erro: INDICE[path] = indexa_pagina(doc, path)

# Busca no conteúdo: de cada página saem o título, a descrição e as palavras do texto principal (já traduzidas, no site em inglês).
# Páginas que só reúnem as outras (início, mapa, raciocínio, treino, debate) ficam fora do conteúdo para não aparecerem em toda busca.
INDICE = {}
SEM_CONTEUDO = {'index.html', 'mapa.html', 'raciocinio.html', 'treino.html', 'debate.html', 'map.html', 'reasoning.html', 'practice.html'}
def normaliza(s):
    import unicodedata
    return unicodedata.normalize('NFD', s.lower()).encode('ascii', 'ignore').decode()
def indexa_pagina(doc, path):
    ti = re.search(r'<title>(.*?)</title>', doc, re.S)
    de = re.search(r'<meta name="description" content="([^"]*)"', doc)
    titulo = html.unescape(ti[1]).split(' | ')[0] if ti else path
    pal = ''
    if path not in SEM_CONTEUDO:
        m = re.search(r'<main id="main">(.*)</main>', doc, re.S)
        corpo = re.sub(r'<(script|style)\b.*?</\1>', ' ', m[1] if m else '', flags=re.S)
        texto = normaliza(html.unescape(re.sub(r'<[^>]+>', ' ', corpo)))
        pal = ' '.join(sorted(set(re.findall(r'[a-z0-9]{3,}', texto))))  # cada palavra uma vez: o índice fica pequeno e a busca por trecho de palavra continua funcionando
    return dict(t=titulo, d=html.unescape(de[1]) if de else '', c=pal)

def cabeca(trilha, titulo, lede='', extra=''):
    return f'<section class="cabeca"><div class="wrap"><p class="trilha">{trilha}</p><h1>{titulo}</h1>' + (f'<p class="lede">{lede}</p>' if lede else '') + extra + '</div></section>'
def lig(c, pre=''): return f'<a href="{pre}argumentos/{c.lower()}.html">{c}</a>'
def status(c): return '<span class="selo ok">Capítulo completo</span>' if c in CAPS else '<span class="selo">Verbete</span>'
def cartao(a, pre=''):
    f = FAMILIAS[a['fam']]
    return f'<a class="cartao" style="--c:{f["cor"]}" data-parte="{f["parte"]}" data-fam="{a["fam"]}" data-st="{"cap" if a["c"] in CAPS else "ver"}" href="{pre}argumentos/{a["slug"]}.html"><span class="cod">{a["c"]}</span><h3>{e(a["frase"])}</h3><p class="falha">{e(a["falha"])}</p>{status(a["c"])}</a>'
def pontos(f, pre=''):
    bol = ''.join(f'<i{" class=ok" if a["c"] in CAPS else ""}></i>' for a in f['args'])
    return f'<a class="linha-f" style="--c:{f["cor"]}" href="{pre}familias/{f["c"].lower()}.html" aria-label="{e(f["nome"])}: {f["n"]} {L("argumentos", "arguments")}" title="{e(f["nome"])}"><span>{f["c"]}</span><span class="pontos">{bol}</span></a>'
def elos(cods, fim=None, pre='', atual=None):
    h = ''.join(f'<li{" class=aqui" if c == atual else ""}><a href="{pre}argumentos/{c.lower()}.html" title="{e(ARGS[c]["frase"])}">{c}</a></li>' for c in cods)
    return f'<ol class="elos">{h}{fim or ""}</ol>'

# ---------- páginas ----------
PORCO = '<svg class="tinta porco" viewBox="0 0 220 220" aria-hidden="true"><circle cx="110" cy="122" r="92" fill="#ffeb5b" stroke="none"/><path d="M58 92c-16-22-26-40-22-52 16 2 36 14 50 30M162 92c16-22 26-40 22-52-16 2-36 14-50 30" fill="#fcfaf5"/><path d="M52 128c-3-40 26-66 58-66s62 26 59 66c-3 36-27 62-59 62s-55-26-58-62z" fill="#fcfaf5"/><path d="M80 142c0-13 13-21 30-21s30 8 30 21-13 21-30 21-30-8-30-21z" fill="#d6ecfb"/><path d="M99 137c0 5-1 9-2 11M122 137c0 5 1 9 2 11"/><path d="M74 104c5 5 12 5 17 0M129 104c5 5 12 5 17 0"/><path d="M96 174c9 5 19 5 28 0"/></svg>'
GALINHA = '<svg class="tinta galinha" viewBox="0 0 220 220" aria-hidden="true"><path d="M86 62c-8-14-2-28 8-26 2-10 18-12 22 0 10-4 20 8 12 24" fill="#d9602a"/><path d="M62 190c-14-34-10-74 8-100 18-26 62-30 82-4 22 28 24 72 8 104" fill="#fcfaf5"/><path d="M60 118c-22 6-40 2-48-8 2 20 18 38 44 40" fill="#d6ecfb"/><path d="M150 96l34 8-30 14" fill="#ffeb5b"/><path d="M152 122c6 10 4 22-4 26-6-8-8-18-6-26" fill="#d9602a"/><path d="M122 92c5-5 11-5 16 0"/><path d="M84 138c10 12 28 14 42 6M78 158c12 10 32 12 48 4"/></svg>'

def item_arg(a):
    f = FAMILIAS[a['fam']]
    ok = a['c'] in CAPS
    formas = ''.join(f'<li>"{e(x)}"</li>' for x in a['formas'])
    bot = 'Abrir o capítulo completo' if ok else 'Abrir o verbete'
    return f'<details class="item" style="--c:{f["cor"]}" data-parte="{f["parte"]}" data-fam="{a["fam"]}" data-st="{"cap" if ok else "ver"}" data-u="argumentos/{a["slug"]}.html"><summary><span class="cod">{a["c"]}</span><b>{e(a["frase"])}</b>{"<i class=ok title=Capítulo&nbsp;completo></i>" if ok else ""}</summary><div class="abre"><p class="falha-i"><strong>Falha principal:</strong> {e(a["falha"])}</p><ul class="formas">{formas}</ul><a class="btn peq" href="argumentos/{a["slug"]}.html">{bot} →</a></div></details>'

def circulo(pre=''):
    aneis = [(250, 'Extraterrestres', 'alem/extraterrestres.html', '#e6f4fd', True), (205, 'IA e robôs', 'alem/ia-e-robos.html', '#bfe0f7', True), (160, 'Animais selvagens', 'alem/animais-selvagens.html', '#d8eebd', False), (115, 'Animais explorados', 'argumentos/a10.html', '#ffeb5b', False)]
    o = ''
    for r, t, u, cor, poss in aneis:
        o += f'<a href="{pre}{u}" class="anel"><circle cx="260" cy="260" r="{r}" fill="{cor}" stroke="#0a3703" stroke-width="2"{" stroke-dasharray=\"8 7\"" if poss else ""}/><text x="260" y="{260 - r + (21 if poss else 27)}" text-anchor="middle" fill="#0a3703">{t}{f"<tspan x=\"260\" dy=\"15\" class=\"poss\">possibilidade</tspan>" if poss else ""}</text></a>'
    return f'<svg class="circulo" viewBox="0 0 520 520" role="img" aria-label="Círculo moral em expansão: humanos, animais explorados, animais selvagens e, como possibilidades, IA e extraterrestres">{o}<circle cx="260" cy="260" r="62" fill="#0a3703"/><text x="260" y="266" text-anchor="middle" fill="#fff">Humanos</text></svg>'

def ramo(f):
    return f'<a class="ramo" style="--c:{f["cor"]}" href="#fam-{f["c"].lower()}"><span class="letra">{f["c"]}</span><b>{e(f["nome"])}</b><small>{e(f["perg"])}</small></a>'

# Os argumentos mais ouvidos no dia a dia (seleção editorial, guiada pelos "4Ns" de Piazza e colegas, 2015).
COMUNS = ['A14', 'G1', 'C1', 'J11', 'C3', 'F1', 'C2', 'H2', 'D1', 'E1', 'B1', 'K1']

def inicio():
    dir_, ind = [f for f in FAMILIAS.values() if f['parte'] == 'DIR'], [f for f in FAMILIAS.values() if f['parte'] == 'IND']
    chips = lambda g, ops: ''.join(f'<button class="chip" type="button" data-g="{g}" data-v="{v}" aria-pressed="{"true" if not v else "false"}">{e(t)}</button>' for v, t in ops)
    folhas = ''.join(f'<section class="grupo-f" id="fam-{f["c"].lower()}" style="--c:{f["cor"]}"><a class="aba-f" href="#fam-{f["c"].lower()}" aria-hidden="true" tabindex="-1">{f["c"]}</a><div class="folha"><h3><span class="letra">{f["c"]}</span><a href="familias/{f["c"].lower()}.html">{e(f["nome"])}</a> <small>{e(f["perg"])}</small></h3><div class="itens">{"".join(item_arg(a) for a in f["args"])}</div></div></section>' for f in FAMILIAS.values())
    guias = ''.join(f'<a href="#fam-{f["c"].lower()}" style="--c:{f["cor"]}" title="{e(f["nome"])}">{f["c"]}</a>' for f in FAMILIAS.values())
    exemplos = [ARGS[c] for c in ('A14', 'G1', 'C2', 'J11', 'H1', 'A10', 'L4', 'F1', 'B1', 'D8', 'E1', 'K1')]
    ex_json = json.dumps([dict(c=a['c'], f=a['frase'], r=a['falha'], u=f'argumentos/{a["slug"]}.html') for a in exemplos], ensure_ascii=False).replace('</', '<\\/')
    ini = exemplos[0]
    comuns = ''.join(f'<a class="comum" style="--c:{FAMILIAS[ARGS[c]["fam"]]["cor"]}" href="argumentos/{c.lower()}.html"><span class="cod">{c}</span><b>{e(ARGS[c]["frase"])}</b></a>' for c in COMUNS)
    ruins = ''.join(f'<details class="riscado"><summary><span>"{e(r["frase"])}"</span><i>{e(TIPOS[r["tipo"]][0])}</i></summary><div><p class="diga"><b>Diga:</b> {e(r["lugar"])}</p><a href="ruins/{r["c"].lower()}.html">Por que esse argumento é ruim →</a></div></details>' for r in RUINS)
    alemc = ''.join(cartao_alem(p) for p in alem.PAGINAS)
    tons = list(CORES.values())
    polc = ''.join(f'<a class="cartao pol-c" style="--c:{tons[i % len(tons)]}" href="politicas/{t["s"]}.html"><span class="cod">{e(t["t"])}</span><h3>"{e(t["frase"])}"</h3></a>' for i, t in enumerate(politicas.TEORIAS))
    corpo = f'''<section class="capa"><div class="wrap capa-in"><p class="etiqueta"><span>Da próxima vez que ouvir um argumento contra o veganismo, lembre:</span></p><h1>Toda objeção tem <mark>uma resposta</mark>.</h1><p class="lede">{e(DESCRICAO)}</p>
<div class="busca-h"><label class="so-leitor" for="hq">O que te disseram?</label><input id="hq" type="search" placeholder="O que te disseram? Ex.: de onde você tira proteína" autocomplete="off"/><div id="hres" class="hres" hidden></div></div>
<div class="comuns-w"><p class="comuns-t">Os mais ouvidos</p><div class="comuns">{comuns}</div></div>
<div class="cena-h">{PORCO}<div class="nota" id="nota"><p class="nota-ti">Alguém disse:</p><p class="nota-f"><s id="n-f">"{e(ini["frase"])}"</s></p><p class="nota-r" id="n-r">{e(ini["falha"])}</p><p class="nota-a"><a id="n-l" href="argumentos/{ini["slug"]}.html">Ver a resposta completa →</a><button id="n-o" type="button" class="btn peq alt">Outra objeção ↻</button></p></div>{GALINHA}</div>
<a class="rolar" href="#argumentos">{L(f"Role para ver mais de {len(ARGS) // 100 * 100} argumentos ↓", f"Scroll to see more than {len(ARGS) // 100 * 100} arguments ↓")}</a></div><script type="application/json" id="n-dados">{ex_json}</script></section>
<section class="bloco-cor lilas" id="argumentos"><div class="wrap"><div class="sec-cab centro-t"><h2>Todos os argumentos</h2><p>Um caderno com 14 divisórias. Toque em uma frase para ver a falha principal sem sair da página.</p></div>
<div class="barra-f"><div class="filtros"><input id="fq" type="search" placeholder="Filtrar: leão, churrasco, B12" aria-label="Filtrar argumentos"/>{chips('parte', [('', 'Todos'), ('DIR', 'Diretos'), ('IND', 'Indiretos')])}{chips('st', [('', 'Tudo'), ('cap', 'Capítulos completos')]) if len(set(CAPS) & set(ARGS)) < len(ARGS) else ''}<span id="contagem" aria-live="polite">{len(ARGS)} {L("argumentos", "arguments")}</span></div><nav class="guias" aria-label="Ir para a família">{guias}</nav></div>
<div class="caderno"><div id="catalogo">{folhas}</div></div></div></section>
<section class="bloco-cor azul" id="politicas"><div class="wrap"><div class="sec-cab centro-t"><h2>E se a pessoa parte de uma teoria política?</h2><p>Liberais, marxistas, anarquistas, utilitaristas, feministas: cada teoria tem um princípio, e nenhuma oferece, nos próprios termos, uma razão para deixar os animais de fora.</p></div>
<div class="grade">{polc}</div><p class="centro-t" style="margin-top:22px"><a class="btn" href="objecoes-politicas.html">Ver todas as objeções políticas</a></p></div></section>
<section class="bloco-cor verde" id="grupos"><div class="wrap"><div class="sec-cab centro-t"><h2>Duas perguntas, catorze famílias</h2><p>Argumentos parecidos erram de modo parecido. Toda objeção tenta responder a uma destas duas perguntas.</p></div>
<div class="arvore-g"><div class="galho"><p class="pergunta"><small>Argumentos diretos</small>Os animais contam?</p><div class="ramos">{"".join(ramo(f) for f in dir_)}</div></div><div class="galho"><p class="pergunta"><small>Argumentos indiretos</small>É necessário, viável, eficaz?</p><div class="ramos">{"".join(ramo(f) for f in ind)}</div><p class="ressalva">Mesmo quando têm uma parte verdadeira, justificam no máximo exceções. Muitos ativistas evitam usá-los para defender os animais: outros movimentos sociais não defendem humanos com argumentos de saúde ou de ambiente. <a href="comece-aqui.html#indiretos">Entenda</a></p></div></div>
<div class="raizes-h"><p>Quase toda conversa termina em uma destas três raízes:</p><div>{"".join(f'<a href="argumentos/{c.lower()}.html"><b>{c}</b> {e(ARGS[c]["frase"])}</a>' for c in RAIZES)}</div><a class="mais" href="mapa.html">Ver o mapa de conexões →</a></div></div></section>
<section class="bloco-cor laranja" id="ruins"><div class="wrap"><div class="sec-cab centro-t"><h2>Pare de dizer isso, ou diga melhor</h2><p>A exigência vale para os dois lados. Estes argumentos circulam entre veganos e não resistem a exame como são ditos. Toque em um para ver como dizer melhor. Corrigir faz parte do processo, mas sem perder o foco: <a href="argumentos-ruins.html#corrigir-sem-perder-o-foco">por quê</a>.</p></div><div class="lista-riscada">{ruins}</div></div></section>
<section class="bloco-cor amarelo" id="alem"><div class="wrap alem-in"><div>{circulo()}</div><div><div class="sec-cab"><h2>Além do veganismo</h2><p>O critério da senciência não termina no prato. Clique em um círculo ou escolha um tema.</p></div><div class="lista-alem">{alemc}</div></div></div></section>
<section class="fecho"><div class="wrap"><h2>Pronto para a próxima conversa?</h2><p>Leia a objeção, pense no que diria e compare com a resposta.</p><a class="btn" href="debate.html">Simular um debate</a> <a class="btn alt" href="treino.html">Treinar respostas</a></div></section>'''
    page('index.html', NOME, DESCRICAO, corpo)

def cartao_ruim(r, pre=''):
    return f'<a class="cartao" style="--c:#b8460f" href="{pre}ruins/{r["c"].lower()}.html"><span class="cod">{r["c"]} · {e(TIPOS[r["tipo"]][0])}</span><h3>"{e(r["frase"])}"</h3><p class="falha">{e(r["por"][0])}</p></a>'

def cartao_alem(p, pre=''):
    return f'<a class="cartao" href="{pre}alem/{p["s"]}.html"><span class="selo{" ok" if p["selo"] != "Possibilidade" else ""}">{e(p["selo"])}</span><h3>{e(p["t"])}</h3><p>{e(p["res"])}</p></a>'

def lista_fontes(ls):
    return '<h2>Fontes e leituras</h2><div class="fontes"><ul>' + ''.join(f'<li><a href="{e(u)}" {EXT}>{e(t)}</a></li>' if u else f'<li>{e(t)}</li>' for t, u in ls) + '</ul></div>'

EQUILIBRIO = """<section class="equilibrio" id="corrigir-sem-perder-o-foco" aria-labelledby="eq-t"><h2 id="eq-t">Corrigir sem perder o foco</h2>
<p>Corrigir os próprios argumentos faz parte de qualquer movimento que leva a verdade a sério. Um argumento ruim dito por um vegano é desmontado na primeira conversa com alguém bem informado, e a derrota cai sobre a causa inteira. Por isso esta página existe.</p>
<p>Mas a correção tem um custo. O tempo e a energia de quem defende os animais são limitados, e cada hora gasta em brigas entre veganos é uma hora a menos para explicar o especismo, responder às objeções de quem ainda come animais e produzir conteúdo de qualidade. É uma troca: quando a briga interna toma o lugar do trabalho para fora, a estratégia provavelmente está errada. O projeto <a href="https://infighting.org" target="_blank" rel="noopener">End Infighting</a> reúne as causas e os custos dessas brigas em movimentos sociais.</p>
<h3>O limite não é bem definido</h3>
<p>Corrigir veganos e responder a exploradores de animais não são duas tarefas separadas. Abandonar um argumento ruim é também preparar a próxima conversa com quem não é vegano. Alguns exemplos:</p>
<ul>
<li><strong>Correção que vale a pena:</strong> parar de dizer que {RUIM:Gorilas, touros e cavalos}. O argumento cai na primeira réplica e troca uma questão ética por uma de biologia mal contada.</li>
<li><strong>Correção que protege pessoas:</strong> desmentir que {RUIM:Veganos não precisam suplementar B12}. Aqui o erro não só enfraquece o argumento, como põe em risco a saúde de quem acredita nele.</li>
<li><strong>Briga que provavelmente não vale:</strong> semanas de discussão pública contra um ativista por uma frase imprecisa, enquanto ninguém responde bem à pergunta "de onde vem a proteína?", que quase todo vegano já ouviu.</li>
<li><strong>Debate que pode se arrastar:</strong> a divergência sobre estratégias, como reformas de bem-estar ou abolição. É um debate legítimo, mas, se ocupa todo o espaço, os animais deixam de ser o centro da conversa.</li>
</ul>
<h3>Uma regra prática</h3>
<p>Antes de corrigir alguém, vale perguntar: <em>essa correção vai melhorar a próxima conversa com quem ainda não é vegano?</em> Se sim, corrija o argumento, e não a pessoa, de preferência em particular ou com uma alternativa melhor pronta. Depois, volte ao trabalho que importa: explicar por que os animais contam.</p>
</section>"""

def marca_ruins(txt, pre='../'):
    def f(m):
        r = next(x for x in RUINS if x.get('frase_pt', x['frase']).startswith(m[1]))  # marcadores usam a frase em português
        return f'<a href="{pre}ruins/{r["c"].lower()}.html">"{e(r["frase"].rstrip("."))}"</a>'
    return re.sub(r'\{RUIM:([^}]+)\}', f, txt)

def paginas_ruins():
    grupos = ''
    for k, (nome, desc) in TIPOS.items():
        grupos += f'<h2 style="margin:0 0 6px">{e(nome)}</h2><p style="margin:0 0 14px">{e(desc)}</p><div class="grade" style="margin-bottom:34px">{"".join(cartao_ruim(r) for r in RUINS if r["tipo"] == k)}</div>'
    corpo = cabeca('<a href="./">Início</a>', 'Argumentos ruins que veganos deveriam parar de usar, ou usar de forma melhor', 'Um argumento não fica bom porque defende a causa certa. O único que sobrevive ao escrutínio repetido é o que sempre foi verdadeiro: prejudicar seres sencientes sem necessidade é injusto.') + f'<section class="secao"><div class="wrap">{marca_ruins(EQUILIBRIO, "")}{grupos}<p>Este grupo vem do livro <em>Veganismo Baseado em Evidências</em>. O critério para julgar cada tática é o do melhor cenário: qual abordagem, avaliada com honestidade sobre suas consequências, reduz mais sofrimento.</p></div></section>'
    page('argumentos-ruins.html', 'Argumentos ruins de veganos: pare de usar ou use melhor', L('Argumentos usados por veganos que não resistem a exame, de saúde e fome a gatos e psicopatia, e como dizer melhor o que cada um tenta dizer.', "Arguments vegans use that don't survive scrutiny, from health and hunger to cats and psychopathy, and how to say better what each one is trying to say."), corpo, 'argumentos-ruins.html', 'CollectionPage')
    for i, r in enumerate(RUINS):
        nome, desc = TIPOS[r['tipo']]
        lig_ = ''.join(f'<a class="no" style="--c:{FAMILIAS[c[0]]["cor"]}" href="../argumentos/{c.lower()}.html"><b>{c}</b> {e(ARGS[c]["frase"])}</a>' for c in dict.fromkeys(UNIDOS[x][0] if x in UNIDOS else x for x in r['liga']))
        ant, prox = RUINS[i - 1] if i else None, RUINS[i + 1] if i + 1 < len(RUINS) else None
        pp = lambda x, t: f'<a href="{SLUG_RUIM[x["c"].lower()]}.html"><small>{t}</small>{x["c"]}. {e(x["frase"])}</a>'
        art = '<div class="troca"><div class="nao"><p class="ti">Por que é ruim</p>' + ''.join(f'<p>{e(x)}</p>' for x in r['por']) + f'</div><div class="sim"><p class="ti">Como dizer melhor</p><p>{e(r["lugar"])}</p>' + (f'<p class="ev">{e(r["nota"])}</p>' if r.get('nota') else '') + f'</div></div><h2>Veja também</h2><div class="nos">{lig_}</div>' + (lista_fontes(r['fontes']) if r.get('fontes') else '') + f'<nav class="pass" aria-label="Outros argumentos">' + (pp(ant, 'Anterior') if ant else '') + (pp(prox, 'Próximo') if prox else '') + '</nav>'
        pag = f'<section class="cena" style="--c:#b8460f"><div class="wrap"><p class="trilha"><a href="../">Início</a> / <a href="../argumentos-ruins.html">Argumentos ruins</a> / {e(nome)}</p><div class="fala"><span class="selo-c">{r["c"]}</span><h1>"{e(r["frase"])}"</h1></div><div class="tese-c"><span>{e(nome)}</span><p>{e(desc)}</p></div></div></section><div class="wrap paineis">{art}</div>'
        page(f'ruins/{r["c"].lower()}.html', f'{r["c"]}: {r["frase"]}', L(f'Por que parar de dizer “{r["frase"].rstrip(".")}”, ou como dizer melhor: {r["por"][0]}', f'Why to stop saying “{r["frase"].rstrip(".")}”, or how to say it better: {r["por"][0]}'), pag, 'argumentos-ruins.html', 'Article', [('Argumentos ruins', 'argumentos-ruins.html')])

def paginas_alem():
    corpo = cabeca('<a href="./">Início</a>', 'Além do veganismo', 'O veganismo é uma consequência do antiespecismo e do senciocentrismo, não o limite deles.') + f'<section class="secao"><div class="wrap alem-in"><div>{circulo()}</div><div class="lista-alem">{"".join(cartao_alem(p) for p in alem.PAGINAS)}</div></div></section>'
    page('alem-do-veganismo.html', 'Além do veganismo', L('Antiespecismo, senciocentrismo, estado da arte da ética animal, sofrimento de animais selvagens e a possibilidade de senciência em IA e extraterrestres.', 'Antispeciesism, sentientism, the state of the art in animal ethics, wild animal suffering and the possibility of sentience in AI and extraterrestrials.'), corpo, 'alem-do-veganismo.html', 'CollectionPage')
    for i, p in enumerate(alem.PAGINAS):
        lado = ''.join(f'<a href="{x["s"]}.html"{" aria-current=page" if x is p else ""}>{e(x["t"])}</a>' for x in alem.PAGINAS)
        # {RUIM:começo da frase} vira um link para a página de "Pare de dizer isso", cujo código é renumerado no build
        def ruim(m):
            r = next(x for x in RUINS if x.get('frase_pt', x['frase']).startswith(m[1]))  # marcadores usam a frase em português
            return f'<a href="../ruins/{r["c"].lower()}.html">{r["c"]}, "{e(r["frase"].rstrip("."))}"</a>'
        texto_ = re.sub(r'\{RUIM:([^}]+)\}', ruim, p['corpo'])
        pag = cabeca(f'<a href="../">Início</a> / <a href="../alem-do-veganismo.html">Além do veganismo</a> / {e(p["selo"])}', e(p['t']), e(p['res'])) + f'<div class="wrap lay"><nav class="indice" aria-label="Além do veganismo"><p class="ti">Nesta seção</p><div class="lado">{lado}</div></nav><article class="artigo">{texto_}{lista_fontes(p["fontes"])}</article></div>'
        page(f'alem/{p["s"]}.html', p['t'], p['res'], pag, 'alem-do-veganismo.html', 'Article', [('Além do veganismo', 'alem-do-veganismo.html')])

def espectro():
    """Bloco "Da esquerda à direita" da página de objeções políticas: valores de cada lado que pedem considerar os animais."""
    E_ = politicas.ESPECTRO
    def tabela(lado, itens):
        linhas = ''.join(f'<tr><td><strong>{e(v)}</strong></td><td>{e(d)} <a href="politicas/{s_}.html">{L("Ver a teoria", "See the theory")} →</a></td></tr>' for v, d, s_ in itens)
        return f'<h3 style="margin:22px 0 10px">{e(lado)}</h3><div class="tabela"><table><tr><th scope="col">{L("Valor", "Value")}</th><th scope="col">{L("Por que leva a considerar os animais", "Why it leads to considering animals")}</th></tr>{linhas}</table></div>'
    return f'<div class="estreito" style="margin-top:40px"><h2>{e(E_["titulo"])}</h2><p>{e(E_["intro"])}</p>' + ''.join(tabela(l, i) for l, i in E_['lados']) + f'<p style="margin-top:18px">{e(E_["fecho"])}</p></div>'

def paginas_politicas():
    """Objeções vindas de teorias éticas e políticas (dados em tools/politicas.py)."""
    tons = list(CORES.values())
    def nos(cods, pre='../'):
        return ''.join(f'<a class="no" style="--c:{FAMILIAS[c[0]]["cor"]}" href="{pre}argumentos/{c.lower()}.html"><b>{c}</b> {e(ARGS[c]["frase"])}</a>' for c in dict.fromkeys(UNIDOS[x][0] if x in UNIDOS else x for x in cods))
    cards = ''.join(f'<a class="cartao" style="--c:{tons[i % len(tons)]}" href="politicas/{t["s"]}.html"><span class="cod">{e(t["t"])}</span><h3>"{e(t["frase"])}"</h3><p class="falha">{e(t["principio"])}</p></a>' for i, t in enumerate(politicas.TEORIAS))
    corpo = cabeca('<a href="./">Início</a>', 'Objeções políticas', 'O que cada teoria ética ou política costuma dizer para deixar os animais de fora, e por que essa exclusão contradiz o princípio da própria teoria.') + f'''<section class="secao"><div class="wrap">
<p class="estreito" style="margin:0 0 26px">{e(politicas.INTRO)}</p>
<div class="grade">{cards}</div>
{espectro()}
<p class="fino" style="margin-top:26px">A seção parte do livro <em>An Introduction to Animals and Political Theory</em>, de Alasdair Cochrane, do artigo <em>Animal Rights, Multiculturalism, and the Left</em>, de Will Kymlicka e Sue Donaldson, e de dois textos de Julio Cesar Prava, revistos: as afirmações foram conferidas e as analogias, ajustadas para não dizer mais do que a evidência permite.</p>
</div></section>'''
    page('objecoes-politicas.html', 'Objeções políticas', L('Liberalismo, marxismo, anarquismo, utilitarismo, Rawls, Kant, feminismo, antirracismo e outras teorias: por que nenhuma oferece, nos próprios termos, razão para excluir os animais.', 'Liberalism, Marxism, anarchism, utilitarianism, Rawls, Kant, feminism, anti-racism and other theories: why none offers, on its own terms, a reason to exclude animals.'), corpo, 'objecoes-politicas.html', 'CollectionPage')
    T = politicas.TEORIAS
    for i, t in enumerate(T):
        cor = tons[i % len(tons)]
        ant, prox = T[i - 1] if i else None, T[i + 1] if i + 1 < len(T) else None
        pp = lambda x, r: f'<a href="{x["s"]}.html"><small>{r}</small>{e(x["t"])}</a>'
        art = ('<h2>Por que excluir os animais contradiz o princípio</h2><ul class="pol-q">' + ''.join(f'<li>{liga(e(x), {"pre": "../"})}</li>' for x in t['quebra']) + '</ul>'
               f'<div class="troca"><div class="nao"><p class="ti">A melhor réplica</p><p>{liga(e(t["replica"]), {"pre": "../"})}</p></div><div class="sim"><p class="ti">A resposta</p><p>{liga(e(t["resposta"]), {"pre": "../"})}</p></div></div>'
               + ''.join(f'<h2>{e(ti)}</h2>' + ''.join(f'<p>{liga(e(x), {"pre": "../"})}</p>' for x in ps) for ti, ps in t.get('mais', []))
               + (f'<h2>{L("Quem defende os animais a partir desta teoria", "Who defends animals from within this theory")}</h2><p>{L("Autores, ativistas e grupos que partem desta teoria e mostram por que ela precisa incluir os animais e os demais seres sencientes.", "Authors, activists and groups who start from this theory and show why it has to include animals and other sentient beings.")}</p><ul class="pol-q">' + ''.join(f'<li><strong>{e(n)}:</strong> {e(d)}</li>' for n, d in t['nomes']) + '</ul>' if t.get('nomes') else '') +
               f'<h2>Veja também</h2><div class="nos">{nos(t["liga"])}</div>' + lista_fontes(t['fontes']) +
               '<nav class="pass" aria-label="Outras teorias">' + (pp(ant, 'Anterior') if ant else '') + (pp(prox, 'Próxima') if prox else '') + '</nav>')
        pag = (f'<section class="cena" style="--c:{cor}"><div class="wrap"><p class="trilha"><a href="../">Início</a> / <a href="../objecoes-politicas.html">Objeções políticas</a> / {e(t["t"])}</p>'
               f'<div class="fala"><h1>"{e(t["frase"])}"</h1></div><div class="tese-c"><span>{e(t["t"])}: o princípio</span><p>{e(t["principio"])}</p></div></div></section><div class="wrap paineis">{art}</div>')
        page(f'politicas/{t["s"]}.html', L(f'{t["t"]} e a questão animal', f'{t["t"]} and the animal question'), L(f'{t["t"]}: por que a objeção "{t["frase"]}" contradiz o princípio da própria teoria.', f'{t["t"]}: why the objection "{t["frase"]}" contradicts the theory\'s own principle.'), pag, 'objecoes-politicas.html', 'Article', [('Objeções políticas', 'objecoes-politicas.html')])

def pagina_debate():
    """Debate simulado: dados em tools/debate.py, lógica em assets/debate.js. A conversa segue o grafo do raciocínio antivegano."""
    G = grafo()
    jogaveis = [c for c in ORDEM if c in debate.OP]
    faltam = [c for c in COMUNS if c not in debate.OP]
    assert not faltam, f'aberturas sem respostas no debate: {faltam}'
    n = {}
    for c in jogaveis:
        o = debate.OP[c]
        n[c] = dict(f=ARGS[c]['frase'], u=f'argumentos/{ARGS[c]["slug"]}.html', cor=FAMILIAS[ARGS[c]['fam']]['cor'],
                    o={t: [o[t], o[t + 'e']] for t in ('f', 'm', 'r')}, p=[[x, m] for x, m in G.get(c, {}).items() if x in debate.OP])
    js = json.dumps(dict(n=n, aberturas=COMUNS, pessoas=debate.PESSOAS), ensure_ascii=False).replace('</', '<\\/')
    corpo = cabeca('<a href="./">Início</a>', 'Debate simulado', 'Alguém começa com um dos argumentos mais ouvidos. Você escolhe a resposta, e a conversa segue para onde esses debates costumam ir. No fim, veja como foi.') + f'''<section class="secao"><div class="wrap estreito">
<div id="debate" class="debate"><noscript><p>O debate simulado precisa de JavaScript. Enquanto isso, use <a href="treino.html">Treinar respostas</a>.</p></noscript></div>
<p class="fino" style="margin-top:26px">Cada rodada tem uma resposta forte, uma fraca (exagerada, enviesada ou que troca a questão ética por outra) e uma ruim. As respostas fortes resumem os capítulos do guia; as fracas e as ruins vêm, em boa parte, dos <a href="argumentos-ruins.html">argumentos que veganos deveriam parar de usar</a>. {L(f"São {len(jogaveis)} argumentos jogáveis, ligados pelo", f"There are {len(jogaveis)} playable arguments, linked by the")} <a href="raciocinio.html">{L("raciocínio antivegano", "anti-vegan line of reasoning")}</a>.</p>
</div></section><script type="application/json" id="deb-dados">{js}</script><script src="assets/debate.js?v={VER_DEB}" defer></script>'''
    page('debate.html', 'Debate simulado', L('Jogo para treinar uma conversa com quem não é vegano: escolha a melhor resposta para cada argumento e veja como você se saiu no debate.', "A game to practice a conversation with someone who isn't vegan: pick the best answer to each argument and see how you did in the debate."), corpo, 'debate.html')

def treino():
    cartas = [dict(c=a['c'], f=a['frase'], r=a['falha'], u=f'argumentos/{a["slug"]}.html', p=FAMILIAS[a['fam']]['parte'], cor=FAMILIAS[a['fam']]['cor'], fam=a['fam']) for a in ARGS.values()]
    cad = [dict(n=c['n'], cods=c['cods']) for c in CADEIAS]
    ops = ''.join(f'<option value="fam:{f["c"]}">{L("Família", "Family")} {f["c"]}: {e(f["nome"])}</option>' for f in FAMILIAS.values())
    opc = ''.join(f'<option value="cad:{i}">{L("Conversa", "Conversation")}: {e(c["n"])}</option>' for i, c in enumerate(CADEIAS))
    dados_ = json.dumps(dict(cartas=cartas, cadeias=cad), ensure_ascii=False).replace('</', '<\\/')
    corpo = cabeca('<a href="./">Início</a>', 'Treinar respostas', 'Leia a objeção, pense no que diria e compare com a falha principal. Escolha uma família, ou siga uma conversa do jeito que ela costuma acontecer.') + f'''<section class="secao"><div class="wrap estreito"><div class="filtros"><label for="t-mod" class="so-leitor">O que treinar</label><select id="t-mod" class="sel"><option value="todos">Todos os argumentos, em ordem aleatória</option><optgroup label="Conversas típicas">{opc}</optgroup><optgroup label="Famílias">{ops}</optgroup></select></div>
<div class="flash" id="flash" aria-live="polite"><p class="flash-m"><span id="t-cod"></span><span id="t-pos"></span></p><p class="flash-q" id="t-q"></p><div id="t-res" hidden><p class="ti">A falha principal</p><p id="t-r"></p><a id="t-l" href="#flash">Ver a resposta completa →</a></div></div>
<div class="flash-b"><button class="btn" id="t-ver" type="button">Mostrar a resposta</button><button class="btn alt" id="t-sabia" type="button" hidden>Eu sabia</button><button class="btn alt" id="t-rever" type="button" hidden>Preciso rever</button></div><p id="t-placar" class="ev"></p></div></section><script type="application/json" id="t-dados">{dados_}</script>'''
    page('treino.html', 'Treinar respostas', L('Treine respostas às objeções ao veganismo com cartões: leia o argumento, pense no que diria e compare com a falha principal.', "Practice answers to objections to veganism with cards: read the argument, think about what you'd say and compare it with the main flaw."), corpo, 'treino.html', 'WebPage')

def cartao_fam(f, pre=''):
    return f'<a class="cartao" style="--c:{f["cor"]}" href="{pre}familias/{f["c"].lower()}.html"><span class="cod">{L("Família", "Family")} {f["c"]} · {f["n"]} {L("argumentos", "arguments")}</span><h3>{e(f["nome"])}</h3><p>{e(f["perg"])}</p></a>'

def comece():
    blocos = ['Formulação: a frase do dia a dia e a versão mais forte, com premissas numeradas', 'Como pode aparecer: outras formas do mesmo argumento', 'Resposta para crianças: linguagem de 8 a 10 anos, sem culpa nem choque', 'Resposta curta: a falha central e uma pergunta de retorno', 'Resposta completa: validade, evidências, a melhor réplica e por que ela também falha', 'Conexões: o que costuma vir antes e depois', 'Erros de raciocínio: lógicos, epistemológicos e morais', 'Contradições: onde o argumento colide com outras crenças da própria pessoa', 'Vieses: os mecanismos psicológicos que o tornam convincente', 'Extrapolações: o que se seguiria se o princípio valesse para humanos', 'O que o argumento acerta: as concessões honestas']
    corpo = cabeca('<a href="./">Início</a>', 'Comece aqui', 'Este guia reúne os argumentos usados para justificar a exploração animal ou rejeitar o veganismo, organizados para você encontrar a resposta de que precisa sem ler tudo.') + f'''<section class="secao"><div class="wrap estreito artigo">
<h2>O critério de fundo</h2><p>Se um ser é senciente, ou seja, pode ser prejudicado ou beneficiado pelo que lhe acontece, seus interesses contam moralmente. Uma justificativa para ignorar esses interesses só é válida se sobreviver a três testes: coerência lógica, suporte empírico e consistência quando aplicada a casos humanos equivalentes.</p>
<h2>Cinco compromissos</h2><ol><li><strong>Honestidade intelectual:</strong> apresentar a versão mais forte de cada argumento, reconhecer o que ele acerta e não fazer afirmação empírica sem fonte.</li><li><strong>Rigor em três planos:</strong> lógico (o argumento é válido?), epistemológico (as premissas têm respaldo na evidência?) e moral (o critério é coerente e relevante?).</li><li><strong>Senciocentrismo:</strong> a senciência é o critério fundador da inclusão moral. Espécie, inteligência, utilidade ou afeto humano não são.</li><li><strong>Antiespecismo e justiça:</strong> interesses semelhantes merecem consideração semelhante, seja qual for a espécie de quem os tem.</li><li><strong>Parcimônia:</strong> preferir o critério mais simples que explica nossos juízos morais mais firmes, sem exceções criadas sob medida para proteger hábitos.</li></ol>
<p>Derrubar espantalhos enfraqueceria o guia e faria dele aquilo que critica. Por isso a versão mais forte de cada argumento vem antes da resposta.</p>
<h2>Como usar</h2><ul><li><strong>Para debater:</strong> localize a objeção pelo <a href="index.html#argumentos">código ou pela busca</a> e siga o <a href="mapa.html">mapa de conexões</a> para antecipar a próxima. A letra indica a família e o número, a posição dentro dela.</li><li><strong>Para reconhecer:</strong> o bloco "Como pode aparecer" mostra as outras formas em que o argumento costuma ser dito ou escrito.</li><li><strong>Para ensinar:</strong> use a resposta para crianças e a curta. As camadas técnicas ficam para quem quer se aprofundar.</li><li><strong>Para debater com quem parte de uma teoria política:</strong> as <a href="objecoes-politicas.html">objeções políticas</a> mostram, teoria por teoria, por que excluir os animais contradiz o princípio de cada uma.</li><li><strong>Para pesquisar:</strong> os índices de <a href="falacias.html">falácias</a> e <a href="vieses.html">vieses</a> permitem atravessar o catálogo por tipo de erro.</li></ul>
<h2>Argumentos diretos e indiretos</h2><p>Os argumentos <strong>diretos (DIR)</strong> contestam o núcleo moral: se os animais sentem, se o indivíduo animal conta e se usar ou matar esse indivíduo é errado. Os <strong>indiretos (IND)</strong> não enfrentam essa questão: alegam que a exploração é necessária, que o veganismo é inviável, prejudicial ou ineficaz, ou que quem o defende não merece crédito.</p><p>Mesmo que um argumento indireto fosse verdadeiro, ele justificaria apenas exceções, nunca a exploração em geral. Por isso a Parte DIR vem primeiro.</p><h3 id="indiretos">Por que os argumentos indiretos não bastam</h3>{IND_TEXTO}
<h2>Os 11 blocos de um capítulo completo</h2><ol>{"".join(f"<li>{e(b)}</li>" for b in blocos)}</ol><p>Comece por <a href="argumentos/a10.html">A10, "São só animais"</a>, o capítulo-raiz: é onde a maioria das cadeias de objeções termina.</p>
</div></section>'''
    page('comece-aqui.html', 'Comece aqui', L('Como usar o guia: o critério da senciência, os cinco compromissos, a diferença entre argumentos diretos e indiretos e os 11 blocos de cada capítulo.', 'How to use the guide: the sentience criterion, the five commitments, the difference between direct and indirect arguments and the 11 blocks of each chapter.'), corpo, 'comece-aqui.html')

def familias():
    corpo = cabeca('<a href="./">Início</a>', 'As 14 famílias', 'Argumentos parecidos erram de modo parecido. Cada família reúne objeções com a mesma pergunta de fundo e o mesmo tipo de erro dominante.') + '<section class="secao"><div class="wrap">' + ''.join(f'<h2 style="margin:0 0 14px">{L("Parte", "Part")} {p}: {L("argumentos " + t, t + " arguments")}</h2>' + (f'<div class="aviso-ind largo"><span>Sobre os argumentos indiretos</span>{IND_TEXTO.replace(chr(34)+"argumentos/", chr(34)+"argumentos/")}</div>' if p == 'IND' else '') + f'<div class="grade" style="margin-bottom:34px">{"".join(cartao_fam(f) for f in FAMILIAS.values() if f["parte"] == p)}</div>' for p, t in (('DIR', L('diretos', 'direct')), ('IND', L('indiretos', 'indirect')))) + '</div></section>'
    page('familias.html', 'As 14 famílias', L('As catorze famílias de argumentos contra o veganismo e o antiespecismo, de senciência e status moral a animais selvagens, o futuro e os motivos de ex-veganos, com a pergunta de fundo de cada uma.', 'The fourteen families of arguments against veganism and antispeciesism, from sentience and moral status to wild animals, the future and ex-vegans\' reasons, with the underlying question of each.'), corpo, 'familias.html', 'CollectionPage')
    for c, f in FAMILIAS.items():
        extra = f'<p class="tese" style="--c:{f["cor"]}"><strong>Pergunta de fundo:</strong> {e(f["perg"])}<br/><strong>Erro dominante:</strong> {e(f["erro"])}</p>'
        if f['parte'] == 'IND': extra += aviso_ind(c, 'Família de argumentos indiretos')
        corpo = cabeca('<a href="../">Início</a> / <a href="../familias.html">Famílias</a>', f'{c}. {e(f["nome"])}', L(f'{f["n"]} argumentos da Parte {f["parte"]}.', f'{f["n"]} arguments in Part {f["parte"]}.'), extra) + f'<section class="secao"><div class="wrap"><div class="grade">{"".join(cartao(a, "../") for a in f["args"])}</div></div></section>'
        page(f'familias/{c.lower()}.html', f'Família {c}: {f["nome"]}', L(f'{f["n"]} argumentos sobre {f["nome"].lower()}. {f["perg"]} Erro dominante: {f["erro"]}.', f'{f["n"]} arguments about {f["nome"].lower()}. {f["perg"]} Dominant error: {f["erro"]}.'), corpo, 'familias.html', 'CollectionPage', [('Famílias', 'familias.html')])

def indice_erro(path, titulo, cab, lede, itens, col):
    cards = ''
    for i in itens:
        cods = ''.join(f'<a href="argumentos/{c.lower()}.html" title="{e(ARGS[c]["frase"])}">{c}</a>' for c in i['cods'])
        cards += f'<div class="cartao erro" id="{slug(i["n"])}"><h3>{e(i["n"])}</h3><p>{e(i["d"])}</p><div class="elos soltos">{cods or e(i["aparece"])}</div></div>'
    corpo = cabeca('<a href="./">Início</a>', titulo, lede) + f'<section class="secao"><div class="wrap"><div class="filtros"><input class="f-simples" type="search" placeholder="{L("Filtrar", "Filter")} {titulo.lower()}" aria-label="{L("Filtrar", "Filter")} {titulo.lower()}"/></div><div class="grade f-alvo">{cards}</div></div></section>'
    page(path, titulo, lede, corpo, path, 'CollectionPage')

def slug(s):
    import unicodedata
    return re.sub(r'[^a-z0-9]+', '-', unicodedata.normalize('NFD', s.lower()).encode('ascii', 'ignore').decode()).strip('-')

def mapa():
    cads = ''.join(f'<div class="cadeia"><h3>{e(n)}</h3><p style="margin:0 0 .6rem;font-size:.95rem">{e(d)}</p>{elos(cs, "<li class=fim><a href=\"#raizes\">Raízes</a></li>")}</div>' for n, d, cs in CADEIAS_LONGAS)
    tipicas = ''
    for ca in CADEIAS:
        rot =re.sub(r'\b([A-N]\d{1,2})\b', lambda m: lig(m[1]) if m[1] in ARGS else m[0], e(ca['fim']))
        tipicas += f'<div class="cadeia"><h3>{e(ca["n"])}</h3>{elos(ca["cods"])}<p style="margin:.6rem 0 0;font-size:.95rem">Costuma terminar em: {rot}</p></div>'
    corpo = cabeca('<a href="./">Início</a>', 'Mapa de conexões', 'Quem perde um argumento indireto costuma recuar para um direto, e vice-versa. Conhecer a cadeia ajuda a antecipar a próxima objeção.') + f'''<section class="secao" id="raizes"><div class="wrap"><div class="sec-cab"><h2>As três raízes</h2><p>Quase toda cadeia de objeções, quando esgotada, termina em uma destas três. As demais funcionam como camadas de proteção: responda à camada, mas mire a raiz.</p></div><div class="raizes">{"".join(cartao(ARGS[c]) for c in RAIZES)}</div></div></section>
<section class="secao areia"><div class="wrap estreito"><div class="sec-cab"><h2>As duas cadeias mais comuns</h2></div>{cads}</div></section>
<section class="secao"><div class="wrap estreito"><div class="sec-cab"><h2>Cadeias típicas</h2><p>Passe o mouse sobre um código para ver a frase, ou clique para abrir a resposta.</p></div>{tipicas}</div></section>
<section class="secao areia"><div class="wrap estreito artigo"><h2>Natural, normal, necessário e gostoso</h2><p>As famílias se encaixam nos "4Ns" de Piazza e colegas (2015), as quatro racionalizações mais comuns do consumo de carne: <strong>natural</strong> (<a href="familias/c.html">família C</a>), <strong>normal</strong> (<a href="familias/d.html">D</a> e <a href="familias/e.html">E</a>), <strong>necessário</strong> (<a href="familias/g.html">G</a>, <a href="familias/h.html">H</a> e <a href="familias/j.html">J</a>) e <strong>gostoso</strong> (<a href="argumentos/j11.html">J11</a>).</p></div></section>'''
    page('mapa.html', 'Mapa de conexões', L('Como as objeções ao veganismo se encadeiam, as três raízes onde quase toda conversa termina e as sequências mais comuns de argumentos.', 'How objections to veganism chain together, the three roots where almost every conversation ends and the most common sequences of arguments.'), corpo, 'mapa.html')

def cena(c, f, frase, abaixo):
    return f'<section class="cena" style="--c:{f["cor"]}"><div class="wrap"><p class="trilha"><a href="../">Início</a> / <a href="../familias/{f["c"].lower()}.html">{f["c"]}. {e(f["nome"])}</a> / Parte {f["parte"]}</p><div class="fala"><span class="selo-c">{c}</span><h1>"{e(frase)}"</h1></div>{abaixo}</div></section>'

def barra_leitura(c, title):
    """Barra de ações do capítulo (ouvir em pt-BR, como citar, imprimir ou PDF), como no Política Para Iniciantes. O JS está em assets/app.js."""
    ano, url = ATUALIZADO[:4], f'{SITE}/argumentos/{c.lower()}.html'
    abnt = L(f'{NOME.upper()}. {e(title)}. BiblioVerse, {ano}. Disponível em: {url}. Acesso em: {{ACESSO}}.',
             f'{NOME}. &quot;{e(title)}.&quot; <em>BiblioVerse</em>, {ano}, {url}. Accessed {{ACESSO}}.')  # em inglês, MLA no lugar da ABNT
    apa = f'{NOME}. ({ano}). <em>{e(title)}</em>. BiblioVerse. {url}'
    return (f'<div class="acoes-cap" data-abnt="{e(abnt)}" data-apa="{e(apa)}">'
            '<button type="button" data-acao="ouvir" aria-pressed="false"><span aria-hidden="true">▶</span> Ouvir</button>'
            '<button type="button" data-acao="citar"><span aria-hidden="true">❝</span> Como citar</button>'
            '<button type="button" data-acao="imprimir"><span aria-hidden="true">⎙</span> Imprimir ou PDF</button></div>')

def pagina_capitulo(c, ant, prox):
    a = ARGS[c]; f = FAMILIAS[a['fam']]
    tese, notas, abas = capitulo(c)
    abaixo = f'<div class="tese-c"><span>A resposta em uma frase</span><p>{tese}</p></div>' + ''.join(f'<p class="notas">{n}</p>' for n in notas)
    if f['parte'] == 'IND': abaixo = aviso_ind(f['c'], 'Antes de responder: argumento indireto') + abaixo
    abaixo += barra_leitura(c, L(f'{c}. "{a["frase"].rstrip(".")}"', f"{c}. ‘{a['frase'].rstrip('.')}’"))
    tabs = ''.join(f'<button type="button" role="tab" id="tab-{i}" aria-controls="p-{i}" aria-selected="{"true" if not n else "false"}"><b>{e(t)}</b><small>{e(s)}</small></button>' for n, (i, t, s, _) in enumerate(abas))
    pans = ''.join(f'<div class="painel" role="tabpanel" id="p-{i}" aria-labelledby="tab-{i}">{h}</div>' for i, _, _, h in abas)
    pag = cena(c, f, a['frase'], abaixo) + f'<div class="abas-w"><div class="wrap"><div class="abas" role="tablist" aria-label="Partes do capítulo">{tabs}</div></div></div><div class="wrap paineis" style="--c:{f["cor"]}">{pans}{passos(ant, prox)}</div>'
    page(f'argumentos/{a["slug"]}.html', f'{c}: {a["frase"]}', re.sub('<[^>]+>', '', tese), pag, TODOS, 'Article', [('Argumentos', TODOS)])

def passos(ant, prox):
    p = lambda c, r: f'<a href="{ARGS[c]["slug"]}.html"><small>{r}</small>{c}. {e(ARGS[c]["frase"])}</a>'
    return '<nav class="pass" aria-label="Outros argumentos">' + (p(ant, 'Anterior') if ant else '') + (p(prox, 'Próximo') if prox else '') + '</nav>'

def pagina_verbete(c, ant, prox):
    a = ARGS[c]; f = FAMILIAS[a['fam']]
    fal = [x for x in FALACIAS if c in x['cods']]; vie = [x for x in VIESES if c in x['cods']]
    cad = [ca for ca in CADEIAS if c in ca['cods']]
    abaixo = f'<div class="tese-c"><span>A falha principal</span><p>{e(a["falha"])}</p></div>'
    corpo = '<h2>Como pode aparecer</h2><div class="baloes">' + ''.join(f'<figure class="balao"><blockquote>"{e(x)}"</blockquote></figure>' for x in a['formas']) + '</div>'
    if f['parte'] == 'IND': corpo += '<div class="retorno"><span>Devolva à questão moral</span><p>Mesmo se fosse verdadeiro, este argumento indireto justificaria no máximo exceções. Os interesses dos animais contam?</p></div>'
    if fal or vie:
        corpo += '<h2>Erros e vieses ligados</h2><div class="grade-v">' + ''.join(f'<a class="cartao vies" href="../{p}.html#{slug(x["n"])}"><span class="cod">{r}</span><h4>{e(x["n"])}</h4><p>{e(x["d"])}</p></a>' for ls, p, r in ((fal, 'falacias', 'Falácia'), (vie, 'vieses', 'Viés')) for x in ls) + '</div>'
    if cad:
        corpo += '<h2>Em que conversa aparece</h2>' + ''.join(f'<div class="cadeia"><h3>Cadeia {e(ca["n"].lower())}</h3>{elos(ca["cods"], pre="../", atual=c)}</div>' for ca in cad)
    corpo += f'<p class="aviso">O capítulo completo deste argumento ainda está em preparação. {L("Veja a", "See")} <a href="../familias/{f["c"].lower()}.html">{L("família", "family")} {f["c"]}</a>: {e(f["perg"])}</p>'
    pag = cena(c, f, a['frase'], abaixo) + f'<div class="wrap paineis" style="--c:{f["cor"]}">{corpo}{passos(ant, prox)}</div>'
    page(f'argumentos/{a["slug"]}.html', f'{c}: {a["frase"]}', L(f'Como responder a "{a["frase"]}" {a["falha"]}.', f'How to answer "{a["frase"]}" {a["falha"]}.'), pag, TODOS, 'WebPage', [('Argumentos', TODOS)])

def secao_cap(c, n, fonte=None):
    """Nós de uma seção (número n) de um capítulo."""
    out, dentro = [], False
    for no in (fonte or CAPS)[c]:
        if no.tag == 'paragraph' and no.get('heading') == '2':
            dentro = texto(no).startswith(f'{n}.')
            continue
        if dentro: out.append(no)
    return out

def grafo():
    """Para onde a conversa vai depois de cada objeção: conexões dos capítulos e cadeias do catálogo."""
    arestas = {}
    def liga_(a, b, porque):
        if a in ARGS and b in ARGS and a != b: arestas.setdefault(a, {}).setdefault(b, porque)
    for c in CAPS_PT:
        for t in secao_cap(c, 6, CAPS_PT):
            if t.tag != 'table': continue
            for r in t.findall('row')[1:]:
                cels = [texto(x) for x in r.findall('cell')]
                if len(cels) < 3: continue
                for x in codigos(cels[1]):
                    if cels[0].startswith('Vem depois'): liga_(c, x, cels[2])
                    elif cels[0].startswith('Vem antes'): liga_(x, c, cels[2])
    for ca in CADEIAS:
        cs = ca['cods'] + [x for x in codigos(ca['fim']) if x not in ca['cods']]
        for a, b in zip(cs, cs[1:]): liga_(a, b, f'Cadeia {ca["n"].lower()}')
    for a, vai in DEPOIS.items():
        for b, porque in vai: liga_(a, UNIDOS[b][0] if b in UNIDOS else b, porque)
    for n, _, cs in CADEIAS_LONGAS:
        cs = cs + ['A10'] if cs[-1] != 'A10' else cs
        for a, b in zip(cs, cs[1:]): liga_(a, b, n)
    for chave, porque in MOTIVOS.items():
        x, y = chave.split('>')
        if y in arestas.get(x, {}): arestas[x][y] = porque
    if EN:
        for vai in arestas.values():
            for y in vai: vai[y] = en.motivo(vai[y])
    return arestas

def curta(c):
    if c not in CAPS: return ARGS[c]['falha']
    ps = [re.sub(r'\s+', ' ', texto(no)) for no in secao_cap(c, 4) if no.tag == 'paragraph' and not texto(no).startswith(('Pergunta de retorno', 'Question to ask back'))]
    return ' '.join(ps)

def raciocinio():
    G = grafo()
    entra = {}
    for a, bs in G.items():
        for b in bs: entra[b] = entra.get(b, 0) + 1
    nos = sorted(set(G) | set(entra), key=ORDEM.index)
    dados_ = {c: dict(f=ARGS[c]['frase'], r=curta(c), u=f'argumentos/{ARGS[c]["slug"]}.html', cor=FAMILIAS[ARGS[c]['fam']]['cor'], cap=c in CAPS, raiz=c in RAIZES, p=[[b, m] for b, m in G.get(c, {}).items()]) for c in nos}
    inicios = [c for c in ('C1', 'G1', 'B1', 'A1', 'H1', 'K1', 'D1', 'L1', 'F1', 'J9', 'E1') if c in dados_]
    js = json.dumps(dict(n=dados_, raizes=RAIZES), ensure_ascii=False).replace('</', '<\\/')
    opcoes = ''.join(f'<option value="{c}">{c}. {e(ARGS[c]["frase"])}</option>' for c in nos)
    chips = ''.join(f'<button type="button" class="chip" data-ini="{c}" style="--c:{FAMILIAS[c[0]]["cor"]}">{c}. {e(ARGS[c]["frase"])}</button>' for c in inicios)
    lista = ''
    for c in nos:
        vai = G.get(c, {})
        if not vai: continue
        itens = ''.join(f'<li><a href="argumentos/{b.lower()}.html"><b>{b}</b> {e(ARGS[b]["frase"])}</a><small>{e(m)}</small></li>' for b, m in vai.items())
        lista += f'<div class="rac-item" style="--c:{FAMILIAS[c[0]]["cor"]}"><h3><a href="argumentos/{c.lower()}.html"><span class="cod">{c}</span> {e(ARGS[c]["frase"])}</a></h3><ul>{itens}</ul></div>'
    n_ar = sum(len(v) for v in G.values())
    corpo = cabeca('<a href="./">Início</a>', 'O raciocínio antivegano', 'Quando uma objeção é respondida, raramente a conversa termina: ela pula para outra. Escolha um argumento, veja a resposta e siga para onde o debate costuma ir depois, até chegar a uma das raízes.') + f'''<section class="secao"><div class="wrap">
<div class="rac-topo"><p class="rac-num"><b>{len(nos)}</b> argumentos conectados por <b>{n_ar}</b> caminhos, a partir das cadeias do catálogo, das conexões de cada capítulo e de um mapeamento editorial deste guia.</p>
<div class="filtros"><label class="so-leitor" for="rac-sel">Começar por</label><select id="rac-sel" class="sel"><option value="">Escolha o argumento que você ouviu…</option>{opcoes}</select></div>
<p class="ti">Ou comece por uma abertura comum</p><div class="filtros rac-ini">{chips}</div></div>
<div id="rac" class="rac" hidden><ol class="rac-trilha" id="rac-trilha" aria-label="Caminho percorrido"></ol>
<div class="rac-cartao" id="rac-atual"></div>
<div class="rac-bot"><button type="button" class="btn alt peq" id="rac-volta">← Voltar um passo</button><button type="button" class="btn alt peq" id="rac-zera">Recomeçar</button></div></div>
<script type="application/json" id="rac-dados">{js}</script>
<div class="sec-cab" style="margin-top:46px"><h2>Todas as conexões</h2><p>Cada argumento e os caminhos que a conversa costuma tomar depois que ele é respondido. As raízes A10, J11 e E12 são onde quase tudo termina; o <a href="mapa.html">mapa de conexões</a> mostra as cadeias completas.</p></div>
<div class="rac-lista">{lista}</div></div></section>'''
    page('raciocinio.html', 'O raciocínio antivegano', L('Para onde vai cada argumento antivegano depois de respondido: um guia interativo das conexões entre as objeções, até as três raízes onde quase toda conversa termina.', 'Where each anti-vegan argument goes once it is answered: an interactive guide to the connections between objections, down to the three roots where almost every conversation ends.'), corpo, 'raciocinio.html')

def sobre():
    n_cap = len(set(CAPS) & set(ARGS))
    CONTEM = L(f'<p>Mais de {len(ARGS) // 100 * 100} argumentos estão catalogados, cada um com suas formas comuns e sua falha principal, e {"todos têm" if n_cap >= len(ARGS) else f"{n_cap} têm"} capítulo completo: a resposta curta, a desmontagem passo a passo, os erros e vieses, os testes de coerência e as conexões com os outros argumentos. O guia também traz {len(RUINS)} argumentos ruins que veganos deveriam abandonar e uma seção sobre o que vai além do veganismo, baseados no livro <em>Veganismo Baseado em Evidências</em>.</p>',
               f'<p>More than {len(ARGS) // 100 * 100} arguments are catalogued, each with its common wordings and its main flaw, and {"every one has" if n_cap >= len(ARGS) else f"{n_cap} have"} a full chapter: the short answer, the step-by-step rebuttal, the errors and biases, the consistency tests and the connections to other arguments. The guide also includes {len(RUINS)} weak arguments vegans should drop and a section on what goes beyond veganism, based in part on the book <em>Veganismo Baseado em Evidências</em> (Evidence-Based Veganism, in Portuguese).</p>')
    corpo = cabeca('<a href="./">Início</a>', 'Sobre o guia', e(DESCRICAO)) + f'''<section class="secao"><div class="wrap estreito artigo"><h2>O projeto</h2><p>O Guia de Argumentação Pelos Animais foi lançado em novembro de 2026 pelo ativista Julio Cesar Prava. O objetivo é mapear todos os argumentos usados para justificar a exploração animal e o especismo, e ajudar veganos e não veganos a melhorar o debate: conhecer a versão mais forte de cada objeção, onde ela falha, o que ela acerta e para onde a conversa costuma ir depois.</p><h2>A abordagem</h2><p>O guia segue a tradição da filosofia analítica e da epistemologia: busca clareza nos conceitos, argumentos válidos e premissas apoiadas em evidência. A ética que o orienta é baseada na senciência, o <a href="https://pt.wikipedia.org/wiki/Sencientismo" target="_blank" rel="noopener">sencientismo</a>: importa moralmente quem pode ter experiências boas ou ruins, seja qual for a espécie. O guia também mostra que ideias como razão e justiça não devem ser instrumentalizadas em benefício próprio.</p><p>Os argumentos de saúde, ambiente e economia aparecem como correção de fatos, e não como justificativa moral: o guia segue a crítica de muitos ativistas ao uso de argumentos indiretos, que desviam do respeito aos animais (<a href=\"comece-aqui.html#indiretos\">entenda</a>).</p><h2>O que o guia contém</h2>{CONTEM}
<h2>Sobre as fontes</h2><p>Afirmações empíricas precisam de fonte. Os links nas referências levam às fontes conferidas na redação. Quando uma tabela indica "fonte ainda não conferida", a referência existe, mas ainda não foi checada no original.</p>
<h2>Sobre o tom</h2><p>O guia discute argumentos, não pessoas. Apresenta a versão mais forte de cada objeção e diz o que ela acerta, porque só assim a resposta vale alguma coisa. Quando compara a estrutura lógica de argumentos, não está equiparando vítimas nem sofrimentos históricos.</p>
<h2>Privacidade</h2><p>Este site não pede cadastro e não usa cookies próprios. Ele carrega as fontes do Google Fonts e a barra de navegação da BiblioVerse.</p><p>Parte da <a href="https://biblioverse.org">BiblioVerse</a>.</p></div></section>'''
    page('sobre.html', 'Sobre o guia', L('O que é o guia de argumentação para defensores dos animais, o que já está pronto, como as fontes são tratadas e qual é o tom adotado.', 'What the argument guide for animal advocates is, what is ready, how sources are handled and what tone it takes.'), corpo, 'sobre.html')

def pagina_biblioteca():
    """Livros e sites para aprender a argumentar pelos animais, um card por livro (dados em tools/biblioteca.py)."""
    tons = list(CORES.values())
    cards = ''
    for i, b in enumerate(sorted(biblioteca.LIVROS, key=lambda x: x['t'].casefold())):  # ordem alfabética
        meta = ' · '.join(x for x in (b['a'], str(b['ano']), b['ed']) if x)
        st = f'<p class="bib-st">{e(b["st"])}</p>' if b['st'] else ''
        cards += (f'<article class="bib-card" style="--c:{tons[i % len(tons)]}" data-foco="{b["foco"]}" data-lingua="{b["lingua"]}">'
                  f'<div class="bib-capa"><span class="bib-lingua">{b["lingua"]}</span><h3>{e(b["t"])}</h3>{st}</div>'
                  f'<div class="bib-corpo"><p class="bib-meta">{e(meta)}</p><p class="bib-foco">{e(biblioteca.FOCOS[b["foco"]])}</p><p>{e(b["d"])}</p>'
                  + (f'<a class="btn peq" href="{e(b["u"])}" {EXT}>{e(b["ul"])} ↗</a>' if b['u'] else '<span class="selo">Link em breve</span>') + '</div></article>')
    chips = ''.join(f'<button class="chip" type="button" data-g="foco" data-v="{v}" aria-pressed="{"true" if not v else "false"}">{e(t)}</button>' for v, t in [('', 'Todos')] + list(biblioteca.FOCOS.items()))
    chips += ''.join(f'<button class="chip" type="button" data-g="lingua" data-v="{v}" aria-pressed="{"true" if not v else "false"}">{t}</button>' for v, t in (('', 'Qualquer idioma'), ('PT', 'Em português'), ('EN', 'Em inglês')))
    sites = ''.join(f'<a class="bib-site" href="{e(u)}" {EXT}><b>{e(n)}</b><span>{e(d)}</span></a>' for n, d, u in sorted(biblioteca.SITES, key=lambda x: x[0].casefold()))
    orgs = ''.join(f'<a class="bib-site" href="{e(u)}" {EXT}><b>{e(n)}</b><span>{e(d)}</span></a>' for n, d, u in sorted(biblioteca.ORGS, key=lambda x: x[0].casefold()))
    corpo = cabeca('<a href="./">Início</a>', 'Biblioteca', 'Livros para aprender a argumentar pelos animais: respostas às objeções mais comuns, os fundamentos éticos e a psicologia que sustenta o hábito de comer animais.') + f'''<section class="secao"><div class="wrap">
<div class="filtros bib-filtros">{chips}<span id="bib-n" aria-live="polite">{len(biblioteca.LIVROS)} {L("livros", "books")}</span></div>
<div class="bib-grade">{cards}</div>
<h2 style="margin-top:40px">Sites e projetos</h2><div class="bib-sites">{sites}</div>
<h2 style="margin-top:40px">Organizações</h2><div class="bib-sites">{orgs}</div>
<p class="fino" style="margin-top:22px">A lista partiu da seleção da <a href="https://vegpedia.com/2024/07/24/livros-e-sites-para-aprender-a-argumentar-a-favor-dos-animais" {EXT}>Vegpedia</a> e foi completada com outros livros focados em rebater argumentos antiveganos e especistas. Cada título foi conferido em catálogo, editora ou resenha.</p>
</div></section>'''
    page('biblioteca.html', 'Biblioteca', L('Livros e sites para aprender a argumentar pelos animais e rebater argumentos antiveganos e especistas, em português e em inglês.', 'Books and websites for learning to argue for animals and answer anti-vegan and speciesist arguments, in English and Portuguese.'), corpo, 'biblioteca.html', 'CollectionPage')

GLOS_GUIA = {  # termo (em português, sem acento e em minúsculas) -> páginas do guia que o aprofundam
    'liberalismo': 'politicas/liberalismo.html', 'libertarianismo': 'politicas/libertarianismo.html', 'anarquismo': 'politicas/anarquismo.html', 'anarquismo verde': 'politicas/anarquismo.html',
    'socialismo': 'politicas/marxismo.html', 'utilitarismo': 'politicas/utilitarismo.html', 'utilitarismo classico': 'politicas/utilitarismo.html', 'contratualismo': 'politicas/contratualismo.html',
    'deontologia': 'politicas/deontologia.html', 'etica do cuidado': 'politicas/cuidado.html', 'etica das virtudes': 'politicas/virtudes.html', 'ecofeminismo': 'politicas/feminismo.html',
    'veganismo feminista': 'politicas/feminismo.html', 'altruismo eficaz': 'politicas/altruismo-eficaz.html', 'ambientalismo (moral)': 'politicas/ambientalismo.html', 'ecologismo': 'politicas/ambientalismo.html',
    'pragmatismo': 'politicas/pragmatismo.html', 'igualitarismo': 'politicas/igualitarismo.html', 'antiespecismo': 'alem/antiespecismo.html', 'especismo': 'alem/antiespecismo.html',
    'sencientismo': 'alem/antiespecismo.html', 'antropocentrismo': 'alem/antiespecismo.html', 'biocentrismo': 'alem/antiespecismo.html', 'ecocentrismo': 'alem/antiespecismo.html',
    'biologia do bem-estar': 'alem/animais-selvagens.html', 'senciencia em ia e sistemas digitais': 'alem/ia-e-robos.html', 'senciencia em robos': 'alem/ia-e-robos.html',
    'senciencia em vida extraterrestre': 'alem/extraterrestres.html', 'abolicionismo': 'alem/correntes-do-veganismo.html', 'veganismo abolicionista': 'alem/correntes-do-veganismo.html',
    'bem-estarismo': 'alem/correntes-do-veganismo.html', 'novo bem-estarismo (neo-welfarism)': 'alem/correntes-do-veganismo.html', 'veganismo pragmatico': 'alem/correntes-do-veganismo.html',
    'veganismo interseccional': 'alem/correntes-do-veganismo.html', 'interseccionalidade': 'alem/correntes-do-veganismo.html', 'libertacao total': 'alem/correntes-do-veganismo.html',
    'antiveganismo': 'raciocinio.html', 'comoditizacao (ou comodificacao)': 'politicas/marxismo.html', 'pseudociencia': 'falacias.html',
}
GLOS_GUIA_ROTULO = {'politicas': ('Objeção política', 'Political objection'), 'alem': ('Além do veganismo', 'Beyond veganism'), 'raciocinio.html': ('O raciocínio antivegano', 'The anti-vegan line of reasoning'),
                    'falacias.html': ('Falácias', 'Fallacies')}

def pagina_glossario():
    """Glossário em uma página só (dados em data/glossario.md e data/novos/glossario_extra.json, lidos por tools/glossario.py).
    Tem busca, filtro por tema, A–Z, remissivas entre verbetes, links para as páginas do guia que aprofundam o termo e DefinedTermSet para os buscadores."""
    import glossario, unicodedata
    if EN: glossario.traduz()
    norm = lambda t: unicodedata.normalize('NFD', t.lower()).encode('ascii', 'ignore').decode()
    inicial = lambda t: (unicodedata.normalize('NFD', t[0].upper()).encode('ascii', 'ignore').decode() or '#')
    secoes = dict(glossario.SECOES)
    # junta verbetes repetidos (mesmo termo em duas seções): ficam com a definição mais completa e aparecem nos dois temas
    vs = []
    for v in glossario.VERBETES:
        outro = next((x for x in vs if x['pt'].lower() == v['pt'].lower()), None)
        if outro:
            outro['secs'].append(v['sec'])
            if len(v['def']) > len(outro['def']): outro['def'], outro['com'], outro['links'] = v['def'], v['com'], v['links'] or outro['links']
        else: vs.append(dict(v, secs=[v['sec']]))
    usados = set()
    for v in vs:
        sl = slug(v['termo']) or 'termo'
        while sl in usados: sl += '-2'
        usados.add(sl); v['slug'] = sl
    # remissivas: termos citados nas definições viram links (até 4 por verbete, só a primeira ocorrência, termos de 6 letras ou mais)
    alvos = sorted((v for v in vs if len(v['termo']) >= 6 and '(' not in v['termo'] and '/' not in v['termo']), key=lambda v: -len(v['termo']))
    padrao = re.compile(r'(?<![\w-])(' + '|'.join(re.escape(v['termo']) for v in alvos) + r')(?![\w-])', re.I) if alvos else None
    por_termo = {v['termo'].lower(): v for v in vs}
    em = lambda t: re.sub(r'\*([^*]+)\*', r'<em>\1</em>', e(t))
    def liga_termos(texto, proprio):
        if not padrao: return em(texto)
        out, pos, feitos, n = '', 0, set(), 0
        for m in padrao.finditer(texto):
            v = por_termo[m[1].lower()]
            if v is proprio or v['slug'] in feitos or n >= 4: continue
            out += em(texto[pos:m.start()]) + f'<a class="glos-ref" href="#{v["slug"]}">{e(m[1])}</a>'
            pos = m.end(); feitos.add(v['slug']); n += 1
        return out + em(texto[pos:])
    # páginas do guia: mapa fixo (GLOS_GUIA) e, para vieses e falácias, correspondência pelo nome
    ancoras_v = {slug(i['n']) for i in VIESES}; ancoras_f = {slug(i['n']) for i in FALACIAS}
    def guia(v):
        t = norm(v['pt']); os_ = []
        alvo = GLOS_GUIA.get(t)
        if alvo:
            ch = alvo.split('/')[0] if '/' in alvo else alvo
            rot = GLOS_GUIA_ROTULO.get(ch, ('No guia', 'In the guide'))[1 if EN else 0]
            os_.append((rot, alvo))
        base = re.sub(r'\s*\(.*?\)', '', v['pt']).strip()
        for dic, pag, ancoras in ((en.VIESES, 'vieses', ancoras_v), (en.FALACIAS, 'falacias', ancoras_f)):
            for nome, val in dic.items():
                if norm(re.sub(r'\s*\(.*?\)', '', nome)) == norm(base):
                    sl = slug(val[0] if EN else nome)
                    if sl in ancoras: os_.append((L('Vieses', 'Biases') if pag == 'vieses' else L('Falácias', 'Fallacies'), f'{pag}.html#{sl}'))
        return os_
    itens, letras = '', []
    for v in vs:
        l = inicial(v['termo'])
        if l not in letras:
            if letras: itens += '</div>'
            letras.append(l); itens += f'<div class="glos-letra" id="letra-{l}"><h2>{l}<a class="glos-topo" href="#glos-az" title="{L("Voltar ao A–Z", "Back to A–Z")}">↑ A–Z</a></h2>'
        links = ''.join(f'<li><a href="{e(u)}" {EXT}>{e(re.sub(r"^https?://(www\.)?", "", u).split("/")[0])}</a></li>' for u in v['links'])
        noguia = ''.join(f'<a class="glos-guia" href="{u}">{e(r)} →</a>' for r, u in guia(v))
        temas = ' · '.join(e(secoes[x]) for x in v['secs'])
        itens += (f'<article class="glos-item" id="{v["slug"]}" data-sec="{" ".join(str(x) for x in v["secs"])}"><h3><a href="#{v["slug"]}">{e(v["termo"])}</a></h3><p class="glos-def">{liga_termos(v["def"][:1].upper() + v["def"][1:], v)}</p>'
                  + (f'<p class="glos-com">{liga_termos(v["com"], v)}</p>' if v['com'] else '') + (f'<ul class="glos-links">{links}</ul>' if links else '')
                  + (f'<p class="glos-no-guia">{noguia}</p>' if noguia else '') + f'<p class="glos-sec">{temas}</p></article>')
    itens += '</div>'
    cont = collections.Counter(x for v in vs for x in v['secs'])
    opt = lambda n, t: f'<option value="{n}">{e(t)} ({cont[n]})</option>'
    ops = (f'<optgroup label="{L("Conceitos, teorias e práticas", "Concepts, theories and practices")}">' + ''.join(opt(n, t) for n, t in glossario.SECOES if n not in (9, 10)) + '</optgroup>'
           + f'<optgroup label="{L("Ingredientes e produtos", "Ingredients and products")}">' + ''.join(opt(n, t) for n, t in glossario.SECOES if n in (9, 10)) + '</optgroup>')
    az = ''.join(f'<a href="#letra-{l}">{l}</a>' for l in letras)
    ld = json.dumps({'@context': 'https://schema.org', '@type': 'DefinedTermSet', 'name': L('Glossário de ética animal e veganismo', 'Glossary of animal ethics and veganism'), 'inLanguage': 'en' if EN else 'pt-BR',
                     'url': f'{SITE}/{"glossary" if EN else "glossario"}.html', 'hasDefinedTerm': [{'@type': 'DefinedTerm', 'name': v['termo'], 'url': f'{SITE}/{"glossary" if EN else "glossario"}.html#{v["slug"]}'} for v in vs]},
                    ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
    corpo = cabeca('<a href="./">Início</a>', L('Glossário', 'Glossary'), L(f'{len(vs)} termos da ética animal, do veganismo e do debate sobre a exploração dos animais, em ordem alfabética. Procure pelo termo ou filtre por tema.', f'{len(vs)} terms from animal ethics, veganism and the debate on animal exploitation, in alphabetical order. Search for a term or filter by topic.')) + f"""<section class="secao"><div class="wrap estreito">
<div class="filtros glos-filtros"><input id="gq" type="search" placeholder="{L("Procurar um termo ou uma ideia", "Search for a term or an idea")}" aria-label="{L("Procurar no glossário", "Search the glossary")}" autocomplete="off"/><label class="so-leitor" for="gs">{L("Tema", "Topic")}</label><select id="gs" class="sel"><option value="">{L("Todos os temas", "All topics")}</option>{ops}</select><span id="gn" aria-live="polite">{len(vs)} {L("termos", "terms")}</span></div>
<nav class="glos-az" id="glos-az" aria-label="{L("Ir para a letra", "Jump to letter")}">{az}</nav>
<div id="glos">{itens}</div>
<p id="gvazio" class="fino" hidden>{L("Nenhum termo encontrado. Tente outra palavra ou escolha 'Todos os temas'.", "No terms found. Try another word or choose 'All topics'.")}</p>
<p class="fino" style="margin-top:26px">{L("Base: rascunho do Dicionário-Guia de Ética e Defesa Animal, da Vegpedia, revisto para este guia. As definições resumem o uso do termo, e o texto em itálico mostra o que ele significa para o debate sobre os animais. Termos citados em outras definições são links. Falta algum termo? Avise e ele entra.", "Based on the draft Dictionary-Guide to Animal Ethics and Advocacy from Vegpedia, revised for this guide. The definitions summarize how the term is used, and the italic text shows what it means for the debate about animals. Terms mentioned in other definitions are links. Missing a term? Let us know and it will be added.")}</p>
</div></section>
<script type="application/ld+json">{ld}</script>
<script>(function(){{var q=document.getElementById("gq"),s=document.getElementById("gs"),n=document.getElementById("gn"),v=document.getElementById("gvazio");
var itens=[].slice.call(document.querySelectorAll(".glos-item")),letras=[].slice.call(document.querySelectorAll(".glos-letra")),az=[].slice.call(document.querySelectorAll(".glos-az a"));
function norm(t){{return t.toLowerCase().normalize("NFD").replace(/[\\u0300-\\u036f]/g,"")}}
var txt=itens.map(function(i){{return norm(i.textContent)}});
function filtra(){{var t=norm(q.value.trim()),sec=s.value,c=0;
itens.forEach(function(i,k){{var ok=(!sec||(" "+i.dataset.sec+" ").indexOf(" "+sec+" ")>-1)&&(!t||txt[k].indexOf(t)>-1);i.hidden=!ok;if(ok)c++}});
letras.forEach(function(l,k){{var tem=!!l.querySelector(".glos-item:not([hidden])");l.hidden=!tem;az[k].classList.toggle("off",!tem)}});
n.textContent=c+(c===1?" {L("termo", "term")}":" {L("termos", "terms")}");v.hidden=c>0}}
q.addEventListener("input",filtra);s.addEventListener("change",filtra);
try{{var p=new URLSearchParams(location.search);if(p.get("q")){{q.value=p.get("q");filtra()}}}}catch(e){{}}
function irPara(){{var id=location.hash.slice(1),el=id&&document.getElementById(id);if(el&&el.hidden){{q.value="";s.value="";filtra();el.scrollIntoView()}}}}
window.addEventListener("hashchange",irPara);irPara();
}})();</script>"""
    page('glossario.html', L('Glossário', 'Glossary'), L(f'Glossário com {len(vs)} termos da ética animal, do veganismo e do antiespecismo, com busca e filtro por tema.', f'Glossary of {len(vs)} terms from animal ethics, veganism and antispeciesism, with search and a topic filter.'), corpo, 'glossario.html', 'CollectionPage')
    for v in vs: BUSCA.append(dict(t=v['termo'], s=L('Glossário: ', 'Glossary: ') + v['def'][:150], u=f'glossario.html#{v["slug"]}', k=secoes[v['secs'][0]]))

def nao_achou():
    corpo = cabeca('<a href="./">Início</a>', 'Página não encontrada', 'Tente a busca ou volte para a lista de argumentos.') + '<section class="secao"><div class="wrap"><a class="btn" href="index.html#argumentos">Ver os argumentos</a></div></section>'
    page('404.html', 'Página não encontrada', L('A página que você procurou não existe. Use a busca ou volte para a lista de argumentos do guia.', "The page you were looking for doesn't exist. Use the search or go back to the guide's list of arguments."), corpo)

# ---------- índice de vieses completo ----------
# Os 16 vieses do catálogo, mais os que os capítulos usam nas tabelas "Vieses". Cada entrada: nome, definição, outros nomes usados nos capítulos.
VIESES_EXTRA = [
    ('Racionalização pelos 4Ns', 'Justificar o consumo de animais dizendo que é natural, normal, necessário e gostoso (Piazza e colegas, 2015).', []),
    ('Busca de hipocrisia', 'Procurar uma incoerência em quem defende uma ideia para não precisar examinar a ideia.', []),
    ('Negação de mente', 'Atribuir menos mente e menos capacidade de sofrer aos animais que comemos.', ['Negação motivada de mente']),
    ('Depreciação de quem faz o bem', 'Diminuir quem age por razões morais, porque sua conduta é sentida como uma acusação.', []),
    ('Desvalorização reativa', 'Rejeitar uma proposta porque veio do lado adversário.', []),
    ('Efeito do mensageiro', 'Avaliar a mensagem por quem a diz, e não pelo que diz.', ['Ataque ao mensageiro']),
    ('Efeito manada e conformidade social', 'Adotar um hábito ou uma ideia porque muita gente em volta adota.', ['Efeito manada', 'Conformidade social']),
    ('Ignorância pluralista', 'Muitos discordam em privado, mas acham que todos os outros concordam.', []),
    ('Efeito do padrão', 'Ficar com a opção que já vem pronta, como o prato com carne.', ['Neutralidade aparente da norma']),
    ('Efeito da verdade ilusória e da mera exposição', 'O que se ouve muitas vezes parece verdadeiro, e o que é familiar parece melhor.', ['Efeito da verdade ilusória', 'Familiaridade']),
    ('Viés de omissão e viés do perpetrador', 'Julgar menos grave o dano que não causamos com as próprias mãos, ou que resulta de deixar de agir.', []),
    ('Viés teleológico e detecção de agente', 'Ver propósito e intenção na natureza: os animais "existiriam para" algo.', []),
    ('Desaparecimento da compaixão', 'Quanto mais vítimas, menos se sente por cada uma; uma vítima identificável comove mais que milhões.', ['Vítima identificável']),
    ('Aversão à perda e efeito dotação', 'Perder o que se tem pesa mais do que ganhar algo equivalente.', ['Aversão à perda']),
    ('Custo irrecuperável e justificação do esforço', 'Continuar porque já se investiu muito, e não porque vale a pena.', []),
    ('Retrospecção rosada', 'Lembrar o passado como melhor do que foi.', []),
    ('Excesso de confiança (Dunning-Kruger)', 'Quem sabe pouco sobre um tema tende a superestimar o que sabe.', []),
    ('Realismo ingênuo e ponto cego do viés', 'Achar que vemos o mundo como ele é e que só os outros são enviesados.', []),
    ('Pensamento antropocêntrico', 'Usar o humano como medida de tudo, inclusive do que conta como sentir.', ['Antropocentrismo']),
    ('Viés do natural', 'O que parece natural é avaliado como melhor e mais seguro.', []),
    ('Viés de disponibilidade', 'Julgar pela lembrança mais fácil, como o caso de um conhecido, e não pelos dados.', ['Heurística de disponibilidade']),
    ('Viés de autoridade', 'Aceitar uma afirmação pelo prestígio de quem a faz.', []),
    ('Viés do presente', 'Dar peso demais ao agora e de menos às consequências futuras.', ['Desconto do futuro']),
    ('Efeito halo', 'Uma qualidade boa, como "local" ou "orgânico", contamina o julgamento de todo o resto.', []),
    ('Orientação à dominância social', 'Preferir hierarquias entre grupos, inclusive entre espécies.', []),
    ('Essencialismo psicológico', 'Achar que cada tipo de ser tem uma essência fixa que define seu lugar.', []),
    ('Masculinidade e carne', 'Associar comer carne à virilidade, o que torna a mudança uma ameaça à identidade.', []),
    ('Estereótipo', 'Julgar alguém por uma imagem simplificada do grupo a que pertence.', ['Estereótipo e preconceito']),
    ('Dissociação e eufemismo', 'Separar o animal da comida, inclusive pelas palavras usadas.', ['Dissociação', 'Eufemismo e linguagem']),
    ('Falso consenso', 'Superestimar quantas pessoas pensam como nós.', []),
    ('Neofobia alimentar', 'Desconfiar de alimentos desconhecidos.', []),
    ('Efeito nocebo', 'A expectativa de que algo fará mal produz sintomas reais.', []),
    ('Viés de saliência', 'Dar peso ao que chama atenção, como a distância percorrida, e não ao que mais pesa.', []),
    ('Viés do meio-termo', 'Achar que a posição do meio é sempre a mais sensata.', []),
    ('Lacuna de empatia', 'Sentir menos empatia por um animal quanto mais distante ele é de nós na evolução.', []),
    ('Tamanhismo', 'Dar menos importância a um animal por ele ser pequeno.', []),
    ('Inteligentismo', 'Dar menos importância a um animal por ele ser considerado pouco inteligente.', []),
    ('Substratismo', 'Dar menos importância a um ser por causa do material de que ele é feito, como no caso de seres não orgânicos.', ['Carbonismo']),
    ('Viés de proporção', 'Julgar uma ajuda pela fração do problema que ela resolve, e não pelo número de indivíduos ajudados.', []),
    ('Hipótese do mundo justo', 'Acreditar que o mundo é justo e que, por isso, quem sofre recebe o que lhe cabe.', []),
    ('Negligência da probabilidade', 'Decidir sob incerteza sem pesar a probabilidade, tratando um risco como certo ou como inexistente.', []),
    ('Efeito de ambiguidade', 'Evitar opções cuja chance de dar certo é desconhecida, mesmo quando podem ser as melhores.', ['Aversão à ambiguidade']),
    ('Viés de avaliabilidade', 'Dar mais peso ao que é fácil de medir do que ao que mais importa.', ['Viés de avaliação']),
    ('Negligência da duração', 'Avaliar uma experiência pelos momentos marcantes e pelo fim, sem contar quanto tempo ela durou.', []),
    ('Viés pró-inovação', 'Superestimar o que uma inovação vai resolver e não ver seus limites.', []),
    ('Digitalização de crenças', 'Tratar uma probabilidade como se fosse zero ou um, em vez de levar a incerteza em conta.', []),
    ('Perseverança da crença', 'Manter uma crença mesmo depois de conhecer evidências contra ela.', ['Viés do conservadorismo', 'Conservadorismo das crenças', 'Reflexo de Semmelweis']),
    ('Efeito de influência contínua', 'Uma informação já corrigida continua a influenciar o que a pessoa pensa.', []),
    ('Viés de soma zero', 'Ver uma situação como disputa em que o ganho de um é a perda de outro, mesmo quando não é.', []),
    ('Cascata de disponibilidade', 'Uma ideia ganha crédito por ser muito repetida em público, e quanto mais crédito ganha, mais é repetida.', []),
    ('Correlação ilusória', 'Ver ligação entre duas coisas que só aconteceram juntas.', []),
    ('Efeito de enquadramento', 'A mesma informação leva a julgamentos diferentes conforme o modo como é apresentada.', []),
    ('Ilusão de profundidade explicativa', 'Achar que se entende como algo funciona bem melhor do que de fato se entende.', []),
]
ALIAS_CAT = {'Dissonância cognitiva (paradoxo da carne)': ['Paradoxo da carne', 'Dissonância cognitiva'], 'Viés de grupo (ingroup)': ['Viés de grupo', 'Identidade de grupo'],
             'Viés de otimismo e excepcionalismo': ['Viés de otimismo'], 'Heurística do afeto': ['Heurística afetiva'], 'Reatância psicológica': [], 'Viés do status quo': ['Viés de status quo'],
             'Cognição protetora da identidade': [], 'Insensibilidade à escala': [], 'Licença moral': [], 'Difusão de responsabilidade': [], 'Ignorância deliberada': []}

def completa_vieses():
    """Junta ao índice os vieses que aparecem nas tabelas dos capítulos, com os códigos de onde aparecem."""
    nomes_cap = {}
    for c in CAPS_PT:
        if c not in ARGS: continue
        for t in secao_cap(c, 9, CAPS_PT):
            if t.tag != 'table': continue
            for r in t.findall('row')[1:]:
                cel = r.findall('cell')
                if cel: nomes_cap.setdefault(re.sub(r'\s+', ' ', texto(cel[0])).strip().lower(), set()).add(c)
    def onde(*nomes):
        s = set()
        for n in nomes: s |= nomes_cap.get(n.lower(), set())
        return s
    for v in VIESES:
        extra = onde(v['n'], *ALIAS_CAT.get(v['n'], []))
        v['cods'] = [c for c in ORDEM if c in set(v['cods']) | extra]
    for n, d, apelidos in VIESES_EXTRA:
        cods = [c for c in ORDEM if c in onde(n, *apelidos)]
        if cods: VIESES.append(dict(n=n, d=d, aparece='', cods=cods))
completa_vieses()
if EN: en.aplica(globals())
# Frases dos argumentos sem ponto final, para a lista ficar uniforme (reticências, ? e ! continuam)
for _a in ARGS.values(): _a['frase'] = re.sub(r'(?<!\.)\.$', '', _a['frase'].strip())

# ---------- montagem ----------
inicio(); comece(); familias(); mapa(); raciocinio(); sobre(); nao_achou(); pagina_biblioteca(); pagina_glossario(); paginas_ruins(); paginas_alem(); paginas_politicas(); pagina_debate(); treino()
indice_erro('falacias.html', L('Falácias', 'Fallacies'), 'Falácia', L(f'{len(FALACIAS)} erros de lógica que explicam boa parte do catálogo. Clique em um código para ver como a falácia aparece no argumento.', f'{len(FALACIAS)} logical errors that explain much of the catalogue. Click a code to see how the fallacy shows up in the argument.'), FALACIAS, 'Em uma frase')
indice_erro('vieses.html', L('Vieses', 'Biases'), 'Viés', L(f'{len(VIESES)} mecanismos psicológicos que tornam esses argumentos convincentes, mesmo quando não se sustentam.', f'{len(VIESES)} psychological mechanisms that make these arguments convincing, even when they do not hold up.'), VIESES, 'Mecanismo')
for i, c in enumerate(ORDEM):
    ant = ORDEM[i - 1] if i else None
    prox = ORDEM[i + 1] if i + 1 < len(ORDEM) else None
    if c in CAPS: pagina_capitulo(c, ant, prox)
    else: pagina_verbete(c, ant, prox)
    a = ARGS[c]; BUSCA.append(dict(t=f'{c}. {a["frase"]}', s=a['falha'], u=f'argumentos/{a["slug"]}.html', k=' '.join(a['formas']) + ' ' + FAMILIAS[a['fam']]['nome']))
for r in RUINS: BUSCA.append(dict(t=f'{r["c"]}. {r["frase"]}', s='Argumento ruim de veganos: ' + r['por'][0], u=f'ruins/{r["c"].lower()}.html', k=TIPOS[r['tipo']][0]))
for p in alem.PAGINAS: BUSCA.append(dict(t=p['t'], s='Além do veganismo: ' + p['res'], u=f'alem/{p["s"]}.html', k=''))
for t in politicas.TEORIAS: BUSCA.append(dict(t=f'{t["t"]}: {t["frase"]}', s='Objeção política: ' + t['principio'], u=f'politicas/{t["s"]}.html', k='política teoria'))
for f in FAMILIAS.values(): BUSCA.append(dict(t=f'Família {f["c"]}: {f["nome"]}', s=f['perg'], u=f'familias/{f["c"].lower()}.html', k=''))
for i in FALACIAS: BUSCA.append(dict(t=i['n'], s='Falácia: ' + i['d'], u=f'falacias.html#{slug(i["n"])}', k=''))
for i in VIESES: BUSCA.append(dict(t=i['n'], s='Viés: ' + i['d'], u=f'vieses.html#{slug(i["n"])}', k=''))

def escreve(rel, txt):
    alvo = os.path.join(OUT, rel)
    os.makedirs(os.path.dirname(alvo), exist_ok=True)
    open(alvo, 'w', encoding='utf-8', newline='\n').write(txt)
if EN: en.copia_assets(os.path.join(ROOT, 'assets'), os.path.join(OUT, 'assets'))
_busca = nova_url(json.dumps(BUSCA, ensure_ascii=False, separators=(',', ':')))
_busca = json.loads(en.traduz_html(_busca) if EN else _busca)
# Cada item ganha a descrição (d) e as palavras do conteúdo (c) da página; páginas sem item próprio entram com título e descrição.
# A ordem dos resultados é decidida em assets/app.js: título, subtítulo, descrição e, por fim, conteúdo.
_cobertas = set()
for _b in _busca:
    _p, _ancora = (_b['u'].split('#') + [''])[:2]
    _info = INDICE.get(_p)
    if not _info: continue
    _b['d'] = '' if _ancora else _info['d']
    _b['c'] = '' if _ancora else _info['c']
    if not _ancora: _cobertas.add(_p)
for _p, _info in INDICE.items():
    if _p not in _cobertas: _busca.append(dict(t=_info['t'], s=_info['d'], u=_p, k='', d='', c=_info['c']))
escreve('assets/busca.json', json.dumps(_busca, ensure_ascii=False, separators=(',', ':')))
def redireciona(pasta, velho, novo):
    alvo = f'{SITE}/{pasta}/{novo}.html'
    escreve(f'{pasta}/{velho}.html', f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"/><title>Página movida</title><meta name="robots" content="noindex"/><link rel="canonical" href="{alvo}"/><meta http-equiv="refresh" content="0; url={novo}.html"/><script>location.replace("{novo}.html" + location.hash)</script></head><body><p><a href="{novo}.html">Esta página mudou de endereço.</a></p></body></html>\n')
if not EN:  # o site em inglês já nasce com os endereços legíveis
    for velho, novo in SLUG_ARG.items(): redireciona('argumentos', velho, novo)
    for velho, novo in SLUG_RUIM.items(): redireciona('ruins', velho, novo)
import icones; icones.gera(len(ARGS), os.path.join(OUT, 'assets'), 'en' if EN else 'pt')
escreve('assets/icon.svg', LOGO.replace('<svg ', '<svg xmlns="http://www.w3.org/2000/svg" ').replace(' aria-hidden="true"', '') + '\n')
escreve('manifest.webmanifest', json.dumps(dict(name=NOME, short_name=CURTO, start_url='/', display='standalone', background_color='#fcfaf5', theme_color='#0a3703', lang='en' if EN else 'pt-BR', icons=[dict(src='assets/icon.svg', sizes='any', type='image/svg+xml'), dict(src='assets/icon-192.png', sizes='192x192', type='image/png'), dict(src='assets/icon-512.png', sizes='512x512', type='image/png', purpose='any maskable')]), ensure_ascii=False, indent=1))
escreve('robots.txt', f'User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n')
def _alt(p):
    """Versões do mesmo conteúdo nos dois idiomas, também no sitemap (além do hreflang no head de cada página)."""
    if not BILINGUE or p in PT_ONLY: return ''
    u_pt, u_en = ALTERNA[p]
    return f'<xhtml:link rel="alternate" hreflang="pt-BR" href="{u_pt}"/><xhtml:link rel="alternate" hreflang="en" href="{u_en}"/><xhtml:link rel="alternate" hreflang="x-default" href="{u_pt}"/>'
urls = ''.join(f'\n<url><loc>{SITE}/{"" if p == "index.html" else p}</loc><lastmod>{LASTMOD.get(p, ATUALIZADO)}</lastmod>{_alt(p)}</url>' for p in PAGINAS if p != '404.html')
escreve('sitemap.xml', f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">{urls}\n</urlset>\n')
if EN:
    escreve('CNAME', 'fortheanimals.biblioverse.org\n'); escreve('.nojekyll', '')
    escreve('llms.txt', en.llms(SITE, NOME, DESCRICAO))
else: escreve('llms.txt', f'# {NOME}\n\n> {DESCRICAO}\n\n## Principais\n- [Comece aqui]({SITE}/comece-aqui.html)\n- [Todos os argumentos]({SITE}/#argumentos)\n- [Treinar respostas]({SITE}/treino.html)\n- [Debate simulado]({SITE}/debate.html)\n- [Argumentos ruins de veganos: pare de usar ou use melhor]({SITE}/argumentos-ruins.html)\n- [Além do veganismo]({SITE}/alem-do-veganismo.html)\n- [Famílias]({SITE}/familias.html)\n- [O raciocínio antivegano]({SITE}/raciocinio.html)\n- [Mapa de conexões]({SITE}/mapa.html)\n- [Falácias]({SITE}/falacias.html)\n- [Vieses]({SITE}/vieses.html)\n- [Glossário]({SITE}/glossario.html)\n')
print(len(PAGINAS), 'páginas geradas' if not EN else 'pages built in English')
if EN: en.relatorio(OUT)
