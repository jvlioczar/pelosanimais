"""Gera os ícones PNG (192, 512 e apple-touch 180) e a imagem de compartilhamento (assets/share.png) a partir do desenho do logo: coelho amarelo num balão de fala verde.
Uso: python tools/icones.py (também é chamado pelo build)."""
import os
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TINTA = (10, 55, 3); AMARELO = (255, 235, 91); CREME = (252, 250, 245); AZUL = (214, 236, 251)
K = 4  # desenha maior e reduz, para suavizar


def elipse_girada(base, cx, cy, rx, ry, ang, cor):
    """Cola em base uma elipse de semieixos rx, ry girada ang graus (sentido horário, como no SVG)."""
    lado = int(2 * max(rx, ry)) + 4
    camada = Image.new('L', (lado, lado), 0)
    ImageDraw.Draw(camada).ellipse([lado / 2 - rx, lado / 2 - ry, lado / 2 + rx, lado / 2 + ry], fill=255)
    camada = camada.rotate(-ang, resample=Image.BICUBIC)
    base.paste(Image.new('RGB', (lado, lado), cor), (int(cx - lado / 2), int(cy - lado / 2)), camada)


def logo(im, x0, y0, esc):
    """Desenha o logo (viewBox 40x40) em im, com origem (x0, y0) e esc pixels por unidade."""
    d = ImageDraw.Draw(im)
    p = lambda x, y: (x0 + x * esc, y0 + y * esc)
    d.rounded_rectangle([*p(2, 2), *p(38, 32)], radius=4 * esc, fill=TINTA)
    d.polygon([p(19, 31), p(11, 38), p(11, 31)], fill=TINTA)
    for cx, ang in ((15.5, -10), (24.5, 10)):
        elipse_girada(im, *p(cx, 11.5), 2.7 * esc, 6.8 * esc, ang, AMARELO)
    d.ellipse([*p(12, 15.2), *p(28, 28.8)], fill=AMARELO)
    for cx, cy, r in ((17, 21, 1.1), (23, 21, 1.1), (20, 24.2, 1)):
        d.ellipse([*p(cx - r, cy - r), *p(cx + r, cy + r)], fill=TINTA)


def icone(n, fundo=CREME, margem=0.12):
    im = Image.new('RGB', (n * K, n * K), fundo)
    lado = n * K * (1 - 2 * margem)
    logo(im, n * K * margem, n * K * margem, lado / 40)
    return im.resize((n, n), Image.LANCZOS)


def fonte(nomes, tam):
    for nm in nomes:
        p = os.path.join(os.environ.get('WINDIR', 'C:/Windows'), 'Fonts', nm)
        if os.path.exists(p): return ImageFont.truetype(p, tam)
    return ImageFont.load_default()


TXT = {
    'pt': ('Guia de Argumentação', 'Pelos Animais', 'Toda objeção merece', 'uma boa resposta.', 'Confira mais de {n} argumentos contra o veganismo e o antiespecismo, tratados de forma honesta', 'pelosanimais.biblioverse.org'),
    'en': ('For the Animals', 'An Argument Guide', 'Every objection deserves', 'a good answer.', 'Explore more than {n} arguments against veganism and antispeciesism, treated honestly', 'fortheanimals.biblioverse.org'),
}

# As mesmas fontes do site (Google Fonts, licença OFL), guardadas em tools/fontes
FONTES = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fontes')
def fonte_site(arq, tam, peso):
    p = os.path.join(FONTES, arq)
    if not os.path.exists(p): return fonte(['segoeuib.ttf', 'arialbd.ttf'], tam)
    f = ImageFont.truetype(p, tam)
    try: f.set_variation_by_name(peso)
    except Exception: pass
    return f
TITULO, TEXTO, MONO = 'mozillaheadline/MozillaHeadline[wdth,wght].ttf', 'inter/Inter[opsz,wght].ttf', 'jetbrainsmono/JetBrainsMono[wght].ttf'

def quebra(d, texto, fnt, larg):
    """Quebra o texto em linhas que caibam na largura. Em duas linhas, equilibra os tamanhos para não deixar uma palavra sozinha."""
    ps = texto.split()
    if d.textlength(texto, font=fnt) > larg:
        pares = [(' '.join(ps[:i]), ' '.join(ps[i:])) for i in range(1, len(ps))]
        cabem = [p for p in pares if max(d.textlength(x, font=fnt) for x in p) <= larg]
        if cabem: return list(min(cabem, key=lambda p: max(d.textlength(x, font=fnt) for x in p)))
    linhas, atual = [], ''
    for p in texto.split():
        t = (atual + ' ' + p).strip()
        if d.textlength(t, font=fnt) <= larg: atual = t
        else: linhas.append(atual); atual = p
    return linhas + [atual]

def compartilhar(n_args, lg='pt'):
    m1, m2, t1, t2, sb, dom = TXT[lg]
    W, H = 1200 * 2, 630 * 2
    im = Image.new('RGB', (W, H), AZUL)
    d = ImageDraw.Draw(im)
    # folha pautada, como no site
    d.rounded_rectangle([90, 90, W - 90, H - 90], radius=56, fill=CREME, outline=TINTA, width=6)
    for y in range(330, H - 120, 76): d.line([150, y, W - 150, y], fill=(205, 225, 240), width=3)
    logo(im, 150, 140, 5.4)
    marca = fonte_site(TITULO, 56, b'Bold')
    d.text((390, 180), m1, font=marca, fill=TINTA)
    d.text((390, 248), m2, font=marca, fill=TINTA)
    tit = fonte_site(TITULO, 150, b'Bold')
    d.text((150, 450), t1, font=tit, fill=TINTA)
    x0, y0, x1, y1 = d.textbbox((150, 630), t2, font=tit)
    d.rectangle([x0 - 16, y0 + 10, x1 + 16, y1 + 14], fill=AMARELO)
    d.text((150, 630), t2, font=tit, fill=TINTA)
    sub = fonte_site(TEXTO, 46, b'SemiBold')
    y = 850
    for ln in quebra(d, sb.format(n=n_args // 10 * 10), sub, W - 300):
        d.text((150, y), ln, font=sub, fill=TINTA); y += 60
    d.text((150, y + 18), dom, font=fonte_site(MONO, 40, b'Bold'), fill=(60, 90, 60))
    return im.resize((1200, 630), Image.LANCZOS)


def gera(n_args, pasta=None, lg='pt'):
    a = pasta or os.path.join(ROOT, 'assets')
    icone(192).save(os.path.join(a, 'icon-192.png'), optimize=True)
    icone(512).save(os.path.join(a, 'icon-512.png'), optimize=True)
    icone(180).save(os.path.join(a, 'apple-touch-icon.png'), optimize=True)
    compartilhar(n_args, lg).save(os.path.join(a, 'share.png'), optimize=True)


if __name__ == '__main__':
    gera(151)
