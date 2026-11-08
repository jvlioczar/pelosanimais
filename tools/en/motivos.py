"""Why the conversation moves from one argument to the next, keyed by the Portuguese text (one 'pt | en' pair per line)."""

_PARES = '''
"Peixe nem grita" é a versão aquática de A3 | "Fish don't even scream" is the underwater version of A3
A acusação de colonialismo vira acusação política | The charge of colonialism becomes a political charge
A autoridade vira tradição | Authority turns into tradition
A busca de uma proteína alternativa | The search for an alternative protein
A caça controla populações | Hunting controls populations
A caça financia a conservação | Hunting funds conservation
A comparação com a natureza vira provocação | The comparison with nature turns into a taunt
A comparação vira provocação | The comparison turns into a taunt
A convenção vira propriedade | Convention turns into property
A criação vira hierarquia de valor | Creation turns into a hierarchy of value
A culpa é da indústria | The industry is to blame
A cultura vira escolha pessoal | Culture turns into personal choice
A cultura vira lei | Culture turns into law
A deficiência vira estereótipo | The deficiency turns into a stereotype
A dependência vira impossibilidade | Dependence turns into impossibility
A dificuldade vira "faço o que posso" | Difficulty turns into "I do what I can"
A discordância vira rótulo de uma única escola | Disagreement becomes the label of a single school
A dúvida vira desafio sobre os limites | Doubt becomes a challenge about the limits
A espécie continua graças à criação | The species survives thanks to farming
A espécie continua, então seria só o ciclo da vida | The species carries on, so it would just be the circle of life
A espécie vira o próprio objeto de valor | The species itself becomes what has value
A espécie é trocada pelas capacidades | Species is swapped for abilities
A exclusão do contrato vira falta de direitos | Exclusion from the contract becomes a lack of rights
A existência vira um problema prático | Their existence becomes a practical problem
A experiência dos avós vira tradição | The grandparents' experience turns into tradition
A família vira cultura | Family turns into culture
A força vira masculinidade | Strength turns into masculinity
A força vira superioridade | Strength turns into superiority
A hierarquia vira ordem de prioridades | Hierarchy turns into an order of priorities
A ideologia vira mera opinião | Ideology becomes mere opinion
A imperfeição vira acusação de hipocrisia | Imperfection becomes a charge of hypocrisy
A intensidade vira prioridade | Intensity turns into priority
A invenção vira contrato | The invention turns into a contract
A irritação vira desprezo | Irritation turns into contempt
A irritação vira provocação | Irritation turns into a taunt
A lei vira tradição | The law turns into tradition
A maioria vira neutralidade | The majority turns into neutrality
A mensagem vira irritação com o mensageiro | The message turns into irritation with the messenger
A moda passaria | The fad would pass
A moda é associada a produtos caros | The fad is linked to expensive products
A necessidade de suplemento vira incapacidade do corpo | The need for a supplement becomes the body's inability
A necessidade vira estereótipo | Necessity turns into a stereotype
A posição vira poder | Position turns into power
A preferência pelos nossos vira um dilema de vida ou morte | Preferring our own becomes a life-or-death dilemma
A premissa escondida do abate humanitário | The hidden premise of humane slaughter
A prioridade vira uma fila de causas | Priority turns into a queue of causes
A provocação revela o prazer | The taunt reveals the pleasure
A provocação vira defesa da liberdade | The taunt becomes a defense of freedom
A racionalidade é reembalada como o que define uma pessoa | Rationality is repackaged as what defines a person
A razão vira medida do sofrimento | Reason becomes the measure of suffering
A rejeição da analogia ganha uma justificativa | Rejecting the analogy gets a justification
A responsabilidade seria do sistema | The responsibility would lie with the system
A superioridade vira a alma | Superiority turns into the soul
A superioridade vira a linguagem | Superiority turns into language
A suposta misantropia vira acusação | Supposed misanthropy becomes an accusation
A sustentabilidade vira critério moral | Sustainability becomes a moral criterion
A sustentabilidade vira justificativa | Sustainability becomes a justification
A tradição vira afeto | Tradition turns into affection
A tradição vira identidade cultural | Tradition turns into cultural identity
A vaca leiteira vira um animal feito para dar leite | The dairy cow becomes an animal made to give milk
A versão agrícola do "você também" | The farming version of "you do it too"
A versão de quem está diante da prateleira | The version of the person standing at the shelf
A versão geral: se não é perfeito, não vale | The general version: if it isn't perfect, it doesn't count
A versão médica | The medical version
A versão totalmente franca | The completely frank version
A vontade vira incapacidade do corpo | The craving becomes the body's inability
Acusa de hipocrisia | Accuses of hypocrisy
Acusa de incoerência | Accuses of inconsistency
Acusa quem não prioriza do mesmo jeito | Accuses those who don't prioritize the same way
Acusa quem toma remédio | Accuses those who take medicine
Acusa veganos de não ligar para humanos | Accuses vegans of not caring about humans
Admite a contradição e não muda | Admits the contradiction and doesn't change
Admite que não vai mudar | Admits they won't change
Admite que o que importa é o sabor | Admits that what matters is the taste
Afirma que o leite é necessário | Claims that milk is necessary
Afirma que ordenhar até ajuda a vaca | Claims that milking even helps the cow
Ama os animais, mas gosta de carne | Loves animals, but likes meat
Apela ao caso do ovo da galinha resgatada | Appeals to the case of the rescued hen's egg
Apela ao domínio dado por Deus | Appeals to God-given dominion
Apela ao médico | Appeals to the doctor
Apela ao pediatra | Appeals to the pediatrician
Apelo a um exemplo religioso concreto | Appeal to a concrete religious example
As capacidades voltam a ser atribuídas à espécie | Abilities are attributed to the species again
As ovelhas existiriam para isso | Sheep would exist for this
As plantas também se defendem | Plants defend themselves too
Associa o veganismo a figuras odiadas | Links veganism to hated figures
Ataca os ultraprocessados veganos | Attacks ultra-processed vegan food
Ativistas seriam radicais | Activists would be radicals
Ativistas são extremistas | Activists are extremists
Até lá, uma pessoa não faz diferença | Until then, one person makes no difference
Busca a origem desse valor na alma | Looks for the source of that value in the soul
Busca na natureza um exemplo para imitar | Looks to nature for an example to copy
Busca outro caso sem dano aparente | Looks for another case with no apparent harm
Busca outro caso-limite | Looks for another edge case
Busca um caso de fronteira favorável | Looks for a favorable borderline case
Busca um caso em que a preferência pareça óbvia | Looks for a case where the preference seems obvious
Busca um caso em que a preferência por humanos pareça óbvia | Looks for a case where preferring humans seems obvious
Busca um caso em que a tradição pareça intocável | Looks for a case where tradition seems untouchable
Busca-se um povo cuja cultura pareça intocável | A people whose culture seems untouchable is sought
Cada um decide | Everyone decides for themselves
Carne é coisa de macho | Meat is for real men
Caso genuíno de incerteza, tratado à parte | A genuine case of uncertainty, treated separately
Cita um caso concreto | Cites a concrete case
Como os especialistas, admite o erro e não muda | Like the experts, admits the error and doesn't change
Concede a dor e desloca para a morte | Concedes the pain and shifts to death
Concede a dor e desloca para o método | Concedes the pain and shifts to the method
Concede a dor e nega a gravidade | Concedes the pain and denies its seriousness
Concede a dor, mas nega que a morte prejudique | Concedes the pain, but denies that death harms
Conclui que a moral é relativa | Concludes that morality is relative
Conclui que carne é necessária | Concludes that meat is necessary
Conclui que nenhuma dieta é inocente | Concludes that no diet is innocent
Confia que a lei garante o bem-estar | Trusts the law to guarantee welfare
Confusão entre dever de agente e proteção de paciente | Confusing an agent's duties with a patient's protection
Conhece alguém que ficou anêmico | Knows someone who became anemic
Conhece um caso de criança doente | Knows of a sick child
Continuação natural: a discussão vira gravidade da morte | Natural next step: the discussion turns to how serious death is
Contrapõe o caso de alguém que adoeceu | Counters with the case of someone who got sick
Converte a norma em dignidade | Turns the norm into dignity
Criticar é etnocentrismo | Criticizing is ethnocentric
Da alma passa-se ao mandato divino | From the soul to a divine mandate
Da anatomia passa-se à necessidade | From anatomy to necessity
Da cozinha passa-se à vida social | From the kitchen to social life
Da escolha pessoal passa-se à moral pessoal | From personal choice to personal morality
Da falta de relato passa-se à negação da experiência | From the lack of a report to denying the experience
Da fome extrema passa-se à necessidade cotidiana | From extreme hunger to everyday necessity
Da intervenção na natureza passa-se à caça | From intervening in nature to hunting
Da morte sem dor passa-se à vida boa | From painless death to a good life
Da pesca esportiva passa-se à pesca comercial | From sport fishing to commercial fishing
Da proteína passa-se aos micronutrientes | From protein to micronutrients
Defende a carne de pasto local | Defends local grass-fed meat
Defende a carne local | Defends local meat
Defende a carne orgânica | Defends organic meat
Defende a dieta carnívora | Defends the carnivore diet
Defende a pecuária regenerativa | Defends regenerative grazing
Defende a pesca sustentável | Defends sustainable fishing
Defende o entretenimento como cultura | Defends entertainment as culture
Defende o gado em terras não agrícolas | Defends cattle on land unfit for crops
Defende os aquários | Defends aquariums
Defende que direitos são só para humanos | Argues that rights are only for humans
Defende só a redução | Defends reduction only
Depois da provocação, resta a franqueza: não vou mudar | After the taunt, only frankness is left: I won't change
Depois de rotular, aponta-se uma falha da pessoa | After the label, a flaw in the person is pointed out
Desloca a discussão da dor para a morte | Shifts the discussion from pain to death
Desloca do indivíduo para a coletividade | Shifts from the individual to the collective
Desloca para um dilema trágico | Shifts to a tragic dilemma
Diante das imagens, afirma-se que o padrão é outro | Faced with the footage, it is claimed the standard is different
Dilemas de cálculo associam a defesa animal ao utilitarismo | Trade-off dilemmas link animal advocacy to utilitarianism
Diz que a OMS exagera | Says the WHO exaggerates
Diz que a lei garante o resto | Says the law guarantees the rest
Diz que a soja desmata | Says soy causes deforestation
Diz que comer carne nos fez evoluir | Says eating meat made us evolve
Diz que comida vegana é sem graça | Says vegan food is bland
Diz que compra de animais soltos | Says they buy free-range
Diz que dieta com suplemento não é natural | Says a diet that needs supplements isn't natural
Diz que imitar carne é querer carne | Says imitating meat means wanting meat
Diz que insetos não sentem | Says insects don't feel
Diz que já come pouca carne | Says they already eat little meat
Diz que nem os filósofos concordam | Says even philosophers don't agree
Diz que nutrição não é ciência sólida | Says nutrition isn't solid science
Diz que o Estado não pode proibir | Says the state can't ban it
Diz que o leite não mata ninguém | Says milk doesn't kill anyone
Diz que os vídeos são exceções | Says the videos are exceptions
Diz que ostras e mexilhões não sentem | Says oysters and mussels don't feel
Diz que peixes não sentem dor | Says fish don't feel pain
Diz que veganos são fracos | Says vegans are weak
Diz que é agenda contra o agro | Says it's an agenda against farmers
Diz que é agenda política | Says it's a political agenda
Diz que é emoção, não ciência | Says it's emotion, not science
Do "sem direitos" passa-se ao estatuto de coisa | From "no rights" to the status of a thing
Do caso da sobra passa-se à ideia de que uma compra não muda nada | From leftovers to the idea that one purchase changes nothing
Do caso individual passa-se às estatísticas de desistência | From the individual case to statistics on quitting
Do costume passa-se à natureza | From custom to nature
Do couro passa-se à lã | From leather to wool
Do desacordo passa-se ao relativismo | From disagreement to relativism
Do dilema humano passa-se aos predadores | From the human dilemma to predators
Do dilema volta-se à preferência pelos nossos | From the dilemma back to preferring our own
Do dinheiro passa-se ao tempo | From money to time
Do estatuto de propriedade passa-se à legalidade | From property status to legality
Do excesso passa-se à existência | From excess to existence
Do incentivo legal passa-se ao econômico | From the legal incentive to the economic one
Do incômodo com a pessoa passa-se à acusação de incoerência | From annoyance with the person to a charge of inconsistency
Do incômodo passa-se ao rótulo de seita | From annoyance to the "cult" label
Do leite como necessidade passa-se ao leite como favor à vaca | From milk as a necessity to milk as a favor to the cow
Do número de quem come passa-se ao número de quem desiste | From how many eat meat to how many quit
Do passado passa-se à necessidade | From the past to necessity
Do povo sem alternativa passa-se ao caso hipotético | From a people with no alternative to the hypothetical case
Do preço passa-se ao acesso | From price to access
Do propósito passa-se à propriedade | From purpose to property
Do relativismo cultural passa-se ao relativismo moral | From cultural relativism to moral relativism
Do texto do Gênesis passa-se ao exemplo de Jesus | From Genesis to the example of Jesus
Do topo da cadeia alimentar passa-se à superioridade | From the top of the food chain to superiority
Dos deveres passa-se à definição jurídica de pessoa | From duties to the legal definition of a person
Enquanto isso, como menos | Meanwhile, I eat less
Estende a dúvida a peixes e outros invertebrados | Extends the doubt to fish and invertebrates
Estende a dúvida às plantas | Extends the doubt to plants
Fala do custo social de mudar | Talks about the social cost of changing
Faz o que pode, comendo menos | Does what they can by eating less
Faço o que posso | I do what I can
Generaliza a acusação de hipocrisia | Generalizes the charge of hypocrisy
Generaliza a impotência | Generalizes powerlessness
Generaliza a tese para toda a ética | Generalizes the claim to all of ethics
Generaliza para todo ovo e leite | Generalizes to all eggs and milk
Há problemas humanos mais importantes | There are more important human problems
Há problemas mais importantes | There are more important problems
Junta a morte sem dor à promessa de vida boa | Pairs painless death with the promise of a good life
Junta as duas promessas | Combines the two promises
Lembra os animais da colheita | Brings up the animals killed in harvests
Lembra os animais mortos na colheita | Brings up the animals killed in harvests
Lembra que estamos no topo da cadeia | Points out that we're at the top of the food chain
Lembra quem vive do gado | Brings up the people who live off cattle
Liberdade religiosa usada como escudo | Religious freedom used as a shield
Mas o Estado não pode proibir | But the state can't ban it
Mesma função, por outro caminho | Same function, by another route
Muda de senciência para meio ambiente | Switches from sentience to the environment
Muda do bem-estar para o ambiente | Switches from welfare to the environment
Muda para a necessidade | Switches to necessity
Muda para o transporte | Switches to transport
Muda para os animais mortos na colheita | Switches to the animals killed in harvests
Nenhum vegano é perfeito | No vegan is perfect
Ninguém é perfeito | Nobody's perfect
O afeto declarado vira hierarquia | Declared affection turns into hierarchy
O agro sustenta o país | Agriculture is the backbone of the economy
O animal já estaria morto | The animal would already be dead
O animal já está morto | The animal is already dead
O argumento se estende ao entretenimento | The argument extends to entertainment
O cavalo existiria para ser montado | The horse would exist to be ridden
O ciclo vira natureza | The cycle turns into nature
O corpo não se adaptaria | The body wouldn't adapt
O custo social vira crítica ao vegano | The social cost turns into criticism of the vegan
O debate vira disputa entre crenças | The debate turns into a clash of beliefs
O desejo natural vira, simplesmente, o sabor | The natural craving becomes, simply, the taste
O dilema de emergência vira regra geral | The emergency dilemma becomes a general rule
O dilema vira hierarquia de valor | The dilemma turns into a hierarchy of value
O domínio dado por Deus vira superioridade | God-given dominion turns into superiority
O fanatismo vira extremismo | Fanaticism turns into extremism
O gado aproveita terras ruins | Cattle make use of poor land
O medo de feminização vira masculinidade | The fear of feminization turns into masculinity
O mesmo raciocínio aplicado a mentes ainda mais simples | The same reasoning applied to even simpler minds
O oposto jurídico de pessoa é coisa | The legal opposite of a person is a thing
O potencial é usado para dizer que o bebê é pessoa em formação | Potential is used to say the baby is a person in the making
O problema seria a indústria | The problem would be the industry
O problema seriam os combustíveis fósseis | The problem would be fossil fuels
O que importa é a espécie | What matters is the species
O que importa é a população, não o indivíduo | What matters is the population, not the individual
O radicalismo afastaria as pessoas | Radicalism would push people away
O relativismo vira ceticismo sobre a ética | Relativism turns into skepticism about ethics
O status especial vira superioridade | Special status turns into superiority
O suplemento vira argumento do natural | The supplement becomes an argument from nature
O veganismo vira agenda política | Veganism becomes a political agenda
O veganismo vira seita | Veganism becomes a cult
O veganismo é pintado como radical | Veganism is painted as radical
O veganismo é reduzido a produtos de mercado | Veganism is reduced to store products
Onde termina a cadeia da impotência | Where the chain of powerlessness ends
Opõe ação política e escolha pessoal | Opposes political action to personal choice
Os empregos dependem disso | Jobs depend on it
Os pais decidem a dieta dos filhos | Parents decide their children's diet
Outro rótulo para não discutir | Another label to avoid discussion
Outro uso de insetos defendido como inofensivo | Another use of insects defended as harmless
Passa a negar a dor dos animais | Moves on to denying animal pain
Passa a negar que os peixes sofram | Moves on to denying that fish suffer
Passa a outras autoridades | Moves on to other authorities
Passa ao caso dos atletas | Moves on to athletes
Passa ao dano feito em casa | Moves on to harm done at home
Passa aos animais criados soltos | Moves on to free-range animals
Passa da convenção para a liberdade individual | Moves from convention to individual freedom
Pedida a prova da superioridade, ela vira a racionalidade | Asked to prove superiority, it turns into rationality
Pedido um critério, oferece-se a alma | Asked for a criterion, the soul is offered
Pedido um critério, oferece-se a racionalidade | Asked for a criterion, rationality is offered
Pedido um critério, oferece-se a superioridade | Asked for a criterion, superiority is offered
Peixes não sentem dor | Fish don't feel pain
Perderiam também a identidade | They'd lose their identity too
Pergunta o que fazer com os animais | Asks what to do with the animals
Pergunta onde fica a linha | Asks where the line is
Pergunta pelas crianças | Asks about children
Primeiro os nossos | Our own first
Prioriza os animais de casa | Puts pets first
Prioriza os humanos | Puts humans first
Prioriza os nossos | Puts our own first
Propõe o dilema de quem salvar | Proposes the dilemma of whom to save
Quando a alma não serve de critério público, resta a espécie | When the soul can't serve as a public criterion, species is what's left
Quando a capacidade não se sustenta, sobra a espécie | When ability doesn't hold up, species is what's left
Quando a convenção é questionada, resta a fronteira da espécie | When convention is questioned, the species line is what's left
Quando a definição de pessoa não separa humanos e animais, resta a espécie | When the definition of a person doesn't separate humans and animals, species is what's left
Quando a dor fica visível e audível, evita-se a evidência | When the pain becomes visible and audible, the evidence is avoided
Quando a exclusão de humanos vulneráveis é apontada | When the exclusion of vulnerable humans is pointed out
Quando a força não justifica, resta a espécie | When strength doesn't justify it, species is what's left
Quando a lei não justifica, resta a espécie | When the law doesn't justify it, species is what's left
Quando a liberdade não basta, resta a franqueza | When freedom isn't enough, frankness is what's left
Quando a linguagem não separa humanos e animais, resta a espécie | When language doesn't separate humans and animals, species is what's left
Quando a norma é desmontada, resta a fronteira nua | When the norm is taken apart, the bare boundary is what's left
Quando a superioridade moral cai, resta o poder | When moral superiority falls, power is what's left
Quando a teoria cai, apela-se ao relativismo | When the theory falls, relativism is invoked
Quando a tradição não basta, relativiza-se a moral | When tradition isn't enough, morality is relativized
Quando as três tentativas falham, resta a fronteira nua | When all three attempts fail, the bare boundary is what's left
Quando bebês e pessoas com deficiência entram na conta, apela-se ao normal da espécie | When babies and people with disabilities enter the picture, what's normal for the species is invoked
Quando o ambiente não é a questão, resta a espécie | When the environment isn't the issue, species is what's left
Quando o apelo à natureza falha, busca-se um critério "objetivo" | When the appeal to nature fails, an "objective" criterion is sought
Quando o argumento acaba, resta a honestidade crua | When the argument runs out, raw honesty is what's left
Quando o argumento acaba, resta a provocação | When the argument runs out, the taunt is what's left
Quando o argumento acaba, resta a reação | When the argument runs out, the reaction is what's left
Quando o indivíduo volta ao centro, resta a espécie | When the individual is back at the center, species is what's left
Quando o natural não convence, apela-se ao necessário | When "natural" doesn't convince, "necessary" is invoked
Quando o propósito é atribuído por quem lucra, resta a espécie | When the purpose is assigned by whoever profits, species is what's left
Quando o relativismo cai, resta a franqueza | When relativism falls, frankness is what's left
Quando os vídeos são inegáveis, evita-se vê-los | When the videos are undeniable, people avoid watching them
Quando se admite a dor, discute-se a intensidade | Once pain is admitted, its intensity is debated
Quando se pergunta de onde vem a dignidade | When asked where dignity comes from
Quando se pergunta por que a espécie importa | When asked why species matters
Quando se pergunta por que valeria só para animais | When asked why it would apply only to animals
Quando se pergunta se os insetos sentem | When asked whether insects feel
Quem discorda estaria projetando sentimentos | Anyone who disagrees would be projecting feelings
Quem vive disso perderia o sustento | People who live off it would lose their livelihood
Querem proibir a carne | They want to ban meat
Radicaliza o deslocamento do indivíduo para o grupo | Takes the shift from individual to group to the extreme
Reação aos dados de cognição animal | A reaction to data on animal cognition
Reação à analogia estrutural | A reaction to the structural analogy
Reação à evidência de emoções | A reaction to the evidence of emotions
Reação à ideia de igual consideração | A reaction to the idea of equal consideration
Reação à linguagem de personalidade | A reaction to the language of personhood
Reação às evidências de comunicação e dor | A reaction to the evidence of communication and pain
Reciprocidade virada contra os animais selvagens | Reciprocity turned against wild animals
Reforça com casos conhecidos | Backs it up with well-known cases
Resposta mais comum à sobreposição de espécies | The most common reply to the argument from species overlap
Se a carne local não é mais limpa, resta: se fosse sustentável, tudo bem | If local meat isn't cleaner, what's left is: if it were sustainable, it'd be fine
Se a colheita mata menos, diz-se que nenhum vegano é perfeito | If plant farming kills fewer animals, the reply is that no vegan is perfect
Se a comida vegetal tem sabor, o problema vira o sabor da carne | If plant food has flavor, the problem becomes the taste of meat
Se a compra repõe o estoque, culpa-se a indústria | If buying restocks the shelf, the industry is blamed
Se a comunicação é gradual, pede-se uma fronteira exata | If communication comes in degrees, an exact boundary is demanded
Se a escolha faz diferença, resta a liberdade de escolher | If the choice makes a difference, the freedom to choose is what's left
Se a exceção não vale para todos, relativiza-se a moral | If the exception doesn't apply to everyone, morality is relativized
Se a imperfeição não desobriga, alega-se impotência | If imperfection doesn't let you off, powerlessness is claimed
Se a lei não protege, alega-se que pelo menos o abate é humanitário | If the law doesn't protect, it is claimed that at least slaughter is humane
Se a linha é difícil, cada um traçaria a sua | If the line is hard to draw, everyone would draw their own
Se a maioria não decide, apela-se à antiguidade | If the majority doesn't decide, age is invoked
Se a moral não é tão relativa, volta-se à escolha pessoal | If morality isn't so relative, it goes back to personal choice
Se a moral é um acordo, cada grupo decide quem entra | If morality is a deal, each group decides who is in
Se a morte é dano, alega-se que eles não entendem a própria vida | If death is a harm, it is claimed they don't understand their own lives
Se a natureza não convence, apela-se à necessidade | If nature doesn't convince, necessity is invoked
Se a natureza não é condenada, a carne também seria natural | If nature isn't condemned, meat would be natural too
Se a necessidade extrema não vale para hoje, propõe-se outro dilema | If extreme necessity doesn't apply today, another dilemma is proposed
Se a origem dos direitos não decide, exige-se reciprocidade | If the origin of rights doesn't settle it, reciprocity is demanded
Se a palavra "pessoa" não decide, os direitos seriam convenção humana | If the word "person" doesn't settle it, rights would be a human convention
Se a pecuária usa mais lavoura, diz-se que o gado pasta onde não se planta | If livestock uses more cropland, it's said cattle graze where crops can't grow
Se a proteína não falta, aponta-se a B12 | If protein isn't lacking, B12 is pointed to
Se a proteína vegetal é completa, aponta-se a B12 | If plant protein is complete, B12 is pointed to
Se a razão não importa para sofrer, passa-se a negar que eles sintam | If reason doesn't matter for suffering, the next move is denying they feel
Se a saúde não decide, muda-se para o ambiente | If health doesn't settle it, the topic switches to the environment
Se a soja vai para a ração, lembram-se os animais mortos na colheita | If soy goes to feed, the animals killed in harvests are brought up
Se a terra poderia ser renaturalizada, defende-se o pastoreio regenerativo | If the land could be rewilded, regenerative grazing is defended
Se a tosa não justifica, passa-se ao mel | If shearing doesn't justify it, the topic moves to honey
Se a vida boa não autoriza matar, diz-se que eles nem existiriam | If a good life doesn't license killing, it's said they wouldn't even exist
Se a vida não é tão boa, junta-se a promessa da morte rápida | If the life isn't that good, the promise of a quick death is added
Se as diferenças de dano são enormes, diz-se que o veganismo também não é perfeito | If the differences in harm are huge, it's said veganism isn't perfect either
Se as imagens são reais, alega-se que o padrão é o abate humanitário | If the footage is real, it's claimed the standard is humane slaughter
Se as plantas não contam, pergunta-se onde fica a linha | If plants don't count, the question becomes where the line is
Se dar a vida não autoriza tirá-la, nega-se que a morte prejudique | If giving life doesn't license taking it, the reply is to deny that death harms
Se for sustentável, tudo bem | If it's sustainable, it's fine
Se há exceções, cada um decidiria a sua | If there are exceptions, everyone would decide their own
Se há proteína vegetal, diz-se que ela é incompleta | If there's plant protein, it's said to be incomplete
Se há uma vítima, resta dizer que é só um animal | If there's a victim, what's left is saying it's just an animal
Se muitos sentem, pede-se uma fronteira exata | If many feel, an exact boundary is demanded
Se ninguém é perfeito, os veganos também não | If nobody's perfect, neither are vegans
Se não precisamos policiar leões, apontam-se os insetos que matamos | If we needn't police lions, the insects we kill are pointed out
Se não é caro, aponta-se o custo social | If it isn't expensive, the social cost is pointed out
Se não é tão difícil, admite-se que a questão é o prazer | If it isn't that hard, it's admitted the issue is pleasure
Se não é tão difícil, diz-se que é caro | If it isn't that hard, it's said to be expensive
Se o caso é anedota, diz-se que o próprio corpo não se adapta | If the case is anecdotal, it's said one's own body doesn't adapt
Se o consumo sustenta a indústria, diz-se que nenhum consumo é ético | If consumption sustains the industry, it's said no consumption is ethical
Se o corpo se adapta, resta "meu corpo, minha escolha" | If the body adapts, what's left is "my body, my choice"
Se o dano acidental é diferente, pergunta-se onde fica a linha | If accidental harm is different, the question becomes where the line is
Se o desejo não justifica, apela-se à necessidade | If desire doesn't justify it, necessity is invoked
Se o dilema não autoriza explorar, resta a espécie | If the dilemma doesn't license exploitation, species is what's left
Se o passado não manda, apela-se ao desejo | If the past doesn't decide, desire is invoked
Se o pastoreio não é escalável, defende-se a carne local e orgânica | If grazing can't scale, local organic meat is defended
Se o potencial não protege todos, apela-se ao normal da espécie | If potential doesn't protect everyone, what's normal for the species is invoked
Se o sofrimento é menor, discute-se a morte | If the suffering is smaller, death is debated
Se o suplemento não invalida a dieta, cita-se alguém que adoeceu | If supplements don't invalidate the diet, someone who got sick is cited
Se os direitos não dependem de deveres, diz-se que são invenção só nossa | If rights don't depend on duties, it's said they're our own invention
Se os leões não servem de modelo, apela-se à anatomia | If lions aren't a model, anatomy is invoked
Se peixes e caranguejos sentem, pergunta-se por insetos e bactérias | If fish and crabs feel, the question turns to insects and bacteria
Se poder comer não obriga, apela-se à evolução | If being able to eat it creates no duty, evolution is invoked
Se querem o sabor, carne é gostosa | If they want the taste, meat tastes good
Se reduzir o dano vale, diz-se que cada um faz o que pode | If reducing harm counts, it's said everyone does what they can
Se só conta quem pode ameaçar, conta a força | If only those who can threaten count, strength counts
Se todos morrem, a morte não seria dano | If everyone dies, death wouldn't be a harm
Se é crença, cada um teria a sua | If it's a belief, everyone would have their own
Segunda tentativa de proteger os mesmos casos | Second attempt to protect the same cases
Segunda tentativa de salvar os bebês sem incluir os animais | Second attempt to save the babies without including the animals
Sei que é errado, mas não vou parar | I know it's wrong, but I won't stop
Sem a criação, esses animais nem existiriam | Without farming, these animals wouldn't even exist
Sem a crítica à teoria, sobra a espécie | Without the critique of the theory, species is what's left
Sem critério, o valor vira a própria espécie | Without a criterion, value becomes the species itself
Sem linguagem não há contrato; muda de "sentir" para "negociar" | No language, no contract; the topic moves from "feeling" to "negotiating"
Sem natureza nem costume, resta a espécie | Without nature or custom, species is what's left
Sem o costume, resta a espécie | Without custom, species is what's left
Sem um traço que separe humanos e animais, resta a espécie | Without a trait that separates humans and animals, species is what's left
Sem uma linha exata, volta-se à fronteira da espécie | Without an exact line, it goes back to the species boundary
Sem uma superioridade relevante, resta a espécie | Without a relevant superiority, species is what's left
Sempre fizemos isso | We've always done it
Superado o custo social, sobra o prazer | Once the social cost is dealt with, pleasure is what's left
São só animais | They're just animals
Tenta empatar o placar diluindo o critério | Tries to even the score by diluting the criterion
Tenta reduzir sem abrir mão | Tries to cut back without giving it up
Tentativa mais sofisticada de salvar a fronteira | A more sophisticated attempt to save the boundary
Terceira tentativa, agora pela via afetiva | Third attempt, now through affection
Terceira tentativa, pela via afetiva | Third attempt, through affection
Terceiriza a responsabilidade | Outsources the responsibility
Transfere a responsabilidade ao sistema | Hands the responsibility to the system
Transfere o problema para a escala | Moves the problem to scale
Trata a preocupação como fanatismo | Treats concern as fanaticism
Troca "alma" por "dignidade" | Swaps "soul" for "dignity"
Troca a capacidade pela relação | Swaps ability for relationship
Troca a hierarquia pela parcialidade | Swaps hierarchy for partiality
Troca a pergunta moral pela legal | Swaps the moral question for the legal one
Troca a racionalidade por outro traço, com o mesmo problema | Swaps rationality for another trait, with the same problem
Troca capacidade por valor, sem nova justificativa | Swaps ability for value, with no new justification
Troca contrato por laço afetivo | Swaps contract for emotional bond
Troca o critério pela parcialidade afetiva | Swaps the criterion for emotional partiality
Um mundo vegano é utópico | A vegan world is utopian
Uma pessoa não faz diferença | One person makes no difference
Usa o equilíbrio de populações como critério | Uses population balance as the criterion
Usa os filósofos que defenderam a superioridade humana | Cites the philosophers who defended human superiority
Usa outro grupo sem escolha | Uses another group with no choice
Veganismo é caro | Veganism is expensive
Veganismo é seita | Veganism is a cult
Veganos ligariam mais para animais do que para humanos | Vegans would care more about animals than humans
Veganos são chatos | Vegans are annoying
Versão anatômica do mesmo argumento | Anatomical version of the same argument
Versão cartesiana: sem alma, sem sentir | Cartesian version: no soul, no feeling
Versão do desejo | The craving version
Versão evolutiva | The evolutionary version
Versão prática do mesmo apelo à convenção | The practical version of the same appeal to convention
Volta ao abate humanitário | Back to humane slaughter
Volta aos empregos | Back to jobs
Volta à educação e à conservação | Back to education and conservation
Volta à escolha pessoal | Back to personal choice
Volta à necessidade de produtos animais | Back to needing animal products
Volta à proteína | Back to protein
Volta à água das culturas | Back to the water used by crops
Vou comer o dobro | I'll eat double
Vou esperar a tecnologia | I'll wait for the technology
É minha escolha | It's my choice
É natural | It's natural
Última fronteira do mesmo argumento | The last frontier of the same argument
A sensação de ser julgado vira defesa do caráter | The feeling of being judged becomes a defense of character
Se todo mundo faz, inclusive gente boa, não pode ser errado | If everyone does it, including good people, it can't be wrong
A pessoa boa também diz que ama os animais | The good person also says they love animals
A bondade geral vira licença para não mudar | General goodness becomes a license not to change
O costume explica por que gente boa não vê o problema | Custom explains why good people don't see the problem
A crítica ao sabor vira deboche | Criticism of flavor turns into mockery
Sem a provocação, sobra o prazer como justificativa | Without the taunt, pleasure is left as the justification
A provocação vira foto do prato | The taunt becomes a photo of the plate
O deboche vira desafio | Mockery becomes a challenge
Quem responde à provocação é acusado de chato | Whoever answers the taunt is accused of being annoying
A provocação verbal vira foto | The verbal taunt becomes a photo
O vegano estaria perdendo o sabor | The vegan would be missing the flavor
Sem a foto, sobra o prazer como justificativa | Without the photo, pleasure is left as the justification
Mostra-se o prato, mas não o abate | The plate is shown, but not the slaughter
A provocação vira desafio | The taunt becomes a challenge
A provocação abre a pergunta sobre a vida na natureza | The provocation opens the question about life in nature
A mesma idealização, agora para os selvagens | The same idealization, now for wild animals
Quando a idílica cai, o sofrimento é declarado natural | When the idyllic view falls, suffering is declared natural
Admite-se o sofrimento, mas nega-se o dever | The suffering is admitted, but the duty denied
A escala vira desculpa | The scale becomes an excuse
O mesmo apelo, agora para não ajudar | The same appeal, now used not to help
Da falta de culpado passa-se à falta de dever | From no culprit it moves to no duty
Se é natural, mexer seria arriscado | If it's natural, meddling would be risky
O apelo à natureza volta para o prato | The appeal to nature returns to the plate
A mesma fuga pela distância entre o ato e o dano | The same escape through the distance between act and harm
Admitido o dever, alega-se que é impossível cumpri-lo | Once the duty is admitted, it's claimed impossible to fulfil
O dever de ajudar fica fora da pauta | The duty to help is left off the agenda
O mesmo tipo de caso, usado no sentido contrário | The same kind of case, used in the opposite direction
Quando se vê a escala, ela vira desculpa | When the scale is seen, it becomes an excuse
Da impossibilidade passa-se ao risco | From impossibility it moves to risk
A escala torna cada ação aparentemente inútil | The scale makes each action seem useless
O problema é reduzido ao caso mais difícil | The problem is reduced to the hardest case
Se é natural, mexer seria arriscado e errado | If it's natural, meddling would be risky and wrong
Do risco passa-se à acusação de arrogância | From risk it moves to the charge of arrogance
O equilíbrio vira a meta a proteger | Balance becomes the goal to protect
O risco é ilustrado pelo caso mais extremo | The risk is illustrated with the most extreme case
A liberdade é tomada como bem-estar | Freedom is taken as wellbeing
O respeito à natureza vira respeito ao equilíbrio | Respect for nature becomes respect for balance
A não interferência vira regra do ativismo | Non-interference becomes a rule of activism
A acusação de imposição, agora em nome dos animais | The charge of imposition, now in the animals' name
O valor passa do indivíduo para a espécie | Value moves from the individual to the species
O equilíbrio é usado para justificar matar | Balance is used to justify killing
A pauta ambiental é confundida com a dos animais | The environmental agenda is confused with the animals'
A pauta é descartada como inviável | The cause is dismissed as unfeasible
A preocupação estratégica volta, agora contra a própria ampliação | The strategic concern returns, now against widening the circle
Sem o fundamento, o vegano fica sem resposta à provocação | Without the foundation, the vegan has no answer to the provocation
A fronteira da espécie vira fronteira do material | The species boundary becomes a boundary of material
A pergunta da fronteira chega às máquinas | The boundary question reaches machines
A possibilidade é descartada como fantasia | The possibility is dismissed as fantasy
Mentes futuras também não existem ainda | Future minds don't exist yet either
O critério biológico volta, agora contra máquinas | The biological criterion returns, now against machines
Do natural passa-se ao intocável | From the natural it moves to the untouchable
O risco é estendido à biotecnologia | The risk is extended to biotechnology
A proposta é descartada como fantasia | The proposal is dismissed as fantasy
O apelo à natureza, agora contra mudar a biologia | The appeal to nature, now against changing biology
A predação vira o caso que ridiculariza a proposta | Predation becomes the case that ridicules the proposal
Os efeitos de hoje sobre o futuro parecem pequenos demais | Today's effects on the future seem too small
O futuro é descartado como fantasia | The future is dismissed as fantasy
O mesmo debate sobre quem vai ou não existir | The same debate about who will or won't exist
O presente humano é colocado à frente de tudo | The human present is put ahead of everything
A possibilidade de mentes artificiais é chamada de ficção | The possibility of artificial minds is called fiction
A proposta tecnológica é ridicularizada | The technological proposal is ridiculed
A prioridade do presente vira prioridade humana | The priority of the present becomes a human priority
A escala do futuro parece tornar inútil qualquer ação | The scale of the future seems to make any action useless
Respondida a dor, alega-se que o animal nem sabe que vai morrer | Once pain is answered, the claim is that the animal doesn't even know it will die
Sem razão, não haveria noção de futuro | Without reason, there would be no sense of the future
Quando o teste humano aparece, apela-se ao potencial | When the human test appears, potential is invoked
A antecipação vira medida de quanto se sofre | Anticipation becomes the measure of how much one suffers
A ignorância da morte vira parte da "morte boa" | Ignorance of death becomes part of the "good death"
O parasitismo mostra que o problema vai além de casa | Parasitism shows the problem goes beyond the home
O estereótipo se apoia na imagem da dieta extrema | The stereotype rests on the image of the extreme diet
Da dieta só de frutas passa-se à proteína | From the all-fruit diet it moves to protein
A suplementação vira objeção | Supplementation becomes the objection
Um caso vira regra | One case becomes the rule
A dieta extrema do outro lado aparece como solução | The extreme diet on the other side appears as the solution
O estereótipo de fraqueza vira diagnóstico | The stereotype of weakness becomes a diagnosis
A dieta restritiva vira modelo de todo veganismo | The restrictive diet becomes the model for all of veganism
A ética é tratada como sintoma | The ethics is treated as a symptom
A posição ética é reduzida a um problema psicológico | The ethical position is reduced to a psychological problem
A utopia vira estereótipo de hippie | Utopia becomes the hippie stereotype
Do estereótipo passa-se ao ataque pessoal | From the stereotype it moves to personal attack
O grupo é tratado como seita | The group is treated as a cult
O hippie vira radical | The hippie becomes a radical
A imagem de contracultura serve para negar a base científica | The countercultural image is used to deny the scientific basis
De outro caso sem demanda passa-se ao animal que morreu sozinho | From another case without demand it moves to the animal that died on its own
Outro hipotético para testar o vegano | Another hypothetical to test the vegan
Do animal morto naturalmente passa-se ao do mercado | From the animal that died naturally it moves to the one in the store
A recusa é tratada como frescura ou desejo escondido | The refusal is treated as fussiness or hidden desire
A recusa é tratada como pureza religiosa | The refusal is treated as religious purity
Busca outro caso em que ninguém foi morto para ser comido | Looks for another case in which no one was killed to be eaten
Da maioria que come passa-se à minoria que não come | From the majority who eat it to the minority who don't
A desistência vira previsão de que o veganismo nunca crescerá | Giving up becomes a prediction that veganism will never grow
A minoria vira utopia | The minority becomes a utopia
Se nunca seremos maioria, o indivíduo não mudaria nada | If we'll never be the majority, the individual would change nothing
A esperança passa da escolha individual para a tecnologia | Hope shifts from individual choice to technology
Da acusação política passa-se ao ataque pessoal | From the political charge it moves to personal attack
O incômodo vira diagnóstico | The annoyance becomes a diagnosis
O ataque busca apoio em estudos sobre depressão | The attack seeks support in studies on depression
O ataque busca apoio em transtornos alimentares | The attack seeks support in eating disorders
Da afirmação passa-se à hipótese | From the claim it moves to the hypothesis
Outro cenário hipotético para testar o vegano | Another hypothetical scenario to test the vegan
Se plantas contam, pergunta-se onde fica a linha | If plants count, the question is where the line falls
Toda dieta causa algum dano | Every diet causes some harm
A impossibilidade de zerar o dano vira acusação | The impossibility of zero harm becomes an accusation
'''

MOTIVOS = {}
for _l in _PARES.strip().split('\n'):
    _pt, _en = _l.split(' | ')
    MOTIVOS[_pt.strip()] = _en.strip()
