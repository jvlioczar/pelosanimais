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
    'pt': ('Guia de Argumentação', 'Pelos Animais', 'Toda objeção tem', 'uma resposta.', '{n} argumentos contra o veganismo, com a versão mais forte e a resposta', 'pelosanimais.biblioverse.org'),
    'en': ('For the Animals', 'An Argument Guide', 'Every objection has', 'an answer.', '{n} arguments against veganism, in their strongest form, with the answer', 'fortheanimals.biblioverse.org'),
}

def compartilhar(n_args, lg='pt'):
    m1, m2, t1, t2, sb, dom = TXT[lg]
    W, H = 1200 * 2, 630 * 2
    im = Image.new('RGB', (W, H), AZUL)
    d = ImageDraw.Draw(im)
    # folha pautada, como no site
    d.rounded_rectangle([90, 90, W - 90, H - 90], radius=56, fill=CREME, outline=TINTA, width=6)
    for y in range(330, H - 120, 76): d.line([150, y, W - 150, y], fill=(205, 225, 240), width=3)
    logo(im, 150, 140, 5.4)
    marca = fonte(['seguibl.ttf', 'segoeuib.ttf', 'arialbd.ttf'], 54)
    d.text((390, 180), m1, font=marca, fill=TINTA)
    d.text((390, 248), m2, font=marca, fill=TINTA)
    tit = fonte(['seguibl.ttf', 'georgiab.ttf', 'arialbd.ttf'], 150)
    d.text((150, 470), t1, font=tit, fill=TINTA)
    l2 = t2
    x0, y0, x1, y1 = d.textbbox((150, 660), l2, font=tit)
    d.rectangle([x0 - 16, y0 + 20, x1 + 16, y1 + 14], fill=AMARELO)
    d.text((150, 660), l2, font=tit, fill=TINTA)
    sub = fonte(['segoeuib.ttf', 'arialbd.ttf'], 50)
    d.text((150, 920), sb.format(n=n_args), font=sub, fill=TINTA)
    d.text((150, 1000), dom, font=fonte(['consolab.ttf', 'cour.ttf', 'arialbd.ttf'], 44), fill=(60, 90, 60))
    return im.resize((1200, 630), Image.LANCZOS)


def gera(n_args, pasta=None, lg='pt'):
    a = pasta or os.path.join(ROOT, 'assets')
    icone(192).save(os.path.join(a, 'icon-192.png'), optimize=True)
    icone(512).save(os.path.join(a, 'icon-512.png'), optimize=True)
    icone(180).save(os.path.join(a, 'apple-touch-icon.png'), optimize=True)
    compartilhar(n_args, lg).save(os.path.join(a, 'share.png'), optimize=True)


if __name__ == '__main__':
    gera(151)
