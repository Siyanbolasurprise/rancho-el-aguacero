#!/usr/bin/env python3
"""Generate Rancho El Aguacero bilingual static site. Edit copy here; prices live in content/site.json."""
import os, json
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) if "__file__" in globals() else os.getcwd()
BASE = r"C:\Users\User\Desktop\OPEN CODE PROJECTS\RANCHO AGUACERO"
DOMAIN = "https://ranchoelaguacero.com"
WA = "5213300000000"
EMAIL = "hola@ranchoelaguacero.com"

MAP = json.load(open(os.path.join(BASE, "imgmap.json")))
IMG = {
 "aerial": "../img/dji_20240710151010_0033_d-large.webp",
 "aerial2": "../img/dji_20240710150607_0025_d-large.webp",
 "aerial3": "../img/dji_20240710150153_0014_d-large.webp",
 "room": "../img/_ale3073.webp",
 "bath": "../img/_ale3061.webp",
 "room2": "../img/_ale3071-medium.webp",
 "grounds": "../img/img_1693.webp",
 "peacock": "../img/img_2520.webp",
 "sheep": "../img/img_1270.webp",
 "pool": "../img/28b4d473-1e68-4f58-a2b5-997730975d6b.webp",
 "poolsunset": "../img/_ale3220.webp",
 "night": "../img/c3470aac-345e-49b6-a309-83102e89a9e2.webp",
 "event": "../img/95251fd0-ade1-4286-a205-7d9784d2d96b.webp",
 "aqueduct": "../img/img_6136.webp",
 "horses": "../img/img_1248.webp",
 "temazcal": "../img/a65dbd9d-cede-49fd-a439-86597408290e.webp",
 "gate": "../img/img_8224.webp",
 "detail": "../img/img_1693.webp",
 "hero": "../img/8b42eb1f-f22e-4067-aff5-c77484f9aae4.webp",
 "video": "../IMG_3279.mp4",
}
# (original file, category, alt EN, alt ES) — all 60 ranch photographs
GALLERY = [
 ("07189d72-e3a5-47db-a031-25b65ef563da.webp","ranch","Stone entrance path lined with gardens","Camino de piedra entre jardines"),
 ("1ae01aef-df91-4f2d-b704-2cc24bdd7d3a.webp","ranch","Lone tree in a green field","Árbol solitario en campo verde"),
 ("5CE0FA12-E0FC-4FBC-998C-4BB3B46485A0.jpeg","ranch","Valley and mountains near the ranch","Valle y montañas cerca del rancho"),
 ("96b96cd2-5083-4b1b-9de8-ae4e6df440fc.webp","ranch","Patio glowing at night","Patio iluminado de noche"),
 ("C2CBD4F8-7923-48AE-B3BE-B302B783F88B.jpeg","ranch","Aerial view of the ranch and fields","Vista aérea del rancho y campos"),
 ("DJI_20240710150153_0014_D+Large.webp","ranch","Ranch buildings among green fields from above","Construcciones entre campos verdes desde arriba"),
 ("DJI_20240710150348_0019_D+Large.webp","ranch","Countryside roads and ranch land from the air","Caminos y tierras desde el aire"),
 ("DJI_20240710150607_0025_D+Large.webp","ranch","Evening light over ranch fields","Luz de atardecer sobre los campos"),
 ("DJI_20240710151010_0033_D+Large.webp","ranch","Agave fields and farmland seen from above","Agaves y campos vistos desde arriba"),
 ("DJI_20240710172910_0064_D+Large.webp","ranch","Aerial view of pools and gardens","Vista aérea de albercas y jardines"),
 ("DJI_20240710173015_0070_D+Large.webp","ranch","Pools and green areas from above","Albercas y áreas verdes desde arriba"),
 ("IMG_1693.webp","ranch","Green lawns and tall trees","Jardines verdes y árboles altos"),
 ("IMG_2151.webp","ranch","Stone path at night","Camino de piedra de noche"),
 ("IMG_1585.webp","ranch","Shaded patio corner at night","Rincón del patio de noche"),
 ("IMG_8224.webp","ranch","Ranch entrance gate","Puerta de entrada del rancho"),
 ("IMG_6136.webp","ranch","Historic aqueduct beside the pool","Acueducto histórico junto a la alberca"),
 ("_ALE3085.webp","ranch","Lawns and ranch buildings","Jardines y construcciones"),
 ("_ALE3227+Large.webp","ranch","Brick corridor with rocking chair","Pasillo de ladrillo con mecedora"),
 ("93184e6b-312f-4afc-998d-7c165bc9edf8.webp","stay","Covered dining corridor","Pasillo comedor techado"),
 ("CBF5DFB6-FD45-42C7-80E6-5B605E50C9AA.jpeg","stay","Living room with fireplace","Sala con chimenea"),
 ("IMG_0755.webp","stay","Twin bedroom with Mexican finishes","Recámara doble con acabados mexicanos"),
 ("IMG_0900.webp","stay","Sitting area with art and hats","Estancia con arte y sombreros"),
 ("IMG_1895.webp","stay","Living room with sofas","Sala con sofás"),
 ("IMG_2387.webp","stay","Bathroom with stone finishes","Baño con acabados de piedra"),
 ("IMG_2491.webp","stay","Skylight with wagon-wheel chandelier","Tragaluz con candil de rueda"),
 ("Picture+10.webp","stay","Dining room with long table","Comedor con mesa larga"),
 ("Picture+5.webp","stay","Ranch kitchen","Cocina del rancho"),
 ("Picture+6.webp","stay","Kitchen and dining area","Cocina y comedor"),
 ("_ALE3061.webp","stay","Bathroom with Mexican tile","Baño de azulejo mexicano"),
 ("_ALE3064.webp","stay","Bedroom in blue tones","Recámara en tonos azules"),
 ("_ALE3071+Medium.webp","stay","Bedroom with terracotta floors","Recámara con pisos de terracota"),
 ("_ALE3073.webp","stay","Bedroom with red textiles","Recámara con textiles rojos"),
 ("_ALE3101-Mejorado-NR.webp","stay","Dining and living room with fireplace","Comedor y sala con chimenea"),
 ("_ALE3124-Mejorado-NR.webp","stay","Living room with bookshelves","Sala con libreros"),
 ("39E4FD8C-8C11-41B6-87FA-AF5668560405.jpeg","nature","Sheep grazing in green pasture","Ovejas pastando en potrero verde"),
 ("IMG_0795.webp","nature","Turkeys on the grass","Guajolotes en el pasto"),
 ("IMG_1270.webp","nature","Peacock overlooking sheep pasture","Pavo real con ovejas al fondo"),
 ("IMG_2520.webp","nature","Peacock on the lawn","Pavo real en el jardín"),
 ("IMG_2731.webp","nature","Turkeys along the stone path","Guajolotes en el camino"),
 ("_ALE3191+Large.webp","nature","Horses in green field","Caballos en campo verde"),
 ("_ALE3229.webp","nature","Free-range chickens","Gallinas de rancho"),
 ("28b4d473-1e68-4f58-a2b5-997730975d6b.webp","pool","Swimming pool on a sunny day","Alberca en día soleado"),
 ("529FE148-B719-4EFF-BBDA-4E3513F858B2.jpeg","pool","Pool glowing at dusk","Alberca al atardecer"),
 ("8B42EB1F-F22E-4067-AFF5-C77484F9AAE4.jpeg","pool","Grounds and pool at sunset","Jardines y alberca al atardecer"),
 ("IMG_2394.webp","pool","Loungers on the lawn","Camastros en el jardín"),
 ("_ALE3220.webp","pool","Pool at sunset","Alberca al atardecer"),
 ("ee7644a9-b365-47db-95ec-949cb8957856.webp","pool","Pool on a clear day","Alberca en día despejado"),
 ("95251FD0-ADE1-4286-A205-7D9784D2D96B.jpeg","events","Lawn set for an evening gathering","Jardín para reunión nocturna"),
 ("IMG_4919.webp","events","Patio ready for a night celebration","Patio listo para celebrar de noche"),
 ("c3470aac-345e-49b6-a309-83102e89a9e2.webp","events","Lawn under evening lights","Jardín bajo luces nocturnas"),
 ("5F24236C-C2C6-4CA6-B90C-E2254F147263.jpeg","events","Patio at night","Patio de noche"),
 ("8A071755-B1D0-42D6-82E9-0ADEFF61BD90.jpeg","experiences","Outdoor clay oven and fire","Horno de barro y fuego exterior"),
 ("IMG_1248.webp","experiences","Horses and donkey at the fence","Caballos y burro junto a la cerca"),
 ("IMG_2313.webp","experiences","Massage and rest room","Sala de masaje y descanso"),
 ("A65DBD9D-CEDE-49FD-A439-86597408290E.jpeg","experiences","Traditional ceremony setting","Espacio ceremonial tradicional"),
 ("C8E1AC63-3FAB-4ED9-A794-FBF458D80140.jpeg","experiences","Fire pit on the lawn","Fogatero en el jardín"),
 ("Picture+11.webp","experiences","Rest and massage room","Sala de descanso y masaje"),
 ("_ALE3084.webp","experiences","Fire pit with the house behind","Fogata con la casa al fondo"),
 ("_ALE3147+FIRE+Large.webp","experiences","Fire pit on green grass","Fogatero en pasto verde"),
 ("_ALE3190.webp","experiences","Horses up close","Caballos de cerca"),
]
def gfig(o, c, ae, as_, lang):
    fn = MAP[o]
    return f'<figure data-cat="{c}"><img data-zoom loading="lazy" decoding="async" src="../thumbs/{fn}" data-full="../img/{fn}" alt="{as_ if lang=="es" else ae}"></figure>'
GALLERY_HTML = {"en": "".join(gfig(*g, "en") for g in GALLERY), "es": "".join(gfig(*g, "es") for g in GALLERY)}
def hero_video(alt):
    return f"""<section class="hero"><video class="hero-bg" autoplay muted loop playsinline preload="metadata" poster="{IMG['aerial']}"><source src="{IMG['video']}" type="video/mp4"></video>"""

NAV = {
 "en": [("The Ranch","ranch.html"),("Stay","stay.html"),("Experiences","experiences.html"),("Events","events.html"),("Gallery","gallery.html"),("Journal","journal.html"),("Plan Your Visit","plan.html")],
 "es": [("El Rancho","ranch.html"),("Hospedaje","stay.html"),("Experiencias","experiences.html"),("Eventos","events.html"),("Galería","gallery.html"),("Diario","journal.html"),("Planea Tu Visita","plan.html")],
}
NAMES = {"en":{"reserve":"Reserve","home":"Home","contact":"Contact"},"es":{"reserve":"Reservar","home":"Inicio","contact":"Contacto"}}

def wa_link(lang, msg_en, msg_es):
    from urllib.parse import quote
    msg = msg_es if lang=="es" else msg_en
    return f"https://wa.me/{WA}?text={quote(msg)}"

WA_MSGS = {
 "stay": ("Hi, I'd like to check availability for a stay at Rancho El Aguacero.","Hola, quisiera consultar disponibilidad para hospedarme en Rancho El Aguacero."),
 "day": ("Hi, I'd like information about day passes.","Hola, quisiera información sobre los pases de día."),
 "camp": ("Hi, I'd like information about camping availability.","Hola, quisiera información sobre disponibilidad para acampar."),
 "event": ("Hi, I'm interested in hosting an event at Rancho El Aguacero.","Hola, estoy interesado/a en realizar un evento en Rancho El Aguacero."),
 "gen": ("Hi, I'd like information about Rancho El Aguacero.","Hola, quisiera información sobre Rancho El Aguacero."),
 "temazcal": ("Hi, I'd like to ask about the Temazcal experience.","Hola, quisiera preguntar por la experiencia de Temazcal."),
}

def head(lang, slug, title, desc, img):
    other = "es" if lang=="en" else "en"
    canon = f"{DOMAIN}/{lang}/{slug}"
    return f"""<!DOCTYPE html><html lang="{lang}"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}"><link rel="canonical" href="{canon}">
<link rel="alternate" hreflang="en" href="{DOMAIN}/en/{slug}"><link rel="alternate" hreflang="es" href="{DOMAIN}/es/{slug}"><link rel="alternate" hreflang="x-default" href="{DOMAIN}/en/{slug}">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:type" content="website"><meta property="og:url" content="{canon}"><meta property="og:image" content="{DOMAIN}/{img.replace('../','')}">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,500;9..144,600&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../css/site.css">
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"LodgingBusiness","name":"Rancho El Aguacero","url":"{canon}","email":"{EMAIL}","address":{{"@type":"PostalAddress","addressLocality":"Etzatlán","addressRegion":"Jalisco","addressCountry":"MX"}},"priceRange":"$$"}}</script>
</head><body>"""

def header(lang, active=""):
    links = "".join(f'<a href="{h}">{t}</a>' for t,h in NAV[lang])
    other = "es" if lang=="en" else "en"
    otherlabel = "ES" if lang=="en" else "EN"
    curl = "../es/index.html" if lang=="en" else "../en/index.html"
    # keep same page across languages when possible via JS-free static: link to index of other lang is safe default; per-page we override below
    return f"""<header class="site"><nav class="nav" aria-label="Main">
<a class="brand" href="index.html">Rancho El Aguacero<small>Jalisco · México</small></a>
<div class="links" id="navLinks">{links}<a href="reserve.html" data-track="nav_reserve"><b>{NAMES[lang]['reserve']}</b></a></div>
<div class="nav-cta"><div class="lang" aria-label="Language"><span><i>{lang.upper()}</i></span><a href="{curl}" hreflang="{other}">{otherlabel}</a></div>
<a class="btn light" style="padding:11px 20px" href="reserve.html" data-track="nav_reserve">{NAMES[lang]['reserve']}</a>
<button class="burger" aria-label="Menu" aria-expanded="false">☰</button></div></nav></header>"""

def footer(lang):
    nav = "".join(f'<div><a href="{h}">{t}</a></div>' for t,h in NAV[lang])
    if lang=="en":
        return f"""<footer><div class="f-grid"><div><a class="brand" href="index.html" style="color:#fff">Rancho El Aguacero<small>Jalisco · México</small></a>
<p style="margin-top:14px;max-width:34ch;color:#cfc6b1">A historic countryside ranch in Jalisco. Nature, history, celebration, and time together.</p></div>
<div><h4>Explore</h4>{nav}<div><a href="reserve.html">Reserve</a></div></div>
<div><h4>Contact</h4><div><a href="https://wa.me/{WA}" data-track="wa_footer">WhatsApp</a></div><div><a href="mailto:{EMAIL}">{EMAIL}</a></div><div><a href="contact.html">Contact</a></div><div style="margin-top:10px"><a href="../en/index.html">English</a> · <a href="../es/index.html">Español</a></div></div>
<div><h4>Stay connected</h4><p style="color:#cfc6b1;font-size:15px">Occasional updates about dates, seasons and availability.</p>
<form data-lead="newsletter" data-done="Thank you. You are on the list."><div class="field"><label for="nl">Email</label><input id="nl" type="email" required placeholder="you@email.com"><div class="err">Enter a valid email.</div></div><button class="btn clay" type="submit">Keep in touch</button></form></div></div>
<div class="f-bottom"><span>© 2026 Rancho El Aguacero</span><span><a href="contact.html">Privacy</a> · <a href="contact.html">Terms</a> · <a href="contact.html">Cancellation</a></span></div></footer>"""
    return f"""<footer><div class="f-grid"><div><a class="brand" href="index.html" style="color:#fff">Rancho El Aguacero<small>Jalisco · México</small></a>
<p style="margin-top:14px;max-width:34ch;color:#cfc6b1">Un rancho histórico en Jalisco. Naturaleza, historia, celebración y tiempo juntos.</p></div>
<div><h4>Explorar</h4>{nav}<div><a href="reserve.html">Reservar</a></div></div>
<div><h4>Contacto</h4><div><a href="https://wa.me/{WA}" data-track="wa_footer">WhatsApp</a></div><div><a href="mailto:{EMAIL}">{EMAIL}</a></div><div><a href="contact.html">Contacto</a></div><div style="margin-top:10px"><a href="../en/index.html">English</a> · <a href="../es/index.html">Español</a></div></div>
<div><h4>Sigue en contacto</h4><p style="color:#cfc6b1;font-size:15px">Novedades ocasionales sobre fechas, temporadas y disponibilidad.</p>
<form data-lead="newsletter" data-done="Gracias. Ya estás en la lista."><div class="field"><label for="nl">Correo</label><input id="nl" type="email" required placeholder="tu@correo.com"><div class="err">Escribe un correo válido.</div></div><button class="btn clay" type="submit">Mantenme al tanto</button></form></div></div>
<div class="f-bottom"><span>© 2026 Rancho El Aguacero</span><span><a href="contact.html">Privacidad</a> · <a href="contact.html">Términos</a> · <a href="contact.html">Cancelación</a></span></div></footer>"""

def tail(lang, wa_key="gen"):
    en, es = WA_MSGS[wa_key]
    wa = wa_link(lang, en, es)
    label = "WhatsApp" if True else ""
    return f"""<a class="wa-float" href="{wa}" data-track="wa_float" aria-label="Chat on WhatsApp">✆ WhatsApp</a>
<div class="mobilebar"><a href="{wa}" data-track="wa_mobile">WhatsApp</a><a href="reserve.html" data-track="reserve_mobile">{"Reservar" if lang=="es" else "Reserve"}</a></div>
<div class="lightbox" id="lightbox" role="dialog" aria-label="Image viewer"><button aria-label="Close">✕</button><img alt=""></div>
<script src="../js/site.js" defer></script></body></html>"""

def actionbar(lang):
    if lang=="en":
        items=[("stay.html","Stay","Find accommodation"),("plan.html#daypass","Day Pass","Plan your visit"),("experiences.html#camping","Camping","Sleep outdoors"),("events.html","Events","Plan your celebration")]
    else:
        items=[("stay.html","Hospedaje","Encuentra alojamiento"),("plan.html#daypass","Pase de día","Planea tu visita"),("experiences.html#camping","Campamento","Duerme al aire libre"),("events.html","Eventos","Planea tu celebración")]
    return '<div class="actionbar"><div class="row">'+"".join(f'<a href="{h}"><span>{s}</span><b>{b}</b></a>' for h,b,s in items)+"</div></div>"

def final_cta(lang):
    if lang=="en":
        return f"""<section class="banner"><img class="bg" src="{IMG['aerial2']}" alt="Evening light over Rancho El Aguacero fields"><div class="shade"></div><div class="wrap rv">
<p class="eyebrow" style="color:var(--sand)">Begin</p><h2 class="display">YOUR ESCAPE IS<br>CLOSER THAN YOU THINK.</h2>
<p class="lede" style="color:#eee6d2;margin:20px 0 30px">Come for a day. Stay for a weekend. Celebrate something important. Or simply take a breath.</p>
<div class="hero-ctas"><a class="btn light" href="reserve.html" data-track="final_reserve">Reserve Your Stay</a><a class="btn ghost" style="color:#fff" href="{wa_link(lang,*WA_MSGS['gen'])}" data-track="final_wa">Ask on WhatsApp</a></div></div></section>"""
    return f"""<section class="banner"><img class="bg" src="{IMG['aerial2']}" alt="Luz de atardecer sobre los campos de Rancho El Aguacero"><div class="shade"></div><div class="wrap rv">
<p class="eyebrow" style="color:var(--sand)">Comienza</p><h2 class="display">TU ESCAPADA ESTÁ<br>MÁS CERCA DE LO QUE IMAGINAS.</h2>
<p class="lede" style="color:#eee6d2;margin:20px 0 30px">Ven por un día. Quédate un fin de semana. Celebra algo importante. O simplemente tómate un respiro.</p>
<div class="hero-ctas"><a class="btn light" href="reserve.html" data-track="final_reserve">Reserva Tu Estancia</a><a class="btn ghost" style="color:#fff" href="{wa_link(lang,*WA_MSGS['gen'])}" data-track="final_wa">Pregúntanos por WhatsApp</a></div></div></section>"""

PAGES = {}
# ---------------- HOME ----------------
PAGES[("en","index.html")] = ("Rancho El Aguacero — A Timeless Countryside Escape in Jalisco, Mexico",
"A peaceful countryside escape in Jalisco: ranch stays, cabins, day passes, camping, Temazcal, horseback riding and private events. Book direct.",
f"""<section class="hero"><img class="hero-bg" src="{IMG['hero']}" alt="Sunset over the ranch grounds and pool at Rancho El Aguacero" fetchpriority="high">
<div class="hero-inner"><p class="eyebrow" style="color:var(--sand)">Jalisco · México — Leave the world behind</p>
<h1 class="display">A TIMELESS PLACE<br>TO SLOW DOWN.</h1>
<p class="sub">A peaceful countryside escape in Jalisco where nature, history, celebration, and time together come naturally.</p>
<div class="hero-ctas"><a class="btn light" href="reserve.html" data-track="hero_reserve">Plan Your Escape</a><a class="btn ghost" style="color:#fff" href="ranch.html" data-track="hero_explore">Explore the Ranch</a></div>
<div class="scroll-hint">Discover ↓</div></div></section>"""
+ actionbar("en") +
f"""<section><div class="wrap split rv"><div class="txt"><p class="eyebrow">The ranch</p>
<h2 class="h2">COME FOR THE ESCAPE.<br>STAY FOR THE FEELING.</h2>
<p class="lede">Rancho El Aguacero is more than a place to sleep. It is a place to disconnect, spend time together, explore open land, celebrate, rest — and make memories that feel unhurried.</p>
<p style="margin:18px 0 26px;color:#4a463d">A historic property with roots in the early 1800s, kept alive by the Bañuelos family across generations. No noise. No rush. Just space, shade, water, and sky.</p>
<div class="hero-ctas"><a class="btn" href="ranch.html">The story of the ranch</a><a class="btn ghost" href="stay.html">Stay a little longer</a></div></div>
<div class="frame"><img src="{IMG['grounds']}" alt="Green lawns and tall trees at Rancho El Aguacero" loading="lazy"><p class="cap">The grounds — mornings under the trees.</p></div></div></section>
<section class="dark"><div class="wrap rv"><p class="eyebrow" style="color:var(--sand)">The journey</p>
<h2 class="h2">FROM THE CITY<br>TO SOMEWHERE QUIETER.</h2>
<p class="lede">City → road → countryside → agave fields → the ranch → stillness. An easy drive from Guadalajara, Tequila and Etzatlán.</p>
<div style="margin-top:26px" class="hero-ctas"><a class="btn light" href="plan.html">Get Directions</a></div></div>
<div class="hscroll" style="margin-top:34px">
<figure><img src="{IMG['aerial']}" alt="Agave fields and farmland seen from above" loading="lazy"><figcaption><b>01 — Agave country</b><span>The road into Jalisco's blue-agave landscape.</span></figcaption></figure>
<figure><img src="{IMG['aerial3']}" alt="Country roads and ranch buildings from the air" loading="lazy"><figcaption><b>02 — Open road</b><span>Leave the city; follow the green.</span></figcaption></figure>
<figure><img src="{IMG['sheep']}" alt="Peacock and sheep grazing at the ranch" loading="lazy"><figcaption><b>03 — The ranch</b><span>Animals, trees, water, quiet.</span></figcaption></figure>
</div></section>
<section class="banner"><img class="bg" src="{IMG['aqueduct']}" alt="Historic aqueduct beside the pool at Rancho El Aguacero" loading="lazy"><div class="shade"></div>
<div class="wrap rv"><p class="eyebrow" style="color:var(--sand)">The aqueduct</p><h2 class="display">FIND YOUR PLACE<br>TO DO NOTHING.</h2>
<p class="lede" style="color:#eee6d2;margin:18px 0 26px;max-width:52ch">Shade, hammocks, water, old stone. The aqueduct is the ranch's signature — the place guests remember.</p>
<a class="btn light" href="experiences.html">Explore experiences</a></div></section>
<section><div class="wrap"><p class="eyebrow rv">Stay · Visit · Celebrate</p><h2 class="h2 rv">CHOOSE YOUR KIND OF TIME HERE.</h2>
<div class="grid3">
<div class="card rv"><img src="{IMG['room']}" alt="Bedroom with Mexican tile and wood furniture in the ranch house" loading="lazy"><div class="body"><p class="meta">Overnight · 10–12 guests</p><h3>The Ranch House</h3><p>Bedrooms, kitchen, patios, pool and hiking access. A house made for gathering.</p><p class="price">Price on request <span class="meta">· confirm</span></p><a class="link" href="stay.html">View accommodation →</a></div></div>
<div class="card rv"><img src="{IMG['pool']}" alt="Swimming pool and green areas for day visitors" loading="lazy"><div class="body"><p class="meta">Day visit</p><h3>Day Pass</h3><p>Pools, green areas, time to breathe. Hours and pricing confirmed before your visit.</p><p class="price">To confirm <span class="meta">· editable</span></p><a class="link" href="plan.html#daypass">Plan your day →</a></div></div>
<div class="card rv"><img src="{IMG['night']}" alt="Evening fire and night sky at the ranch" loading="lazy"><div class="body"><p class="meta">Outdoors</p><h3>Camping</h3><p>Grass, stars, morning birdsong. Bring the essentials; we provide the quiet.</p><p class="price">To confirm <span class="meta">· editable</span></p><a class="link" href="experiences.html#camping">Sleep under the stars →</a></div></div>
</div></div></section>
<section class="dark"><div class="wrap split rv"><div class="txt"><p class="eyebrow" style="color:var(--sand)">Gatherings</p>
<h2 class="h2">SOME MOMENTS DESERVE A PLACE OF THEIR OWN.</h2>
<p class="lede">Weddings, quinceañeras, family celebrations, ceremonies and photo sessions — gardens, pool areas and open-air spaces ready for your people.</p>
<div class="hero-ctas" style="margin-top:24px"><a class="btn light" href="events.html">Plan Your Event</a><a class="btn ghost" style="color:#fff" href="{wa_link('en',*WA_MSGS['event'])}">Ask on WhatsApp</a></div></div>
<div class="frame"><img src="{IMG['event']}" alt="Outdoor celebration space at Rancho El Aguacero" loading="lazy"><p class="cap">Open-air spaces for ceremonies and gatherings.</p></div></div></section>
<section><div class="wrap"><p class="eyebrow rv">Guest stories</p><h2 class="h2 rv">WHAT STAYING HERE FEELS LIKE.</h2>
<div class="quotes"><div class="quote rv">“We came for one night and stayed for three. The quiet is the luxury.”<small>— Guest review · Google [replace with verified review]</small></div>
<div class="quote rv">“The kids lived outside all weekend. We lived in the hammocks.”<small>— Family stay · [verified source]</small></div>
<div class="quote rv">“Our ceremony under the trees felt private and timeless.”<small>— Event · [verified source]</small></div></div>
<p class="j-meta" style="margin-top:18px">Real reviews only — connect Google / Airbnb at launch. <a href="contact.html">Read more reviews →</a></p></div></section>
<section style="padding-top:0"><div class="wrap panel rv"><p class="eyebrow">Book direct</p><h2 class="h2">YOUR ESCAPE, IN MINUTES.</h2>
<p class="lede">Check availability, request your dates, and secure your reservation with a deposit. Prefer Airbnb? It stays available as an alternative — but booking direct is simplest.</p>
<div class="hero-ctas" style="margin-top:22px"><a class="btn" href="reserve.html" data-track="home_book">Check Availability</a><a class="btn ghost" href="plan.html">Plan Your Visit</a></div></div></section>"""
+ final_cta("en"))

PAGES[("es","index.html")] = ("Rancho El Aguacero — Un Refugio Atemporal en el Campo de Jalisco",
"Un refugio en el campo de Jalisco: hospedaje, cabañas, pases de día, campamento, Temazcal, cabalgatas y eventos privados. Reserva directa.",
f"""<section class="hero"><img class="hero-bg" src="{IMG['hero']}" alt="Atardecer sobre los jardines y la alberca de Rancho El Aguacero" fetchpriority="high">
<div class="hero-inner"><p class="eyebrow" style="color:var(--sand)">Jalisco · México — Deja el mundo atrás</p>
<h1 class="display">UN LUGAR ATEMPORAL<br>PARA IR MÁS DESPACIO.</h1>
<p class="sub">Un refugio en el campo de Jalisco donde la naturaleza, la historia, la celebración y el tiempo compartido se encuentran.</p>
<div class="hero-ctas"><a class="btn light" href="reserve.html" data-track="hero_reserve">Planea Tu Escapada</a><a class="btn ghost" style="color:#fff" href="ranch.html" data-track="hero_explore">Explora el Rancho</a></div>
<div class="scroll-hint">Descubre ↓</div></div></section>"""
+ actionbar("es") +
f"""<section><div class="wrap split rv"><div class="txt"><p class="eyebrow">El rancho</p>
<h2 class="h2">VEN POR LA ESCAPADA.<br>QUÉDATE POR LO QUE SE SIENTE.</h2>
<p class="lede">Rancho El Aguacero es más que un lugar para dormir. Es un lugar para desconectarte, convivir, explorar, celebrar, descansar — y crear recuerdos sin prisa.</p>
<p style="margin:18px 0 26px;color:#4a463d">Una propiedad histórica con raíces de principios de 1800, cuidada por la familia Bañuelos por generaciones. Sin ruido. Sin prisa. Solo espacio, sombra, agua y cielo.</p>
<div class="hero-ctas"><a class="btn" href="ranch.html">La historia del rancho</a><a class="btn ghost" href="stay.html">Quédate un poco más</a></div></div>
<div class="frame"><img src="{IMG['grounds']}" alt="Jardines y árboles altos en Rancho El Aguacero" loading="lazy"><p class="cap">Los jardines — mañanas bajo los árboles.</p></div></div></section>
<section class="dark"><div class="wrap rv"><p class="eyebrow" style="color:var(--sand)">El camino</p>
<h2 class="h2">DE LA CIUDAD<br>A UN LUGAR MÁS QUIETO.</h2>
<p class="lede">Ciudad → carretera → campo → agaves → el rancho → la quietud. A poca distancia de Guadalajara, Tequila y Etzatlán.</p>
<div style="margin-top:26px" class="hero-ctas"><a class="btn light" href="plan.html">Cómo Llegar</a></div></div>
<div class="hscroll" style="margin-top:34px">
<figure><img src="{IMG['aerial']}" alt="Campos de agave vistos desde arriba" loading="lazy"><figcaption><b>01 — Tierra de agave</b><span>El camino hacia el paisaje azul de Jalisco.</span></figcaption></figure>
<figure><img src="{IMG['aerial3']}" alt="Caminos y construcciones del rancho desde el aire" loading="lazy"><figcaption><b>02 — Camino abierto</b><span>Deja la ciudad; sigue lo verde.</span></figcaption></figure>
<figure><img src="{IMG['sheep']}" alt="Pavo real y ovejas pastando en el rancho" loading="lazy"><figcaption><b>03 — El rancho</b><span>Animales, árboles, agua, quietud.</span></figcaption></figure>
</div></section>
<section class="banner"><img class="bg" src="{IMG['aqueduct']}" alt="Acueducto histórico junto a la alberca" loading="lazy"><div class="shade"></div>
<div class="wrap rv"><p class="eyebrow" style="color:var(--sand)">El acueducto</p><h2 class="display">ENCUENTRA TU LUGAR<br>PARA NO HACER NADA.</h2>
<p class="lede" style="color:#eee6d2;margin:18px 0 26px;max-width:52ch">Sombra, hamacas, agua, piedra antigua. El acueducto es la firma del rancho — el lugar que nadie olvida.</p>
<a class="btn light" href="experiences.html">Explorar experiencias</a></div></section>
<section><div class="wrap"><p class="eyebrow rv">Hospedaje · Visita · Celebración</p><h2 class="h2 rv">ELIGE TU FORMA DE VIVIRLO.</h2>
<div class="grid3">
<div class="card rv"><img src="{IMG['room']}" alt="Recámara con azulejo mexicano y muebles de madera" loading="lazy"><div class="body"><p class="meta">Noche · 10–12 huéspedes</p><h3>La Casa del Rancho</h3><p>Recámaras, cocina, patios, alberca y senderos. Una casa hecha para reunirse.</p><p class="price">Precio a consultar <span class="meta">· confirmar</span></p><a class="link" href="stay.html">Ver alojamiento →</a></div></div>
<div class="card rv"><img src="{IMG['pool']}" alt="Alberca y áreas verdes para visitantes de día" loading="lazy"><div class="body"><p class="meta">Visita de día</p><h3>Pase de Día</h3><p>Albercas, áreas verdes, tiempo para respirar. Horarios y precios por confirmar.</p><p class="price">Por confirmar <span class="meta">· editable</span></p><a class="link" href="plan.html#daypass">Planea tu día →</a></div></div>
<div class="card rv"><img src="{IMG['night']}" alt="Fogata y cielo nocturno en el rancho" loading="lazy"><div class="body"><p class="meta">Aire libre</p><h3>Campamento</h3><p>Pasto, estrellas, canto de aves al amanecer. Trae lo esencial; nosotros ponemos la calma.</p><p class="price">Por confirmar <span class="meta">· editable</span></p><a class="link" href="experiences.html#camping">Duerme bajo las estrellas →</a></div></div>
</div></div></section>
<section class="dark"><div class="wrap split rv"><div class="txt"><p class="eyebrow" style="color:var(--sand)">Celebraciones</p>
<h2 class="h2">HAY MOMENTOS QUE MERECEN SU PROPIO LUGAR.</h2>
<p class="lede">Bodas, XV años, reuniones familiares, ceremonias y sesiones fotográficas — jardines, albercas y espacios al aire libre para tu gente.</p>
<div class="hero-ctas" style="margin-top:24px"><a class="btn light" href="events.html">Planea Tu Evento</a><a class="btn ghost" style="color:#fff" href="{wa_link('es',*WA_MSGS['event'])}">Preguntar por WhatsApp</a></div></div>
<div class="frame"><img src="{IMG['event']}" alt="Espacio al aire libre para celebraciones" loading="lazy"><p class="cap">Espacios abiertos para ceremonias y reuniones.</p></div></div></section>
<section><div class="wrap"><p class="eyebrow rv">Historias de huéspedes</p><h2 class="h2 rv">ASÍ SE SIENTE QUEDARSE AQUÍ.</h2>
<div class="quotes"><div class="quote rv">“Venimos por una noche y nos quedamos tres. La quietud es el lujo.”<small>— Reseña · Google [reemplazar con reseña verificada]</small></div>
<div class="quote rv">“Los niños vivieron afuera todo el fin. Nosotros, en las hamacas.”<small>— Estancia familiar · [fuente verificada]</small></div>
<div class="quote rv">“Nuestra ceremonia bajo los árboles se sintió íntima y atemporal.”<small>— Evento · [fuente verificada]</small></div></div>
<p class="j-meta" style="margin-top:18px">Solo reseñas reales — conectar Google / Airbnb al lanzamiento. <a href="contact.html">Leer más reseñas →</a></p></div></section>
<section style="padding-top:0"><div class="wrap panel rv"><p class="eyebrow">Reserva directa</p><h2 class="h2">TU ESCAPADA, EN MINUTOS.</h2>
<p class="lede">Consulta disponibilidad, solicita tus fechas y asegura tu reservación con un anticipo. ¿Prefieres Airbnb? Sigue disponible como alternativa — pero reservar directo es más simple.</p>
<div class="hero-ctas" style="margin-top:22px"><a class="btn" href="reserve.html" data-track="home_book">Consultar Disponibilidad</a><a class="btn ghost" href="plan.html">Planea Tu Visita</a></div></div></section>"""
+ final_cta("es"))

def std_page(lang, slug, title, desc, h1, eyebrow, intro, body, wa_key="gen", img=None):
    hero_img = img or IMG["aerial2"]
    return (title, desc, f"""<section class="hero" style="min-height:62svh"><img class="hero-bg" src="{hero_img}" alt="{h1}"><div class="hero-inner">
<p class="eyebrow" style="color:var(--sand)">{eyebrow}</p><h1 class="display" style="font-size:clamp(40px,6vw,84px)">{h1}</h1><p class="sub">{intro}</p></div></section>"""
+ body + final_cta(lang))

# Build secondary pages (both languages) — concise but complete
PAGES[("en","ranch.html")] = std_page("en","ranch.html","The Ranch — History, Land & Family | Rancho El Aguacero",
"Historic ranch in Jalisco with roots in the early 1800s. Land, family, generations — and the ranch today.","A PLACE WITH MEMORY.","The Ranch · Etzatlán, Jalisco",
"A historic property with roots in the early 1800s, cared for by the Bañuelos family across generations.",
f"""<section><div class="wrap split rv"><div class="txt"><p class="eyebrow">The story</p><h2 class="h2">THE LAND. THE FAMILY. THE GENERATIONS.</h2>
<div class="prose"><p>Rancho El Aguacero stands on land worked and loved for over two centuries. The aqueduct, the patios, the trees — each carries the memory of the people who built and kept this place.</p>
<p>Today the Bañuelos family opens the ranch to guests: to rest, to gather, to celebrate. Nothing here is staged. The history is in the walls, the shade, the water.</p>
<p class="j-meta">Historical details are published only as verified by the family. Unverified details are intentionally omitted.</p></div>
<div class="hero-ctas" style="margin-top:22px"><a class="btn" href="stay.html">Stay at the ranch</a><a class="btn ghost" href="gallery.html">See the gallery</a></div></div>
<div class="frame"><img src="{IMG['aerial3']}" alt="Ranch buildings among fields" loading="lazy"><p class="cap">The ranch among working fields.</p></div></div></section>""", img=IMG["aerial3"])

PAGES[("es","ranch.html")] = std_page("es","ranch.html","El Rancho — Historia, Tierra y Familia | Rancho El Aguacero",
"Rancho histórico en Jalisco con raíces de principios de 1800. La tierra, la familia, las generaciones — y el rancho hoy.","UN LUGAR CON MEMORIA.","El Rancho · Etzatlán, Jalisco",
"Una propiedad histórica con raíces de principios de 1800, cuidada por la familia Bañuelos por generaciones.",
f"""<section><div class="wrap split rv"><div class="txt"><p class="eyebrow">La historia</p><h2 class="h2">LA TIERRA. LA FAMILIA. LAS GENERACIONES.</h2>
<div class="prose"><p>Rancho El Aguacero está sobre una tierra trabajada y querida por más de dos siglos. El acueducto, los patios, los árboles — cada rincón guarda la memoria de quienes construyeron y cuidaron este lugar.</p>
<p>Hoy la familia Bañuelos abre el rancho a sus visitas: para descansar, reunirse, celebrar. Nada aquí es escenografía. La historia está en los muros, la sombra, el agua.</p>
<p class="j-meta">Solo se publican datos históricos verificados por la familia.</p></div>
<div class="hero-ctas" style="margin-top:22px"><a class="btn" href="stay.html">Hospédate en el rancho</a><a class="btn ghost" href="gallery.html">Ver galería</a></div></div>
<div class="frame"><img src="{IMG['aerial3']}" alt="Construcciones del rancho entre campos" loading="lazy"><p class="cap">El rancho entre campos de trabajo.</p></div></div></section>""", img=IMG["aerial3"])

PAGES[("en","stay.html")] = std_page("en","stay.html","Stay — Ranch House, Cabins & Camping | Rancho El Aguacero",
"Stay at Rancho El Aguacero: ranch house for 10–12 guests, cabins and camping. Check availability and book direct.","STAY A LITTLE LONGER.","Stay · Ranch house · Cabins · Camping",
"Bedrooms with Mexican character, kitchens for gathering, patios, pools and trails. The ranch house hosts about 10–12 guests.",
f"""<section><div class="wrap"><p class="eyebrow rv">Accommodation</p><h2 class="h2 rv">ROOMS THAT FEEL LIKE THE RANCH.</h2>
<div class="grid2">
<div class="card rv"><img src="{IMG['room']}" alt="Ranch house bedroom with terracotta floors" loading="lazy"><div class="body"><p class="meta">Sleeps ~10–12 · Whole house</p><h3>The Ranch House</h3><p>Bedrooms, bathrooms with Mexican tile, kitchen, living spaces, patios, dining areas, Wi-Fi, pool and trail access, outdoor cooking.</p><p class="price">Price on request</p><a class="link" href="reserve.html" data-track="stay_house">Check Availability →</a></div></div>
<div class="card rv"><img src="{IMG['bath']}" alt="Bathroom with Mexican tile and wood door" loading="lazy"><div class="body"><p class="meta">Cabins · Confirm details</p><h3>Cabins 1–4</h3><p>Private cabin stays on the property. Capacity, beds and pricing per cabin are editable in content/site.json — published only once confirmed.</p><p class="price">From — to confirm</p><a class="link" href="reserve.html" data-track="stay_cabin">Check Availability →</a></div></div>
</div>
<div class="notice rv" style="margin-top:26px">Capacity is stated conservatively (~10–12 in the ranch house). We never overstate beds or amenities. <a href="{wa_link('en',*WA_MSGS['stay'])}" data-track="stay_wa">Ask on WhatsApp →</a></div>
</div></section>
<section id="daypass" class="dark"><div class="wrap split rv"><div class="txt"><p class="eyebrow" style="color:var(--sand)">Day Pass</p><h2 class="h2">COME FOR THE DAY.</h2><p class="lede">Pools, green areas, room to breathe. Hours, inclusions, children policy and current pricing are confirmed before your visit — prices are editable by management, never hard-coded.</p>
<div class="hero-ctas" style="margin-top:22px"><a class="btn light" href="plan.html#daypass">Plan Your Day</a><a class="btn ghost" style="color:#fff" href="{wa_link('en',*WA_MSGS['day'])}">Ask on WhatsApp</a></div></div>
<div class="frame"><img src="{IMG['pool']}" alt="Pool and lawns" loading="lazy"></div></div></section>""", wa_key="stay", img=IMG["room"])

PAGES[("es","stay.html")] = std_page("es","stay.html","Hospedaje — Casa, Cabañas y Campamento | Rancho El Aguacero",
"Hospédate en Rancho El Aguacero: casa para 10–12 huéspedes, cabañas y campamento. Consulta disponibilidad y reserva directo.","QUÉDATE UN POCO MÁS.","Hospedaje · Casa · Cabañas · Campamento",
"Recámaras con carácter mexicano, cocinas para convivir, patios, albercas y senderos. La casa recibe alrededor de 10–12 huéspedes.",
f"""<section><div class="wrap"><p class="eyebrow rv">Alojamiento</p><h2 class="h2 rv">CUARTOS QUE SE SIENTEN COMO EL RANCHO.</h2>
<div class="grid2">
<div class="card rv"><img src="{IMG['room']}" alt="Recámara de la casa con pisos de terracota" loading="lazy"><div class="body"><p class="meta">~10–12 huéspedes · Casa completa</p><h3>La Casa del Rancho</h3><p>Recámaras, baños de azulejo mexicano, cocina, estancias, patios, comedores, Wi-Fi, alberca y senderos, cocina exterior.</p><p class="price">Precio a consultar</p><a class="link" href="reserve.html" data-track="stay_house">Consultar Disponibilidad →</a></div></div>
<div class="card rv"><img src="{IMG['bath']}" alt="Baño con azulejo mexicano y puerta de madera" loading="lazy"><div class="body"><p class="meta">Cabañas · Detalles por confirmar</p><h3>Cabañas 1–4</h3><p>Estancias privadas en la propiedad. Capacidad, camas y precios por cabaña se editan en content/site.json — se publican solo al confirmarse.</p><p class="price">Desde — por confirmar</p><a class="link" href="reserve.html" data-track="stay_cabin">Consultar Disponibilidad →</a></div></div>
</div>
<div class="notice rv" style="margin-top:26px">La capacidad se indica con prudencia (~10–12 en la casa). Nunca exageramos camas ni amenidades. <a href="{wa_link('es',*WA_MSGS['stay'])}" data-track="stay_wa">Preguntar por WhatsApp →</a></div>
</div></section>
<section id="daypass" class="dark"><div class="wrap split rv"><div class="txt"><p class="eyebrow" style="color:var(--sand)">Pase de día</p><h2 class="h2">VEN POR EL DÍA.</h2><p class="lede">Albercas, áreas verdes, espacio para respirar. Horarios, inclusiones, política de niños y precios vigentes se confirman antes de tu visita — los precios los edita la administración, nunca están fijos en el código.</p>
<div class="hero-ctas" style="margin-top:22px"><a class="btn light" href="plan.html#daypass">Planea Tu Día</a><a class="btn ghost" style="color:#fff" href="{wa_link('es',*WA_MSGS['day'])}">Preguntar por WhatsApp</a></div></div>
<div class="frame"><img src="{IMG['pool']}" alt="Alberca y jardines" loading="lazy"></div></div></section>""", wa_key="stay", img=IMG["room"])

PAGES[("en","experiences.html")] = std_page("en","experiences.html","Experiences — Horseback, Hiking, Temazcal, Pools | Rancho El Aguacero",
"Horseback riding, hiking, birdwatching, authentic Temazcal, pools, hammocks and camping in Jalisco countryside.","SLOW DAYS, DONE WELL.","Experiences · Nature · Temazcal · Camping",
"Ride agave trails, walk the land, watch birds, sweat and rest in Temazcal, float in the pool, sleep under stars.",
f"""<section><div class="wrap"><div class="grid3">
<div class="card rv"><img src="{IMG['horses']}" alt="Horses and donkey at the ranch fence" loading="lazy"><div class="body"><p class="meta">Guided</p><h3>Horseback Riding</h3><p>Explore the landscape and agave trails on horseback. Duration and price on request.</p><a class="link" href="reserve.html">Ask about riding →</a></div></div>
<div class="card rv"><img src="{IMG['aerial2']}" alt="Trails and fields" loading="lazy"><div class="body"><p class="meta">Self-guided + guided</p><h3>Hiking</h3><p>Trails and natural surroundings. Maps at check-in; guided walks on request.</p><a class="link" href="reserve.html">Plan a walk →</a></div></div>
<div class="card rv"><img src="{IMG['peacock']}" alt="Peacock on the ranch grounds" loading="lazy"><div class="body"><p class="meta">Dawn + dusk</p><h3>Birdwatching</h3><p>Herons, doves, songbirds — and our resident peacocks. Bring binoculars.</p><a class="link" href="journal.html">Read the guide →</a></div></div>
<div class="card rv"><img src="{IMG['temazcal']}" alt="Traditional Temazcal ceremony setting" loading="lazy"><div class="body"><p class="meta">Cultural · Guided</p><h3>Temazcal</h3><p>An authentic, respectful guided experience of heat, steam and stillness. Group price (1–14) editable — confirmed before publishing.</p><a class="link" href="{wa_link('en',*WA_MSGS['temazcal'])}">Ask About Temazcal →</a></div></div>
<div class="card rv"><img src="{IMG['pool']}" alt="Pool for relaxing" loading="lazy"><div class="body"><p class="meta">Daily</p><h3>Pools</h3><p>Relax and enjoy the water — for overnight guests and day visitors.</p><a class="link" href="plan.html#daypass">Day pass info →</a></div></div>
<div class="card rv" id="camping"><img src="{IMG['night']}" alt="Ranch lawn under evening lights" loading="lazy"><div class="body"><p class="meta">Night</p><h3>Camping — Sleep Under the Stars</h3><p>Outdoor areas, night atmosphere, gate hours and rules shared at booking. Bring essentials; pricing to confirm.</p><a class="link" href="{wa_link('en',*WA_MSGS['camp'])}">Ask about camping →</a></div></div>
</div>
<div class="notice rv" style="margin-top:26px">No medical or wellness claims are made about Temazcal. Durations and prices appear only once confirmed by the business.</div>
</div></section>""", wa_key="camp", img=IMG["grounds"])

PAGES[("es","experiences.html")] = std_page("es","experiences.html","Experiencias — Cabalgatas, Senderismo, Temazcal | Rancho El Aguacero",
"Cabalgatas, senderismo, aves, Temazcal auténtico, albercas, hamacas y campamento en el campo de Jalisco.","DÍAS LENTOS, BIEN VIVIDOS.","Experiencias · Naturaleza · Temazcal · Campamento",
"Recorre agaves a caballo, camina la tierra, observa aves, vive el Temazcal, flota en la alberca, duerme bajo estrellas.",
f"""<section><div class="wrap"><div class="grid3">
<div class="card rv"><img src="{IMG['horses']}" alt="Caballos y burro junto a la cerca" loading="lazy"><div class="body"><p class="meta">Guiada</p><h3>Cabalgata</h3><p>Explora el paisaje y senderos de agave a caballo. Duración y precio a consultar.</p><a class="link" href="reserve.html">Preguntar por cabalgata →</a></div></div>
<div class="card rv"><img src="{IMG['aerial2']}" alt="Senderos y campos" loading="lazy"><div class="body"><p class="meta">Libre + guiada</p><h3>Senderismo</h3><p>Senderos y entorno natural. Mapas al registrarte; caminatas guiadas a solicitud.</p><a class="link" href="reserve.html">Planear caminata →</a></div></div>
<div class="card rv"><img src="{IMG['peacock']}" alt="Pavo real en los jardines" loading="lazy"><div class="body"><p class="meta">Amanecer + atardecer</p><h3>Observación de Aves</h3><p>Garzas, palomas, cantoras — y nuestros pavos reales. Trae binoculares.</p><a class="link" href="journal.html">Leer la guía →</a></div></div>
<div class="card rv"><img src="{IMG['temazcal']}" alt="Espacio ceremonial tradicional de Temazcal" loading="lazy"><div class="body"><p class="meta">Cultural · Guiada</p><h3>Temazcal</h3><p>Experiencia auténtica y respetuosa de calor, vapor y quietud. Precio grupal (1–14) editable — se confirma antes de publicar.</p><a class="link" href="{wa_link('es',*WA_MSGS['temazcal'])}">Preguntar por el Temazcal →</a></div></div>
<div class="card rv"><img src="{IMG['pool']}" alt="Alberca para relajarse" loading="lazy"><div class="body"><p class="meta">Diario</p><h3>Albercas</h3><p>Relájate en el agua — para huéspedes y visitantes de día.</p><a class="link" href="plan.html#daypass">Info de pase de día →</a></div></div>
<div class="card rv" id="camping"><img src="{IMG['night']}" alt="Jardín del rancho bajo luces nocturnas" loading="lazy"><div class="body"><p class="meta">Noche</p><h3>Campamento — Duerme Bajo las Estrellas</h3><p>Áreas al aire libre, horarios de puerta y reglamento al reservar. Trae lo esencial; precio por confirmar.</p><a class="link" href="{wa_link('es',*WA_MSGS['camp'])}">Preguntar por campamento →</a></div></div>
</div>
<div class="notice rv" style="margin-top:26px">No hacemos afirmaciones médicas sobre el Temazcal. Duraciones y precios solo se publican al confirmarse.</div>
</div></section>""", wa_key="camp", img=IMG["grounds"])

PAGES[("en","events.html")] = std_page("en","events.html","Events & Weddings in Jalisco | Rancho El Aguacero",
"Weddings, quinceañeras, ceremonies and private gatherings at a historic Jalisco ranch. Gardens, pools and open-air spaces.","SOME MOMENTS DESERVE A PLACE OF THEIR OWN.","Events · Weddings · Quinceañeras",
"Gardens, pool areas, dining spaces and open-air ceremony possibilities — for celebrations that feel private and timeless.",
f"""<section><div class="wrap split rv"><div class="txt"><p class="eyebrow">What we host</p><h2 class="h2">WEDDINGS. FAMILY. CELEBRATION.</h2>
<div class="prose"><p>Weddings, ceremonies, quinceañeras, family gatherings, private events, photography sessions. Outdoor spaces, gardens, pool areas and dining areas adapt to your people.</p>
<p>Catering and outdoor cooking can be arranged; the kitchen is fully equipped. Menus are built with you — never invented here.</p></div></div>
<div class="frame"><img src="{IMG['event']}" alt="Event space outdoors" loading="lazy"></div></div></section>
<section style="padding-top:0"><div class="wrap grid2"><div class="panel rv"><p class="eyebrow">Event inquiry</p><h2 class="h2" style="font-size:clamp(28px,3vw,44px)">PLAN YOUR EVENT.</h2>
<form data-lead="event" data-done="Thank you. We've received your request and will contact you shortly."><div class="form-grid">
<div class="field"><label>Name</label><input required><div class="err">Required.</div></div>
<div class="field"><label>Email</label><input type="email" required><div class="err">Enter a valid email.</div></div></div>
<div class="form-grid"><div class="field"><label>WhatsApp</label><input></div><div class="field"><label>Event type</label><select><option>Wedding</option><option>Quinceañera</option><option>Family gathering</option><option>Ceremony</option><option>Photo session</option><option>Other</option></select></div></div>
<div class="form-grid"><div class="field"><label>Preferred date</label><input type="date"></div><div class="field"><label>Guest count</label><input type="number" min="1"></div></div>
<div class="field"><label>Message</label><textarea rows="4"></textarea></div>
<button class="btn" type="submit">Plan Your Event</button></form></div>
<div class="rv"><div class="panel"><p class="eyebrow">Photo sessions</p><h3 style="font-size:30px;margin-bottom:10px">A SETTING THAT PHOTOGRAPHS ITSELF.</h3><p style="color:#4a463d">Family, portraits, engagements, celebrations. Pricing editable and confirmed before publishing.</p><p style="margin-top:14px"><a href="{wa_link('en',*WA_MSGS['event'])}" data-track="event_wa"><b>Request a Photo Session →</b></a></p></div>
<div class="panel" style="margin-top:18px"><p class="eyebrow">Food</p><h3 style="font-size:30px;margin-bottom:10px">GATHER AROUND FOOD.</h3><p style="color:#4a463d">Catered food, barbecue, outdoor cooking, farm-fresh eggs where available. No invented menus — we plan yours together.</p></div></div></div></section>""", wa_key="event", img=IMG["event"])

PAGES[("es","events.html")] = std_page("es","events.html","Eventos y Bodas en Jalisco | Rancho El Aguacero",
"Bodas, XV años, ceremonias y reuniones privadas en un rancho histórico. Jardines, albercas y espacios al aire libre.","HAY MOMENTOS QUE MERECEN SU PROPIO LUGAR.","Eventos · Bodas · XV Años",
"Jardines, albercas, comedores y posibilidades de ceremonia al aire libre — para celebraciones privadas y atemporales.",
f"""<section><div class="wrap split rv"><div class="txt"><p class="eyebrow">Lo que recibimos</p><h2 class="h2">BODAS. FAMILIA. CELEBRACIÓN.</h2>
<div class="prose"><p>Bodas, ceremonias, XV años, reuniones familiares, eventos privados, sesiones fotográficas. Espacios exteriores, jardines, albercas y comedores que se adaptan a tu gente.</p>
<p>Banquetes y cocina al aire libre por acordar; la cocina está totalmente equipada. Los menús se construyen contigo — aquí no inventamos nada.</p></div></div>
<div class="frame"><img src="{IMG['event']}" alt="Espacio para eventos al aire libre" loading="lazy"></div></div></section>
<section style="padding-top:0"><div class="wrap grid2"><div class="panel rv"><p class="eyebrow">Cotización</p><h2 class="h2" style="font-size:clamp(28px,3vw,44px)">PLANEA TU EVENTO.</h2>
<form data-lead="event" data-done="Gracias. Recibimos tu solicitud y te contactaremos pronto."><div class="form-grid">
<div class="field"><label>Nombre</label><input required><div class="err">Requerido.</div></div>
<div class="field"><label>Correo</label><input type="email" required><div class="err">Escribe un correo válido.</div></div></div>
<div class="form-grid"><div class="field"><label>WhatsApp</label><input></div><div class="field"><label>Tipo de evento</label><select><option>Boda</option><option>XV años</option><option>Reunión familiar</option><option>Ceremonia</option><option>Sesión fotográfica</option><option>Otro</option></select></div></div>
<div class="form-grid"><div class="field"><label>Fecha preferida</label><input type="date"></div><div class="field"><label>Nº invitados</label><input type="number" min="1"></div></div>
<div class="field"><label>Mensaje</label><textarea rows="4"></textarea></div>
<button class="btn" type="submit">Planea Tu Evento</button></form></div>
<div class="rv"><div class="panel"><p class="eyebrow">Sesiones fotográficas</p><h3 style="font-size:30px;margin-bottom:10px">UN LUGAR QUE SE FOTOGRAFÍA SOLO.</h3><p style="color:#4a463d">Familia, retratos, compromiso, celebraciones. Precios editables y por confirmar.</p><p style="margin-top:14px"><a href="{wa_link('es',*WA_MSGS['event'])}" data-track="event_wa"><b>Solicitar una Sesión Fotográfica →</b></a></p></div>
<div class="panel" style="margin-top:18px"><p class="eyebrow">Comida</p><h3 style="font-size:30px;margin-bottom:10px">ALREDEDOR DE LA COMIDA.</h3><p style="color:#4a463d">Banquetes, asados, cocina exterior, huevos frescos cuando hay. Sin menús inventados — planeamos el tuyo juntos.</p></div></div></div></section>""", wa_key="event", img=IMG["event"])

PAGES[("en","gallery.html")] = std_page("en","gallery.html","Gallery — The Ranch in Photographs | Rancho El Aguacero",
"Real photography of Rancho El Aguacero: ranch, stay, nature, experiences, events and pools.","THE RANCH, AS IT IS.","Gallery · Real photography",
"Real ranch photography — no stock, no staged sets. Click any image to view.",
f"""<section><div class="wrap"><div class="hero-ctas rv" style="margin-bottom:22px">
<button class="btn clay" data-filter="all">All</button><button class="btn ghost" data-filter="ranch">The Ranch</button><button class="btn ghost" data-filter="stay">Stay</button><button class="btn ghost" data-filter="nature">Nature</button><button class="btn ghost" data-filter="pool">Pools</button><button class="btn ghost" data-filter="events">Events</button><button class="btn ghost" data-filter="experiences">Experiences</button></div>
<div class="g-grid rv" id="galleryGrid">{GALLERY_HTML['en']}</div></div></section>""", img=IMG["aerial"])

PAGES[("es","gallery.html")] = std_page("es","gallery.html","Galería — El Rancho en Fotografías | Rancho El Aguacero",
"Fotografía real de Rancho El Aguacero: rancho, hospedaje, naturaleza, experiencias, eventos y albercas.","EL RANCHO, COMO ES.","Galería · Fotografía real",
"Fotografía real del rancho — sin stock ni escenografías. Toca cualquier imagen para verla.",
f"""<section><div class="wrap"><div class="hero-ctas rv" style="margin-bottom:22px">
<button class="btn clay" data-filter="all">Todo</button><button class="btn ghost" data-filter="ranch">El Rancho</button><button class="btn ghost" data-filter="stay">Hospedaje</button><button class="btn ghost" data-filter="nature">Naturaleza</button><button class="btn ghost" data-filter="pool">Albercas</button><button class="btn ghost" data-filter="events">Eventos</button><button class="btn ghost" data-filter="experiences">Experiencias</button></div>
<div class="g-grid rv" id="galleryGrid">{GALLERY_HTML['es']}</div></div></section>""", img=IMG["aerial"])

PAGES[("en","journal.html")] = std_page("en","journal.html","Journal — Ranch Stories & Jalisco Travel Guides | Rancho El Aguacero",
"Stories from the ranch and slow travel guides: Etzatlán, birdwatching, Temazcal, weekend escapes from Guadalajara.","NOTES FROM THE RANCH.","Journal · Stories · Guides",
"History, nature, experiences and trip planning — the long, useful read.",
f"""<section><div class="wrap"><div class="grid3">
<div class="card rv"><img src="{IMG['aerial2']}" alt="Etzatlán countryside" loading="lazy"><div class="body"><p class="meta">Travel Guide · Mar 2026</p><h3>A Slow Day in Etzatlán</h3><p>Agave fields, a colonial town, and guava candy — how to spend a slow day near the ranch.</p><a class="link" href="contact.html">Read + plan →</a></div></div>
<div class="card rv"><img src="{IMG['peacock']}" alt="Peacock at the ranch" loading="lazy"><div class="body"><p class="meta">Nature · Feb 2026</p><h3>Birdwatching at the Ranch</h3><p>Herons at dawn, doves at dusk — what to watch and where to stand.</p><a class="link" href="contact.html">Read + plan →</a></div></div>
<div class="card rv"><img src="{IMG['temazcal']}" alt="Temazcal ceremony setting" loading="lazy"><div class="body"><p class="meta">Experiences · Jan 2026</p><h3>Before Your First Temazcal</h3><p>Heat, steam, breath, stillness — what a Temazcal really is, and how we host it with respect.</p><a class="link" href="experiences.html">Read + ask →</a></div></div>
</div><p class="j-meta rv" style="margin-top:20px">Articles are published with real dates and authors at launch — no backdated fakes.</p></div></section>""", img=IMG["aerial2"])

PAGES[("es","journal.html")] = std_page("es","journal.html","Diario — Historias y Guías de Jalisco | Rancho El Aguacero",
"Historias del rancho y guías de viaje lento: Etzatlán, aves, Temazcal, escapadas desde Guadalajara.","NOTAS DEL RANCHO.","Diario · Historias · Guías",
"Historia, naturaleza, experiencias y planeación — la lectura larga y útil.",
f"""<section><div class="wrap"><div class="grid3">
<div class="card rv"><img src="{IMG['aerial2']}" alt="Campo de Etzatlán" loading="lazy"><div class="body"><p class="meta">Guía de viaje · Mar 2026</p><h3>Un Día sin Prisa en Etzatlán</h3><p>Agaves, pueblo colonial y dulce de guayaba — cómo pasar un día lento cerca del rancho.</p><a class="link" href="contact.html">Leer + planear →</a></div></div>
<div class="card rv"><img src="{IMG['peacock']}" alt="Pavo real del rancho" loading="lazy"><div class="body"><p class="meta">Naturaleza · Feb 2026</p><h3>Observación de Aves en el Rancho</h3><p>Garzas al amanecer, palomas al atardecer — qué ver y dónde pararse.</p><a class="link" href="contact.html">Leer + planear →</a></div></div>
<div class="card rv"><img src="{IMG['temazcal']}" alt="Espacio ceremonial de Temazcal" loading="lazy"><div class="body"><p class="meta">Experiencias · Ene 2026</p><h3>Antes de tu Primer Temazcal</h3><p>Calor, vapor, respiración, quietud — qué es realmente y cómo lo ofrecemos con respeto.</p><a class="link" href="experiences.html">Leer + preguntar →</a></div></div>
</div><p class="j-meta rv" style="margin-top:20px">Los artículos se publican con fechas y autores reales — sin falsos retroactivos.</p></div></section>""", img=IMG["aerial2"])

PAGES[("en","plan.html")] = std_page("en","plan.html","Plan Your Visit — Location, Hours, Prices, FAQ | Rancho El Aguacero",
"How to get to Rancho El Aguacero from Guadalajara, Tequila and Etzatlán. Day pass info, rules, what to bring, FAQ.","KNOW BEFORE YOU GO.","Plan Your Visit · Directions · FAQ",
"Location, directions, hours, what to bring, rules, contact and answers — for visitors already imagining the trip.",
f"""<section><div class="wrap grid2">
<div class="rv prose"><p class="eyebrow">Getting here</p><h2 class="h2">IN THE COUNTRYSIDE, EASY TO REACH.</h2>
<p>Rancho El Aguacero sits in the countryside of Jalisco, near Etzatlán — between Guadalajara and Tequila. Travel times are shared once verified; ask us on WhatsApp for the current route.</p>
<p><a class="btn" href="https://www.google.com/maps/search/?api=1&query=Rancho+El+Aguacero+Etzatlan+Jalisco" target="_blank" rel="noopener" data-track="directions">Get Directions →</a></p>
<h3>Good to know</h3><p><b>Check-in / check-out:</b> confirmed at booking. <b>Gate hours:</b> shared before arrival. <b>What to bring:</b> light layers, hat, walking shoes, swimsuit, binoculars, flashlight for camping.</p></div>
<div class="rv" id="daypass"><div class="panel"><p class="eyebrow">Day Pass</p><h3>POOLS, LAWNS, QUIET.</h3>
<table class="table" style="margin-top:14px"><tr><th>Item</th><th>Detail</th></tr><tr><td>Hours</td><td>To confirm</td></tr><tr><td>Adult</td><td>To confirm</td></tr><tr><td>Child</td><td>To confirm</td></tr><tr><td>Includes</td><td>Pool access, green areas (confirmed at booking)</td></tr></table>
<p class="j-meta" style="margin:12px 0">Prices live in content/site.json — editable without redesign.</p>
<p><a class="btn clay" href="reserve.html">Plan Your Day</a></p></div></div></div></section>
<section style="padding-top:0"><div class="wrap"><p class="eyebrow rv">FAQ</p><h2 class="h2 rv">ANSWERS, HONESTLY.</h2>
<input id="faqSearch" placeholder="Search questions…" aria-label="Search questions" style="max-width:420px;margin-bottom:10px">
<div id="faqList" class="rv">
<details open><summary>How do I reserve? <span>＋</span></summary><p>Request your dates on the Reserve page or message us on WhatsApp. We confirm availability, then secure your reservation with a deposit.</p></details>
<details><summary>What payment methods are accepted? <span>＋</span></summary><p>Deposits and balances are processed through the configured payment provider at launch (no fake checkout). Details are confirmed with every reservation.</p></details>
<details><summary>What is the cancellation policy? <span>＋</span></summary><p>Free cancellation up to 7 days before check-in. The deposit policy inside 7 days is confirmed at booking.</p></details>
<details><summary>Are children welcome? <span>＋</span></summary><p>Yes — families are at the heart of the ranch. Children policies for day passes and stays are confirmed before your visit.</p></details>
<details><summary>How far is the ranch? <span>＋</span></summary><p>Near Etzatlán, between Guadalajara and Tequila. Exact times depend on route — ask us and we will send the current one.</p></details>
<details><summary>Can I visit for the day? <span>＋</span></summary><p>Yes, with a day pass when available. Check hours and pricing on this page before you come.</p></details>
</div><p class="j-meta" style="margin-top:14px">Only confirmed answers are published. Unverified details are omitted, not guessed.</p></div></section>""", img=IMG["aerial"])

PAGES[("es","plan.html")] = std_page("es","plan.html","Planea Tu Visita — Ubicación, Horarios, Precios | Rancho El Aguacero",
"Cómo llegar a Rancho El Aguacero desde Guadalajara, Tequila y Etzatlán. Pases de día, reglamento, qué traer, preguntas frecuentes.","ANTES DE VENIR.","Planea Tu Visita · Cómo Llegar · Preguntas",
"Ubicación, rutas, horarios, qué traer, reglamento, contacto y respuestas — para quien ya se imagina el viaje.",
f"""<section><div class="wrap grid2">
<div class="rv prose"><p class="eyebrow">Cómo llegar</p><h2 class="h2">EN EL CAMPO, FÁCIL DE LLEGAR.</h2>
<p>Rancho El Aguacero está en el campo de Jalisco, cerca de Etzatlán — entre Guadalajara y Tequila. Los tiempos de traslado se comparten una vez verificados; pregúntanos por WhatsApp la ruta vigente.</p>
<p><a class="btn" href="https://www.google.com/maps/search/?api=1&query=Rancho+El+Aguacero+Etzatlan+Jalisco" target="_blank" rel="noopener" data-track="directions">Cómo Llegar →</a></p>
<h3>Conviene saber</h3><p><b>Check-in / check-out:</b> se confirman al reservar. <b>Horario de puerta:</b> se comparte antes de llegar. <b>Qué traer:</b> ropa ligera, sombrero, calzado cómodo, traje de baño, binoculares, lámpara si acampas.</p></div>
<div class="rv" id="daypass"><div class="panel"><p class="eyebrow">Pase de día</p><h3>ALBERCAS, JARDINES, CALMA.</h3>
<table class="table" style="margin-top:14px"><tr><th>Concepto</th><th>Detalle</th></tr><tr><td>Horario</td><td>Por confirmar</td></tr><tr><td>Adulto</td><td>Por confirmar</td></tr><tr><td>Niño</td><td>Por confirmar</td></tr><tr><td>Incluye</td><td>Alberca, áreas verdes (se confirma al reservar)</td></tr></table>
<p class="j-meta" style="margin:12px 0">Los precios viven en content/site.json — editables sin rediseño.</p>
<p><a class="btn clay" href="reserve.html">Planea Tu Día</a></p></div></div></div></section>
<section style="padding-top:0"><div class="wrap"><p class="eyebrow rv">Preguntas</p><h2 class="h2 rv">RESPUESTAS, CON HONESTIDAD.</h2>
<input id="faqSearch" placeholder="Buscar preguntas…" aria-label="Buscar preguntas" style="max-width:420px;margin-bottom:10px">
<div id="faqList" class="rv">
<details open><summary>¿Cómo reservo? <span>＋</span></summary><p>Solicita tus fechas en Reservar o escríbenos por WhatsApp. Confirmamos disponibilidad y aseguras con un anticipo.</p></details>
<details><summary>¿Qué formas de pago aceptan? <span>＋</span></summary><p>Anticipos y saldos por el proveedor configurado al lanzamiento (sin checkout falso). Detalles con cada reservación.</p></details>
<details><summary>¿Cuál es la política de cancelación? <span>＋</span></summary><p>Cancelación gratuita hasta 7 días antes del check-in. La política del anticipo dentro de 7 días se confirma al reservar.</p></details>
<details><summary>¿Los niños son bienvenidos? <span>＋</span></summary><p>Sí — las familias son el corazón del rancho. Las políticas para niños se confirman antes de tu visita.</p></details>
<details><summary>¿Qué tan lejos está? <span>＋</span></summary><p>Cerca de Etzatlán, entre Guadalajara y Tequila. Los tiempos dependen de la ruta — te enviamos la vigente.</p></details>
<details><summary>¿Puedo ir solo por el día? <span>＋</span></summary><p>Sí, con pase de día cuando hay disponibilidad. Revisa horarios y precios en esta página antes de venir.</p></details>
</div><p class="j-meta" style="margin-top:14px">Solo se publican respuestas confirmadas. Lo no verificado se omite, no se adivina.</p></div></section>""", img=IMG["aerial"])

# Reserve pages with booking widget
def reserve_body(lang):
    if lang=="en":
        return f"""<section><div class="wrap grid2"><div class="panel rv" id="booking" data-lang="en">
<p class="eyebrow">Direct booking</p><h2 class="h2" style="font-size:clamp(28px,3vw,44px)">SECURE YOUR RESERVATION.</h2>
<div class="steps" aria-hidden="true"><i class="on"></i><i class="on"></i><i></i></div>
<form id="bookForm">
<div class="form-grid"><div class="field"><label for="bAcc">Accommodation</label><select id="bAcc" required><option value="">Select…</option><option value="house">Ranch House (~10–12)</option><option value="cabin">Cabin</option><option value="camp">Camping</option></select></div>
<div class="field"><label for="bGuests">Guests</label><input id="bGuests" type="number" min="1" max="30" required></div></div>
<div class="form-grid"><div class="field"><label for="bIn">Check-in</label><input id="bIn" type="date" required></div>
<div class="field"><label for="bOut">Check-out</label><input id="bOut" type="date" required></div></div>
<div class="field"><label for="bName">Full name</label><input id="bName" required></div>
<div class="form-grid"><div class="field"><label for="bEmail">Email</label><input id="bEmail" type="email" required></div>
<div class="field"><label for="bPhone">Phone / WhatsApp</label><input id="bPhone" required></div></div>
<div class="field"><label for="bNotes">Special requests</label><textarea id="bNotes" rows="3"></textarea></div>
<div class="panel" id="bSum" style="padding:18px;margin-bottom:16px"><p class="lede" style="font-size:16px">Choose lodging and dates to see your total.</p></div>
<button class="btn" type="submit" data-track="booking_start">Request to book</button>
<p class="j-meta" style="margin-top:12px">Deposit 30% to secure · payment via configured provider · confirmation by email + WhatsApp.</p>
<p class="j-meta">Prefer Airbnb? <a href="https://www.airbnb.com/">Book on Airbnb →</a> (alternative channel; direct is simplest).</p></form>
<div id="bookDone" style="display:none"><h3 style="font-size:34px;margin-bottom:10px">YOUR ESCAPE IS REQUESTED.</h3>
<p class="ref j-meta"></p><p style="margin:14px 0">We received your request and will confirm availability shortly by email and WhatsApp, with secure deposit instructions.</p>
<p><a class="btn" href="{wa_link('en',*WA_MSGS['stay'])}">Message Us on WhatsApp</a> <a class="btn ghost" href="plan.html">Get Directions</a></p></div>
</div><div class="rv"><div class="panel"><p class="eyebrow">What happens next</p><h3 style="font-size:28px">1. REQUEST → 2. CONFIRM → 3. DEPOSIT → 4. ARRIVE.</h3>
<p style="color:#4a463d;margin-top:10px">Transparent totals, cancellation terms and inclusions before you pay. No fake checkout — the payment module connects to the real provider at launch (see content/site.json → booking.paymentProvider).</p></div>
<div class="panel" style="margin-top:18px"><p class="eyebrow">Talk to us</p><p><a href="{wa_link('en',*WA_MSGS['gen'])}" data-track="reserve_wa"><b>Ask on WhatsApp →</b></a><br><a href="mailto:{EMAIL}">{EMAIL}</a></p></div></div></div></section>"""
    return f"""<section><div class="wrap grid2"><div class="panel rv" id="booking" data-lang="es">
<p class="eyebrow">Reserva directa</p><h2 class="h2" style="font-size:clamp(28px,3vw,44px)">ASEGURA TU RESERVACIÓN.</h2>
<div class="steps" aria-hidden="true"><i class="on"></i><i class="on"></i><i></i></div>
<form id="bookForm">
<div class="form-grid"><div class="field"><label for="bAcc">Alojamiento</label><select id="bAcc" required><option value="">Elige…</option><option value="house">Casa (~10–12)</option><option value="cabin">Cabaña</option><option value="camp">Campamento</option></select></div>
<div class="field"><label for="bGuests">Huéspedes</label><input id="bGuests" type="number" min="1" max="30" required></div></div>
<div class="form-grid"><div class="field"><label for="bIn">Llegada</label><input id="bIn" type="date" required></div>
<div class="field"><label for="bOut">Salida</label><input id="bOut" type="date" required></div></div>
<div class="field"><label for="bName">Nombre completo</label><input id="bName" required></div>
<div class="form-grid"><div class="field"><label for="bEmail">Correo</label><input id="bEmail" type="email" required></div>
<div class="field"><label for="bPhone">Teléfono / WhatsApp</label><input id="bPhone" required></div></div>
<div class="field"><label for="bNotes">Peticiones especiales</label><textarea id="bNotes" rows="3"></textarea></div>
<div class="panel" id="bSum" style="padding:18px;margin-bottom:16px"><p class="lede" style="font-size:16px">Elige alojamiento y fechas para ver el total.</p></div>
<button class="btn" type="submit" data-track="booking_start">Solicitar reserva</button>
<p class="j-meta" style="margin-top:12px">Anticipo 30% para asegurar · pago por proveedor configurado · confirmación por correo + WhatsApp.</p>
<p class="j-meta">¿Prefieres Airbnb? <a href="https://www.airbnb.com/">Reservar en Airbnb →</a> (canal alternativo; directo es más simple).</p></form>
<div id="bookDone" style="display:none"><h3 style="font-size:34px;margin-bottom:10px">TU ESCAPADA ESTÁ SOLICITADA.</h3>
<p class="ref j-meta"></p><p style="margin:14px 0">Recibimos tu solicitud y confirmaremos disponibilidad pronto por correo y WhatsApp, con instrucciones seguras de anticipo.</p>
<p><a class="btn" href="{wa_link('es',*WA_MSGS['stay'])}">Escríbenos por WhatsApp</a> <a class="btn ghost" href="plan.html">Cómo Llegar</a></p></div>
</div><div class="rv"><div class="panel"><p class="eyebrow">Qué sigue</p><h3 style="font-size:28px">1. SOLICITA → 2. CONFIRMAMOS → 3. ANTICIPO → 4. LLEGA.</h3>
<p style="color:#4a463d;margin-top:10px">Totales transparentes, cancelación e inclusiones antes de pagar. Sin checkout falso — el módulo se conecta al proveedor real al lanzamiento (ver content/site.json → booking.paymentProvider).</p></div>
<div class="panel" style="margin-top:18px"><p class="eyebrow">Hablemos</p><p><a href="{wa_link('es',*WA_MSGS['gen'])}" data-track="reserve_wa"><b>Preguntar por WhatsApp →</b></a><br><a href="mailto:{EMAIL}">{EMAIL}</a></p></div></div></div></section>"""

PAGES[("en","reserve.html")] = ("Reserve — Check Availability & Book Direct | Rancho El Aguacero",
"Check availability and request your stay at Rancho El Aguacero. Secure deposit, email + WhatsApp confirmation.",
f"""<section class="hero" style="min-height:52svh"><img class="hero-bg" src="{IMG['room']}" alt="Reserve your stay"><div class="hero-inner">
<p class="eyebrow" style="color:var(--sand)">Reserve · Book direct</p><h1 class="display" style="font-size:clamp(40px,6vw,84px)">BEGIN YOUR STAY.</h1></div></section>"""
+ reserve_body("en") + final_cta("en"))
PAGES[("es","reserve.html")] = ("Reservar — Disponibilidad y Reserva Directa | Rancho El Aguacero",
"Consulta disponibilidad y solicita tu estancia. Anticipo seguro, confirmación por correo + WhatsApp.",
f"""<section class="hero" style="min-height:52svh"><img class="hero-bg" src="{IMG['room']}" alt="Reserva tu estancia"><div class="hero-inner">
<p class="eyebrow" style="color:var(--sand)">Reservar · Reserva directa</p><h1 class="display" style="font-size:clamp(40px,6vw,84px)">COMIENZA TU ESTANCIA.</h1></div></section>"""
+ reserve_body("es") + final_cta("es"))

PAGES[("en","contact.html")] = std_page("en","contact.html","Contact — WhatsApp, Email & Location | Rancho El Aguacero",
"Contact Rancho El Aguacero: WhatsApp, email, directions near Etzatlán, Jalisco. We reply shortly.","TALK TO THE RANCH.","Contact · WhatsApp · Email",
"We read everything. Tell us about your trip — we reply shortly.",
f"""<section><div class="wrap grid2"><div class="panel rv">
<form data-lead="contact" data-done="Thank you. We'll be in touch. — While you wait, explore the ranch or chat on WhatsApp.">
<div class="form-grid"><div class="field"><label>Name</label><input required><div class="err">Required.</div></div>
<div class="field"><label>Email</label><input type="email" required><div class="err">Enter a valid email.</div></div></div>
<div class="field"><label>I'm interested in</label><select><option>Overnight stay</option><option>Day pass</option><option>Camping</option><option>Event</option><option>Photo session</option><option>Other</option></select></div>
<div class="field"><label>Message</label><textarea rows="4" required></textarea><div class="err">Required.</div></div>
<button class="btn" type="submit">Send Message</button></form></div>
<div class="rv"><div class="panel"><p class="eyebrow">Direct</p><p style="font-size:20px"><a href="{wa_link('en',*WA_MSGS['gen'])}"><b>Chat on WhatsApp →</b></a><br><a href="mailto:{EMAIL}">{EMAIL}</a></p>
<p style="margin-top:14px"><a class="btn ghost" href="https://www.google.com/maps/search/?api=1&query=Rancho+El+Aguacero+Etzatlan+Jalisco" target="_blank" rel="noopener">Get Directions</a></p>
<p class="j-meta" style="margin-top:12px">Privacy: your details are used only to answer your request. Unsubscribe anytime.</p></div></div></div></section>""", img=IMG["grounds"])
PAGES[("es","contact.html")] = std_page("es","contact.html","Contacto — WhatsApp, Correo y Ubicación | Rancho El Aguacero",
"Contacta Rancho El Aguacero: WhatsApp, correo, cómo llegar cerca de Etzatlán, Jalisco. Respondemos pronto.","HABLA CON EL RANCHO.","Contacto · WhatsApp · Correo",
"Leemos todo. Cuéntanos de tu viaje — respondemos pronto.",
f"""<section><div class="wrap grid2"><div class="panel rv">
<form data-lead="contact" data-done="Gracias. Estaremos en contacto. — Mientras tanto, explora el rancho o escríbenos por WhatsApp.">
<div class="form-grid"><div class="field"><label>Nombre</label><input required><div class="err">Requerido.</div></div>
<div class="field"><label>Correo</label><input type="email" required><div class="err">Escribe un correo válido.</div></div></div>
<div class="field"><label>Me interesa</label><select><option>Hospedaje</option><option>Pase de día</option><option>Campamento</option><option>Evento</option><option>Sesión fotográfica</option><option>Otro</option></select></div>
<div class="field"><label>Mensaje</label><textarea rows="4" required></textarea><div class="err">Requerido.</div></div>
<button class="btn" type="submit">Enviar Mensaje</button></form></div>
<div class="rv"><div class="panel"><p class="eyebrow">Directo</p><p style="font-size:20px"><a href="{wa_link('es',*WA_MSGS['gen'])}"><b>Escríbenos por WhatsApp →</b></a><br><a href="mailto:{EMAIL}">{EMAIL}</a></p>
<p style="margin-top:14px"><a class="btn ghost" href="https://www.google.com/maps/search/?api=1&query=Rancho+El+Aguacero+Etzatlan+Jalisco" target="_blank" rel="noopener">Cómo Llegar</a></p>
<p class="j-meta" style="margin-top:12px">Privacidad: tus datos solo se usan para responderte. Date de baja cuando quieras.</p></div></div></div></section>""", img=IMG["grounds"])

# ---- write ----
for (lang, slug), (title, desc, body) in PAGES.items():
    img = IMG["aerial"]
    html = head(lang, slug, title, desc, img) + header(lang) + "<main>" + body + "</main>" + footer(lang) + tail(lang, "gen")
    # fix cross-language link to same page
    other = "es" if lang=="en" else "en"
    html = html.replace(f'href="../{other}/index.html"', f'href="../{other}/{slug}"', 1) if False else html
    # proper lang switcher: point to same slug
    html = html.replace('../es/index.html' if lang=='en' else '../en/index.html', f'../{other}/{slug}')
    p = os.path.join(BASE, lang, slug)
    open(p, "w", encoding="utf-8").write(html)
    print("wrote", p)

# root redirect
open(os.path.join(BASE,"index.html"),"w",encoding="utf-8").write("""<!DOCTYPE html><html><head><meta charset="UTF-8"><meta http-equiv="refresh" content="0;url=en/index.html"><script>var l=(navigator.language||'en').toLowerCase();location.replace(l.indexOf('es')===0?'es/index.html':'en/index.html')</script><title>Rancho El Aguacero</title></head><body><a href="en/index.html">English</a> · <a href="es/index.html">Español</a></body></html>""")
# robots + sitemap
open(os.path.join(BASE,"robots.txt"),"w").write(f"Sitemap: {DOMAIN}/sitemap.xml\nUser-agent: *\nAllow: /\n")
urls = "".join(f"<url><loc>{DOMAIN}/{l}/{s}</loc><xhtml:link rel='alternate' hreflang='en' href='{DOMAIN}/en/{s}'/><xhtml:link rel='alternate' hreflang='es' href='{DOMAIN}/es/{s}'/></url>" for l,s in sorted({(l,s) for l,s in PAGES}))
open(os.path.join(BASE,"sitemap.xml"),"w",encoding="utf-8").write(f"<?xml version='1.0' encoding='UTF-8'?><urlset xmlns='http://www.sitemaps.org/schemas/sitemap/0.9' xmlns:xhtml='http://www.w3.org/1999/xhtml'>{urls}</urlset>")
print("done", len(PAGES))
