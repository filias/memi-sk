"""Memi Slovakia - practice your memory about Slovakia."""

import os

from memi_engine import MemiConfig, create_app

# Import providers to register them
import memi_sk.providers  # noqa: F401

# The home page opens on the menu, and its empty card shows Slovakia's outline in its flag above
# "vyber kategóriu". The engine has no setting for that, so this rides on
# analytics_html (raw HTML at the bottom of every page, after app.js); loading
# a category replaces the card's text, so the map goes with it.
# static/flag-map-slovakia.svg: Wikimedia Commons, "Flag-map of Slovakia.svg" by Stasyan117, CC BY-SA 4.0.
HOME_CARD_HTML = """
<style>
    #status.home { width: 100%; text-align: center; }
    #status .home-map, #done-art .home-map { display: block; max-width: 80%; max-height: calc(min(500px, 90vw) * 0.6); margin: 0 auto 1.5rem; }
</style>
<script>
(function () {
    var status = document.getElementById('status');
    if (status && status.textContent.trim() === 'vyber kategóriu') {
        status.classList.add('home');
        status.insertAdjacentHTML('afterbegin', '<img class="home-map" src="/static/flag-map-slovakia.svg" alt="Slovensko">');
    }
})();
</script>
"""

config = MemiConfig(
    analytics_html=(
        '<script data-goatcounter="https://memi-sk.goatcounter.com/count"'
        ' async src="//gc.zgo.at/count.js"></script>'
    ) + HOME_CARD_HTML,
    # What the page tells Google and screen readers it is: this game
    # is Slovak, not the engine's default English.
    html_lang="sk",
    # Details panel beside the card on reveal: the Wikipedia intro (in
    # Slovak where it exists) and, for places, a map.
    layout="enriched",
    title="memi slovensko",
    subtitle="precvič si pamäť",
    favicon_color="#0B4EA2",
    sponsor_url="https://github.com/sponsors/filias",
    sponsor_text="podporiť",
    # The memi.games landing page, then every other public edition (memi
    # mallorca is private), in the landing page's order.
    related_sites=[
        {"name": "memi.games", "url": "https://memi.games"},
        {"name": "memi", "url": "https://world.memi.games"},
        {"name": "memi portugal", "url": "https://pt.memi.games"},
        {"name": "memi lisboa", "url": "https://lx.memi.games"},
        {"name": "memi united states", "url": "https://us.memi.games"},
        {"name": "memi pyrenees", "url": "https://py.memi.games"},
        {"name": "memi kraków", "url": "https://kr.memi.games"},
        {"name": "memi romania", "url": "https://ro.memi.games"},
    ],
    label_related_sites="ďalšie hry memi",
    about_html="""
        <p>Memi Slovensko je pamäťová hra o Slovensku. Kraje, pamiatky,
        jedlá, slávne osobnosti &mdash; vždy je čo nové objaviť alebo si
        pripomenúť.</p>

        <h2>Ako hrať</h2>
        <p>Vyber kategóriu, pozri sa na obrázok a skús uhádnuť, čo to je,
        skôr než odhalíš odpoveď. Žiadne účty, žiadne body, žiadny časový
        limit.</p>
        <p>V spodnej lište nájdeš niekoľko pomocníkov:</p>
        <ul>
            <li><strong>nápovedy:</strong> zapne postupné nápovedy
            písmen &mdash; najprv odhalí prvé písmeno, potom ďalšie, a
            tak ďalej. Užitočné, keď máš odpoveď na jazyku.</li>
            <li><strong>zistiť viac:</strong> objaví sa pri odhalení a
            otvorí článok na Wikipédii (alebo zdrojovú stránku) k
            položke, aby si si o nej mohol prečítať viac.</li>
            <li><strong>nahlásiť:</strong> označ kartu, ak obrázok
            nezodpovedá odpovedi (zlý obrázok, rozbitá miniatúra a
            podobne).</li>
        </ul>
        <p>Hrať sa dá dvoma spôsobmi:</p>
        <ul>
            <li><strong>Pre učenie:</strong> keď položku nepoznáš, odhal
            odpoveď a klikni na odkaz <em>zistiť viac</em>, aby si si o
            nej prečítal. Každé vystavenie posilňuje spojenie medzi
            obrazom a názvom.</li>
            <li><strong>Pre vlastný test:</strong> keď ti kategória príde
            známa, prejdi ju a pozri, koľko z nej dokážeš pomenovať bez
            odhalenia.</li>
        </ul>

        <h2>Prečo to funguje</h2>
        <p>Toto je jednoduchá forma <em>aktívneho vybavovania</em>
        &mdash; ťahania informácií z pamäte namiesto opakovaného čítania.
        <em>Testovací efekt</em>, dobre zdokumentovaný v kognitívnej
        psychológii, ukazuje, že vybavovacia prax vytvára trvalejšie
        pamäťové stopy než samotné opakované vystavovanie.</p>
        <p>Keďže je každý podnet obraz, hra využíva aj <em>efekt
        nadradenosti obrazu</em>: obrázky sa kódujú bohatšie než slová a
        ľahšie sa neskôr vybavujú. Pomenovanie položky je forma
        <em>vybavovania s nápovedou</em>, ktorá leží medzi jednoduchým
        rozpoznaním (&bdquo;videl som to už?&ldquo;) a <em>voľným
        vybavovaním</em> bez pomoci.</p>
        <p>Krátke a časté sedenia fungujú lepšie než dlhé &mdash;
        <em>efekt rozloženia</em>. Pár minút denne stačí.</p>

        <p>Mapa s vlajkou na úvodnej stránke: <a href="https://commons.wikimedia.org/wiki/File:Flag-map_of_Slovakia.svg">Stasyan117</a>, CC BY-SA 4.0.</p>
    """,
    label_theme="téma",
    label_about="o memi",
    label_report="nahlásiť",
    label_reported="nahlásené",
    label_clues_on="nápovedy: áno",
    label_clues_off="nápovedy: nie",
    label_show_letter="ukázať písmeno",
    label_pick_category="vyber kategóriu",
    label_loading="načítava sa...",
    label_all_done="hotovo! klikni na nový začiatok",
    label_click_to_reveal="klikni na obrázok pre odhalenie odpovede",
    label_click_for_new="klikni znova pre ďalší",
    label_back="späť k hre",
    label_more="zistiť viac",
    label_all="všetky",
    label_open_map="otvoriť mapu",
    label_listen="vypočuť",
    # The "all done" card shows the same flag map as the home card.
    done_html='<img class="home-map" src="/static/flag-map-slovakia.svg" alt="Slovensko">',
)

instance_static = os.path.join(os.path.dirname(__file__), "..", "static")
app = create_app(config, instance_static=instance_static)

if __name__ == "__main__":
    app.run(debug=True, port=8087)
