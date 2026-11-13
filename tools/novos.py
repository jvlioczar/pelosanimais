"""Argumentos acrescentados em 2026-11-13 (lotes 1 a 5). Lê data/novos/lote*.json (falha em português, versão em inglês e motivos
das conexões) e a frase de cada capítulo em data/capitulos_md/<código>.md. As outras formas em português ficam aqui."""
import glob, json, os, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FORMAS_PT = {
 'L17': ['Vocês também preferem cachorro a barata', 'Veganos também se sentem superiores aos outros animais', 'Vocês decidem pelos animais, isso também é se achar superior'],
 'L18': ['Você chora por um porco, mas não por um mosquito', 'Ninguém consegue sentir pena de bilhões'],
 'L19': ['Você não segue todas as causas na sua vida pessoal', 'Defende bicho e destrata gente', 'Vegano que vota em fulano não tem moral para falar'],
 'L20': ['A mídia vegana é exagerada', 'Isso é propaganda com musiquinha triste', 'Já desmentiram aquele documentário'],
 'L21': ['Para vegano, vegetariano é pior que quem come carne', 'Nem quem reduz escapa da patrulha', 'Vocês brigam mais entre si do que com a indústria'],
 'L22': ['Vocês desprezam quem resgata cães e gatos', 'Protetor que come carne não vale nada para vocês', 'Só vegano ama bicho?'],
 'L23': ['Choram pelo pintinho e apoiam matar bebês', 'Se a vida importa, por que não a do feto?', 'Se você é contra o aborto, deveria ser vegano'],
 'L24': ['Só implicam com o candomblé', 'Atacar o sacrifício religioso é racismo religioso'],
 'L25': ['Veganos são ateus', 'Veganos não gostam de cristãos nem de Jesus', 'Veganos não gostam de muçulmanos', 'Veganismo quer tomar o lugar da religião'],
 'L26': ['Veganos querem purificar o mundo', 'É uma moral contra a natureza humana', 'É coisa de quem precisa se sentir moralmente superior'],
 'C12': ['Achar que estamos fora do ciclo é ilusão', 'O que importa é participar do ciclo de forma consciente', 'Todo ser vivo se alimenta de outro'],
 'D13': ['Tenho que respeitar meus ancestrais', 'Recusar a comida da minha mãe é desrespeito', 'Minha família sempre viveu assim, quem sou eu para dizer que estavam errados?'],
 'E16': ['Perguntei ao ChatGPT e ele disse que comer carne é uma escolha pessoal', 'Até a inteligência artificial discorda de vocês', 'A IA é neutra, e ela não manda ninguém virar vegano'],
 'H15': ['O foco deve ser o sistema agrícola, e não a dieta', 'O que conta é o solo e o modelo de agricultura que você financia', 'Prefiro carne de um bom produtor a soja de monocultura'],
 'H16': ['Sistemas regenerativos e locais, com animais, é que cuidam da terra', 'Soberania alimentar pede animais integrados à lavoura', 'Um mundo vegano seria um deserto de soja'],
 'J19': ['Vocês querem acabar com o agro', 'Sem o agro, vocês não comem nem a sua salada', 'Vegano cospe no prato em que come'],
 'J20': ['Me sinto deslocado socialmente', 'Quero pertencer, e comer é uma das atividades do grupo', 'Não quero ser o diferente da mesa'],
 'J21': ['É só marketing para vender produto caro', 'Veganismo é nicho de mercado para quem tem dinheiro', 'As mesmas empresas de carne vendem o hambúrguer vegano'],
 'J22': ['3,2 bilhões de pessoas obtêm boa parte da proteína animal dos peixes', 'O mínimo que podemos fazer é garantir um abate rápido e sem sofrimento', 'Uma mensagem para os veganos sensíveis demais'],
 'M13': ['Sencientistas querem reduzir a biodiversidade', 'Sencientistas são a favor da perda de biodiversidade', 'Para vocês, tanto faz uma espécie se extinguir'],
 'M14': ['Vocês querem asfaltar a natureza para acabar com o sofrimento', 'Para acabar com a predação, só destruindo os ecossistemas', 'Isso é ecocídio com boas intenções'],
 'M15': ['Então uma formiga vale o mesmo que uma pessoa?', 'Vocês acham que uma barata vale o mesmo que o seu filho?', 'Se tudo importa igual, nada importa'],
 'M16': ['Então não posso tirar o carrapato do meu cachorro?', 'Para sencientista, matar mil vermes para salvar um bicho é crime', 'O parasita também é um animal, ou vocês escolhem quem merece?'],
 'L27': ['Já era difícil aguentar os veganos, agora tem sencientista', 'Sencientista é vegano que perdeu o juízo', 'Isso é veganismo levado ao delírio'],
 'N7': ['Saí por causa dos próprios veganos', 'O movimento é tóxico, cansei da patrulha', 'Não quero ser confundido com essa gente'],
 'N8': ['Não quero ser rotulado como nada', 'Quando eu dizia que era vegano, todo mundo me vigiava', 'Prefiro comer sem dar nome a isso'],
 'N9': ['Eu lia cada rótulo e nunca era suficiente', 'O veganismo acabou com a minha saúde mental', 'Cansei de carregar o peso do mundo'],
 'N10': ['Virei vegano por causa de um documentário de saúde e depois vi que não era bem assim', 'Era pelo meio ambiente, mas hoje compro carne local', 'Nunca foi pelos animais'],
}
PT, EN, MOTIVOS = [], {}, {}
_ordem = lambda c: (c[0], int(c[1:]))
_args = {}
for f in sorted(glob.glob(os.path.join(ROOT, 'data', 'novos', 'lote*.json'))):
    d = json.load(open(f, encoding='utf-8'))
    _args.update(d['args']); MOTIVOS.update(d['motivos'])
for c in sorted(_args, key=_ordem):
    frase = re.match(r'# \S+\. "(.*)"', open(os.path.join(ROOT, 'data', 'capitulos_md', c + '.md'), encoding='utf-8').readline())[1]
    PT.append((c, frase, FORMAS_PT[c], _args[c]['falha_pt']))
    e = _args[c]['en']; EN[c] = (e['frase'], e['formas'], e['falha'])
