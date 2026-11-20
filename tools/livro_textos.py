"""Textos editáveis do livro (tools/livro.py). Edite à vontade e rode de novo: python tools/livro.py
Parágrafos separados por linha em branco. Links no formato [texto](https://endereco), **negrito** e listas com linhas começando por "- ". Texto vazio ('') deixa a página com o marcador de "a preencher"."""

AUTOR = 'Julio Cesar Prava'
EDITORA = ''  # editora, se houver; vazio não aparece no livro

DEDICATORIA = '''A todos os seres sencientes inocentes que nascem na natureza selvagem para sofrer e logo morrer, a todos os que são postos no mundo para ser explorados e mortos, e a todos os que ainda virão e enfrentarão a fúria da natureza e da humanidade.'''

AGRADECIMENTOS = '''Agradeço a todas as pessoas que pensam e trabalham para ajudar os animais, principalmente àquelas que, postas diante de razões melhores, não têm medo de assumi-las e de deixar para trás aquilo em que acreditavam, para assim buscar o melhor mundo possível.'''

# Ficha catalográfica: deixe vazio para manter o quadro reservado; cole aqui o texto fornecido pela bibliotecária ou pelo bibliotecário.
FICHA = ''

SOBRE_AUTOR = """[Julio Cesar Prava](https://www.instagram.com/sencientista/) é designer gráfico e ativista pelos animais. Em 2017, fundou a [Vegpedia](https://vegpedia.com), para mapear o movimento vegano no Brasil e no mundo. Recentemente, lançou o Guia de Argumentação Pelos Animais."""

SOBRE_PROJETO = """O Guia de Argumentação Pelos Animais foi lançado em novembro de 2026 para mapear os argumentos usados para justificar a exploração animal e o especismo, e para ajudar veganos e não veganos a melhorar o debate: conhecer a versão mais forte de cada objeção, onde ela falha, o que ela acerta e para onde a conversa costuma ir depois.

**O projeto tem dois formatos: o site e este livro.** O livro reúne só o essencial de cada argumento: a frase, a falha principal, uma réplica e uma pergunta para devolver. O site é gratuito, mais completo e atualizado com frequência. Este livro registra o conteúdo como estava na data desta edição; ao acessar o site, você pode encontrar argumentos revistos e melhorados, num esforço contínuo e honesto de se aproximar cada vez mais da verdade. No site você encontra também:

- o capítulo completo de cada argumento: a versão mais forte, o que ele acerta, a desmontagem passo a passo, a melhor tréplica, os erros e vieses, as contradições e as fontes;
- o mapa de conexões entre os argumentos e o raciocínio antivegano passo a passo;
- um debate simulado e um treino com cartões para praticar as respostas;
- os argumentos que veganos deveriam parar de usar;
- as objeções políticas e éticas, teoria por teoria;
- a seção Além do veganismo, a biblioteca e o glossário;
- a versão em inglês, For the Animals.

O guia segue a filosofia analítica, com conceitos claros e premissas apoiadas em evidência, e o sencientismo: importa moralmente quem pode ter experiências boas ou ruins, seja qual for a espécie."""

CONTRACAPA = """Toda objeção merece uma boa resposta.

Este livro reúne {n} argumentos usados contra o veganismo e o antiespecismo, um por página: a frase como ela costuma ser dita, a falha principal, uma réplica para usar na hora e uma pergunta para manter a conversa aberta.

Aqui as respostas são diretas e curtas, para usar numa conversa. Cada página leva ao capítulo completo no site, onde a objeção aparece na sua versão mais forte, com o que ela acerta, onde falha, a desmontagem passo a passo e as fontes."""

# Descrição curta de cada família, na página "As famílias", logo depois de "Como usar este livro".
FAMILIAS = {
    'A': 'Se os animais sentem, quais sentem e se isso basta para que contem moralmente.',
    'B': 'Se matar sem dor é um dano, se existe abate humanitário e se o bem-estar na criação resolve o problema.',
    'C': 'Apelos à natureza e à biologia: caninos, evolução, cadeia alimentar e o ciclo da vida.',
    'D': 'Tradição, família, cultura e religião como justificativa para usar animais.',
    'E': 'Escolha pessoal, relativismo e outras formas de encerrar a conversa sem responder a ela.',
    'F': 'Ilhas desertas, dilemas e casos extremos, usados para testar o princípio ou para fugir dele.',
    'G': 'Proteína, B12, ferro, leite e ômega-3: se é possível viver bem sem produtos animais.',
    'H': 'Soja, desmatamento, colheitas, água e clima: se o veganismo seria pior para o planeta.',
    'I': 'Testes em animais, couro, pele, zoológicos, rodeios, trabalho e animais de companhia: os usos fora do prato.',
    'J': 'Preço, acesso, tempo, sabor e vida social: se é viável e justo pedir a mudança.',
    'K': 'Se a escolha de uma pessoa faz diferença, e de quem é a responsabilidade.',
    'L': 'Críticas às pessoas veganas e ao movimento, no lugar de respostas aos argumentos.',
    'M': 'Os motivos de quem foi vegano e desistiu, e se isso muda o que é certo.',
    'N': 'Debates recentes da ética animal que muitos veganos ainda desconhecem, mas que envolvem seres sencientes: o sofrimento dos animais selvagens, a possível senciência de inteligências artificiais e o peso dos seres que ainda vão nascer.',
}
