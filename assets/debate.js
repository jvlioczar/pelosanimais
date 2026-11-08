/* Debate simulado: uma pessoa começa com um argumento comum, você escolhe a resposta, e a conversa segue
   pelas conexões do raciocínio antivegano. Dados em <script id="deb-dados">, gerados por tools/build.py. */
(function () {
  var raiz = document.getElementById('debate');
  var bloco = document.getElementById('deb-dados');
  if (!raiz || !bloco) return;
  var D = JSON.parse(bloco.textContent);
  var PONTOS = { f: 2, m: 1, r: 0 };
  var ROTULO = { f: 'Resposta forte', m: 'Resposta fraca', r: 'Resposta ruim' };
  var LIGA = ['Tá, mas ', 'Beleza, mas ', 'Hmm. E ', 'Pode ser, mas ', 'Ok, mas ', 'Mesmo assim, '];

  // Memória leve do que já foi jogado, para não repetir pessoa nem abertura (só neste navegador).
  function le(k) { try { return JSON.parse(localStorage.getItem(k) || '[]'); } catch (e) { return []; } }
  function grava(k, v) { try { localStorage.setItem(k, JSON.stringify(v.slice(-24))); } catch (e) {} }
  function sorteia(lista) { return lista[Math.floor(Math.random() * lista.length)]; }
  function embaralha(l) { l = l.slice(); for (var i = l.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)); var t = l[i]; l[i] = l[j]; l[j] = t; } return l; }
  function novoDe(lista, chave) {
    var vistos = le(chave), livres = lista.filter(function (x) { return vistos.indexOf(x) < 0; });
    if (!livres.length) { livres = lista.slice(); vistos = []; }
    var x = sorteia(livres); vistos.push(x); grava(chave, vistos); return x;
  }
  function esc(s) { var d = document.createElement('div'); d.textContent = s; return d.innerHTML; }
  function minuscula(s) { if (/^I(?![a-z])/.test(s)) return s; return /^[A-ZÀ-Ý](?![A-ZÀ-Ý0-9])/.test(s) ? s.charAt(0).toLowerCase() + s.slice(1) : s; }

  var proximo = null, J;

  function preparaProximo() {
    var p = novoDe(D.pessoas.map(function (x, i) { return i; }), 'deb-pessoas');
    var a = novoDe(D.aberturas, 'deb-aberturas');
    proximo = { p: p, a: a };
  }

  function comeca() {
    if (!proximo) preparaProximo();
    J = { pessoa: D.pessoas[proximo.p], total: 4 + Math.floor(Math.random() * 3), usados: [], hist: [], atual: proximo.a, motivo: '' };
    proximo = null;
    raiz.innerHTML = '<div class="deb-cab"><span class="deb-av" aria-hidden="true">' + esc(J.pessoa[0].charAt(0)) + '</span><div><b>' + esc(J.pessoa[0]) + '</b><small>' + esc(J.pessoa[1]) + '</small></div><span class="deb-cont" id="deb-cont"></span></div><div class="deb-log" id="deb-log" aria-live="polite"></div>';
    rodada();
  }

  function rodada() {
    var c = J.atual, n = D.n[c], i = J.usados.length;
    J.usados.push(c);
    document.getElementById('deb-cont').textContent = 'Rodada ' + (i + 1) + ' de ' + J.total;
    var liga = /\bmas\b/.test(n.f) ? sorteia(['Olha, ', 'Sinceramente? ', 'Hmm. ']) : sorteia(LIGA);
    var fala = i === 0 ? n.f : liga + minuscula(n.f);
    var log = document.getElementById('deb-log');
    var h = '';
    if (J.motivo) h += '<p class="deb-rumo">O raciocínio muda de rumo: ' + esc(minuscula(J.motivo)) + '</p>';
    h += '<div class="deb-fala ela" style="--c:' + n.cor + '"><p>' + esc(fala) + '</p><a class="deb-cod" href="' + n.u + '" target="_blank" rel="noopener">' + c + '</a></div>';
    var ops = embaralha(['f', 'm', 'r']);
    h += '<div class="deb-ops" role="group" aria-label="Escolha sua resposta"><p class="ti">O que você responde?</p>' + ops.map(function (t) {
      return '<button type="button" class="deb-op" data-t="' + t + '">' + esc(n.o[t][0]) + '</button>';
    }).join('') + '</div>';
    var bloco = document.createElement('div'); bloco.className = 'deb-rodada'; bloco.innerHTML = h; log.appendChild(bloco);
    bloco.querySelectorAll('.deb-op').forEach(function (b) { b.addEventListener('click', function () { escolhe(bloco, c, b.getAttribute('data-t')); }); });
    bloco.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }

  function escolhe(bloco, c, t) {
    var n = D.n[c];
    J.hist.push({ c: c, t: t });
    bloco.querySelector('.deb-ops').outerHTML = '<div class="deb-fala voce"><p>' + esc(n.o[t][0]) + '</p></div>' +
      '<div class="deb-retorno t-' + t + '"><p class="deb-nota">' + ROTULO[t] + '</p><p>' + esc(n.o[t][1]) + '</p>' +
      (t !== 'f' ? '<p class="deb-melhor"><b>Uma resposta melhor:</b> ' + esc(n.o.f[0]) + '</p>' : '') +
      '<p><a href="' + n.u + '" target="_blank" rel="noopener">Ver a resposta completa a "' + esc(n.f) + '" ↗</a></p></div>';
    var fim = J.usados.length >= J.total;
    var seguir = document.createElement('button');
    seguir.type = 'button'; seguir.className = 'btn deb-seguir'; seguir.textContent = fim ? 'Ver o resultado' : 'Continuar a conversa';
    bloco.appendChild(seguir);
    seguir.addEventListener('click', function () { seguir.remove(); if (fim) resultado(); else avanca(c); });
  }

  function avanca(c) {
    // Segue as conexões do raciocínio antivegano; sem conexão disponível, a pessoa muda de assunto.
    var cands = D.n[c].p.filter(function (x) { return J.usados.indexOf(x[0]) < 0; });
    if (cands.length) { var x = sorteia(cands); J.atual = x[0]; J.motivo = x[1]; }
    else {
      var livres = Object.keys(D.n).filter(function (k) { return J.usados.indexOf(k) < 0; });
      J.atual = sorteia(livres); J.motivo = 'a conversa muda de assunto';
    }
    rodada();
  }

  function resultado() {
    var pts = J.hist.reduce(function (s, h) { return s + PONTOS[h.t]; }, 0), max = J.hist.length * 2, pc = Math.round(100 * pts / max);
    var nome = J.pessoa[0], nivel, frase;
    if (pc >= 80) { nivel = 'Você foi muito bem'; frase = nome + ': "Nunca tinha pensado por esse lado. Me manda aquele link depois?"'; }
    else if (pc >= 50) { nivel = 'Você foi razoável'; frase = nome + ': "Alguns pontos fazem sentido, outros achei forçados."'; }
    else { nivel = 'O debate não foi bem'; frase = nome + ': "Viu? Nem vocês sabem explicar direito."'; }
    preparaProximo();
    var px = D.pessoas[proximo.p], pa = D.n[proximo.a];
    var lista = J.hist.map(function (h) {
      var n = D.n[h.c];
      return '<li class="t-' + h.t + '"><a href="' + n.u + '" target="_blank" rel="noopener">' + esc(n.f) + '</a><span>' + ROTULO[h.t] + '</span></li>';
    }).join('');
    var r = document.createElement('section'); r.className = 'deb-fim'; r.setAttribute('aria-labelledby', 'deb-fim-t');
    r.innerHTML = '<p class="deb-placar">' + pts + ' de ' + max + ' pontos</p><h2 id="deb-fim-t">' + nivel + '</h2><p class="deb-reacao">' + esc(frase) + '</p>' +
      '<ol class="deb-hist">' + lista + '</ol>' +
      '<p class="fino">Forte vale 2 pontos, fraca vale 1 e ruim vale 0. Num debate real, o tom e a escuta importam tanto quanto o argumento.</p>' +
      '<div class="deb-prox"><p class="ti">Próximo debate</p><p><b>' + esc(px[0]) + '</b>, ' + esc(px[1]) + ', vai começar com: "' + esc(pa.f) + '"</p>' +
      '<button type="button" class="btn" id="deb-de-novo">Começar o próximo debate</button> <a class="btn alt" href="raciocinio.html">Ver o raciocínio antivegano</a></div>';
    document.getElementById('deb-log').appendChild(r);
    r.scrollIntoView({ behavior: 'smooth', block: 'start' });
    document.getElementById('deb-de-novo').addEventListener('click', function () { comeca(); raiz.scrollIntoView({ behavior: 'smooth', block: 'start' }); });
  }

  preparaProximo();
  var px = D.pessoas[proximo.p];
  raiz.innerHTML = '<div class="deb-intro"><p><b>' + esc(px[0]) + '</b>, ' + esc(px[1]) + ', quer conversar sobre veganismo. A conversa terá de 4 a 6 rodadas, seguindo o caminho que esses debates costumam fazer.</p><button type="button" class="btn" id="deb-ini">Começar o debate</button></div>';
  document.getElementById('deb-ini').addEventListener('click', comeca);
})();
