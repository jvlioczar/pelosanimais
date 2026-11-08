"""Political objections, Beyond veganism, library and the long texts of build.py, in English.
Political objections and Beyond veganism are keyed by their Portuguese slug ('s'); the English slug is the new 's'.
Source lists show only titles; sources in Portuguese are marked."""

QE_EN = 'https://questaodeetica.biblioverse.org/en/'
COCHRANE = ('An Introduction to Animals and Political Theory', 'https://doi.org/10.1057/9780230290594')
COCHRANE_LIB = ('Do Animals Have an Interest in Liberty?', 'https://doi.org/10.1111/j.1467-9248.2008.00742.x')
QE11 = ('To what extent do ethical theories agree about what we owe animals?', QE_EN + 'v11/06-to-what-extent-do-ethical-theories-agree-about-what-we.html')
ZOOPOLIS = ('Zoopolis: A Political Theory of Animal Rights', 'https://openlibrary.org/works/OL16590337W')
KYM = ('Animal Rights, Multiculturalism, and the Left', 'https://doi.org/10.1111/josp.12047')

POL_INTRO = ('Every ethical or political theory starts from a principle: protect individual freedom, end exploitation, reduce suffering, '
             'treat like cases alike, care for the vulnerable. For most of history, these theories applied their principle only to humans. '
             'This section gathers the objections that usually come from each of them and shows why excluding animals does not follow from the principle, '
             'but from a cut made before it. The point is not that every theory says the same thing, but that none of them offers, on its own terms, '
             'a reason to leave out those who can be harmed.')

POL_ESPECTRO = dict(
    titulo='From left to right',
    intro="You don't need to change political sides to be vegan. You only need to take seriously the values each side already holds. The values below are the ones usually associated with each camp, and none of them belongs to one side alone.",
    lados=[
        ('If you identify with the left', [
            ('Equality', 'It asks that similar interests get similar weight. Excluding those who feel just because of their species creates an unjustified inequality.', 'igualitarismo'),
            ('Fighting exploitation', 'Animal farming uses the bodies and lives of those who can neither resist nor bargain, on a scale of billions a year.', 'marxismo'),
            ('Protecting the vulnerable', "Animals are the extreme case of vulnerability: they don't vote, speak or organize.", 'antidiscriminacao'),
            ('Critique of domination', "If no hierarchy is natural just because it exists, the hierarchy between species also has to justify itself.", 'anarquismo'),
        ]),
        ('If you identify with the right', [
            ('Individual liberty', "One person's liberty ends where harm to another begins. An animal is an individual with interests, and cannot consent to being used.", 'liberalismo'),
            ('Non-aggression and legitimate property', 'Whoever holds that no one may be attacked or taken as property without consent has reasons to extend this to those who feel.', 'libertarianismo'),
            ('Personal responsibility', "Veganism is each person's consumer choice and doesn't depend on the state: it's the person taking responsibility for the consequences of what they buy.", 'liberalismo'),
            ('Tradition, family and character', 'Many traditions value compassion toward animals, and caring for those who depend on us is a virtue, not a fad.', 'virtudes'),
            ('Free markets and innovation', 'The market already offers plant-based alternatives and invests in cultivated meat. Choosing them is using market freedom in favor of animals.', 'libertarianismo'),
        ]),
    ],
    fecho='The two sides may disagree about the means, such as laws, markets or cultural change, and evidence helps choose what works best. But on each side\'s own terms, there is no good reason to leave animals out.',
)

POLITICAS = {
 'liberalismo': dict(s='liberalism', t='Liberalism', frase="Freedom is a right of rational individuals; animals aren't subjects of liberal rights.",
  principio='Protect individuals against harm caused by others and ensure each can live their own life. For Mill, the only legitimate reason to limit someone\'s freedom is to prevent harm to others.',
  quebra=['Liberalism already protects individuals who are not autonomous, such as babies and people with profound cognitive disabilities. Rationality is not, in practice, the condition for protection.',
          'The harm principle works against the exclusion: if animals can be harmed, and the evidence says they can (A5), using and killing them is exactly the kind of action that affects others.',
          'Treating someone who feels as property is what liberalism rejected among humans. Owning a sentient being is not a neutral starting point (A17).'],
  replica='The most serious version, defended by Cochrane himself, grants that many animals may not have an intrinsic interest in liberty, in the sense of choosing their own life the way an adult human does.',
  resposta='Even granting this, Cochrane concludes that they have strong interests in not suffering and in staying alive, and that a consistent liberalism must protect them. The debate about liberty changes the kind of right, not the fact that there are rights. And intensive farming violates even the most basic freedom of movement.',
  fontes=[COCHRANE, COCHRANE_LIB, ('On Liberty', 'https://www.gutenberg.org/ebooks/34901')]),
 'libertarianismo': dict(s='libertarianism', t='Libertarianism and anarcho-capitalism', frase="What's mine is mine: animals are property, and the freedom to use property is sacred.",
  principio='Self-ownership and the non-aggression principle: no one may initiate violence against another individual.',
  quebra=['Self-ownership rests on being a subject, someone whose life can go well or badly. Sentient animals are subjects in this sense too.',
          'The non-aggression principle forbids initiating violence against someone who threatened no one. Breeding, mutilating and killing an animal is initiating violence.',
          'Saying the animal is property is the conclusion in dispute, not a premise. Beings who can be victims do not become property without an argument, and that argument is missing (A17).'],
  replica='The most serious version says rights come from agreements between agents able to respect non-aggression, and that animals, who cannot respect it, are outside the agreement.',
  resposta='Babies cannot respect non-aggression either, and no libertarian treats them as property. The capacity to be aggressed against, not the capacity to sign an agreement, is what makes aggression wrong (A7, A23).',
  fontes=[COCHRANE]),
 'marxismo': dict(s='marxism', t='Marxism, socialism and communism', frase="Exploitation is a relation between human classes. Animals aren't workers, and the struggle is a different one.",
  principio='End exploitation and the turning of beings and lives into commodities.',
  quebra=['Billions of animals are bred, used and sold as commodities, on a scale no other exploitation reaches. The critique of commodification applies to them directly.',
          'Whether "labor" applies to animals is a real debate: Marx himself distinguished human labor from animal activity. But authors such as Ted Benton and Kendra Coulter show that cows, horses and working dogs perform productive functions without choice or compensation.',
          'Even those who reject calling it labor must explain why the exploitation of a sentient being would be acceptable just because it is not human.'],
  replica='The most serious version says the priority must be the human working class, and that the animal cause diverts energy from the revolution.',
  resposta='Ending the exploitation of animals does not compete with the workers\' struggle, and industrial animal farming also exploits the humans who work in it (J3). And "first one cause, then the other" has been used against almost every struggle that came after (J6, K4).',
  fontes=[COCHRANE, ('Natural Relations: Ecology, Animal Rights and Social Justice', 'https://openlibrary.org/works/OL3947274W'), ('Animals, Work, and the Promise of Interspecies Solidarity', 'https://openlibrary.org/works/OL20789885W')]),
 'anarquismo': dict(s='anarchism', t='Anarchism', frase='Anarchism fights domination between people; animals are not part of that.',
  principio='Reject hierarchies and forms of domination that cannot be justified.',
  quebra=['The relationship between humans and farmed animals is one of the most complete hierarchies there is: one side decides when the other is born, where it lives, with whom it breeds and when it dies.',
          'Concern for animals is part of the anarchist tradition itself: the geographer Élisée Reclus defended vegetarianism as part of the same refusal of domination.'],
  replica='The most serious version says the relevant domination is the kind its victims can refuse, and that animals do not organize against it.',
  resposta='Being unable to resist is exactly what makes domination more serious, not less. Anarchism does not require the victim to organize for domination to be illegitimate.',
  fontes=[COCHRANE, ('On Vegetarianism', 'https://theanarchistlibrary.org/library/elisee-reclus-on-vegetarianism')]),
 'utilitarismo': dict(s='utilitarianism', t='Utilitarianism', frase='Human pleasures are worth more: better to be a human dissatisfied than a pig satisfied.',
  principio='Maximize well-being and minimize suffering for everyone affected, counting each one\'s interest equally.',
  quebra=['Bentham, one of the founders of utilitarianism, already said the question is not whether animals can reason, but whether they can suffer. Excluding them contradicts the theory itself.',
          "Mill's line compares kinds of pleasure, but it does not zero out animal suffering. Even if intellectual pleasures were worth more, an animal's pain would still count (A16, A22).",
          'Scale changes the sum: tens of billions of land animals and trillions of fish every year.'],
  replica='The most serious version grants that animals count, but says that farming with a good life and a painless death could be justified in the calculation, because it brings happy animals into existence (B6).',
  resposta='That is a real debate within utilitarianism, but it does not describe actual animal farming, in which most animals live in intensive systems. And the idea that one animal can be replaced by another faces serious objections (B6, A16).',
  fontes=[COCHRANE, QE11]),
 'contratualismo': dict(s='contractualism', t='Contractualism and Rawlsian justice', frase='Justice holds among those who have a sense of justice and can make agreements.',
  principio='Choose the rules of a society impartially, as if we did not know what position we would occupy in it.',
  quebra=['Rawls himself left animals out of justice, but he recognized duties of compassion toward them.',
          'The veil of ignorance exists to discount what is luck, like race, sex and talent. Mark Rowlands observed that species is also luck, and so should also go behind the veil (A21).',
          'Not knowing whether you would be born human or chicken, no one would approve rules that allow chickens to be bred and killed for a meal.'],
  replica='The most serious version says only those who can follow the rules can be party to the contract.',
  resposta='Babies and people with profound cognitive disabilities cannot follow the rules either, and justice protects them. Being a beneficiary of a rule has never required being able to follow it (A7, A23).',
  fontes=[COCHRANE, ('Animal Rights: A Philosophical Defence', 'https://openlibrary.org/works/OL1900454W')]),
 'deontologia': dict(s='deontology', t='Deontology and Kantianism', frase='Only rational beings are ends in themselves; toward animals we have, at most, indirect duties.',
  principio='Treat beings who have value of their own as ends, and never merely as means.',
  quebra=['Kant said cruelty to animals is wrong because it hardens human character. It would follow that torturing an animal in secret, with no effect on anyone, would not be wrong, a conclusion almost no one accepts (A20).',
          'Present-day interpreters of the Kantian tradition itself, such as Christine Korsgaard, argue that sentient animals are ends in themselves, because they have a good of their own.',
          'Tom Regan, within a rights theory, showed that being the "subject of a life" is enough to have inherent value.'],
  replica='The most serious version says dignity comes from moral autonomy, which animals lack.',
  resposta='Moral autonomy is also missing in many humans the theory protects as ends. If protection does not depend on it in those cases, it cannot depend on it in the case of animals (A11, A12).',
  fontes=[COCHRANE, QE11]),
 'comunitarismo': dict(s='communitarianism', t='Communitarianism', frase='Duties arise from the community and its traditions, and animals are not members of it.',
  principio='Morality is built in the bonds and practices of a community.',
  quebra=['Domesticated animals have lived inside our communities for thousands of years. Sue Donaldson and Will Kymlicka propose treating them as members, with adapted citizenship rights.',
          'A community\'s traditions change, and many changed precisely to include those who were outside (D1, D2).',
          'A community that defines its members by what suits it repeats the exclusion that struggles for inclusion fought against.'],
  replica='The most serious version says membership requires taking part in shared practices, which animals do not do.',
  resposta='Dogs, horses, cows and chickens take part in our practices all the time, just as tools. The question is whether that participation should be exploitation or membership.',
  fontes=[COCHRANE, ZOOPOLIS]),
 'igualitarismo': dict(s='egalitarianism', t='Egalitarianism and prioritarianism', frase='Equality is among human citizens; animals belong to another category.',
  principio='Reduce unjust inequalities and give priority to those who are worst off.',
  quebra=['If priority goes to the worst off, animals in intensive farming and many wild animals are among the worst-off beings there are.',
          'That inequality between species is natural does not make it just: egalitarianism fights precisely the disadvantages no one chose.',
          'Excluding animals is deciding in advance who can be worst off, which contradicts the principle.'],
  replica='The most serious version says the relevant equality is equality of political status, which only makes sense among members of a society.',
  resposta='Even if political status is discussed separately, priority to the worst off refers to well-being, and an animal\'s well-being can go badly. Among theories that disagree on almost everything, this is a point of convergence.',
  fontes=[COCHRANE, QE11]),
 'cuidado': dict(s='care-ethics', t='Ethics of care', frase='Care applies to close relationships, not to unknown animals.',
  principio='Respond to the needs of the vulnerable and the dependent with attention and responsibility.',
  quebra=['Domesticated animals are, by definition, dependent on us: we made them that way.',
          'The feminist care tradition has already applied the concept to animals, as Josephine Donovan and Carol J. Adams show.',
          'Care is not limited to those we know by name: it also guides what we do to those affected by our choices.'],
  replica='The most serious version says care depends on a relationship, and we have no relationship with the chicken at the supermarket.',
  resposta='Buying the chicken is a relationship: it is the choice that orders its life and death (K2). An ethics of care that ignores those who depend on our choices loses its own foundation.',
  fontes=[COCHRANE, ('The Feminist Care Tradition in Animal Ethics', 'https://openlibrary.org/works/OL18205862W')]),
 'virtudes': dict(s='virtue-ethics', t='Virtue ethics', frase='Virtue is about human character; treating animals well matters only because it makes us better.',
  principio='Cultivate virtues like compassion, justice and temperance, and avoid vices like cruelty.',
  quebra=['Compassion is directed at the one who suffers. If the animal\'s suffering did not matter in itself, there would be nothing for compassion to respond to.',
          'A just and compassionate person who pays for the avoidable suffering of others acts against their own virtues.',
          'Reducing the animal\'s value to its effect on our character is the same structure as Kant\'s indirect duties, which almost no one accepts (A20).'],
  replica='The most serious version says a virtuous person can eat meat with moderation and gratitude, without cruelty.',
  resposta='Moderation applies to what affects only ourselves, not to harm to others (E5). And when there is an alternative, causing someone\'s death for a meal is hard to reconcile with compassion.',
  fontes=[COCHRANE, QE11]),
 'feminismo': dict(s='feminism', t='Feminism', frase='Feminism is about women; talking about cows and hens is changing the subject, or even offensive.',
  principio='End oppression linked to sex and control over the body and reproduction.',
  quebra=['Milk and egg production is based on controlling the reproduction of females: repeated insemination, separation from their young and disposal when production drops (B7, C10).',
          'This observation does not equate women with cows, nor victims with each other. It points to a shared structure of control over bodies that feel (L7).',
          'Part of feminism itself made this link, as Carol J. Adams did in The Sexual Politics of Meat, although not every current accepts it.'],
  replica='The most serious version says comparisons between women and animals have historically served to dehumanize women.',
  resposta='Care with such comparisons is legitimate, and the argument does not depend on them (L7). The principle is enough: controlling the body and reproduction of someone who feels, for others\' profit, is what feminism fights.',
  fontes=[COCHRANE, ('The Sexual Politics of Meat', 'https://openlibrary.org/works/OL3468840W')]),
 'antidiscriminacao': dict(s='anti-discrimination', t='Anti-racism, anti-ableism and the fight against other discrimination', frase='Comparing speciesism to racism or ableism is offensive; they are different things.',
  principio='Do not give less weight to someone\'s interests because of a trait that does not change how much they can be harmed, such as race, disability, origin or appearance.',
  quebra=['The comparison is not between victims but between structures of reasoning: in every case, a trait irrelevant to the harm is used to discount interests (A10, A24).',
          'Ableism and speciesism share a criterion: treating cognitive ability as the measure of worth. Authors such as Sunaura Taylor, who lives with a disability, discuss this link in Beasts of Burden.',
          'Each struggle has its own history and its own victims, and none needs to be diluted. But the principle that sustains them does not stop at the species line.'],
  replica='The most serious version says these comparisons have been used to animalize and dehumanize human groups, and should therefore be avoided.',
  resposta='The caution is fair, and the argument for animals stands without analogies (L7). But the problem with dehumanization was always treating someone as if they did not matter; the consistent answer is that no one who feels should be treated that way.',
  fontes=[COCHRANE, KYM, ('Beasts of Burden: Animal and Disability Liberation', 'https://openlibrary.org/works/OL20045362W')]),
 'esquerda-multiculturalismo': dict(s='progressive-left-and-multiculturalism', t='The progressive left and multiculturalism', frase='The animal cause is a white middle-class concern that ends up attacking the cultural practices of minorities.',
  principio='Defend vulnerable groups, fight domination and respect cultural diversity.',
  quebra=['Will Kymlicka and Sue Donaldson show that the animal cause is almost invisible on the left, despite its affinities with feminism, social justice and disability rights, and that this exclusion does not follow from the left\'s own principles.',
          'Part of the resistance comes from fear that talking about animal rights lowers the human dignity of groups that have already been dehumanized. But defending animals does not require denying anything to any human.',
          'Most animals killed today are in the industrial farming of majorities and large companies, not in minority practices.'],
  replica='The most serious version points to a real problem: animal campaigns have targeted minority practices, such as ritual slaughter or hunting by Indigenous peoples, while ignoring far more numerous majority practices.',
  resposta='The criticism is fair and should be taken seriously: the standard has to be the same for everyone, and starting with the most widespread exploitation is the most consistent course. That is an argument against selectivity, not against animals. A respect for diversity that did not count animals would repeat the very cut it fights (D2, J6).',
  fontes=[KYM, COCHRANE, ZOOPOLIS]),
 'pacifismo': dict(s='pacifism', t='Pacifism and nonviolence', frase='Nonviolence is a commitment between people, not to animals.',
  principio='Refuse violence as a means of resolving conflicts and reaching goals.',
  quebra=['Breeding and slaughter are organized physical violence against beings who feel, not accidents.',
          'Traditions of nonviolence, such as ahimsa in Jainism and Hinduism, have always included animals.',
          'A refusal of violence that makes an exception for the most routine and widespread violence there is has no foundation.'],
  replica='The most serious version says pacifism deals with conflicts between agents, and that killing animals for food is not a conflict.',
  resposta='It is even worse: there is no conflict at all, and the violence is done only to obtain a product that has alternatives. If violence is refused even in conflicts, it should be refused where there is no conflict.',
  fontes=[COCHRANE]),
 'altruismo-eficaz': dict(s='effective-altruism', t='Effective altruism', frase='Resources for doing good are limited, and should go to humans first.',
  principio='Use evidence and reason to do the most good possible with the resources available.',
  quebra=["Effective altruism's criteria, scale, neglectedness and tractability, favor the animal cause: the number of victims is enormous and the resources devoted to it are small.",
          'Excluding animals in advance is deciding the result before doing the math, the opposite of what the approach proposes.',
          'Not eating animals takes no resources from any other cause (J6).'],
  replica='The most serious version says it is hard to compare well-being across species, and that uncertainty favors the better-known human causes.',
  resposta='The uncertainty is real, but it cuts both ways, and the scale is so large that the animal cause stays a priority even with heavy discounts on the weight of each animal.',
  fontes=[COCHRANE, ('How does the animal cause fare on the priority criteria?', QE_EN + 'v8/02-how-does-the-animal-cause-fare-on-the-priority-criteria.html')]),
}

LIVRO = 'Veganismo Baseado em Evidências (Evidence-Based Veganism, in Portuguese)'
INCERTEZA = '''<div class="bloco curta"><p><strong>How to decide under uncertainty.</strong> Instead of asking only "is this being sentient, yes or no?", ask how likely it is and weigh that by the size of the harm or benefit at stake. A moderate probability multiplied by an immense scale can outweigh a high certainty over small numbers. Uncertainty about a borderline case does not contaminate the certainty about the criterion: sentience is still what matters.</p></div>'''

ALEM = {
 'antiespecismo': dict(s='antispeciesism', selo='Foundation', t='Antispeciesism and sentientism',
  res='Veganism is one consequence of a broader criterion: what matters morally is the capacity to be harmed or benefited.',
  corpo='''<h2>Two names, one idea</h2><p><strong>Sentientism</strong> holds that what matters morally is the capacity to be harmed or benefited, present in any sentient being, human or not. <strong>Antispeciesism</strong> is the consequence: giving similar weight to similar harms, whatever the species.</p><p>That is why the discussion does not end at the plate. If we accept the criterion, it also applies to what we do by omission, to animals no one exploits and to beings that may come to exist.</p>
<h2>Four competing criteria</h2><div class="tabela"><table><tr><th scope="col">Criterion</th><th scope="col">What it puts at the center</th><th scope="col">The problem</th></tr>
<tr><td><strong>Anthropocentrism</strong></td><td>Human interests, above all</td><td>Narrows the circle with no justification for stopping at the species</td></tr>
<tr><td><strong>Environmentalism</strong>, as a moral view</td><td>Ecosystems, biodiversity and species, valuable in themselves</td><td>Treats individuals capable of suffering as means to an end</td></tr>
<tr><td><strong>Biocentrism</strong></td><td>Every living being, sentient or not</td><td>Confuses biological function with interest: without subjective experience there is no possible victim, only a process</td></tr>
<tr><td><strong>Sentientism</strong></td><td>Whoever can have good or bad experiences</td><td>The criterion this guide adopts</td></tr></table></div>
<h2>What is not speciesism</h2><p>Recognizing real differences is not discrimination. Saying an animal does not need to vote is an observation. Saying it can suffer without that mattering, because it is not very intelligent, is speciesism. The line between recognizing a difference and using it to discard interests is where the debate should happen.</p>
<h2>Hierarchies that survive among vegans</h2><p>People who have already rejected exploitation for food can keep speciesism in other forms:</p><ul><li><strong>Humans above animals</strong> in any conflict of interests, accepting experimentation or ritual sacrifice.</li><li><strong>Pets above farmed animals.</strong></li><li><strong>Mammals and birds above fish</strong>, who are numerically the largest victims of exploitation.</li><li><strong>Vertebrates above invertebrates</strong>, dismissing insects and decapods without examination.</li><li><strong>Exploited animals above wild ones</strong>, which reveals an omission bias: who caused the harm matters more than who suffers it.</li><li><strong>Abstract concepts above individuals</strong>, such as biodiversity or ecosystem balance.</li><li><strong>Those who exist now above those yet to come</strong>, a time discount that disregards future suffering.</li></ul>
<p>The test is the veil of ignorance: would you accept the hierarchy without knowing in which position you would be born? There are billions of humans and quintillions of animals, counting invertebrates. No one who took that ratio seriously would bet on a hierarchy with humans systematically on top.</p>
<h2>Humanism taken all the way</h2><p>This is not anti-humanism. Humanism brought universality and impartiality, which helped overcome hierarchies between human groups, but those principles stopped at the species line without justification. Posthumanism keeps the commitment to evidence, equality and individual freedom, and corrects that failure.</p>''',
  fontes=[(f'{LIVRO}, chapters 7, 9 and 11', None), ('The argument from relevance', 'https://www.animal-ethics.org/argument-from-relevance/'), ('Animal Rights: A Philosophical Defence', None)]),
 'estado-da-arte': dict(s='state-of-the-art', selo='Overview', t='The state of the art in animal ethics',
  res='Since 1975, animal ethics has been tested on ever harder cases, by authors from schools that disagree with each other, and has reached the same rejection of speciesism.',
  corpo='''<h2>Different currents, same conclusion</h2><p>When theories built on incompatible premises converge on the same practical conclusion, that convergence works as a corroboration no single theory offers. Many vegans still don't know these authors.</p><div class="tabela"><table><tr><th scope="col">Route</th><th scope="col">Author or group</th><th scope="col">Contribution</th></tr>
<tr><td>Equal consideration</td><td>Peter Singer</td><td>Systematized the principle in 1975 and extended it beyond food</td></tr>
<tr><td>Contractualism</td><td>Mark Rowlands</td><td>Behind the veil of ignorance, no one would know whether they would be born human, which makes species as arbitrary as wealth</td></tr>
<tr><td>Capabilities</td><td>Martha Nussbaum</td><td>Anyone with sentience, emotion and movement toward their own good is a full subject of justice</td></tr>
<tr><td>Political critique</td><td><em>Cahiers antispécistes</em>: Yves Bonnardel, David Olivier and Françoise Blanchon</td><td>Since 1991, analyzes speciesism as a system of domination</td></tr>
<tr><td>Focus on suffering</td><td>Magnus Vinding, Tobias Baumann, Brian Tomasik, Teo Ajantaival and Jamie Woodhouse</td><td>Reducing suffering at scale, including in the future</td></tr>
<tr><td>Wild animal suffering</td><td>Oscar Horta, Kyle Johannsen and Luciano Carlos Cunha</td><td>Extend the criterion to suffering no human caused, by consequentialist and deontological routes</td></tr>
<tr><td>Uncertainty</td><td>Jeff Sebo</td><td>Under uncertainty about who is sentient, we have reason to widen the circle, without waiting for a certainty that may never come</td></tr>
<tr><td>Technological change</td><td>Jacy Reese Anthis</td><td>How technology and institutions can speed up the end of animal farming</td></tr>
<tr><td>Abolishing biological suffering</td><td>David Pearce</td><td>Proposes consensual biotechnology to reduce the capacity to suffer, including intervening in predation</td></tr>
<tr><td>Harmless relationships</td><td>Alasdair Cochrane</td><td>Asks whether certain relationships involving no real harm would be compatible with a sentientist politics</td></tr></table></div>
<p>In Brazil, Luciano Carlos Cunha is the most prolific author in the field, with fourteen books, counting standalone titles and a twelve-volume collection.</p>
<h2>What science has declared</h2><ul><li><strong>Cambridge Declaration (2012):</strong> humans are not unique in possessing the neurological substrates that generate consciousness.</li><li><strong>New York Declaration (2024):</strong> strong evidence for mammals and birds, and a realistic possibility of conscious experience in all vertebrates and many invertebrates, including cephalopods, decapods and insects. It also states that certainty should not be a precondition for considering welfare risks.</li><li><strong>Montreal Declaration (2022):</strong> philosophers from different currents declared animal exploitation morally unacceptable.</li></ul>
<h2>The price of following the argument</h2><p>When someone takes an argument as far as it logically goes, the most common reaction tends to be hostility, not counter-argument. Difficult proposals deserve to be refuted, not dismissed as eccentric. Agreeing with the authors above on every point is another discussion.</p>''',
  fontes=[(f'{LIVRO}, chapter 14', None), ('The New York Declaration on Animal Consciousness', 'https://sites.google.com/nyu.edu/nydeclaration/declaration'), ('The Cambridge Declaration on Consciousness', None), ('Montreal Declaration on Animal Exploitation', None), ('Wild Animal Ethics', None), ('Frontiers of Justice; Justice for Animals', None), ('Saving Animals, Saving Ourselves; The Moral Circle', None), ('The End of Animal Farming', None), ('The Hedonistic Imperative', None), ('Animal Rights Without Liberation', None)]),
 'animais-selvagens': dict(s='wild-animals', selo='Ethical question', t='Wild animal suffering',
  res='Hunger, disease and predation were not caused by us. But if sentience is what matters, this suffering cannot be dismissed just because it is natural.',
  corpo='''<h2>The argument</h2><p>If our omissions are also moral choices, neglecting suffering we did not cause, but could relieve to some extent, is also morally relevant. Authors such as Oscar Horta and Kyle Johannsen reach this conclusion by different routes, which suggests it does not depend on one specific ethical theory.</p>
<h2>The myth of idyllic nature</h2><p>The idea of a nature that is intrinsically good for those who live in it is, at best, an unverified assumption. At worst, it is a convenient way of justifying inaction. Copying nature does not work as a criterion either: as John Stuart Mill pointed out, nature kills, tortures and destroys all the time.</p>
<h2>Research before action</h2><p>Ecosystems are complex, and a well-intentioned intervention, such as vaccinating a population, can have effects that make the outcome worse. That does not mean never intervening. It calls for serious research and small, reversible interventions before anything bigger. That is the proposal of what is called welfare biology.</p><p>The right question is not "should we intervene in nature?". It is what the evidence suggests about this specific intervention, and how much it needs to improve before justifying a bigger action.</p>
<h2>What this does not say</h2><ul><li><strong>It does not license exploitation.</strong> See <a href="../argumentos/c2.html">C2, "Lions eat other animals"</a>: lions are not moral agents and have no alternative.</li><li><strong>It does not require locking up predators.</strong> <a href="../argumentos/f3.html">F3</a> is often used to ridicule the question, which is serious and does not favor eating animals.</li><li><strong>It is not against environmental care.</strong> The environment is treated as a means to the lives of real sentient beings, not as an end.</li></ul>
<p>Artificial intelligence may help model scenarios of suffering in wild populations, which are hard to calculate by hand, and prioritize where to intervene.</p>''',
  fontes=[(f'{LIVRO}, chapters 11, 14 and 16', None), ('Wild animal suffering', 'https://www.animal-ethics.org/wild-animal-suffering-section/'), ('Debunking the Idyllic View of Natural Processes', None), ('The Case for Intervention in Nature on Behalf of Animals', None), ('Towards Welfare Biology', 'https://link.springer.com/article/10.1007/BF00852469'), ('Wild Animal Ethics', None), ('Razões Para Ajudar (in Portuguese)', None), ('O sofrimento dos animais selvagens: pensando em soluções (in Portuguese)', None)]),
 'ia-e-robos': dict(s='ai-and-robots', selo='Possibility', t='Sentience in AI and robots',
  res='No current system is recognized as sentient. But the possibility is not absurd, and the criterion does not depend on what a being is made of.',
  corpo=f'''<p class="aviso"><strong>This is a possibility, not a fact.</strong> There is no consensus on whether digital systems can have experiences, or on how we would know.</p>
<h2>The criterion ignores the substrate</h2><p>If what matters is there being someone for whom things can go well or badly, the boundary of the biological substrate is as irrelevant as the boundary of species. If sentient beings created by digital means appear, their interests count.</p>
<h2>What is known so far</h2><ul><li>A 2023 report, based on scientific theories of consciousness, concluded that no AI system at the time was a strong candidate, but that there was no obvious technical barrier to building one.</li><li>A 2024 report argued that AI companies should take the question seriously, assessing and preparing for it, considering the possibility of conscious systems in the near future to be realistic.</li></ul>
<h2>Why it is hard</h2><p>A system saying it suffers proves nothing, because it may have been trained on human texts describing suffering. The error runs both ways: attributing a mind to something without one and denying a mind to someone who has one. The second has a bad track record, as <a href="../argumentos/a5.html">A5</a> shows.</p>
{INCERTEZA}
<h2>Why think about it in advance</h2><p>Even a small chance, multiplied by the astronomical scale at which these systems could exist, justifies attention and research now, not after the problem is under way.</p>
<h2>A shift in priority</h2><p>For decades, many people have defended rights for robots that might one day feel, a frequent theme in science fiction, while ignoring the suffering of animals that already exist. The concern needs a shift in priority, not just in scope.</p>
<h2>AI also affects animals</h2><p>It cuts both ways. It can help understand animal language, detect pain and stress and speed up cultivated meat research. It is also already used to optimize confinement and automate processes, removing witnesses from inside farms. The outcome depends on who applies it and by what criterion.</p>''',
  fontes=[(f'{LIVRO}, chapters 15 and 16', None), ('Consciousness in Artificial Intelligence: Insights from the Science of Consciousness', 'https://arxiv.org/abs/2308.08708'), ('Taking AI Welfare Seriously', 'https://arxiv.org/abs/2411.00986'), ('The Moral Circle', None)]),
 'definicao-de-veganismo': dict(s='defining-veganism', selo='Debate', t='The definition of veganism, debated',
  res='What defines veganism: refusing the exploitation of animals, or refusing everything of animal origin? The question has come back strongly with cultivated meat and precision fermentation.',
  corpo='''<p class="aviso"><strong>This is an open debate.</strong> This page presents the positions and what is at stake for the animals. There is no single official definition, and organizations and activists disagree.</p>
<h2>Where the word came from</h2><p>The word <em>vegan</em> was coined in 1944 by Donald Watson and other founders of the Vegan Society, in the United Kingdom, to name people who did not consume animal products. In 1949, Leslie Cross observed that the society had defined a diet but not veganism, and proposed a definition centered on the relationship with animals: the principle of the emancipation of animals from exploitation by humans. In the following years, the society began to speak of ending the use of animals for food, commodities, work, hunting, vivisection and any other form of exploitation.</p>
<p>The definition the Vegan Society uses today, in force since 1988, combines the two. It describes veganism as a philosophy that seeks to exclude, as far as is possible and practicable, all forms of exploitation of and cruelty to animals, and adds that, in dietary terms, it means dispensing with all products derived wholly or partly from animals.</p>
<h2>First debate: recovering the center</h2><p>In common use, "vegan" has often become a label for a diet, a lifestyle or a product: a badge on the packaging, a food trend (<a href="../argumentos/l13.html">L13</a>), a list of ingredients. For some animal advocates, this moved the center of the idea. What matters would not be the purity of the plate, but no longer exploiting beings who feel.</p>
<div class="tabela"><table><tr><th scope="col">Emphasis</th><th scope="col">What counts</th><th scope="col">Risk</th></tr>
<tr><td><strong>On exploitation</strong></td><td>Whether the choice harms or uses animals</td><td>Can seem vague if it does not say what to do in practice</td></tr>
<tr><td><strong>On the product's origin</strong></td><td>Whether there is any ingredient of animal origin</td><td>Turns an ethical position into a labeling rule, and can penalize choices that harm no animal</td></tr></table></div>
<p>Those who defend recovering the center do not propose abandoning the practice: in real life, almost every animal product involves exploitation, and avoiding it is still the way. They propose remembering that the reason is the animal, and that rules created with no connection to it, such as requiring everything to be natural or organic, are not part of the idea ({RUIM:Vegano bom só come natural}).</p>
<h2>Second debate: the new technologies</h2><p>Cellular agriculture brings together techniques for producing animal-based foods without breeding and killing animals. <strong>Cultivated meat</strong> grows from animal cells in bioreactors. <strong>Precision fermentation</strong> uses microorganisms to produce proteins identical to those in milk or eggs, with no animal taking part in production.</p>
<p>Here the two emphases part ways. By the origin rule, these products would not be vegan, because they are chemically meat, milk or egg. By the exploitation rule, the question is different: was any animal used or harmed? The answer depends on the technique.</p>
<div class="tabela"><table><tr><th scope="col">Point</th><th scope="col">What is being discussed</th></tr>
<tr><td>Source of the cells</td><td>Cultivated meat starts from cells taken from animals by biopsy or from cell lines kept in the lab. An occasional biopsy is very different from breeding and slaughter.</td></tr>
<tr><td>Culture medium</td><td>Early processes used fetal bovine serum, obtained at slaughter. It is being replaced by animal-free media (<a href="../argumentos/k5.html">K5</a>).</td></tr>
<tr><td>Precision fermentation</td><td>The proteins are produced by microorganisms from the genetic sequence; no animal is used in production.</td></tr>
<tr><td>Scale and cost</td><td>There are still serious doubts about when, or whether, these products will become cheap (<a href="../argumentos/k5.html">K5</a>).</td></tr></table></div>
<p>That is why some propose updating the definition, removing the idea of "products of animal origin" and keeping only exploitation and cruelty. Those who resist usually point out that the simple origin rule is easy to follow and to explain, and fear that a more open definition would be used to justify products that still involve animals.</p>
<h2>What is at stake for the animals</h2><p>The reason for veganism, since Leslie Cross, is the animal. A definition tied to the chemical origin of ingredients may lead vegans to reject technologies that would greatly reduce breeding and slaughter, and to push away people willing to switch products without switching habits ({RUIM:Carne cultivada não é vegana}). At the same time, caution is warranted: until a product is actually free of exploitation along the whole chain, the label should not be granted in advance.</p>
<p>One criterion helps with both questions, the same one that guides this whole guide: ask who is harmed. If no one is used, confined, injured or killed, the reason to refuse disappears. If someone is, a "plant-based" or "lab-made" origin changes nothing (<a href="../argumentos/l8.html">L8</a>).</p>''',
  fontes=[('The Vegan Society: definition of veganism', 'https://www.vegansociety.com/go-vegan/definition-veganism'), ('Veganism Defined (1951)', 'https://www.all-creatures.org/articles/veganism-defined.html'), ('Vegan Literary Studies, University of Geneva', 'https://www.unige.ch/vls/index.php?cID=629'), ('The debate on cultivated meat', QE_EN + 'v8/12-the-debate-on-cultivated-meat.html'), (f'{LIVRO}, chapter 15', None)]),
 'extraterrestres': dict(s='extraterrestrials', selo='Possibility', t='Sentience in extraterrestrial beings',
  res='There is no evidence of life beyond Earth, let alone sentient life. The question tests whether our criterion is really a criterion, or just a preference for our own species.',
  corpo=f'''<p class="aviso"><strong>This is a possibility, not a fact.</strong> To date there is no evidence of extraterrestrial life. This page is an exercise in consistency, not a claim about what exists.</p>
<h2>The criterion ignores the planet</h2><p>If we ever discover sentient beings elsewhere in the universe, the same criterion would require their interests to be taken into account. The species line was never the right criterion, and the planetary one would not be either.</p>
<h2>The symmetry test</h2><p>By the principle of <a href="../argumentos/a10.html">A10, "They're just animals"</a>, sentient extraterrestrials could be bred for food because they are not of our species. By the same rule, they could breed us. Almost no one accepts the second half, which shows the principle is not taken seriously.</p><p>The same goes for <a href="../argumentos/a2.html">A2</a> and <a href="../argumentos/a11.html">A11</a>: if superiority or "what is normal for the species" decided, a more capable species would have a status above ours. Whoever rejects the conclusion is rejecting the premise.</p>
<h2>How would we know</h2><p>Probably with more difficulty than with animals, with whom we share an evolutionary kinship that helps interpret signs of pain. A very different mind may have no structure or behavior we recognize. Lack of resemblance to us would not be proof of an absence of experience.</p>
{INCERTEZA}
<h2>What this changes here and now</h2><p>Almost nothing in practice, and that is exactly why the exercise is useful: with no personal interest at stake, it is easier to see that what would make us respect an unknown being is the capacity to feel, not appearance, intelligence or origin. That capacity already exists, here, in those we call animals.</p>''',
  fontes=[(f'{LIVRO}, chapter 7', None), ('The Moral Circle', None)]),
 'fundamentos': dict(s='foundations', selo='Foundation', t='What supports animal ethics, and what weakens it',
  res='Critical reason, relevance, impartiality and sentience support veganism and animal ethics. Partiality, relativism, tribalism, ableism, making abstractions sacred and weak will weaken them.',
  corpo='''<p>Veganism and animal ethics don't depend on liking animals or on any particular ethical theory. They depend on a few principles almost everyone already accepts in other contexts. When those principles are taken seriously, the conclusion comes with them. When they're abandoned, it disappears, and other just causes tend to go with it.</p>
<h2>What supports it</h2><div class="tabela"><table><tr><th scope="col">Principle</th><th scope="col">What it says</th><th scope="col">Where it appears in this guide</th></tr>
<tr><td><strong>Critical reason and logical consistency</strong></td><td>Accepting the conclusions that follow from premises we already accept, and treating like cases alike</td><td><a href="../falacias.html">Fallacies</a>, <a href="../argumentos/a11.html">A11</a></td></tr>
<tr><td><strong>Relevance</strong></td><td>A criterion can only decide who is harmed if it's related to the capacity to be harmed. Species, colour or intelligence aren't</td><td><a href="../argumentos/a1.html">A1</a>, <a href="../argumentos/a10.html">A10</a></td></tr>
<tr><td><strong>Impartiality</strong></td><td>Judging as if we didn't know which position we'd be born into: the veil of ignorance</td><td><a href="../argumentos/a21.html">A21</a></td></tr>
<tr><td><strong>Universality</strong></td><td>A moral rule applies to all like cases, not only to those that suit us</td><td><a href="../argumentos/a13.html">A13</a>, <a href="../argumentos/a24.html">A24</a></td></tr>
<tr><td><strong>Sentience and interests</strong></td><td>Whoever can have good or bad experiences has interests that count, wherever the harm comes from</td><td><a href="../argumentos/a5.html">A5</a>, <a href="../familias/m.html">family M</a></td></tr>
<tr><td><strong>The moral circle and progress</strong></td><td>Moral history is, to a large extent, the inclusion of those who were once excluded</td><td><a href="../argumentos/a9.html">A9</a></td></tr>
<tr><td><strong>Justice</strong></td><td>Not imposing serious harm on others to obtain small benefits</td><td><a href="../argumentos/j11.html">J11</a></td></tr>
<tr><td><strong>The common good</strong></td><td>Thinking about everyone affected, including those who don't vote, can't speak and aren't born yet</td><td><a href="../argumentos/m11.html">M11</a></td></tr></table></div>
<h2>What weakens it</h2><div class="tabela"><table><tr><th scope="col">Attitude</th><th scope="col">How it weakens</th><th scope="col">Where it appears in this guide</th></tr>
<tr><td><strong>Merely instrumental rationality</strong></td><td>Using reason only to get what one wants, without asking whether the end is just</td><td><a href="../argumentos/j11.html">J11</a>, <a href="../argumentos/e12.html">E12</a></td></tr>
<tr><td><strong>Logical inconsistency</strong></td><td>Accepting a principle in one case and rejecting it in a like case when the conclusion is uncomfortable</td><td><a href="../argumentos/e8.html">E8</a></td></tr>
<tr><td><strong>Escaping what is relevant</strong></td><td>Swapping the question "does this harm someone?" for others: tradition, taste, health, who is speaking</td><td><a href="../familias.html">Part IND</a></td></tr>
<tr><td><strong>Partiality</strong></td><td>Giving greater weight to the interests of those who resemble us</td><td><a href="../argumentos/a21.html">A21</a></td></tr>
<tr><td><strong>Relativism</strong></td><td>Treating the question of harming others as a matter of taste</td><td><a href="../argumentos/e2.html">E2</a></td></tr>
<tr><td><strong>Views in conflict with sentience</strong></td><td>Anthropocentrism, environmentalism as a moral view and biocentrism put something other than the capacity to feel at the center</td><td><a href="antiespecismo.html">Antispeciesism and sentientism</a>, <a href="../argumentos/m7.html">M7</a></td></tr>
<tr><td><strong>Moral and cultural stagnation</strong></td><td>Taking current custom as the limit of what is right</td><td><a href="../argumentos/d1.html">D1</a></td></tr>
<tr><td><strong>Making abstractions sacred</strong></td><td>Treating as sacred something that doesn't feel, such as "the natural", a system, a tradition, or concepts like species and ecosystem, and placing it above beings who feel</td><td><a href="../argumentos/m2.html">M2</a>, <a href="../argumentos/m7.html">M7</a>, <a href="../argumentos/a18.html">A18</a></td></tr>
<tr><td><strong>Shielding ideas</strong></td><td>Protecting certain beliefs from any revision. This moral conservatism prevents seeking what is best for all sentient beings, because it rules out new proposals in advance, such as helping wild animals or using science against suffering</td><td><a href="../argumentos/m5.html">M5</a>, <a href="../argumentos/m10.html">M10</a></td></tr>
<tr><td><strong>Lack of motivation and weak will</strong></td><td>Knowing what is right and not acting, because habit, pleasure or social pressure win out over moral belief</td><td><a href="../argumentos/e12.html">E12</a>, <a href="../argumentos/e8.html">E8</a></td></tr>
<tr><td><strong>Injustice</strong></td><td>Accepting that the stronger use the weaker because they can</td><td><a href="../argumentos/c6.html">C6</a></td></tr>
<tr><td><strong>Tribalism</strong></td><td>Dividing the world into "us" and "them" and reserving morality for one's own group</td><td><a href="../argumentos/a13.html">A13</a></td></tr>
<tr><td><strong>Selfishness</strong></td><td>Measuring everything by one's own interest</td><td><a href="../argumentos/e1.html">E1</a></td></tr>
<tr><td><strong>Ableism</strong></td><td>Measuring someone's worth by intelligence or ability, the same criterion that excludes disabled people</td><td><a href="../argumentos/a1.html">A1</a>, <a href="../argumentos/a11.html">A11</a></td></tr></table></div>
<h2>Why this matters</h2><p>The principles in the first table are the same ones that support human rights, the fight against racism, sexism and ableism, and care for future generations. The attitudes in the second table are the same ones that, throughout history, have served to exclude humans from the moral circle. That's why defending animals doesn't compete with other just causes: it rests on the same foundations and faces the same adversaries.</p>
<h2>Knowing isn't enough, but it helps</h2><p>Some people know animal ethics well and still eat animals. That doesn't show moral beliefs motivate no one. It shows they don't decide behavior on their own: a person may think the wrong isn't serious, may have stronger competing motivations, such as habit, pleasure and social pressure, or may simply choose not to act. As Luciano Carlos Cunha argues, emotional persuasion faces the same limits, and rational persuasion has the advantage of explaining why a practice should be rejected. That's why, besides arguments, it helps to create conditions that make action easier: environments, habits and groups that make it easier to do what one already knows is right.</p>
<p>It's also why choosing arguments well is worthwhile. An argument that persuades someone through selfishness, tribalism or anthropocentrism can win a conversation and, at the same time, strengthen exactly what weakens the cause. That's the subject of the page <a href="argumentos-diretos.html">Restraint with indirect arguments</a>.</p>''',
  fontes=[('The argument from relevance', 'https://www.animal-ethics.org/argument-from-relevance/'), ('The Expanding Circle', None), ('Moral Tribes', None), ('Crenças morais, motivação para agir e o caso de especialistas em ética animal que consomem animais (in Portuguese)', 'https://senciencia.org/2024/07/08/crencas-morais-motivacao-para-agir-e-o-caso-de-especialistas-em-etica-animal-que-consomem-animais'), ('Beasts of Burden: Animal and Disability Liberation', None), ('Eclipse of Reason', None), ('A Theory of Justice', None)]),
 'argumentos-diretos': dict(s='direct-arguments', selo='Strategy', t='Restraint with indirect arguments',
  res='Just as vegans should be careful when criticizing other vegans, those who use health and environment arguments should be careful not to strengthen anthropocentrism and environmentalism, which work against animals.',
  corpo='''<p>This guide asks for restraint in two directions. On the <a href="../argumentos-ruins.html">Stop saying this</a> page, it asks vegans to correct their own bad arguments without turning internal criticism into the main subject. Here the request is different: that those who use indirect arguments, about health, the environment or the economy, hold back on them and make room for direct arguments, which deal with what matters: animals are someone, not something.</p>
<h2>The problem isn't only weakness</h2><p>Indirect arguments have true parts and can be useful for correcting misinformation. The deeper problem is that they can ground the wrong principle. Someone who stops eating meat because it's bad for their health learns that the criterion is self-interest. Someone who stops because of emissions learns that the criterion is the planet. In neither case do they learn that the animal matters.</p>
<div class="tabela"><table><tr><th scope="col">Indirect argument</th><th scope="col">Principle it teaches</th><th scope="col">Where that principle can lead</th></tr>
<tr><td>"Meat is bad for your health"</td><td>What matters is my wellbeing</td><td>Fish, "lean" chicken and fish oil capsules; abandoning veganism if the person feels worse (<a href="../argumentos/g10.html">G10</a>)</td></tr>
<tr><td>"Animal farming is destroying the planet"</td><td>What matters is environmental impact</td><td>"Regenerative" meat, insect farming, hunting invasive species, swapping beef for chicken or shrimp (<a href="../argumentos/h3.html">H3</a>, <a href="../argumentos/h11.html">H11</a>, <a href="../argumentos/h14.html">H14</a>)</td></tr>
<tr><td>"It's cheaper"</td><td>What matters is price</td><td>Going back to meat when it gets cheaper (<a href="../argumentos/j1.html">J1</a>)</td></tr></table></div>
<p>Swapping beef for chicken, fish or shrimp shows the risk well. Since one cow yields far more meat than a chicken or a fish, this swap can lower emissions per kilo and, at the same time, multiply the number of animals bred and killed. A successful environmental argument can make things worse for animals.</p>
<h2>Strengthening the adversary</h2><p>Anthropocentrism and environmentalism as a moral view are among the main reasons animals are excluded (<a href="fundamentos.html">What supports animal ethics</a>). An argument that only works within these views can win a conversation and, at the same time, reinforce the idea that animals matter only for what they do to us or to the ecosystem. Other movements defending harmed groups don't argue that discrimination is bad because it harms the discriminator's health or the climate.</p>
<p>There's also a sign in practice. In a Faunalytics survey of former vegetarians and vegans, health was the only motivation cited by a majority (58%) of those who abandoned the diet. The figure doesn't prove cause, but it fits the idea that a change built on self-interest unravels when that interest seems to shift.</p>
<h2>How to use them without losing your way</h2><ul><li><strong>Use facts to correct facts.</strong> If someone says a vegan diet is dangerous or that vegans' soy is clearing the Amazon, correct it with evidence. It's an answer to an objection, not the foundation.</li><li><strong>Always return to the moral question.</strong> After correcting the fact, ask: even if it were true, would it justify what is done to animals?</li><li><strong>Don't promise what isn't up to you.</strong> Saying veganism will make someone healthier or save the planet turns the cause into an empirical bet that can be lost (<a href="../argumentos-ruins.html">Stop saying this</a>).</li><li><strong>Start with the fundamentals.</strong> Sentience, relevance, impartiality and the test of applying the same rule to humans are arguments that work in any scenario and protect against future suffering, including that of wild animals and new minds.</li></ul>
<h2>Restraint isn't prohibition</h2><p>This isn't about forbidding those who came to veganism through health or climate, or looking down on them. Many arrive by one path and stay for another. It's about not letting the indirect argument take the place of the direct one, and not teaching, without noticing, the principles that keep animals outside the moral circle.</p>''',
  fontes=[('A Journey Through Animal Ethics, vol. IX, ch. 10: Why focus on consideration for sentient beings and on the future?', 'https://questaodeetica.biblioverse.org/en/v9/10-why-focus-on-consideration-for-sentient-beings-and-on-the.html'), ('Faunalytics, Study of Current and Former Vegetarians and Vegans', 'https://faunalytics.org/a-summary-of-faunalytics-study-of-current-and-former-vegetarians-and-vegans/'), ('Rationalizing meat consumption. The 4Ns', 'https://doi.org/10.1016/j.appet.2015.04.011')]),
}

# Library: keyed by the book's title (titles stay in the original language)
FOCOS = {'rebater': 'Answers to objections', 'etica': 'Ethical foundations', 'psico': 'Psychology of the habit'}
LIVROS = {
 'An Introduction to Animals and Political Theory': dict(d='Examines how the major political theories, such as liberalism, utilitarianism, communitarianism, Marxism and feminism, treat animals, and shows where each fails in excluding them.', ul='Publisher'),
 'Uma breve introdução à ética animal': dict(st='A short introduction to animal ethics: from the classic questions to current debates', d='Gathers the arguments used to defend speciesism and presents the objections to each, for general readers and academics.', ul='Review'),
 'Uma Jornada pela Ética Animal': dict(st='A Journey Through Animal Ethics, a 12-volume collection', ed='Open access', d='The most complete collection in Portuguese: each chapter examines an objection, and volume XII sums up the answers in tables. The basis of the Questão de Ética site, which has an English version.', u=QE_EN, ul='Read free'),
 'Ética & Animais': dict(st='Ethics & Animals: a guide to philosophical argument', d='Presents the main ethical theories applied to animals, from Singer and Regan to the ethics of care, for those who want to argue on philosophical grounds.', ul='About the book'),
 '30 Non-Vegan Excuses & How to Respond to Them': dict(st='', ed='Free e-book', d='Short and direct: thirty common excuses, each with an answer.', ul='Read free'),
 'How to Argue with a Meat Eater': dict(d='Goes through the most common objections, from ethics to health, nutrition and the environment, with tips for staying calm in the conversation.', ul='Publisher'),
 'This Is Vegan Propaganda': dict(d='Takes apart the stories the industry tells about animal farming and shows what actually happens.', ul='Catalog'),
 'Eat Like You Care': dict(st='An Examination of the Morality of Eating Animals', d='Examines the morality of eating animals and answers, one by one, the most common justifications.', ul='Catalog'),
 'Introduction to Animal Rights': dict(d='Takes on the burning-house dilemma and shows why a choice in an emergency does not justify exploitation.', ul='Publisher'),
 'Making a Stand for Animals': dict(d='A clear introduction to animal ethics that answers the objections to ending speciesism, including about wild animals.', ul='Catalog'),
 'Meat Logic': dict(d='Assesses, one by one, the rationalizations for eating animals in light of the fact that we do not need them to live well.', ul='Review'),
 'Por que amamos cachorros, comemos porcos e vestimos vacas': dict(st='Portuguese edition of Why We Love Dogs, Eat Pigs, and Wear Cows: An Introduction to Carnism', d='Explains carnism, the belief system that makes us love some animals and eat others without noticing the contradiction.', ul='About the book'),
 'How To Argue With Vegans': dict(ed='Self-published', d='From the author of the Vegan Sidekick comics: goes through the most common objections, from dismissive reactions to the more elaborate ones, and shows why none justifies exploiting animals.', ul='Catalog'),
 'Como sobreviver sem carne e outros milagres inexplicáveis': dict(st='How to survive without meat and other inexplicable miracles', ed='Oficina do Livro (Portugal)', d='A recent release: answers awkward questions about giving up meat using science and history, without moralizing.', ul='Bookstore'),
 'Libertação animal já': dict(st='Portuguese edition of Animal Liberation Now', ed='WMF Martins Fontes; Brazilian edition 2026', d='The revised and updated version of the 1975 classic, with recent data on factory farming, animal testing and new technologies.', ul='Publisher'),
 'Libertação Animal': dict(st='Portuguese edition of Animal Liberation', d='The book that popularized the term "speciesism" and the principle of equal consideration of interests.', ul='About the book'),
 'Veganismo': dict(st='Veganism: the many reasons for a more ethical life', ed='Self-published', d='Brings together, in Portuguese, the arguments of the vegan movement, with the references behind each one.', ul='Catalog'),
}
SITES = {
 'https://www.sentientism.info': ('Sentientism', 'A worldview committed to evidence, reason and compassion for all sentient beings, with a community and interviews'),
 'https://s-risks.org': ('Reducing Risks of Future Suffering', 'A blog on risks of large-scale suffering in the future, including those linked to artificial intelligence'),
 'https://sentience-research.org': ('Sentience Research', 'A research project on identifying, measuring and understanding sentience in animals, humans and machines'),
 'https://lab.sapienship.co': ('Sapienship Lab', 'A media hub for educators, students and lifelong learners'),
 'https://ethicalfood.biblioverse.org': ('Ethical Food Guide', 'A directory and map of alternative protein companies, from plant-based and cultivated meat to fermentation'),
 'https://animalcharityevaluators.org': ('Animal Charity Evaluators', 'Researches the most effective ways to help animals and recommends charities'),
 'https://animalsaustralia.org': ('Animals Australia', 'An Australian animal protection organization'),
 'https://longtermrisk.org': ('Center on Long-Term Risk', 'Research on worst-case risks from the development of advanced artificial intelligence'),
 'https://faunalytics.org': ('Faunalytics', 'Research and data to help advocates help animals effectively'),
 'https://www.instagram.com/inea.educacao.antiespecista/': ('Instituto de Educação Antiespecista', 'Antispeciesist education in Brazil, on Instagram (in Portuguese)'),
 'https://invinciblewellbeing.com': ('Invincible Wellbeing', 'Research, with academic partners, on the biological roots of pain and ways to treat it'),
 'https://www.lse.ac.uk/sentience': ('Jeremy Coller Centre for Animal Sentience', 'A research centre on animal sentience at the London School of Economics'),
 'https://new-harvest.org': ('New Harvest', 'A research institute for cellular agriculture, such as cultivated meat'),
 'https://rethinkpriorities.org': ('Rethink Priorities', 'Research on priorities for doing good, including the welfare of animals and invertebrates'),
 'https://www.sentienceinstitute.org': ('Sentience Institute', 'A research institute on social and technological change, especially moral circle expansion'),
 'https://sentientfutures.ai': ('Sentient Futures', 'Research, policy and community for taking into account the welfare of animals and artificial minds'),
 'https://gfi.org': ('The Good Food Institute', 'A nonprofit supporting plant-based, cultivated and fermentation-made proteins'),
 'https://www.wildanimalinitiative.org': ('Wild Animal Initiative', 'Research on the welfare of wild animals'),
 'https://questaodeetica.biblioverse.org/desbancando.html': ('Questão de Ética', "The 248 objections from Luciano Carlos Cunha's collection, with answers, also in English"),
 'https://www.adaptt.org': ('ADAPTT', 'An archive of writing on veganism, ethics and animal liberation, with starter guides, lectures and ways to take action'),
 'https://senciencia.org/': ('Senciência', 'Texts on animal ethics and speciesism, in Portuguese'),
 'https://www.animal-ethics.org/pt/': ('Animal Ethics', 'International organization with texts on speciesism, sentience and wild animals'),
 'https://medium.com/veganismo-s': ('Veganismos', 'A Medium publication on veganism and animal ethics, in Portuguese'),
 'https://www.carnismdebunked.com': ('Carnism Debunked', 'Answers to the arguments used to defend animal exploitation'),
 'https://www.sentienceinstitute.org/foundational-questions-summaries': ('Sentience Institute', 'A summary of the evidence on the foundational questions of effective animal advocacy'),
 'https://veganadvocacy.org/communication-hacks': ('Center for Effective Vegan Advocacy', 'Training for advocates, with communication tips for talking about veganism'),
 'https://reducing-suffering.org/': ('Essays on Reducing Suffering', 'Essays on reducing suffering, focused on farmed animals, wild animals and invertebrates'),
 'https://centerforreducingsuffering.org/': ('Center for Reducing Suffering', 'Research on reducing severe suffering, taking all sentient beings into account'),
 'https://www.hedweb.com/confile.htm': ('HedWeb', 'Writings on using biotechnology to abolish suffering, including that of wild animals'),
 'https://infighting.org': ('End Infighting', 'Causes and costs of infighting in social movements, and tools to avoid it'),
 'https://yourveganfallacyis.com/pt-br': ('Your Vegan Fallacy Is', 'Common fallacies against veganism, on cards'),
 'https://www.alyssonaugusto.com.br/argumentos': ('Argumentos em defesa dos animais', 'Answers organized by topic, in Portuguese'),
 'https://veganagente.com.br/falacias-antiveganas/': ('Guia de falácias antiveganas', 'A guide to anti-vegan fallacies, in Portuguese'),
}
SITES_URL = {'https://questaodeetica.biblioverse.org/desbancando.html': QE_EN + 'debunking-objections.html', 'https://www.animal-ethics.org/pt/': 'https://www.animal-ethics.org/', 'https://yourveganfallacyis.com/pt-br': 'https://yourveganfallacyis.com/en'}

# Long texts of build.py (module-level constants)
TEXTOS = {
 'DESCRICAO': 'The argument guide for animal advocates systematically catalogs every idea used to exploit, harm or kill animals or to avoid helping them, with a thorough explanation of the objections and biases of people who oppose veganism and antispeciesism.',
 'IND_TEMA': {'G': 'health and nutrition', 'H': 'the environment and agriculture', 'I': 'the usefulness of testing, clothing, entertainment and companion animals',
              'J': 'cost, practicality and the economy', 'K': 'effectiveness and individual responsibility', 'L': 'who defends veganism'},
 'IND_EXEMPLO': {
  'G': "If veganism were defended on health grounds, anyone who manages to be healthy eating animals, and many people do, would have no reason to change. And if an animal product turned out to be demonstrably healthier, the same argument would start defending exploitation. The eater's health says nothing about whether what is done to the animal is just.",
  'H': 'If veganism were defended on environmental grounds, low-impact exploitation would be acceptable, even if it killed more sentient beings. And it is already being promoted: insect farming, "sustainable" hunting, "sustainable" leather. It is possible to reduce environmental impact and increase exploitation at the same time.',
  'I': 'If the defense of animals depended on showing that testing, clothing or entertainment with animals are useless, one useful use would be enough to justify them. But usefulness does not settle the question: no benefit justifies using people who did not consent, and the same holds for animals.',
  'J': 'If veganism were defended for being cheap, practical or good for the economy, any situation in which exploitation were cheaper or created more jobs would justify it. No one accepts this reasoning when the victims are human: exploiting people was once profitable too.',
  'K': "If veganism were defended only by each person's impact, anyone who proved their purchase changes nothing would be let off. But no one accepts this for other harms: taking part in an injustice is still wrong even when each person's share is small.",
  'L': 'If the question depended on who defends animals, vegans being pleasant and consistent would make the argument valid, and being annoying and inconsistent would make it invalid. But the animals suffer just the same, whoever the messenger is.',
 },
 'IND_AVISO': ('This is an indirect argument: it discusses health, the environment, the economy, practicality or who defends veganism, not whether animals deserve respect. '
    'Many activists question using this kind of argument to defend animals, because it sidesteps what matters. '
    'Other social movements do not do this: no one defends the rights of people who face discrimination by saying that treating them fairly is good for the environment. '
    'Here, the facts serve to correct what is wrong; the moral justification comes from respect for the animals.'),
 'IND_TEXTO': ('<p><strong>Indirect</strong> arguments do not discuss whether it is right to exploit animals. They discuss health, the environment, the economy, practicality or the credibility of those who defend veganism. '
    'Many activists and animal rights philosophers question using this kind of argument to defend animals, because it sidesteps what is important: respect for the animals themselves.</p>'
    '<p>Other social movements do not rely on indirect arguments to defend humans. People fighting for the rights of minorities and of those who are harmed do not need to prove that treating them fairly is good for the environment, for health or for the economy: '
    'the fact that they are harmed is reason enough. Even so, veganism is often defended with health or environmental arguments, '
    'as if the end of animal exploitation were not reason enough in itself.</p>'
    '<p>Indirect arguments are useful on the level of facts: they show that a practical objection is false, that vegan living is healthy and possible, that animal farming causes harm. '
    'But on their own they do not justify the morality of respecting animals. And they can even pull the other way: "sustainable" leather, "sustainable" hunting, organic meat, insect farming and '
    'genetically modified animals are defended in the name of the environment and keep or increase exploitation (<a href="argumentos/h13.html">H13</a>). '
    'That is why each chapter in Part IND answers on the argument\'s own ground, corrects the facts and brings the conversation back to the moral question.</p>'
    '<p>When health, protein or the environment are used to justify eating animals, the reasoning usually fails on two levels. On the level of facts, because the premises are often false: '
    'a well-planned plant-based diet meets our needs and causes less environmental harm. On the moral level, because it leaps from what <em>is</em> to what <em>ought to be</em>, '
    'the move philosophers call the is-ought fallacy: even if eating animals brought some benefit, that would not show it is just to make them suffer and die to obtain it. '
    'Showing the facts is always necessary; stopping there is never enough.</p>'),
 'EQUILIBRIO': """<section class="equilibrio" id="corrigir-sem-perder-o-foco" aria-labelledby="eq-t"><h2 id="eq-t">Correcting without losing focus</h2>
<p>Correcting our own arguments is part of any movement that takes the truth seriously. A bad argument from a vegan gets taken apart in the first conversation with someone well informed, and the whole cause takes the loss. That is why this page exists.</p>
<p>But correction has a cost. The time and energy of animal advocates are limited, and every hour spent fighting among vegans is an hour less for explaining speciesism, answering the objections of people who still eat animals and producing quality content. It is a trade-off: when infighting takes the place of outward work, the strategy is probably wrong. The <a href="https://infighting.org" target="_blank" rel="noopener">End Infighting</a> project gathers the causes and costs of this kind of conflict in social movements.</p>
<h3>The line is not clear-cut</h3>
<p>Correcting vegans and answering people who exploit animals are not two separate tasks. Dropping a bad argument also prepares the next conversation with someone who is not vegan. Some examples:</p>
<ul>
<li><strong>A correction worth making:</strong> stop saying {RUIM:Gorilas, touros e cavalos}. The argument falls at the first reply and swaps an ethical question for a badly told biology story.</li>
<li><strong>A correction that protects people:</strong> refuting {RUIM:Veganos não precisam suplementar B12}. Here the error does not just weaken the argument; it puts at risk the health of those who believe it.</li>
<li><strong>A fight that is probably not worth it:</strong> weeks of public argument against an activist over one imprecise sentence, while no one gives a good answer to "where do you get your protein?", which almost every vegan has heard.</li>
<li><strong>A debate that can drag on:</strong> the disagreement over strategy, such as welfare reforms or abolition. It is a legitimate debate, but if it takes up all the space, the animals stop being at the center of the conversation.</li>
</ul>
<h3>A rule of thumb</h3>
<p>Before correcting someone, ask: <em>will this correction improve the next conversation with someone who is not yet vegan?</em> If so, correct the argument, not the person, ideally in private or with a better alternative ready. Then get back to the work that matters: explaining why animals count.</p>
</section>""",
}

# Decision trees shown in chapters A1 and A10 ([[ARVORE]] in the chapter file)
ARVORE = {
    'A1': '''<div class="arvore"><p class="q">Rational in what sense?</p><ul><li><span class="r">Strong: abstract reasoning</span>P2 becomes true, <span class="f">but P1 excludes babies and people with profound intellectual disabilities</span></li><li><span class="r">Weak: learning, inferring, solving problems</span>P1 now includes those humans, <span class="f">but P2 becomes false for many animals</span></li></ul></div>''',
    'A10': '''<div class="arvore"><p class="q">Is there a characteristic C?</p><ul><li><span class="r">No, it's just the species</span><span class="f">Bare speciesism: prejudice without a criterion</span></li><li><span class="r">Yes, C is a specific trait</span>Does every human have C?<ul><li><span class="r">No</span><span class="f">Species overlap: it excludes protected humans</span></li><li><span class="r">Yes</span>Is C relevant to pain and death?<ul><li><span class="r">No</span><span class="f">An irrelevant criterion, like knowing algebra</span></li><li><span class="r">Yes</span><span class="f">Then the criterion is sentience, which animals have</span></li></ul></li></ul></li></ul></div>''',
}
