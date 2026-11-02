import os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src = open(os.path.join(R, "automation", "costruisci_box.py"), encoding="utf-8").read().split("def w(rel")[0]
ns = {}; exec(src, ns); CAT = [c for c in ns["CAT"] if not c[0].startswith("singoli")]
def rw(rel, f):
    p = os.path.join(R, rel); t = open(p, encoding="utf-8").read(); t = f(t); open(p, "w", encoding="utf-8", newline="\n").write(t)
def nav(t, home, serv, blog, shop, comp, tit):
    m = re.search(r"main:\n(.*?)(\n#|\Z)", t, re.S)
    nuovo = 'main:\n  - title: "Home"\n    url: %s\n  - title: "%s"\n    url: %s\n  - title: "%s"\n    url: %s\n  - title: "Blog"\n    url: %s\n  - title: "%s"\n    url: %s\n' % (home, tit[0], shop, tit[1], comp, blog, tit[2], tit[3])
    return t[:m.start()] + nuovo.rstrip("\n") + t[m.end(1):]
# IT
rw("_data/navigation.yml", lambda t: nav(t, "/", None, "/blog/", "/negozio/", "/componi-il-tuo-box/", ("Box", "Componi il tuo box", "Contatti", "/contatti/")))
rw("_data/sottomenu.yml", lambda t: t.rstrip("\n") + "\n\nBox:\n" + "".join('  - title: "%s"\n    url: /negozio/categoria/%s/\n' % (c[1], c[0]) for c in CAT) + '  - divider: true\n  - title: "Tutti i box"\n    url: /negozio/\n')
# EN
rw("_data/i18n/en/navigation.yml", lambda t: nav(t, "/en/", None, "/en/blog/", "/en/shop/", "/en/build-your-box/", ("Boxes", "Build your own box", "Contact", "/en/contact/")))
rw("_data/i18n/en/sottomenu.yml", lambda t: t.rstrip("\n") + "\n\nBoxes:\n" + "".join('  - title: "%s"\n    url: /en/shop/category/%s/\n' % (c[2], c[6]) for c in CAT) + '  - divider: true\n  - title: "All boxes"\n    url: /en/shop/\n')
print("nav OK")
