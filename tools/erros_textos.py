# -*- coding: utf-8 -*-
"""Textos das páginas de cada falácia e de cada viés (falacias/<slug>.html e vieses/<slug>.html).

Chave: o nome em português, igual ao do catálogo (FALACIAS e VIESES em build.py).
Para cada item: (explicação PT, analogia PT, explicação EN, analogia EN). A explicação é objetiva e para o público geral;
a analogia usa um exemplo do dia a dia, fora do debate sobre os animais.

RUINS_ERROS liga os itens de "Pare de dizer isso" (pela frase em português) às falácias e vieses que eles cometem,
para a parte "Quando quem defende os animais comete o mesmo erro". Só entram ligações claras.
"""

FAL = {
 'Apelo à natureza': (
  'Concluir que algo é bom, certo ou aceitável só porque é natural, ou ruim só porque é artificial. "Natural" descreve a origem de algo; não diz se é bom. Doenças, venenos e terremotos são naturais, e óculos, vacinas e anestesia não são.',
  'Dizer que um cogumelo é seguro porque nasceu na floresta, sem perguntar qual cogumelo é.',
  'Concluding that something is good, right or acceptable just because it is natural, or bad just because it is artificial. "Natural" describes where something comes from; it does not say whether it is good. Diseases, poisons and earthquakes are natural, while glasses, vaccines and anesthesia are not.',
  'Saying a mushroom is safe because it grew in the forest, without asking which mushroom it is.'),
 'Lei de Hume (do é ao deve)': (
  'Tirar uma conclusão sobre o que deve ser feito apenas de fatos sobre o que é. O filósofo David Hume observou que, entre "é" e "deve", falta sempre uma premissa moral, e é ela que precisa ser defendida. Os fatos importam, mas sozinhos não decidem o que é certo.',
  'Do fato de que muita gente fura fila não se segue que furar fila seja certo.',
  'Drawing a conclusion about what ought to be done from facts about what is, and nothing else. The philosopher David Hume observed that between "is" and "ought" a moral premise is always missing, and that premise is what needs defending. Facts matter, but on their own they do not settle what is right.',
  'From the fact that many people jump the queue it does not follow that jumping the queue is right.'),
 'Apelo à tradição': (
  'Defender uma prática só porque ela é antiga ou faz parte de um costume. A idade de uma prática mostra que ela durou, não que seja justa: muitas tradições foram abandonadas justamente porque causavam dano.',
  'Manter uma regra da empresa só porque "sempre foi assim", mesmo quando ela prejudica os funcionários.',
  'Defending a practice only because it is old or part of a custom. A practice\'s age shows that it has lasted, not that it is just: many traditions were abandoned precisely because they caused harm.',
  'Keeping a company rule only because "it has always been this way", even when it harms the employees.'),
 'Apelo à multidão e à normalidade': (
  'Tomar o que a maioria faz ou pensa como prova de que é certo ou verdadeiro. A quantidade de adeptos mede a popularidade de uma ideia, não a sua correção.',
  'Achar que um boato é verdade porque todo mundo no grupo da família está compartilhando.',
  'Taking what most people do or think as proof that it is right or true. The number of followers measures an idea\'s popularity, not its correctness.',
  'Believing a rumor is true because everyone in the family group chat is sharing it.'),
 'Apelo à autoridade': (
  'Aceitar uma conclusão porque alguém importante a defendeu ou praticou, em vez de examinar as razões. Especialistas merecem atenção no seu campo, mas o nome não substitui o argumento, e a competência numa área não se transfere para outra, como a moral.',
  'Comprar um remédio porque um ator famoso disse que funciona.',
  'Accepting a conclusion because someone important defended or practiced it, instead of examining the reasons. Experts deserve attention in their field, but a name does not replace an argument, and competence in one area does not transfer to another, such as ethics.',
  'Buying a medicine because a famous actor said it works.'),
 'Critério arbitrário (especismo)': (
  'Escolher como fronteira moral um traço que não tem relação com o que está em jogo. Se o que torna um dano grave é o sofrimento de quem o recebe, usar a espécie, a inteligência ou a linguagem para decidir quem conta é usar um traço irrelevante, como seria usar a cor da pele.',
  'Decidir quem recebe atendimento de urgência pela cor da camisa, e não pela gravidade do caso.',
  'Choosing as the moral boundary a trait that has nothing to do with what is at stake. If what makes a harm serious is the suffering of the one who receives it, using species, intelligence or language to decide who counts is using an irrelevant trait, as using skin color would be.',
  'Deciding who gets emergency care by the color of their shirt, not by how serious the case is.'),
 'Definição persuasiva': (
  'Definir uma palavra de um jeito que já traz embutida a conclusão que se quer, para vencer a discussão sem argumentar. A definição troca o debate sobre os fatos por um truque de vocabulário.',
  'Dizer que "um bom motorista nunca recebe multa" e, com isso, concluir que quem já foi multado não sabe dirigir.',
  'Defining a word in a way that already contains the desired conclusion, to win the discussion without arguing. The definition replaces a debate about facts with a trick of vocabulary.',
  'Saying that "a good driver never gets a ticket" and concluding that anyone who has had one cannot drive.'),
 'Petição de princípio': (
  'Usar como premissa justamente aquilo que se queria provar. O argumento parece avançar, mas anda em círculo: a conclusão já estava escondida no ponto de partida.',
  '"Esse jornal é confiável porque é o que ele mesmo diz."',
  'Using as a premise exactly what one wanted to prove. The argument seems to move forward but goes in a circle: the conclusion was already hidden in the starting point.',
  '"This newspaper is reliable because it says so itself."'),
 'Falácia do contínuo': (
  'Concluir que, se não existe uma linha exata separando dois extremos, não há diferença real entre eles. A falta de uma fronteira precisa não apaga as diferenças claras nas pontas.',
  'Não saber o segundo exato em que o dia vira noite não significa que meio-dia e meia-noite sejam iguais.',
  'Concluding that, if there is no exact line separating two extremes, there is no real difference between them. The lack of a precise boundary does not erase the clear differences at the ends.',
  'Not knowing the exact second when day turns into night does not mean noon and midnight are the same.'),
 'Generalização do acidente': (
  'Aplicar a um caso excepcional uma regra feita para os casos comuns, ou usar uma exceção para justificar a regra. Uma situação extrema ou rara não decide o que vale no dia a dia.',
  'Usar o fato de que uma ambulância pode furar o sinal vermelho para defender que qualquer um possa.',
  'Applying a rule made for ordinary cases to an exceptional one, or using an exception to justify the rule. An extreme or rare situation does not settle what holds in everyday life.',
  'Using the fact that an ambulance may run a red light to argue that anyone may.'),
 'Falsa dicotomia': (
  'Apresentar só duas opções quando existem outras. Ao esconder as alternativas, o argumento força a escolha da opção que favorece quem fala.',
  '"Ou você concorda com tudo o que eu digo, ou é meu inimigo."',
  'Presenting only two options when there are others. By hiding the alternatives, the argument forces a choice of the option that favors the speaker.',
  '"Either you agree with everything I say, or you are my enemy."'),
 'Falácia do nirvana': (
  'Rejeitar uma solução porque ela não é perfeita, comparando-a com um ideal impossível. Reduzir um dano continua valendo a pena mesmo quando não dá para eliminá-lo por completo.',
  'Desistir do cinto de segurança porque ele não evita todas as mortes no trânsito.',
  'Rejecting a solution because it is not perfect, by comparing it with an impossible ideal. Reducing a harm is still worthwhile even when it cannot be eliminated entirely.',
  'Giving up seat belts because they do not prevent every road death.'),
 'Tu quoque': (
  'Responder a uma crítica apontando que quem critica também faz algo parecido, em vez de mostrar que a crítica está errada. A incoerência de quem fala pode ser real, mas não torna a crítica falsa.',
  'Um fumante avisa que cigarro faz mal, e a resposta é "mas você fuma".',
  'Answering a criticism by pointing out that the critic does something similar, instead of showing that the criticism is wrong. The speaker\'s inconsistency may be real, but it does not make the criticism false.',
  'A smoker warns that cigarettes are harmful, and the reply is "but you smoke".'),
 'Ad hominem e envenenamento do poço': (
  'Atacar a pessoa que apresenta um argumento, e não o argumento. No envenenamento do poço, a pessoa é desqualificada antes de falar, para que ninguém leve a sério o que ela vai dizer.',
  'Rejeitar uma conta de matemática porque quem a fez é antipático.',
  'Attacking the person who presents an argument instead of the argument. In poisoning the well, the person is discredited before speaking, so that no one takes seriously what they will say.',
  'Rejecting a math calculation because the person who did it is unpleasant.'),
 'Culpa por associação': (
  'Rejeitar uma ideia por causa de pessoas ou grupos ruins que também a defenderam. Uma ideia não fica errada porque alguém detestável concordou com ela.',
  'Recusar-se a beber água porque um criminoso também bebia.',
  'Rejecting an idea because of bad people or groups who also held it. An idea does not become wrong because someone detestable agreed with it.',
  'Refusing to drink water because a criminal also drank it.'),
 'Falácia da prioridade': (
  'Descartar um problema porque existe outro que seria mais grave. Pessoas e sociedades lidam com vários problemas ao mesmo tempo, e a existência de um maior não torna o menor aceitável.',
  'Dizer que não vale a pena consertar um vazamento em casa enquanto houver guerras no mundo.',
  'Dismissing a problem because there is another one that would be more serious. People and societies deal with many problems at once, and the existence of a bigger one does not make the smaller one acceptable.',
  'Saying it is not worth fixing a leak at home while there are wars in the world.'),
 'Evidência anedótica': (
  'Usar um caso pessoal ou alguns exemplos conhecidos contra dados de muitos casos. Histórias marcam a memória, mas um caso isolado pode ser exceção, coincidência ou ter outra causa.',
  '"Meu tio fumou a vida toda e viveu até os 95, então cigarro não faz mal."',
  'Using a personal case or a few well-known examples against data from many cases. Stories stick in memory, but a single case may be an exception, a coincidence or have another cause.',
  '"My uncle smoked all his life and lived to 95, so smoking is not harmful."'),
 'Cherry picking': (
  'Escolher só os dados, estudos ou exemplos que favorecem a própria posição e ignorar os que a contrariam. Cada dado citado pode ser verdadeiro, e mesmo assim o quadro apresentado ser falso.',
  'Mostrar só as fotos em que o time aparece vencendo e concluir que ele nunca perdeu.',
  'Choosing only the data, studies or examples that favor one\'s position and ignoring those that contradict it. Each piece of data cited may be true, and the picture presented may still be false.',
  'Showing only the photos where the team is winning and concluding it never lost.'),
 'Falso meio-termo': (
  'Supor que a posição intermediária entre duas é automaticamente a correta. Às vezes um dos lados simplesmente está certo, e o meio-termo entre o verdadeiro e o falso continua errado.',
  'Se alguém diz que 2 + 2 = 4 e outro diz que é 6, a resposta não é 5.',
  'Assuming that the position halfway between two others is automatically the correct one. Sometimes one side is simply right, and the midpoint between true and false is still wrong.',
  'If one person says 2 + 2 = 4 and another says 6, the answer is not 5.'),
 'Mudança de questão (red herring)': (
  'Desviar a discussão para outro assunto, que pode até ser verdadeiro e interessante, mas não responde à pergunta que estava em debate. Também chamada de "arenque vermelho" ou desvio de assunto.',
  'Perguntado se fez o trabalho, o aluno responde falando de como o professor é injusto.',
  'Diverting the discussion to another subject, which may even be true and interesting, but does not answer the question under debate. Also called a red herring.',
  'Asked whether he did the homework, the student answers by talking about how unfair the teacher is.'),
 'Espantalho': (
  'Distorcer ou exagerar a posição do outro para refutá-la com facilidade. O que se derruba é o boneco, não a posição real.',
  'Alguém propõe menos açúcar na merenda, e a resposta é "então você quer proibir as crianças de comer doce?".',
  'Distorting or exaggerating the other side\'s position in order to refute it easily. What gets knocked down is the dummy, not the real position.',
  'Someone proposes less sugar in school lunches, and the reply is "so you want to ban children from eating sweets?".'),
 'Apelo ao ridículo': (
  'Responder a uma ideia com zombaria, como se fazer graça dela fosse refutá-la. Uma ideia pode soar estranha e mesmo assim ser verdadeira.',
  'Rir de quem dizia que a Terra gira em torno do Sol, em vez de examinar as observações.',
  'Answering an idea with mockery, as if making fun of it refuted it. An idea can sound strange and still be true.',
  'Laughing at those who said the Earth goes around the Sun, instead of examining the observations.'),
 'Apelo à ignorância': (
  'Concluir que algo é verdadeiro porque não se provou que é falso, ou falso porque não se provou que é verdadeiro. A falta de prova é um motivo para cautela, não uma prova do contrário.',
  '"Ninguém provou que esse prédio vai cair, então não precisa de vistoria."',
  'Concluding that something is true because it has not been proven false, or false because it has not been proven true. Lack of proof is a reason for caution, not proof of the opposite.',
  '"No one has proven this building will collapse, so it needs no inspection."'),
 'Falsa causa (post hoc)': (
  'Concluir que uma coisa causou outra só porque veio antes dela, ou porque as duas aconteceram juntas. Sequência no tempo não é prova de causa; pode haver coincidência ou uma terceira causa.',
  'O galo canta e o sol nasce, mas não é o canto que faz o sol nascer.',
  'Concluding that one thing caused another just because it came first, or because the two happened together. Sequence in time is not proof of cause; there may be coincidence or a third cause.',
  'The rooster crows and the sun rises, but the crowing does not make the sun rise.'),
 'Ladeira escorregadia': (
  'Afirmar que um primeiro passo levará, inevitavelmente, a uma série de consequências extremas, sem mostrar por que cada etapa aconteceria. Algumas cadeias são reais, mas precisam ser demonstradas, não supostas.',
  '"Se deixar seu filho ver um desenho hoje, amanhã ele vai largar a escola."',
  'Claiming that a first step will inevitably lead to a series of extreme consequences, without showing why each stage would happen. Some chains are real, but they need to be shown, not assumed.',
  '"If you let your child watch one cartoon today, tomorrow they will drop out of school."'),
 'Apelo à legalidade': (
  'Tomar o que a lei permite como prova de que é moralmente certo, ou o que ela proíbe como prova de que é errado. A lei é feita por pessoas e muda; muitas práticas legais foram depois reconhecidas como injustas.',
  'Achar que, se não existe lei contra mentir para um amigo, mentir para ele está certo.',
  'Taking what the law allows as proof that it is morally right, or what it forbids as proof that it is wrong. Laws are made by people and change; many legal practices were later recognized as unjust.',
  'Thinking that, since there is no law against lying to a friend, lying to them is fine.'),
 'Bulverismo': (
  'Supor que o outro está errado e passar a explicar por que ele pensa assim, como psicologia, interesse ou grupo, sem mostrar onde está o erro. O nome vem de um texto do escritor C. S. Lewis.',
  '"Você só acha que a ponte vai cair porque tem medo de altura", sem olhar para a ponte.',
  'Assuming the other person is wrong and going on to explain why they think so, in terms of psychology, interest or group, without showing where the error lies. The name comes from an essay by the writer C. S. Lewis.',
  '"You only think the bridge will collapse because you are afraid of heights", without looking at the bridge.'),
 'Falácia da falácia': (
  'Concluir que uma ideia é falsa porque alguém a defendeu com um argumento ruim. Uma conclusão pode ser verdadeira mesmo quando foi mal defendida.',
  'Alguém diz que a Terra é redonda "porque a bola é redonda"; o argumento é ruim, mas a Terra continua redonda.',
  'Concluding that an idea is false because someone defended it with a bad argument. A conclusion can be true even when it was badly defended.',
  'Someone says the Earth is round "because balls are round"; the argument is bad, but the Earth is still round.'),
 'Equívoco': (
  'Usar a mesma palavra em dois sentidos diferentes dentro do mesmo raciocínio, como se fosse um só. A conclusão parece seguir das premissas, mas só porque o sentido da palavra mudou no meio do caminho.',
  '"A pena é leve; o que é leve não pesa; logo, a pena não pesa na vida do condenado."',
  'Using the same word in two different senses within the same reasoning, as if it were one. The conclusion seems to follow from the premises, but only because the meaning of the word shifted along the way.',
  '"A feather is light; what is light is not dark; so a feather is not dark."'),
 'Generalização precipitada': (
  'Tirar uma conclusão sobre todos a partir de poucos casos, ou de casos que não representam o conjunto. Algumas experiências ruins não dizem como é o grupo inteiro.',
  'Ser mal atendido numa loja e concluir que todas as lojas da cidade atendem mal.',
  'Drawing a conclusion about all from a few cases, or from cases that do not represent the whole. A few bad experiences do not say what the whole group is like.',
  'Getting poor service at one shop and concluding that every shop in town is bad.'),
 'Apelo ao medo': (
  'Tentar convencer assustando com consequências exageradas ou improváveis, no lugar de apresentar evidências. O medo chama atenção, mas não mede o tamanho real do risco.',
  'Dizer que quem viajar de avião vai morrer num acidente, para convencer alguém a ir de carro, que é mais arriscado.',
  'Trying to persuade by frightening people with exaggerated or unlikely consequences, instead of presenting evidence. Fear grabs attention, but it does not measure the real size of a risk.',
  'Telling someone they will die in a plane crash to convince them to drive instead, which is riskier.'),
 'Eufemismo': (
  'Trocar o nome de algo por uma palavra mais branda para que um dano pareça menor ou desapareça. A palavra muda a impressão, não o fato.',
  'Chamar uma demissão em massa de "otimização do quadro de pessoal".',
  'Replacing the name of something with a milder word so that a harm seems smaller or disappears. The word changes the impression, not the fact.',
  'Calling mass layoffs "workforce optimization".'),
 'Negação do antecedente': (
  'Erro de forma: "se A, então B; não A; logo, não B". A regra só diz o que acontece quando A ocorre; B pode acontecer por outros caminhos.',
  '"Se chover, a rua fica molhada; não choveu; logo, a rua está seca." Alguém pode ter lavado a calçada.',
  'A formal error: "if A, then B; not A; therefore, not B". The rule only says what happens when A occurs; B can happen in other ways.',
  '"If it rains, the street gets wet; it did not rain; so the street is dry." Someone may have hosed down the pavement.'),
 'Afirmação do consequente': (
  'Erro de forma: "se A, então B; B; logo, A". O fato de B ter acontecido não mostra que A aconteceu, porque B pode ter outras causas.',
  '"Se choveu, a rua está molhada; a rua está molhada; logo, choveu." Alguém pode ter lavado a calçada.',
  'A formal error: "if A, then B; B; therefore, A". The fact that B happened does not show that A did, because B may have other causes.',
  '"If it rained, the street is wet; the street is wet; so it rained." Someone may have hosed down the pavement.'),
}

VIE = {
 'Dissonância cognitiva (paradoxo da carne)': (
  'O desconforto de ter duas crenças ou atitudes em conflito, como gostar de animais e comê-los. Em vez de mudar o comportamento, muita gente reduz o desconforto mudando a crença, por exemplo passando a ver os animais comidos como menos capazes de sentir. A psicologia chama esse caso de paradoxo da carne.',
  'O fumante que sabe que cigarro faz mal e passa a dizer que "de alguma coisa todo mundo morre".',
  'The discomfort of holding two conflicting beliefs or attitudes, such as liking animals and eating them. Instead of changing behavior, many people reduce the discomfort by changing the belief, for example by coming to see the animals they eat as less able to feel. Psychologists call this case the meat paradox.',
  'The smoker who knows cigarettes are harmful and starts saying "everyone dies of something".'),
 'Raciocínio motivado': (
  'Avaliar argumentos e evidências conforme a conclusão que se deseja, e não conforme a qualidade deles. Os argumentos que favorecem o que queremos parecem fortes; os contrários, fracos.',
  'O torcedor que vê pênalti em toda falta contra o seu time e nenhum na falta a favor.',
  'Assessing arguments and evidence according to the conclusion one wants, rather than their quality. Arguments that favor what we want seem strong; opposing ones seem weak.',
  'The fan who sees a penalty in every foul against their team and none in fouls in its favor.'),
 'Viés de confirmação': (
  'Procurar, notar e lembrar mais as informações que confirmam o que já pensamos, e deixar passar as que contrariam.',
  'Depois de comprar um carro, achar que todos os comentários sobre aquele modelo são elogios.',
  'Seeking, noticing and remembering more the information that confirms what we already think, and letting slip what contradicts it.',
  'After buying a car, feeling that every comment about that model is praise.'),
 'Viés do status quo': (
  'Preferir que as coisas continuem como estão só porque é o estado atual, e exigir de qualquer mudança mais provas do que se exige do que já existe.',
  'Manter um plano de celular caro há anos porque mudar parece trabalhoso, mesmo sabendo que existe um melhor.',
  'Preferring things to stay as they are just because that is the current state, and demanding more proof from any change than from what already exists.',
  'Keeping an expensive phone plan for years because switching seems like a hassle, even knowing a better one exists.'),
 'Justificação do sistema': (
  'Tendência a defender e legitimar a forma como a sociedade já está organizada, vendo-a como justa e necessária, mesmo quando ela prejudica alguém, às vezes até quem a defende.',
  'Quem diz que uma regra antiga e desigual da firma "deve ter um bom motivo" sem saber qual é.',
  'The tendency to defend and legitimize the way society is already organized, seeing it as fair and necessary, even when it harms someone, sometimes even those who defend it.',
  'Someone who says an old, unequal company rule "must have a good reason" without knowing what it is.'),
 'Ignorância deliberada': (
  'Evitar de propósito informações que poderiam obrigar a mudar de opinião ou de hábito. Não saber vira uma forma de não se sentir responsável.',
  'Não abrir a fatura do cartão para não ter de encarar quanto gastou.',
  'Deliberately avoiding information that might force a change of opinion or habit. Not knowing becomes a way of not feeling responsible.',
  'Not opening the credit card bill so as not to face how much was spent.'),
 'Categorização funcional': (
  'Atribuir capacidades e valor a um animal conforme o uso que fazemos dele: animais classificados como "de comida" recebem menos mente e menos consideração do que os "de companhia", mesmo quando são parecidos.',
  'Ver o mesmo móvel como valioso na sala e como lixo na calçada, só pela categoria em que foi posto.',
  'Attributing abilities and value to an animal according to the use we make of it: animals classified as "food" are credited with less mind and less consideration than "companion" animals, even when they are similar.',
  'Seeing the same piece of furniture as valuable in the living room and as trash on the curb, just because of the category it was put in.'),
 'Viés de grupo (ingroup)': (
  'Favorecer quem faz parte do nosso grupo e desvalorizar quem está fora dele, seja o grupo uma família, um time, um país ou uma espécie.',
  'Achar a mesma jogada genial quando é do seu time e desleal quando é do adversário.',
  'Favoring those who belong to our group and devaluing those outside it, whether the group is a family, a team, a country or a species.',
  'Finding the same move brilliant when your team does it and dirty when the opponent does.'),
 'Insensibilidade à escala': (
  'Não ajustar a preocupação ao tamanho do problema: a reação a um dano que atinge milhões ou bilhões é quase a mesma que a um dano que atinge poucos.',
  'Doar quase o mesmo valor para salvar duas mil aves ou duzentas mil, como em estudos clássicos sobre o tema.',
  'Failing to scale concern to the size of the problem: the reaction to a harm affecting millions or billions is almost the same as to one affecting a few.',
  'Giving almost the same amount to save two thousand birds or two hundred thousand, as in classic studies on the subject.'),
 'Difusão de responsabilidade': (
  'Sentir-se menos responsável por um dano quando muitas pessoas participam dele. Quanto mais gente envolvida, menor parece a parte de cada um.',
  'Ninguém chama ajuda num acidente cheio de testemunhas, porque cada um supõe que outro já chamou.',
  'Feeling less responsible for a harm when many people take part in it. The more people involved, the smaller each person\'s share seems.',
  'No one calls for help at an accident with many witnesses, because each assumes someone else already did.'),
 'Reatância psicológica': (
  'Reagir contra uma ideia ou pedido quando se sente que a própria liberdade está sendo ameaçada, às vezes fazendo o contrário só para afirmar a autonomia.',
  'O adolescente que passa a fazer algo justamente porque foi proibido.',
  'Pushing back against an idea or request when one feels one\'s freedom is being threatened, sometimes doing the opposite just to assert autonomy.',
  'The teenager who starts doing something precisely because it was forbidden.'),
 'Cognição protetora da identidade': (
  'Avaliar fatos e argumentos de modo a proteger a identidade e o lugar no próprio grupo. Aceitar a ideia teria um custo social, então ela é rejeitada antes de ser examinada.',
  'Recusar um dado sobre o próprio bairro porque admiti-lo seria trair os vizinhos.',
  'Assessing facts and arguments in a way that protects one\'s identity and place in one\'s group. Accepting the idea would have a social cost, so it is rejected before being examined.',
  'Refusing a fact about one\'s own neighborhood because admitting it would be betraying the neighbors.'),
 'Heurística do afeto': (
  'Julgar algo pelo sentimento que ele desperta: o que agrada parece seguro e bom, e o que desagrada parece arriscado e ruim, antes de qualquer análise.',
  'Achar que uma cidade é perigosa porque não gostou da comida de lá.',
  'Judging something by the feeling it arouses: what pleases seems safe and good, and what displeases seems risky and bad, before any analysis.',
  'Thinking a city is dangerous because you did not like its food.'),
 'Licença moral': (
  'Depois de fazer algo bom, sentir-se autorizado a fazer algo ruim, como se a boa ação tivesse gerado um crédito.',
  'Pedir a sobremesa maior porque foi à academia de manhã.',
  'After doing something good, feeling entitled to do something bad, as if the good deed had earned a credit.',
  'Ordering the bigger dessert because you went to the gym in the morning.'),
 'Viés de otimismo e excepcionalismo': (
  'Achar que os riscos e as regras que valem para os outros não se aplicam a nós, ou que o nosso caso é uma exceção.',
  'Achar que mandar mensagem dirigindo é perigoso para os outros, mas não para quem dirige bem.',
  'Believing that the risks and rules that apply to others do not apply to us, or that our case is an exception.',
  'Thinking texting while driving is dangerous for others but not for a good driver like yourself.'),
 'Viés de sobrevivência': (
  'Tirar conclusões olhando só para quem "sobreviveu" a um processo, sem ver os que ficaram pelo caminho e por isso não aparecem.',
  'Achar que largar a faculdade leva ao sucesso porque alguns bilionários largaram, sem contar os milhões que largaram e não ficaram ricos.',
  'Drawing conclusions by looking only at those who "survived" a process, without seeing those who fell by the wayside and therefore do not show up.',
  'Thinking dropping out of college leads to success because some billionaires did, without counting the millions who dropped out and did not get rich.'),
 'Racionalização pelos 4Ns': (
  'Justificar o consumo de produtos animais com quatro ideias que pesquisadores agruparam como os "4Ns": é natural, normal, necessário e gostoso (nice, em inglês). Elas costumam vir prontas, antes de qualquer reflexão.',
  'Defender um hábito dizendo que "todo mundo faz, é assim mesmo e não dá para viver sem", sem examinar nenhuma das três coisas.',
  'Justifying the consumption of animal products with four ideas that researchers grouped as the "4Ns": it is natural, normal, necessary and nice. They tend to come ready-made, before any reflection.',
  'Defending a habit by saying "everyone does it, that is how it is and you cannot live without it", without examining any of the three.'),
 'Busca de hipocrisia': (
  'Procurar incoerências em quem defende uma mudança para se sentir dispensado de mudar. Achar uma falha no mensageiro alivia a pressão da mensagem.',
  'Ignorar o conselho do médico para parar de beber porque ele próprio toma uma taça de vinho.',
  'Looking for inconsistencies in those who advocate a change in order to feel excused from changing. Finding a flaw in the messenger relieves the pressure of the message.',
  'Ignoring the doctor\'s advice to stop drinking because the doctor has a glass of wine.'),
 'Negação de mente': (
  'Atribuir menos mente, menos inteligência e menos capacidade de sofrer aos seres que usamos ou comemos. A crença costuma seguir o hábito: quanto mais se come um animal, menos mente se reconhece nele.',
  'Achar que o garçom não se importa de ser maltratado porque "é só o trabalho dele".',
  'Attributing less mind, less intelligence and less capacity to suffer to the beings we use or eat. The belief tends to follow the habit: the more an animal is eaten, the less mind is recognized in it.',
  'Assuming the waiter does not mind being mistreated because "it is just their job".'),
 'Depreciação de quem faz o bem': (
  'Desvalorizar ou ridicularizar quem age de modo mais ético, porque o exemplo dessa pessoa faz os outros se sentirem julgados, mesmo quando ela não julga ninguém.',
  'Zombar do colega que devolve o troco a mais, chamando-o de "certinho".',
  'Devaluing or ridiculing those who act more ethically, because their example makes others feel judged, even when they judge no one.',
  'Mocking the coworker who returns extra change, calling them a "goody-goody".'),
 'Desvalorização reativa': (
  'Dar menos valor a uma proposta só porque ela vem de alguém visto como adversário. A mesma ideia parece melhor quando vem do próprio lado.',
  'Rejeitar um plano do síndico rival que você teria aplaudido se viesse do seu candidato.',
  'Giving less value to a proposal just because it comes from someone seen as an opponent. The same idea seems better when it comes from one\'s own side.',
  'Rejecting a plan from the rival building manager that you would have applauded coming from your own candidate.'),
 'Efeito do mensageiro': (
  'Julgar uma mensagem pela pessoa que a transmite: a mesma informação é aceita ou rejeitada conforme a simpatia, o status ou o grupo de quem fala.',
  'Aceitar um conselho financeiro de um amigo bem-sucedido e recusar o mesmo conselho vindo de um desconhecido.',
  'Judging a message by the person delivering it: the same information is accepted or rejected according to the speaker\'s likability, status or group.',
  'Accepting financial advice from a successful friend and refusing the same advice from a stranger.'),
 'Efeito manada e conformidade social': (
  'Adotar crenças e comportamentos porque muita gente ao redor os adota, e evitar destoar do grupo para não ser rejeitado.',
  'Entrar na fila mais longa do restaurante achando que, se tanta gente espera, a comida deve ser melhor.',
  'Adopting beliefs and behaviors because many people around us adopt them, and avoiding standing out from the group so as not to be rejected.',
  'Joining the longest restaurant queue assuming that, if so many people wait, the food must be better.'),
 'Ignorância pluralista': (
  'Quando muitos discordam de algo em silêncio, mas cada um acha que é o único, porque os outros também não dizem nada.',
  'Numa aula, ninguém pergunta porque cada um acha que só ele não entendeu.',
  'When many people privately disagree with something, but each thinks they are the only one, because the others say nothing either.',
  'In a class, no one asks a question because each thinks they alone did not understand.'),
 'Efeito do padrão': (
  'Ficar com a opção que já vem pronta, a que acontece se ninguém escolher, mesmo quando outra seria preferida.',
  'Aceitar as configurações de fábrica de um aplicativo sem nunca abrir o menu.',
  'Sticking with the option that comes ready-made, the one that happens if no one chooses, even when another would be preferred.',
  'Accepting an app\'s factory settings without ever opening the menu.'),
 'Efeito da verdade ilusória e da mera exposição': (
  'O que se ouve muitas vezes passa a parecer verdadeiro, e o que é familiar passa a parecer melhor, mesmo sem nenhuma prova nova.',
  'Acreditar num ditado popular só porque o ouviu a vida inteira.',
  'What one hears many times starts to seem true, and what is familiar starts to seem better, even without any new evidence.',
  'Believing a popular saying just because you have heard it all your life.'),
 'Viés de omissão e viés do perpetrador': (
  'Julgar um dano causado por uma ação como pior do que o mesmo dano causado por omitir uma ajuda, e dar mais peso aos danos que têm um culpado claro.',
  'Achar grave empurrar alguém na piscina, mas não deixar de jogar a boia para quem está se afogando.',
  'Judging a harm caused by an action as worse than the same harm caused by failing to help, and giving more weight to harms that have a clear culprit.',
  'Thinking it is serious to push someone into a pool, but not to fail to throw a life ring to someone drowning.'),
 'Viés de intenção': (
  'Reagir com mais força a um dano quando alguém o causou de propósito do que a um dano igual que aconteceu sem intenção, como por causas naturais.',
  'Ficar indignado com quem quebrou um vaso de raiva, mas indiferente ao vaso quebrado pelo vento, embora o prejuízo seja o mesmo.',
  'Reacting more strongly to a harm when someone caused it on purpose than to an equal harm that happened without intent, such as from natural causes.',
  'Being outraged at someone who smashed a vase in anger, but indifferent to a vase broken by the wind, though the loss is the same.'),
 'Viés teleológico e detecção de agente': (
  'Ver propósito e intenção onde há apenas processos: pensar que as coisas da natureza "existem para" algo, ou que alguém as planejou.',
  'Achar que a chuva caiu "para" estragar o seu passeio.',
  'Seeing purpose and intention where there are only processes: thinking that things in nature "exist for" something, or that someone planned them.',
  'Feeling that the rain fell "to" ruin your outing.'),
 'Ameaça simbólica': (
  'Perceber um grupo como ameaça aos valores, às crenças e ao modo de vida do próprio grupo, mesmo quando ele não ameaça nada material. Na teoria da ameaça intergrupal, de Walter e Cookie Stephan (2000), essa ameaça simbólica se distingue da ameaça realista, que diz respeito à segurança ou aos recursos. Os veganos não tiram nada de ninguém, mas destoam da norma de comer animais, e por isso costumam ser sentidos como ameaça a tradições e identidades.',
  'Ver o vizinho que passou a ir de bicicleta ao trabalho como uma crítica ao seu carro, embora ele nunca tenha dito nada.',
  'Perceiving a group as a threat to one’s own group’s values, beliefs and way of life, even when it threatens nothing material. In the intergroup threat theory of Walter and Cookie Stephan (2000), this symbolic threat is distinguished from realistic threat, which concerns safety or resources. Vegans take nothing from anyone, but they depart from the norm of eating animals, and so they are often felt as a threat to traditions and identities.',
  'Taking the neighbour who started cycling to work as a criticism of your car, even though they never said a word.'),
 'Desaparecimento da compaixão': (
  'Quanto mais vítimas, menos se sente por cada uma. Uma vítima identificável comove mais do que milhões descritas por números.',
  'A foto de uma criança comove mais do que a notícia de que milhares passam fome.',
  'The more victims there are, the less one feels for each. One identifiable victim moves people more than millions described in numbers.',
  'A photo of one child moves people more than the news that thousands are starving.'),
 'Aversão à perda e efeito dotação': (
  'Sentir uma perda com mais força do que um ganho do mesmo tamanho, e dar mais valor ao que já se tem só por já ser nosso.',
  'Recusar trocar uma caneca velha por uma nova igual, só porque a velha já é sua.',
  'Feeling a loss more strongly than a gain of the same size, and valuing what one already has more just because it is ours.',
  'Refusing to swap an old mug for an identical new one, just because the old one is yours.'),
 'Custo irrecuperável e justificação do esforço': (
  'Continuar num caminho porque já se investiu muito nele, e não porque ele ainda vale a pena; e valorizar algo só porque custou caro ou deu trabalho.',
  'Ficar até o fim de um filme ruim porque o ingresso já foi pago.',
  'Continuing down a path because much has already been invested in it, not because it is still worthwhile; and valuing something just because it was costly or hard.',
  'Sitting through a bad film to the end because the ticket is already paid for.'),
 'Retrospecção rosada': (
  'Lembrar o passado como melhor do que foi, guardando os bons momentos e esquecendo os ruins.',
  'Lembrar da escola só pelas amizades e esquecer as provas e o tédio.',
  'Remembering the past as better than it was, keeping the good moments and forgetting the bad ones.',
  'Remembering school only for the friendships and forgetting the exams and the boredom.'),
 'Excesso de confiança (Dunning-Kruger)': (
  'Quem sabe pouco sobre um assunto tende a superestimar o que sabe, porque falta justamente o conhecimento necessário para perceber os próprios erros.',
  'Depois de assistir a alguns vídeos, achar que entende mais de medicina do que o médico.',
  'Those who know little about a subject tend to overestimate what they know, because they lack precisely the knowledge needed to notice their own errors.',
  'After watching a few videos, thinking you understand medicine better than the doctor.'),
 'Realismo ingênuo e ponto cego do viés': (
  'Achar que vemos o mundo como ele é, de forma neutra, e que quem discorda é que está sendo enviesado, desinformado ou ideológico.',
  'Achar que o próprio sotaque é "neutro" e que os outros é que falam com sotaque.',
  'Believing we see the world as it is, neutrally, and that those who disagree are the ones who are biased, uninformed or ideological.',
  'Thinking your own accent is "neutral" and that it is other people who have accents.'),
 'Pensamento antropocêntrico': (
  'Usar o ser humano como medida de tudo, inclusive do que conta como inteligência ou sentimento, de modo que só o que se parece conosco é reconhecido.',
  'Achar que só é música o que segue as regras da música que conhecemos.',
  'Using the human being as the measure of everything, including what counts as intelligence or feeling, so that only what resembles us is recognized.',
  'Thinking that only what follows the rules of the music we know counts as music.'),
 'Viés do natural': (
  'Preferir o que é considerado natural e desconfiar do que é considerado artificial, mesmo quando não há diferença de qualidade ou de segurança. É a versão psicológica do apelo à natureza.',
  'Preferir um suco "natural" com mais açúcar a um com adoçante, achando que é automaticamente mais saudável.',
  'Preferring what is considered natural and distrusting what is considered artificial, even when there is no difference in quality or safety. It is the psychological counterpart of the appeal to nature.',
  'Preferring a "natural" juice with more sugar to one with sweetener, assuming it is automatically healthier.'),
 'Viés de disponibilidade': (
  'Julgar a frequência ou o risco de algo pela facilidade com que exemplos vêm à mente, como o caso de um conhecido ou uma notícia marcante, e não pelos dados.',
  'Ter mais medo de avião do que de carro depois de ver um acidente aéreo no noticiário.',
  'Judging how frequent or risky something is by how easily examples come to mind, such as an acquaintance\'s case or a striking news story, rather than by the data.',
  'Being more afraid of flying than of driving after seeing a plane crash on the news.'),
 'Viés de autoridade': (
  'Dar peso excessivo à opinião de quem tem status ou posição de autoridade, inclusive fora da área em que essa pessoa é especialista.',
  'Seguir o conselho de investimento de um médico só porque ele é médico.',
  'Giving excessive weight to the opinion of those with status or authority, including outside the area in which they are experts.',
  'Following a doctor\'s investment advice just because they are a doctor.'),
 'Viés do presente': (
  'Dar peso demais ao que acontece agora e de menos às consequências futuras, mesmo quando elas são maiores.',
  'Adiar a consulta ao dentista para evitar o incômodo de hoje e acabar com um problema maior depois.',
  'Giving too much weight to what happens now and too little to future consequences, even when they are larger.',
  'Putting off the dentist to avoid today\'s discomfort and ending up with a bigger problem later.'),
 'Efeito halo': (
  'Deixar que uma qualidade positiva de alguém ou de algo influencie a avaliação de todas as outras qualidades, sem relação entre elas.',
  'Achar que uma pessoa bonita também deve ser honesta e competente.',
  'Letting one positive quality of someone or something influence the assessment of all their other qualities, with no link between them.',
  'Assuming that a good-looking person must also be honest and competent.'),
 'Orientação à dominância social': (
  'Traço de personalidade de quem aceita ou prefere hierarquias entre grupos, com uns acima e outros abaixo. Pesquisas o associam tanto ao preconceito contra grupos humanos quanto à aceitação do uso de animais.',
  'Achar natural que certas pessoas sirvam e outras mandem, sem perguntar por quê.',
  'A personality trait of those who accept or prefer hierarchies between groups, with some above and others below. Research links it both to prejudice against human groups and to acceptance of using animals.',
  'Finding it natural that some people serve and others give orders, without asking why.'),
 'Essencialismo psicológico': (
  'Supor que cada categoria tem uma essência fixa e invisível que define o que seus membros são e o que lhes é devido, como se "ser animal" ou "ser humano" determinasse tudo.',
  'Achar que um objeto usado por alguém famoso carrega algo dessa pessoa.',
  'Assuming that each category has a fixed, invisible essence that defines what its members are and what they are owed, as if "being an animal" or "being human" determined everything.',
  'Feeling that an object used by someone famous carries something of that person.'),
 'Masculinidade e carne': (
  'Associação cultural entre comer carne e ser homem, força ou virilidade. Recusar a carne passa a parecer uma ameaça à identidade masculina, e não apenas uma escolha alimentar.',
  'Achar que pedir salada num churrasco de amigos "pega mal" para um homem.',
  'The cultural association between eating meat and being a man, strength or virility. Refusing meat comes to seem like a threat to male identity, not just a food choice.',
  'Feeling that ordering a salad at a friends\' barbecue "looks bad" for a man.'),
 'Estereótipo': (
  'Atribuir a todos os membros de um grupo características que valem, no máximo, para alguns, e julgar cada pessoa por essa imagem pronta.',
  'Achar que todo torcedor de um time rival é briguento.',
  'Attributing to all members of a group traits that apply, at most, to some, and judging each person by that ready-made image.',
  'Thinking every fan of a rival team is a troublemaker.'),
 'Dissociação e eufemismo': (
  'Separar mentalmente o animal da comida, por exemplo com palavras diferentes para o animal e para a carne, ou com embalagens que escondem a origem. A separação facilita comer sem pensar no animal.',
  'Comprar "nuggets" sem pensar na galinha, e "bacon" sem pensar no porco.',
  'Mentally separating the animal from the food, for example with different words for the animal and the meat, or packaging that hides the origin. The separation makes it easier to eat without thinking of the animal.',
  'Buying "nuggets" without thinking of the chicken, and "bacon" without thinking of the pig.'),
 'Falso consenso': (
  'Superestimar quantas pessoas pensam e agem como nós, e por isso tomar a própria opinião como óbvia ou universal.',
  'Achar que "todo mundo" vota no mesmo candidato que você e seus amigos.',
  'Overestimating how many people think and act as we do, and therefore taking one\'s own opinion as obvious or universal.',
  'Thinking "everyone" votes for the same candidate as you and your friends.'),
 'Neofobia alimentar': (
  'Desconfiar de alimentos desconhecidos e recusá-los antes de provar. Com a exposição repetida, a resistência costuma diminuir.',
  'A criança que recusa uma fruta nova só por não conhecer, e passa a gostar depois de provar algumas vezes.',
  'Distrusting unfamiliar foods and refusing them before tasting. With repeated exposure, the resistance usually decreases.',
  'The child who refuses a new fruit just because it is unfamiliar, and comes to like it after tasting it a few times.'),
 'Efeito nocebo': (
  'A expectativa de que algo fará mal pode produzir sintomas reais, mesmo quando a causa não está ali. É o oposto do efeito placebo.',
  'Ler a bula de um remédio, esperar dor de cabeça e sentir dor de cabeça, mesmo tomando um comprimido sem princípio ativo.',
  'Expecting something to cause harm can produce real symptoms, even when the cause is not there. It is the opposite of the placebo effect.',
  'Reading a medicine\'s leaflet, expecting a headache and getting one, even after taking a pill with no active ingredient.'),
 'Viés de saliência': (
  'Dar mais peso ao que chama atenção, por ser visível, vívido ou fácil de perceber, do que ao que realmente pesa mais.',
  'Achar que o ar-condicionado gasta mais energia que a geladeira, porque o barulho dele é mais notável.',
  'Giving more weight to what catches attention, because it is visible, vivid or easy to perceive, than to what actually matters more.',
  'Thinking the air conditioner uses more energy than the fridge, because its noise is more noticeable.'),
 'Viés do meio-termo': (
  'Achar que a posição intermediária é sempre a mais sensata, só por estar no meio. É a tendência psicológica por trás da falácia do falso meio-termo.',
  'Escolher sempre o tamanho médio do café, sem pensar no quanto se quer beber.',
  'Believing the intermediate position is always the most sensible, just because it is in the middle. It is the psychological tendency behind the false middle ground fallacy.',
  'Always choosing the medium coffee, without thinking about how much you want to drink.'),
 'Lacuna de empatia': (
  'Sentir menos empatia por um ser quanto mais diferente ele é de nós, ou quanto mais distante na evolução, mesmo quando ele pode sofrer.',
  'Comover-se mais com um vizinho doente do que com milhares de doentes num país distante.',
  'Feeling less empathy for a being the more different it is from us, or the more distant in evolution, even when it can suffer.',
  'Being more moved by a sick neighbor than by thousands of sick people in a distant country.'),
 'Tamanhismo': (
  'Dar menos importância a um ser por ele ser pequeno, como se o tamanho do corpo medisse o tamanho do que ele pode sofrer.',
  'Achar que a dor de uma criança importa menos do que a de um adulto porque ela é menor.',
  'Giving less importance to a being because it is small, as if body size measured how much it can suffer.',
  'Thinking a child\'s pain matters less than an adult\'s because the child is smaller.'),
 'Inteligentismo': (
  'Dar menos importância a um ser por considerá-lo pouco inteligente, como se a inteligência medisse a capacidade de sofrer ou o direito de não ser prejudicado.',
  'Achar que tudo bem enganar alguém porque ele "não é muito esperto".',
  'Giving less importance to a being because it is considered not very intelligent, as if intelligence measured the capacity to suffer or the claim not to be harmed.',
  'Thinking it is fine to cheat someone because they are "not very bright".'),
 'Substratismo': (
  'Dar menos importância a um ser por causa do material de que ele é feito, como silício em vez de carbono, antes de examinar se ele pode ter experiências.',
  'Achar que uma carta não diz nada só porque foi escrita a máquina, e não à mão.',
  'Giving less importance to a being because of the material it is made of, such as silicon rather than carbon, before examining whether it can have experiences.',
  'Thinking a letter says nothing just because it was typed rather than handwritten.'),
 'Viés de proporção': (
  'Julgar uma ajuda pela fração do problema que ela resolve, e não pelo número de indivíduos que ela alcança. Salvar mil parece pouco quando o problema tem um milhão, embora sejam mil vidas.',
  'Achar que não vale ajudar num abrigo porque ele não acaba com todos os animais de rua.',
  'Judging help by the fraction of the problem it solves, rather than by the number of individuals it reaches. Saving a thousand seems little when the problem has a million, although it is a thousand lives.',
  'Thinking it is not worth helping at a shelter because it will not end all stray animals.'),
 'Hipótese do mundo justo': (
  'Acreditar que o mundo é justo e que, por isso, quem sofre de algum modo merece ou recebe o que lhe cabe. A crença tranquiliza, mas leva a culpar ou ignorar as vítimas.',
  'Dizer que quem foi assaltado "devia ter tomado mais cuidado".',
  'Believing the world is just and that, therefore, those who suffer somehow deserve it or get what is coming to them. The belief is reassuring, but it leads to blaming or ignoring victims.',
  'Saying that someone who was robbed "should have been more careful".'),
 'Negligência da probabilidade': (
  'Decidir sob incerteza sem pesar a probabilidade, tratando um risco como certo ou como inexistente, em vez de considerar a chance e o tamanho do dano juntos.',
  'Não fazer seguro porque "acidente não acontece comigo", ou ter pânico de algo raríssimo.',
  'Deciding under uncertainty without weighing probability, treating a risk as certain or nonexistent, instead of considering the chance and the size of the harm together.',
  'Skipping insurance because "accidents do not happen to me", or panicking about something extremely rare.'),
 'Efeito de ambiguidade': (
  'Evitar opções cuja chance de dar certo é desconhecida, preferindo as de resultado conhecido, mesmo quando as incertas podem ser as melhores.',
  'Continuar num emprego ruim porque o novo, embora promissor, tem riscos que não dá para calcular.',
  'Avoiding options whose chance of success is unknown, preferring those with known outcomes, even when the uncertain ones may be better.',
  'Staying in a bad job because the new one, though promising, has risks that cannot be calculated.'),
 'Viés de avaliabilidade': (
  'Dar mais peso ao que é fácil de medir ou comparar do que ao que mais importa, só porque o primeiro é mais visível nos números.',
  'Escolher um celular pelo número de megapixels, que é fácil de comparar, e não pela qualidade real das fotos.',
  'Giving more weight to what is easy to measure or compare than to what matters most, just because the former is more visible in numbers.',
  'Choosing a phone by its megapixel count, which is easy to compare, rather than by the real quality of its photos.'),
 'Negligência da duração': (
  'Avaliar uma experiência pelos momentos mais marcantes e pelo final, sem levar em conta quanto tempo ela durou.',
  'Lembrar de umas férias como ótimas por causa do último dia, esquecendo uma semana de chuva.',
  'Judging an experience by its most striking moments and its ending, without taking into account how long it lasted.',
  'Remembering a holiday as great because of the last day, forgetting a week of rain.'),
 'Viés pró-inovação': (
  'Superestimar o que uma inovação vai resolver e quão rápido, sem ver seus limites, custos e riscos.',
  'Achar que um aplicativo novo vai resolver sozinho a desorganização de uma empresa.',
  'Overestimating what an innovation will solve and how quickly, without seeing its limits, costs and risks.',
  'Thinking a new app will single-handedly fix a company\'s disorganization.'),
 'Digitalização de crenças': (
  'Tratar uma probabilidade como se fosse zero ou um, como certeza ou impossibilidade, em vez de levar a incerteza em conta.',
  'Dizer que "não vai chover" quando a previsão dá 30% de chance, e sair sem guarda-chuva.',
  'Treating a probability as if it were zero or one, as certainty or impossibility, instead of taking the uncertainty into account.',
  'Saying "it will not rain" when the forecast gives a 30% chance, and going out without an umbrella.'),
 'Perseverança da crença': (
  'Manter uma crença mesmo depois de ver as evidências em que ela se apoiava serem derrubadas.',
  'Continuar achando que um colega roubou algo mesmo depois de o objeto aparecer na sua própria gaveta.',
  'Holding on to a belief even after seeing the evidence it rested on being knocked down.',
  'Still thinking a coworker stole something even after the item turns up in your own drawer.'),
 'Efeito de influência contínua': (
  'Uma informação já corrigida continua a influenciar o que a pessoa pensa e decide, porque a correção não apaga a primeira impressão.',
  'Continuar desconfiando de um restaurante depois que a notícia sobre intoxicação foi desmentida.',
  'Information that has already been corrected keeps influencing what a person thinks and decides, because the correction does not erase the first impression.',
  'Still distrusting a restaurant after the news about food poisoning was retracted.'),
 'Viés de soma zero': (
  'Ver uma situação como disputa em que o ganho de um é necessariamente a perda de outro, mesmo quando os dois podem ganhar ou quando os recursos não são os mesmos.',
  'Achar que, se o colega for elogiado, sobra menos elogio para você.',
  'Seeing a situation as a contest in which one side\'s gain is necessarily the other\'s loss, even when both can gain or when the resources are not the same.',
  'Thinking that if your coworker is praised, there is less praise left for you.'),
 'Cascata de disponibilidade': (
  'Uma ideia ganha credibilidade por ser muito repetida em público, e quanto mais credibilidade ganha, mais é repetida, num ciclo que se alimenta sozinho.',
  'Um boato sobre um produto se espalha nas redes e, de tanto aparecer, vira "fato conhecido".',
  'An idea gains credibility by being repeated a lot in public, and the more credibility it gains, the more it is repeated, in a self-feeding cycle.',
  'A rumor about a product spreads on social media and, by appearing so often, becomes "common knowledge".'),
 'Correlação ilusória': (
  'Ver ligação entre duas coisas que apenas aconteceram juntas algumas vezes, ou perceber uma relação mais forte do que a que existe.',
  'Achar que lavar o carro faz chover, porque lembra das vezes em que choveu logo depois.',
  'Seeing a link between two things that merely happened together a few times, or perceiving a stronger relationship than actually exists.',
  'Thinking washing the car makes it rain, because you remember the times it rained right after.'),
 'Efeito de enquadramento': (
  'A mesma informação leva a julgamentos diferentes conforme o modo como é apresentada, por exemplo pelo lado do ganho ou da perda, ou com uma palavra mais suave.',
  'Uma carne "90% magra" parece melhor que uma "com 10% de gordura", embora sejam a mesma.',
  'The same information leads to different judgments depending on how it is presented, for example in terms of gains or losses, or with a gentler word.',
  'Meat that is "90% lean" seems better than meat that is "10% fat", although they are the same.'),
 'Ilusão de profundidade explicativa': (
  'Achar que se entende como algo funciona muito melhor do que de fato se entende. A ilusão costuma desaparecer quando se tenta explicar o assunto passo a passo.',
  'Achar que sabe como funciona um zíper até tentar explicar a alguém.',
  'Thinking one understands how something works much better than one actually does. The illusion usually vanishes when one tries to explain the subject step by step.',
  'Thinking you know how a zipper works until you try to explain it to someone.'),
}

# Itens de "Pare de dizer isso" (frase em português) -> falácias e vieses que eles cometem.
RUINS_ERROS = {
 'Ser vegano vai te deixar mais saudável.': ['Generalização precipitada'],
 'Vire vegano pelo planeta.': ['Mudança de questão (red herring)'],
 'Ser vegano evita pandemias.': ['Generalização precipitada', 'Mudança de questão (red herring)'],
 'As superbactérias vêm dos antibióticos dados aos animais.': ['Mudança de questão (red herring)'],
 'Quem come carne é psicopata.': ['Ad hominem e envenenamento do poço', 'Generalização precipitada', 'Estereótipo'],
 'Não veganos são nossos inimigos, e odiá-los é normal.': ['Viés de grupo (ingroup)', 'Generalização precipitada'],
 'Se os humanos desaparecessem, o planeta e os animais ficariam melhores.': ['Apelo à natureza'],
 'Não existe ex-vegano.': ['Definição persuasiva'],
 'Destruir propriedade não é violência.': ['Equívoco', 'Definição persuasiva'],
 'Precisamos dar direitos aos animais.': ['Equívoco'],
 'Todo vegano precisa ser amigável com os não veganos, ou não convencemos ninguém.': ['Falsa dicotomia'],
 'Ser vegano é muito caro.': ['Generalização precipitada'],
 'Todos os animais são mortos conscientes, sem atordoamento.': ['Generalização precipitada'],
 'Na Índia quase todo mundo é vegano.': ['Equívoco'],
 'Hitler nem era vegetariano de verdade.': ['Culpa por associação'],
 'Jesus era vegetariano.': ['Apelo à autoridade'],
 'Grandes gênios como Einstein e Da Vinci eram veganos.': ['Apelo à autoridade'],
 'Os animais são esfolados vivos para fazer casacos de pele.': ['Generalização precipitada'],
 'Os animais têm direito à vida, e ponto.': ['Petição de princípio'],
 'Deus não fez os animais para os humanos.': ['Apelo à autoridade'],
 'Porcos são mais inteligentes que uma criança de três anos.': ['Cherry picking', 'Inteligentismo'],
 'Os humanos vêm primeiro.': ['Critério arbitrário (especismo)'],
 'Essa lei parcial é injusta com os outros animais.': ['Falácia do nirvana'],
 'Não é sua mãe, não é seu leite.': ['Apelo à natureza'],
 'Nenhum animal adulto bebe leite.': ['Apelo à natureza'],
 'Ovo é menstruação de galinha.': ['Heurística do afeto'],
 'Numa sala com um coelho e uma maçã, a criança come a maçã e brinca com o coelho.': ['Apelo à natureza'],
 'O ser humano é biologicamente herbívoro.': ['Apelo à natureza', 'Lei de Hume (do é ao deve)'],
 'Está provado que a carne não teve nenhum papel na evolução humana.': ['Generalização precipitada'],
 'Brócolis e espinafre têm mais proteína que carne.': ['Equívoco'],
 'Veganos não precisam suplementar B12.': ['Apelo à natureza'],
 'Toda a B12 da carne vem de suplemento.': ['Generalização precipitada'],
 'A anemia atinge sobretudo quem come carne.': ['Correlação ilusória'],
 'Todas as entidades de nutrição do mundo aprovam a dieta vegana para qualquer pessoa.': ['Generalização precipitada', 'Apelo à autoridade'],
 'Médico não entende nada de nutrição.': ['Generalização precipitada', 'Ad hominem e envenenamento do poço'],
 'Veganos são mais sexies e melhores de cama.': ['Mudança de questão (red herring)'],
 'Está provado que veganos são mais empáticos.': ['Generalização precipitada'],
 'A gorila Koko conversava em língua de sinais.': ['Cherry picking'],
 'Ostras e mexilhões sentem dor como qualquer outro animal.': ['Generalização precipitada'],
 'A pecuária polui mais do que todos os carros, aviões e navios juntos.': ['Cherry picking'],
 'A pecuária causa 51% das emissões de gases de efeito estufa do mundo.': ['Cherry picking'],
 'Testes em animais não servem para nada: 90% dos remédios falham.': ['Generalização precipitada'],
 'A ciência prova que o veganismo é o certo.': ['Lei de Hume (do é ao deve)'],
 'Alimento que pode conter traços de leite não é vegano.': ['Falácia do nirvana'],
 'Carne cultivada não é vegana, pois é de origem animal.': ['Equívoco'],
 'Vegano bom só come natural, orgânico e saudável.': ['Apelo à natureza'],
 'Quem compra produtos de grandes empresas não é vegano.': ['Culpa por associação', 'Falácia do nirvana'],
 'Quem é a favor do capitalismo não é vegano de verdade.': ['Definição persuasiva'],
 'Quem defende mudanças passo a passo não é vegano de verdade.': ['Definição persuasiva', 'Falácia do nirvana'],
 'Quem não aceita mudar pouco a pouco não entende como o mundo funciona.': ['Falsa dicotomia'],
 'Veganos deveriam focar só em ativismo direto, conversando pessoa por pessoa.': ['Falsa dicotomia'],
 'Veganos deveriam focar só em ativismo institucional, mudando leis, regras e decisões judiciais.': ['Falsa dicotomia'],
 'Veganos deveriam focar só em pessoas poderosas e influentes.': ['Falsa dicotomia'],
 'O veganismo não deve se aliar a outras causas, como o feminismo, o abolicionismo ou o transumanismo.': ['Culpa por associação'],
 'Ser vegano exige ser anticapitalista.': ['Definição persuasiva'],
 'Veganismo e ambientalismo sem luta de classes é jardinagem.': ['Apelo ao ridículo', 'Definição persuasiva'],
 'Veganismo que não debate racismo é gastronomia de playboy.': ['Ad hominem e envenenamento do poço', 'Apelo ao ridículo'],
}

# Atribuições do catálogo revistas em 2026-11-22: não se sustentavam no próprio capítulo.
REMOVER = {'Falácia do contínuo': ['F7'], 'Afirmação do consequente': ['C1'], 'Negação de mente': ['J21', 'B9']}
