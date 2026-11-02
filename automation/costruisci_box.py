# Dati e costruzione shop "Box Ricorrenti": 12 categorie box + 3 categorie "Componi il tuo box" + prodotti IT/EN.
# Prezzi in centesimi = SEGNAPOSTO da confermare. Nessun marchio e nessuna cifra nutrizionale inventata.
import json, os
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
E = lambda s: s.encode().decode("unicode_escape") if False else s
# (id, nome it, nome en, emoji, desc it, desc en, slug en)
CAT = [
 ("box-casa-pulita","Box Casa Pulita","Clean Home Box","\U0001F9FD","Detersivi e prodotti per la pulizia di casa, in abbonamento.","Cleaning products for the home, on subscription.","clean-home-box"),
 ("box-carta-sacchetti","Box Carta e Sacchetti","Paper & Bags Box","\U0001F9FB","Carta igienica, rotoli cucina, fazzoletti e sacchetti: li ricevi a casa quando servono.","Toilet paper, kitchen rolls, tissues and bin bags delivered when you need them.","paper-bags-box"),
 ("box-igiene","Box Igiene Persona","Personal Care Box","\U0001F9F4","Sapone, shampoo, dentifricio e igiene quotidiana.","Soap, shampoo, toothpaste and daily hygiene.","personal-care-box"),
 ("box-bimbo","Box Bimbo","Baby Box","\U0001F37C","Salviette, creme e detergenti per la cura dei piu' piccoli.","Wipes, creams and cleansers for babies.","baby-box"),
 ("box-animali","Box Animali","Pet Box","\U0001F43E","Cibo, snack e igiene per cane e gatto.","Food, treats and hygiene for dogs and cats.","pet-box"),
 ("box-caffe-colazione","Box Caffe' e Colazione","Coffee & Breakfast Box","\u2615","Caffe', te', biscotti e tutto per la colazione.","Coffee, tea, biscuits and everything for breakfast.","coffee-breakfast-box"),
 ("box-frutta-essiccata","Box Frutta Essiccata","Dried Fruit Box","\U0001F34E","Frutta essiccata e confezionata sottovuoto, senza zuccheri aggiunti dove indicato.","Dried, vacuum-packed fruit, with no added sugar where stated.","dried-fruit-box"),
 ("box-snack-secchi","Box Snack Secchi","Dried Snacks Box","\U0001F968","Snack essiccati e frutta secca per lo spuntino.","Dried snacks and nuts for a quick bite.","dried-snacks-box"),
 ("box-erbe-spezie","Box Erbe e Spezie","Herbs & Spices Box","\U0001F33F","Erbe aromatiche e spezie essiccate, in confezioni sottovuoto che conservano l'aroma.","Dried herbs and spices in vacuum packs that keep the aroma.","herbs-spices-box"),
 ("box-dispensa-sottovuoto","Box Dispensa Sottovuoto","Vacuum-Packed Pantry Box","\U0001F96B","Legumi, riso, farine e pasta in confezioni sottovuoto, per la dispensa di ogni mese.","Pulses, rice, flours and pasta in vacuum packs for the monthly pantry.","vacuum-pantry-box"),
 ("box-tisane-zuppe","Box Tisane e Zuppe","Herbal Tea & Soup Box","\U0001F375","Miscele per tisane e verdure disidratate per zuppe e brodi.","Herbal tea blends and dehydrated vegetables for soups and broths.","herbal-tea-soup-box"),
 ("box-ufficio","Box Ufficio","Office Box","\U0001F4CE","Carta, cancelleria, caffe' e pulizia per studi e piccole aziende.","Paper, stationery, coffee and cleaning for studios and small businesses.","office-box"),
 ("singoli-casa","Componi: Casa e Pulizia","Build: Home & Cleaning","\U0001F9FA","Scegli i singoli prodotti per la casa e crea il tuo box.","Pick single home products and build your own box.","build-home-cleaning"),
 ("singoli-persona","Componi: Persona, Bimbo e Animali","Build: Personal, Baby & Pets","\U0001F9F4","Scegli i singoli prodotti per la persona e crea il tuo box.","Pick single personal care products and build your own box.","build-personal-baby-pets"),
 ("singoli-dispensa","Componi: Dispensa e Cucina","Build: Pantry & Kitchen","\U0001F96B","Scegli i singoli prodotti da dispensa e crea il tuo box.","Pick single pantry products and build your own box.","build-pantry-kitchen"),
]
# (id, cat, nome it, nome en, prezzo, contenuto it, contenuto en, slug en)
P = [
 ("casa-pulita-base","box-casa-pulita","Box Casa Pulita Base","Clean Home Box Basic",1900,"detersivo piatti, detersivo lavatrice, sgrassatore e spugne","dish soap, laundry detergent, degreaser and sponges","clean-home-box-basic"),
 ("casa-pulita-plus","box-casa-pulita","Box Casa Pulita Plus","Clean Home Box Plus",3400,"tutto il Base piu' pastiglie lavastoviglie, anticalcare e panni in microfibra","everything in Basic plus dishwasher tablets, descaler and microfibre cloths","clean-home-box-plus"),
 ("carta-sacchetti","box-carta-sacchetti","Box Carta e Sacchetti","Paper & Bags Box",2400,"carta igienica, rotoli cucina, fazzoletti e sacchetti spazzatura","toilet paper, kitchen rolls, tissues and bin bags","paper-bags-box"),
 ("igiene-base","box-igiene","Box Igiene Persona Base","Personal Care Box Basic",1800,"sapone mani, bagnoschiuma, shampoo e dentifricio","hand soap, shower gel, shampoo and toothpaste","personal-care-box-basic"),
 ("igiene-plus","box-igiene","Box Igiene Persona Plus","Personal Care Box Plus",3200,"tutto il Base piu' deodorante, balsamo e spazzolini","everything in Basic plus deodorant, conditioner and toothbrushes","personal-care-box-plus"),
 ("bimbo","box-bimbo","Box Bimbo","Baby Box",3900,"salviette, crema cambio, detergente bagnetto e cotone","wipes, nappy cream, bath wash and cotton pads","baby-box"),
 ("animali-cane","box-animali","Box Cane","Dog Box",3500,"cibo secco, snack, salviette e sacchetti igienici","dry food, treats, wipes and waste bags","dog-box"),
 ("animali-gatto","box-animali","Box Gatto","Cat Box",3200,"cibo secco o umido, snack e lettiera","dry or wet food, treats and cat litter","cat-box"),
 ("caffe-colazione","box-caffe-colazione","Box Caffe' e Colazione","Coffee & Breakfast Box",2600,"caffe' in grani o cialde, te', biscotti e zucchero","coffee beans or pods, tea, biscuits and sugar","coffee-breakfast-box"),
 ("frutta-essiccata","box-frutta-essiccata","Box Frutta Essiccata","Dried Fruit Box",2200,"mele, banana, mango e fragole essiccate, in buste sottovuoto","dried apple, banana, mango and strawberry in vacuum bags","dried-fruit-box"),
 ("snack-secchi","box-snack-secchi","Box Snack Secchi","Dried Snacks Box",2800,"frutta secca, pomodori secchi e chips di verdure essiccate","nuts, dried tomatoes and dehydrated vegetable chips","dried-snacks-box"),
 ("erbe-spezie","box-erbe-spezie","Box Erbe e Spezie","Herbs & Spices Box",1800,"erbe aromatiche, peperoncino e spezie essiccate, in buste sottovuoto","dried herbs, chilli and spices in vacuum bags","herbs-spices-box"),
 ("dispensa-sottovuoto","box-dispensa-sottovuoto","Box Dispensa Sottovuoto","Vacuum-Packed Pantry Box",3600,"legumi, riso, farina e pasta in confezioni sottovuoto","pulses, rice, flour and pasta in vacuum packs","vacuum-pantry-box"),
 ("tisane-zuppe","box-tisane-zuppe","Box Tisane e Zuppe","Herbal Tea & Soup Box",2100,"miscele per tisane e verdure disidratate per zuppe","herbal tea blends and dehydrated vegetables for soups","herbal-tea-soup-box"),
 ("ufficio","box-ufficio","Box Ufficio","Office Box",3900,"carta A4, penne, caffe' e prodotti per la pulizia","A4 paper, pens, coffee and cleaning products","office-box"),
 # singoli per "Componi il tuo box"
 ("detersivo-piatti","singoli-casa","Detersivo piatti 1 L","Dish soap 1 L",290,"Detersivo per piatti, flacone da 1 litro.","Dish soap, 1 litre bottle.","dish-soap"),
 ("detersivo-lavatrice","singoli-casa","Detersivo lavatrice","Laundry detergent",690,"Detersivo liquido per lavatrice.","Liquid laundry detergent.","laundry-detergent"),
 ("carta-igienica","singoli-casa","Carta igienica 8 rotoli","Toilet paper 8 rolls",490,"Confezione da 8 rotoli.","Pack of 8 rolls.","toilet-paper"),
 ("sapone-mani","singoli-persona","Sapone mani","Hand soap",250,"Sapone liquido per le mani.","Liquid hand soap.","hand-soap"),
 ("shampoo","singoli-persona","Shampoo","Shampoo",390,"Shampoo per uso quotidiano.","Shampoo for daily use.","shampoo"),
 ("crocchette-gatto","singoli-persona","Crocchette per gatto 1,5 kg","Cat kibble 1.5 kg",1190,"Crocchette per gatto adulto.","Kibble for adult cats.","cat-kibble"),
 ("mele-essiccate","singoli-dispensa","Mele essiccate 100 g","Dried apples 100 g",450,"Mele essiccate in busta sottovuoto.","Dried apples in a vacuum bag.","dried-apples"),
 ("pomodori-secchi","singoli-dispensa","Pomodori secchi 100 g","Dried tomatoes 100 g",390,"Pomodori essiccati in busta sottovuoto.","Dried tomatoes in a vacuum bag.","dried-tomatoes"),
 ("legumi-sottovuoto","singoli-dispensa","Legumi sottovuoto 500 g","Vacuum-packed pulses 500 g",350,"Legumi secchi in confezione sottovuoto.","Dried pulses in a vacuum pack.","vacuum-pulses"),
 ("caffe-in-grani","singoli-dispensa","Caffe' in grani 500 g","Coffee beans 500 g",790,"Caffe' in grani, miscela da 500 g.","Coffee beans, 500 g blend.","coffee-beans"),
]
def w(rel, txt):
    p = os.path.join(R, rel); os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, "w", encoding="utf-8", newline="\n").write(txt)
for rel in ["_negozio/categoria-esempio.md","_negozio/prodotto-esempio.md","en/negozio/categoria/esempio.md","en/negozio/prodotto-esempio.md"]:
    p = os.path.join(R, rel)
    if os.path.exists(p): os.remove(p)
cp = os.path.join(R, "_data", "catalogo.json")
d = json.load(open(cp, encoding="utf-8"))
d["categorie"] = [{"nome": a, "id": i, "icona": ic, "descrizione": di,
    "immagine": "assets/images/categorie/%s.webp" % i if os.path.exists(os.path.join(R, "assets/images/categorie/%s.webp" % i)) else "",
    "tr": {"en": {"nome": b, "descrizione": de}}} for (i, a, b, ic, di, de, _s) in CAT]
ic_cat = {c[0]: c[3] for c in CAT}
prod = []
for (pid, cat, a, b, pr, ci, ce, _s) in P:
    sing = cat.startswith("singoli")
    di = ci if sing else "Contiene: %s." % ci
    de = ce if sing else "Contains: %s." % ce
    prod.append({"tipo": "fisico", "id": pid, "nome": a, "categoria": cat, "prezzo_centesimi": pr,
      "descrizione": di,
      "descrizione_completa": di + ("\nPuoi aggiungerlo al tuo box personalizzato." if sing else "\nIn abbonamento: scegli la frequenza dopo l'ordine.\nContenuto e marchi indicativi, da confermare."),
      "immagine": "assets/images/prodotti/%s.webp" % pid if os.path.exists(os.path.join(R, "assets/images/prodotti/%s.webp" % pid)) else "",
      "icona": ic_cat[cat], "visibile": True,
      "tr": {"en": {"nome": b, "descrizione": de,
        "descrizione_completa": de + ("\nYou can add it to your custom box." if sing else "\nSubscription: pick the frequency after ordering.\nContents and brands are indicative and to be confirmed.")}}})
d["prodotti"] = prod
json.dump(d, open(cp, "w", encoding="utf-8", newline="\n"), ensure_ascii=False, indent=2)
json.load(open(cp, encoding="utf-8"))
for (i, a, b, ic, di, de, s) in CAT:
    w("_negozio/categoria-%s.md" % i, '---\nlayout: negozio-categoria\ntitle: "%s"\ncid: %s\npermalink: /negozio/categoria/%s/\ndescription: "%s"\nref: shop-cat-%s\n---\n' % (a, i, i, di.replace('"', "'"), i))
    w("en/negozio/categoria/%s.md" % s, '---\nlayout: negozio-categoria\ntitle: "%s"\ncid: %s\npermalink: /en/shop/category/%s/\ndescription: "%s"\nlang: en\nlocale: en\nref: shop-cat-%s\n---\n' % (b, i, s, de.replace('"', "'"), i))
for (pid, cat, a, b, pr, ci, ce, s) in P:
    w("_negozio/%s.md" % pid, '---\nlayout: negozio-prodotto\ntitle: "%s"\npid: %s\npermalink: /negozio/%s/\ndescription: "%s"\nref: shop-prod-%s\n---\n' % (a, pid, pid, a, pid))
    w("en/negozio/%s.md" % pid, '---\nlayout: negozio-prodotto\ntitle: "%s"\npid: %s\npermalink: /en/shop/%s/\ndescription: "%s"\nlang: en\nlocale: en\nref: shop-prod-%s\n---\n' % (b, pid, s, b, pid))
# pagina "Componi il tuo box"
w("_pages/componi-box.md", '''---
layout: single
title: "Componi il tuo box"
permalink: /componi-il-tuo-box/
description: "Crea il tuo box personalizzato scegliendo i prodotti che usi di piu'."
author_profile: false
ref: componi-box
---

Scegli i prodotti che consumi di piu', aggiungili al carrello e ricevi un box fatto su misura per te.

## Come funziona

1. Entra in una delle tre sezioni qui sotto.
2. Scegli i prodotti e le quantita' con i pulsanti + e -.
3. Vai al carrello e invia l'ordine: dopo l'ordine concordiamo con te la frequenza (mensile, ogni 2 mesi o trimestrale).

## Scegli da dove partire

- [Casa e pulizia]({% include shop-url.html k="cat" id="singoli-casa" %})
- [Persona, bimbo e animali]({% include shop-url.html k="cat" id="singoli-persona" %})
- [Dispensa e cucina]({% include shop-url.html k="cat" id="singoli-dispensa" %})
''')
w("en/componi-box.md", '''---
layout: single
title: "Build your own box"
permalink: /en/build-your-box/
description: "Create your own custom box by choosing the products you use most."
author_profile: false
lang: en
locale: en
ref: componi-box
---

Pick the products you use most, add them to the cart and get a box made just for you.

## How it works

1. Open one of the three sections below.
2. Choose products and quantities with the + and - buttons.
3. Go to the cart and send your order: after ordering we agree the frequency with you (monthly, every 2 months or quarterly).

## Where to start

- [Home and cleaning]({% include shop-url.html k="cat" id="singoli-casa" %})
- [Personal care, baby and pets]({% include shop-url.html k="cat" id="singoli-persona" %})
- [Pantry and kitchen]({% include shop-url.html k="cat" id="singoli-dispensa" %})
''')
print("OK", len(CAT), len(P))
