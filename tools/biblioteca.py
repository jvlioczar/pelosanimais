"""Biblioteca: livros e sites para aprender a argumentar pelos animais. Ponto de partida: a lista da Vegpedia
(https://vegpedia.com/2024/07/24/livros-e-sites-para-aprender-a-argumentar-a-favor-dos-animais), completada com livros
focados em rebater argumentos antiveganos e especistas. Cada livro foi conferido em catálogo, editora ou resenha (2026-11-07)."""

# foco: 'rebater' (respostas a objeções), 'etica' (fundamentos filosóficos), 'psico' (por que defendemos o hábito)
FOCOS = {'rebater': 'Respostas a objeções', 'etica': 'Fundamentos éticos', 'psico': 'Psicologia do hábito'}

LIVROS = [
    dict(t='An Introduction to Animals and Political Theory', st='', a='Alasdair Cochrane', ano=2010, ed='Palgrave Macmillan', lingua='EN', foco='rebater',
         d='Examina como as grandes teorias políticas, como o liberalismo, o utilitarismo, o comunitarismo, o marxismo e o feminismo, tratam os animais, e mostra onde cada uma falha ao excluí-los.', u='https://doi.org/10.1057/9780230290594', ul='Editora'),
    dict(t='Uma breve introdução à ética animal', st='Desde as questões clássicas até o que vem sendo discutido atualmente', a='Luciano Carlos Cunha', ano=2021, ed='Appris', lingua='PT', foco='rebater',
         d='Reúne os argumentos usados para defender o especismo e apresenta as objeções a cada um, para leigos e acadêmicos.', u='https://philarchive.org/rec/DOSUIA', ul='Resenha'),
    dict(t='Uma Jornada pela Ética Animal', st='Coleção em 12 volumes', a='Luciano Carlos Cunha', ano=2025, ed='Acesso aberto', lingua='PT', foco='rebater',
         d='A coleção mais completa em português: cada capítulo examina uma objeção, e o volume XII resume as respostas em quadros. Base do site Questão de Ética.', u='https://questaodeetica.biblioverse.org/', ul='Ler grátis'),
    dict(t='Ética & Animais', st='Um guia de argumentação filosófica', a='Carlos Naconecy', ano=2006, ed='EDIPUCRS', lingua='PT', foco='etica',
         d='Apresenta as principais teorias éticas aplicadas aos animais, de Singer e Regan à ética do cuidado, para quem quer argumentar com base filosófica.', u='https://www.goodreads.com/work/quotes/36529914', ul='Sobre o livro'),
    dict(t='30 Non-Vegan Excuses & How to Respond to Them', st='30 desculpas de não veganos e como respondê-las', a='Ed Winters', ano=2020, ed='E-book gratuito', lingua='EN', foco='rebater',
         d='Curto e direto: trinta desculpas comuns, cada uma com uma resposta. Circula também uma tradução em português.', u='https://www.all-creatures.org/articles2/act-earthling-ed.html', ul='Ler grátis'),
    dict(t='How to Argue with a Meat Eater', st='And win every time', a='Ed Winters', ano=2023, ed='Ebury', lingua='EN', foco='rebater',
         d='Passa pelas objeções mais comuns, de ética a saúde, nutrição e ambiente, com dicas para manter a calma na conversa.', u='https://www.penguin.co.nz/books/how-to-argue-with-a-meat-eater-and-win-every-time-9781529907001', ul='Editora'),
    dict(t='This Is Vegan Propaganda', st='And other lies the meat industry tells you', a='Ed Winters', ano=2022, ed='Ebury', lingua='EN', foco='rebater',
         d='Desmonta as histórias que a indústria conta sobre a criação de animais e mostra o que acontece de fato.', u='https://openlibrary.org/works/OL25324216W', ul='Catálogo'),
    dict(t='Eat Like You Care', st='Em português: Coma com consciência', a='Gary L. Francione e Anna Charlton', ano=2013, ed='Exempla Press', lingua='EN', foco='rebater',
         d='Examina a moralidade de comer animais e responde, uma a uma, às justificativas mais comuns.', u='https://openlibrary.org/works/OL27049208W', ul='Catálogo'),
    dict(t='Introduction to Animal Rights', st='Your child or the dog?', a='Gary L. Francione', ano=2000, ed='Temple University Press', lingua='EN', foco='rebater',
         d='Enfrenta o dilema da casa em chamas e mostra por que uma escolha numa emergência não justifica a exploração.', u='https://tupress.temple.edu/books/introduction-to-animal-rights', ul='Editora'),
    dict(t='Making a Stand for Animals', st='', a='Oscar Horta', ano=2022, ed='Routledge', lingua='EN', foco='rebater',
         d='Introdução clara à ética animal que responde às objeções ao fim do especismo, inclusive sobre os animais selvagens.', u='https://openlibrary.org/works/OL27090032W', ul='Catálogo'),
    dict(t='Meat Logic', st='Why do we eat animals?', a='Charles Horn', ano=2014, ed='CreateSpace', lingua='EN', foco='rebater',
         d='Avalia, uma a uma, as racionalizações para comer animais diante do fato de que não precisamos deles para viver bem.', u='https://all-creatures.org/book/r-meat-logic.html', ul='Resenha'),
    dict(t='Por que amamos cachorros, comemos porcos e vestimos vacas', st='Uma introdução ao carnismo', a='Melanie Joy', ano=2010, ed='', lingua='PT', foco='psico',
         d='Explica o carnismo, o sistema de crenças que nos faz amar uns animais e comer outros sem perceber a contradição.', u='https://www.goodreads.com/book/show/20656567', ul='Sobre o livro'),
    dict(t='How To Argue With Vegans', st='', a='Richard Watts e Benny Malone', ano=2021, ed='Publicação independente', lingua='EN', foco='rebater',
         d='Do autor das tirinhas Vegan Sidekick: passa pelas objeções mais comuns, das reações de desdém às mais elaboradas, e mostra por que nenhuma justifica explorar animais.', u='https://openlibrary.org/works/OL25447111W', ul='Catálogo'),
    dict(t='Como sobreviver sem carne e outros milagres inexplicáveis', st='', a='Nuno Alvim', ano=2026, ed='Oficina do Livro (Portugal)', lingua='PT', foco='rebater',
         d='Lançamento recente: responde a perguntas incômodas sobre deixar de comer carne usando ciência e história, sem moralismo.', u='https://www.continente.pt/produto/como-sobreviver-sem-carne-e-outros-milagres-inexplicaveis-de-nuno-alvim-8979457.html', ul='Livraria'),
    dict(t='Libertação animal já', st='Edição atualizada de Libertação Animal (em inglês, Animal Liberation Now)', a='Peter Singer', ano=2023, ed='WMF Martins Fontes, 2026 no Brasil', lingua='PT', foco='etica',
         d='Versão revista e atualizada do clássico de 1975, com dados recentes sobre a criação industrial, os testes em animais e as novas tecnologias.', u='https://www.martinsfontespaulista.com.br/libertacao-animal-ja-1206626/p', ul='Editora'),
    dict(t='Libertação Animal', st='', a='Peter Singer', ano=1975, ed='', lingua='PT', foco='etica',
         d='O livro que popularizou o termo "especismo" e o princípio da igual consideração de interesses.', u='https://en.wikipedia.org/wiki/Animal_Liberation_(book)', ul='Sobre o livro'),
    dict(t='Veganismo', st='As muitas razões para uma vida mais ética', a='Robson Fernando de Souza', ano=2017, ed='Publicação independente', lingua='PT', foco='rebater',
         d='Reúne em português os argumentos do movimento vegano, com as referências por trás de cada um.', u='https://openlibrary.org/works/OL29711903W', ul='Catálogo'),
]

SITES = [
    ('Questão de Ética', 'As 248 objeções da coleção de Luciano Carlos Cunha, com respostas', 'https://questaodeetica.biblioverse.org/desbancando.html'),
    ('Senciência', 'Textos sobre ética animal e especismo', 'https://senciencia.org/'),
    ('Veganismos', 'Publicação no Medium sobre veganismo e ética animal', 'https://medium.com/veganismo-s'),
    ('Argumentos em defesa dos animais', 'Respostas organizadas por tema', 'https://www.alyssonaugusto.com.br/argumentos'),
    ('Guia de falácias antiveganas', 'Do site Veganagente', 'https://veganagente.com.br/falacias-antiveganas/'),
    ('Sua Falácia Vegana É', 'Falácias comuns contra o veganismo, em cartões', 'https://yourveganfallacyis.com/pt-br'),
    ('Carnism Debunked', 'Em inglês: respostas aos argumentos usados para defender a exploração animal', 'https://www.carnismdebunked.com'),
    ('ADAPTT', 'Em inglês: acervo de textos sobre veganismo, ética e libertação animal, com guias para começar, palestras e formas de agir', 'https://www.adaptt.org'),
    ('Sentientism', 'Em inglês: visão de mundo comprometida com evidência, razão e compaixão por todos os seres sencientes, com comunidade e entrevistas', 'https://www.sentientism.info'),
    ('Essays on Reducing Suffering', 'Em inglês: ensaios sobre como reduzir o sofrimento, com foco em animais criados para consumo, animais selvagens e invertebrados', 'https://reducing-suffering.org/'),
    ('Reducing Risks of Future Suffering', 'Em inglês: blog sobre riscos de sofrimento em larga escala no futuro, inclusive ligados à inteligência artificial', 'https://s-risks.org'),
    ('Sentience Research', 'Em inglês: projeto de pesquisa sobre como identificar, medir e entender a senciência em animais, humanos e máquinas', 'https://sentience-research.org'),
    ('HedWeb', 'Em inglês: textos sobre o uso da biotecnologia para abolir o sofrimento, inclusive o dos animais selvagens', 'https://www.hedweb.com/confile.htm'),
    ('End Infighting', 'Em inglês: causas e custos das brigas internas em movimentos sociais, e ferramentas para evitá-las', 'https://infighting.org'),
    ('Sapienship Lab', 'Em inglês: central de mídia para educadores, estudantes e quem gosta de aprender', 'https://lab.sapienship.co'),
    ('Ethical Food Guide', 'Em inglês e português: diretório e mapa de empresas de proteínas alternativas, de carnes vegetais e cultivadas a fermentação', 'https://ethicalfood.biblioverse.org'),
]

# Organizações antiespecistas ou dedicadas a todos os seres sencientes, em ordem alfabética.
ORGS = [
    ('Animal Charity Evaluators', 'Em inglês: pesquisa as formas mais eficazes de ajudar os animais e recomenda organizações', 'https://animalcharityevaluators.org'),
    ('Animals Australia', 'Em inglês: organização australiana de proteção animal', 'https://animalsaustralia.org'),
    ('Center for Effective Vegan Advocacy', 'Em inglês: formação para ativistas, com dicas de comunicação para conversar sobre veganismo', 'https://veganadvocacy.org/communication-hacks'),
    ('Center for Reducing Suffering', 'Em inglês: pesquisa sobre como reduzir o sofrimento intenso, levando em conta todos os seres sencientes', 'https://centerforreducingsuffering.org/'),
    ('Center on Long-Term Risk', 'Em inglês: pesquisa sobre os piores riscos ligados ao desenvolvimento de inteligência artificial avançada', 'https://longtermrisk.org'),
    ('Ética Animal', 'Organização internacional com textos em português sobre especismo, senciência e animais selvagens', 'https://www.animal-ethics.org/pt/'),
    ('Faunalytics', 'Em inglês: pesquisas e dados para que ativistas ajudem os animais de forma eficaz', 'https://faunalytics.org'),
    ('Instituto de Educação Antiespecista', 'Educação antiespecista no Brasil, pelo Instagram', 'https://www.instagram.com/inea.educacao.antiespecista/'),
    ('Invincible Wellbeing', 'Em inglês: pesquisa, com parceiros acadêmicos, sobre as raízes biológicas da dor e formas de tratá-la', 'https://invinciblewellbeing.com'),
    ('Jeremy Coller Centre for Animal Sentience', 'Em inglês: centro de pesquisa sobre senciência animal na London School of Economics', 'https://www.lse.ac.uk/sentience'),
    ('New Harvest', 'Em inglês: instituto de pesquisa em agricultura celular, como a carne cultivada', 'https://new-harvest.org'),
    ('Rethink Priorities', 'Em inglês: pesquisa sobre prioridades para fazer o bem, incluindo o bem-estar de animais e de invertebrados', 'https://rethinkpriorities.org'),
    ('Sentience Institute', 'Em inglês: instituto de pesquisa sobre mudança social e tecnológica, em especial a expansão do círculo moral', 'https://www.sentienceinstitute.org'),
    ('Sentient Futures', 'Em inglês: pesquisa, políticas públicas e comunidade para levar em conta o bem-estar de animais e de mentes artificiais', 'https://sentientfutures.ai'),
    ('The Good Food Institute', 'Em inglês: organização sem fins lucrativos que apoia proteínas vegetais, cultivadas e de fermentação', 'https://gfi.org'),
    ('Wild Animal Initiative', 'Em inglês: pesquisa sobre o bem-estar de animais selvagens', 'https://www.wildanimalinitiative.org'),
]

