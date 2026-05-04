"""Ľudia — historical and modern Slovak figures."""

# Pre-1918 figures (Great Moravia and Hungarian Kingdom era)
HISTORICKE = [
    "Pribina",
    "Ľudovít Štúr",
    "Janko Kráľ",
    "Pavol Országh Hviezdoslav",
    "Andrej Sládkovič",
]

# 20th century (1918–1989)
MODERNE = [
    "Andrej Hlinka",
    "Milan Rastislav Štefánik",
    "Jozef Tiso",
    "Gustáv Husák",
    "Alexander Dubček",
    "Jozef Murgaš",
    "Štefan Banič",
    "Aurel Stodola",
    "Eugen Suchoň",
    "Andy Warhol",
]

# Contemporary (1989–today)
SUCASNI = [
    "Peter Sagan",
    "Marián Hossa",
    "Pavol Demitra",
    "Marek Hamšík",
    "Daniela Hantuchová",
    "Dominik Hrbatý",
    "Andrej Kiska",
    "Zuzana Čaputová",
    "Robert Fico",
]

ALL = HISTORICKE + MODERNE + SUCASNI

# Wikipedia article titles (where they differ from the display name)
WIKIPEDIA: dict[str, str] = {}

# Era — used as the tag
OBDOBIA = {
    **{p: "do roku 1918" for p in HISTORICKE},
    **{p: "20. storočie" for p in MODERNE},
    **{p: "súčasnosť" for p in SUCASNI},
}
