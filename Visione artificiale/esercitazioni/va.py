import cv2 as cv
import numpy as np
import IPython
import html
import base64
from ipywidgets import IntSlider


def show(*images, enlarge_small_images = True, max_per_row = -1, font_size = 0):
    """
    Visualizza una o più immagini nell'output della cella, 
    con un eventuale titolo sopra ciascuna di esse.
    Esempi di utilizzo:
    - va.show(img) : visualizza l'immagine img
    - va.show(img1, img2, img3) : visualizza le immagini img1, img2 e img3
    - va.show(img, title) : visualizza l'immagine img con il titolo title
    - va.show((img1, title1), (img2, title2)) : visualizza le immagini img1 e img2 con i rispettivi titoli title1 e title2
    """
    if len(images) == 2 and type(images[1])==str:
        # Gestisce il caso in cui è chiamato solo con immagine e titolo separatamente, senza essere una tupla
        images = [(images[0], images[1])]

    def convert(imgOrTuple):
        try:
            img, title = imgOrTuple
            if type(title)!=str: # "Falso positivo", assume fosse solo immagine senza titolo
                img, title = imgOrTuple, ''
        except ValueError: # Non può fare unpack: assume sia solo un'immagine senza titolo
            img, title = imgOrTuple, ''        
        if type(img)==str:
            data = img    # Suppone sia il path
        else:
            img = convert_for_display(img)
            if enlarge_small_images:
                REF_SCALE = 400
                h, w = img.shape[:2]
                if h<REF_SCALE or w<REF_SCALE:
                    # Immagini molto piccole vengono ingrandite
                    scale = max(1, min(REF_SCALE//h, REF_SCALE//w))
                    img = cv.resize(img,(w*scale,h*scale), interpolation=cv.INTER_NEAREST)
            data = 'data:image/png;base64,' + base64.b64encode(cv.imencode('.png', img)[1]).decode('utf8')
        return data, title
    
    if max_per_row == -1:
        max_per_row = len(images)
    
    rows = [images[x:x+max_per_row] for x in range(0, len(images), max_per_row)]
    font = f"font-size: {font_size}px;" if font_size else ""
    
    html_content = ""
    for r in rows:
        l = [convert(t) for t in r]
        html_content += "".join(["<table><tr>"] 
                + [f"<td style='text-align:center;{font}'>{html.escape(t)}</td>" for _,t in l]    
                + ["</tr><tr>"] 
                + [f"<td style='text-align:center;'><img src='{d}'></td>" for d,_ in l]
                + ["</tr></table>"])
    IPython.display.display(IPython.display.HTML(html_content))

def convert_for_display(img):
    if img.dtype!=np.uint8:
        # Valori dei pixel non byte
        a, b = img.min(), img.max()
        if a==b:
            offset, mult, d = 0, 0, 1
        elif a<0:
            # Ci sono dei valori negativi: riscala facendo corrispondere lo 0 a 128
            offset, mult, d = 128, 127, max(abs(a), abs(b))
        else:
            # Tutti valori positivi o zero: riscala [0,max] in [0,255]
            offset, mult, d = 0, 255, b
        # Normalizza e trasforma in byte
        img = np.clip(offset + mult*(img.astype(float))/d, 0, 255).astype(np.uint8)
    return img
        
def center_text(img, text, center, color, fontFace = cv.FONT_HERSHEY_PLAIN, fontScale = 1, thickness = 1, lineType = cv.LINE_AA, max_w = -1):
    """
    Utilizza cv.getTextSize e cv.putText per centrare il testo nel punto center.
    """
    while True:
        (w, h), _ = cv.getTextSize(text, fontFace, fontScale, thickness)
        if max_w<0 or w<max_w or fontScale<0.2:
            break
        fontScale *= 0.8
    pt = (center[0]-w//2, center[1]+h//2)
    cv.putText(img, text, pt, fontFace, fontScale, color, thickness, lineType)

    
def draw_hist(hist, height = 192, back_color = (160,225,240), border = 5):
    """
    Restituisce un'immagine con il disegno dell'istogramma.
    """
    size = hist.size
    img = np.full((height, size+border*2, 3), back_color, dtype=np.uint8)
    nh = np.empty_like(hist, dtype=np.int32)
    cv.normalize(hist, nh, 0, height-1-border*2, cv.NORM_MINMAX, cv.CV_32S)
    for i in range(size):
        img[-border-nh[i]:-border,border+i,0:3] = i
    return img    

_test_ok_image = {True: 'images/test_ok.png', False: 'images/test_fail.png'}

def _test_cases(*conditions):
    show(*[(_test_ok_image[c], t) for t,c in conditions])


def _is(vMin, vMax, vInit = None, step = 1):
    return IntSlider(min=vMin, max=vMax, value=vInit or vMin, step = step, continuous_update=False)


def _test_ndarray(obj, shape, type):
    return isinstance(obj, np.ndarray) and obj.shape == shape and obj.dtype == type


def test_immagini_1(immagine1, immagine2, immagine3, immagine4):
    _test_cases(
        ('immagine1', _test_ndarray(immagine1, (256,200), np.uint8) and np.all(immagine1 == np.arange(256)[:,np.newaxis])),
        ('immagine2', _test_ndarray(immagine2, (200,256), np.uint8) and np.all(immagine2 == np.arange(256))),
        ('immagine3', _test_ndarray(immagine3, (256,200), np.uint8) 
            and np.all(((immagine1%3==0) & (immagine3==0)) | ((immagine1%3!=0) & (immagine1 == immagine3)))
        ),
        ('immagine4', _test_ndarray(immagine4, (30,20), np.uint8) and np.all(immagine4 == np.arange(150,180)[:,np.newaxis]))
    )

def test_immagini_2(gray_toys, toys_s, somma_per_righe):
    _test_cases(
        ('gray_toys', _test_ndarray(gray_toys, (301, 400), np.uint8) and np.sum(gray_toys) in [4122182,4122099]),
        ('toys_s', _test_ndarray(toys_s, (301, 400), np.uint8) and np.sum(toys_s) in [4286398,4286309]),
        ('somma_per_righe', _test_ndarray(somma_per_righe, (301, ), np.uint32) and np.sum(somma_per_righe) in [4286398,4286309,toys_s.sum()]),
    )

def test_calibrazione_3(immagini, punti_immagine, punti_oggetto, po):
    _test_cases(
        ('immagini', type(immagini)==list and not immagini),
        ('punti_immagine', type(punti_immagine)==list and not punti_immagine),
        ('punti_oggetto', type(punti_oggetto)==list and not punti_oggetto),
        ('po', type(po)==np.ndarray and po.shape==(42, 3) and po.dtype==np.float32
                and np.array_equal(po[:,2], np.zeros(42))
                and np.array_equal(po[:,1], np.repeat(np.arange(0, 6), 7))
                and np.array_equal(po[:,0], np.tile(np.arange(0, 7), 6))
        )
    )

def test_filtri_2(func_emboss):
    test_cases = [('thunderbirds',3,7), ('fuji',3,9), ('cervino',5,13)]
    img = [cv.imread('filtri/'+t+'.jpg') for t,*_ in test_cases]
    rok = [np.load(f'filtri/{i}_{sb}_{se}.npy') for i, sb, se in test_cases]
    res = [func_emboss(i, sb, se) for i, (_, sb, se) in zip(img, test_cases)]
    check = [_test_ok_image[np.sum(np.abs(a-b))/a.size<0.01] for a, b in zip(res, rok)]
    show(*[(i,t) for case in zip(img, res, rok, check) 
           for i, t in zip(case, ('Originale', 'Risultato', 'Risultato atteso', 'Verifica'))], max_per_row=4)

def test_basi_1(func_perfetti):
    t = [6, 28, 496, 8128]
    ok = all([func_perfetti(t[i-1] if i>0 else 5)==([] if t==0 else t[:i]) for i in range(len(t)+1)])
    _test_cases(('Verifica', ok))

def test_basi_2(func_stat):
    tests = (
        ("Beautiful is better than ugly.", (5, 2, 9, 5.0)),
        ("Explicit is better than implicit.", (5, 2, 8, 5.6)),
        ("Simple is better than complex.", (5, 2, 7, 5.0)),
        ("Complex is better than complicated.", (5, 2, 11, 6.0)),
        ("Flat is better than nested.", (5, 2, 6, 4.4)),
        ("If the implementation is easy to explain, it may be a good idea.", (13, 1, 14, 3.8461538461538463)),
        ("", (0, None, None, None)),
        (" , .", (0, None, None, None)),
    )
    _test_cases(*[(f'"{t}"', func_stat(t)==r) for t,r in tests])
    
def test_basi_3(risultati, slicing):
    if len(risultati)>len(slicing):
        slicing = slicing + ((None,) * (len(risultati)-len(slicing)))
    _test_cases(*[(str(r), r==s) for r, s in zip(risultati, slicing)])

def test_basi_4(f_py, f_np):
    nomi = ("A", "B", "C", "D", "E", "cA", "rB")
    _test_cases(*[(n, np.array_equal(np.array(x, dtype=float), y.astype(float))) for n, x, y in zip(nomi, f_py(), f_np())])
    
def test_basi_5(f):
    np = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 
          101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 
          197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 
          311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 
          431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 
          557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 
          661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797,
          809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 
          937, 941, 947, 953, 967, 971, 977, 983, 991, 997, 1009, 1013, 1019, 1021, 1031, 1033, 1039, 1049, 
          1051, 1061, 1063, 1069, 1087, 1091, 1093, 1097, 1103, 1109, 1117, 1123, 1129, 1151, 1153, 1163, 
          1171, 1181, 1187, 1193, 1201, 1213, 1217, 1223]
    _test_cases(*[(str(n), f(n).tolist()==list(filter(lambda i: i<=n, np))) for n in range(0, 1201, 100)])
    
def test_basi_6(f):
    tests = [0, 3, 11, 42, 113, 428, 1370, 4741, 16687, 61208]
    _test_cases(*[(f'n={i}', f(i)==x) for i, x in enumerate(tests)])
    
def test_analisi_2(m):
    _test_cases(('Verifica numero di componenti connesse',cv.connectedComponents(m)[0]==29))

def test_analisi_3(m):
    _test_cases(('Verifica numero di componenti connesse',cv.connectedComponents(m)[0]==29),
                ('Verifica assenza di buchi',cv.connectedComponents(cv.bitwise_not(m))[0]==2),
               )

def test_analisi_4(cca,mask2):    
    def check_tuple(t):
        if not isinstance(t, tuple):
            return False
        m, a = t
        return isinstance(m, np.ndarray) and m.shape==mask2.shape and a+0==a
    
    ok = isinstance(cca, list) and len(cca)==28 and all(check_tuple(x) for x in cca)
    _test_cases(('Verifica formato lista cca',ok))

def test_movimento_1(frames):
    _test_cases(('Verifica numero di frame nella lista',len(frames)==1700))
    
def test_movimento_2(OBJ_SIZE, hists):
    _test_cases(('Verifica OBJ_SIZE',OBJ_SIZE==18),
                ('Verifica hists',np.allclose(np.load('movimento/hists.npy'), np.vstack(hists)))
               )

def test_movimento_5(l):
    _test_cases(('Verifica lunghezza lista',len(l)==1700),
                ('Verifica lunghezza liste contenute',all(len(x)==5 for x in l))
               )

def test_tm_1(r):
    _test_cases(('Controllo posizione Waldo', ( np.abs( np.array(r) - np.array((830, 593, 32, 57)) ) < 5).all() ))

def test_tm_2(templates):
    h, w, c = 72, 35, 3
    zf = 1.0, 1.2, 1.4, 1.6
    _test_cases(*[(f'Dimensioni al {s:.0%}', t.shape[0]==round(s*h) and t.shape[1]==round(s*w) and t.shape[2]==c ) for t, s in zip(templates, zf)])

def test_tm_3(r):
    _test_cases(('Controllo posizione Waldo', ( np.abs( np.array(r) - np.array((989, 204, 42, 86)) ) < 7).all() ))

def test_tm_4(r):
    _test_cases(('Controllo posizione Waldo', ( np.abs( np.array(r) - np.array((1152, 292, 50, 58)) ) < 5).all() ))

def test_tm_5(rettangoli):    
    rok = np.load('tm/rc.npy')
    tutti_giusti = all(np.any(np.all(np.abs(np.array(r) - rok) < 7, axis=1)) for r in rettangoli) 
    trovati_tutti = all(np.any(np.all(np.abs(r - np.array(rettangoli)) < 7, axis = 1)) for r in rok)
    _test_cases((f'Controllo monete: {len(rettangoli)}/{len(rok)}', tutti_giusti and trovati_tutti))

def test_tm_6(rettangoli):    
    rok = np.load('tm/rc.npy')
    tutti_giusti = all(np.any(np.all(np.abs(np.array(r) - rok) < 5, axis=1)) for r in rettangoli) 
    trovati_tutti = all(np.any(np.all(np.abs(r - np.array(rettangoli)) < 5, axis = 1)) for r in rok)
    _test_cases((f'Controllo monete: {len(rettangoli)}/{len(rok)}', tutti_giusti and trovati_tutti and len(rok)==len(rettangoli)))

def test_dnn_1(net, class_names):    
    _test_cases(('Nomi delle classi', len(class_names)==80 and open('dnn/cn.chk').read() == ''.join(class_names)),
                ('Numero di livelli della rete', len(net.getLayerNames())==254))

def test_dnn_2(class_colors):
    _test_cases(('Controllo colori', np.all(np.abs(np.load('dnn/colors.npy') - np.array(class_colors)) < 3)))

def test_dnn_3(border_w, border_h, blob):
    _test_cases(('Dimensioni bordi', border_w==0 and border_h==39),
                ('Contenuto blob', np.allclose(np.load('dnn/tb.npy'), blob, 0.05)))
    
