"""Memi Slovensko - precvič si pamäť o Slovensku."""

import os

from memi_engine import MemiConfig, create_app

# Import providers to register them
import memi_sk.providers  # noqa: F401

config = MemiConfig(
    title="memi slovensko",
    subtitle="precvič si pamäť",
    favicon_color="#0B4EA2",
    themes=["light", "blue", "red", "dark"],
    default_theme="light",
    sponsor_url="https://github.com/sponsors/filias",
    sponsor_text="podporiť",
    about_html="""
        <p>Memi Slovensko je pamäťová hra o Slovensku.</p>
        <p>Vyber kategóriu, pozri sa na obrázok a skús uhádnuť, čo to je,
        skôr než odhalíš odpoveď.</p>
        <p>Kraje, pamiatky, jedlá, slávne osobnosti — vždy je čo nové
        objaviť alebo si pripomenúť.</p>
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
    done_html="""
        <svg width="200" height="180" viewBox="0 0 80 72" xmlns="http://www.w3.org/2000/svg">
            <defs>
                <clipPath id="heart-clip">
                    <path d="M40 68 C40 68 4 44 4 22 C4 10 14 2 24 2 C30 2 36 6 40 12 C44 6 50 2 56 2 C66 2 76 10 76 22 C76 44 40 68 40 68Z"/>
                </clipPath>
            </defs>
            <g clip-path="url(#heart-clip)">
                <rect x="0" y="0"  width="80" height="24" fill="#FFFFFF"/>
                <rect x="0" y="24" width="80" height="24" fill="#0B4EA2"/>
                <rect x="0" y="48" width="80" height="24" fill="#EE1C25"/>
                <!-- Slovak coat of arms -->
                <g transform="translate(14, 16)">
                    <!-- red shield -->
                    <path d="M0 0 L20 0 L20 22 Q20 30 10 34 Q0 30 0 22 Z"
                          fill="#EE1C25" stroke="#FFFFFF" stroke-width="1"/>
                    <!-- three blue hills -->
                    <path d="M1.5 26 L6 19 L10 26 L14 19 L18.5 26 L18.5 32 L1.5 32 Z"
                          fill="#0B4EA2"/>
                    <!-- white double cross -->
                    <rect x="9" y="4"  width="2" height="22" fill="#FFFFFF"/>
                    <rect x="5" y="8"  width="10" height="2" fill="#FFFFFF"/>
                    <rect x="3" y="15" width="14" height="2" fill="#FFFFFF"/>
                </g>
            </g>
            <path d="M40 68 C40 68 4 44 4 22 C4 10 14 2 24 2 C30 2 36 6 40 12 C44 6 50 2 56 2 C66 2 76 10 76 22 C76 44 40 68 40 68Z"
                  fill="none" stroke="var(--subtle, #888)" stroke-width="1.5"/>
        </svg>
    """,
)

instance_static = os.path.join(os.path.dirname(__file__), "..", "static")
app = create_app(config, instance_static=instance_static)

if __name__ == "__main__":
    app.run(debug=True, port=8087)
