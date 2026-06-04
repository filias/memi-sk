"""People — historical and modern Slovak figures."""

# Pre-1918 figures (Great Moravia and Hungarian Kingdom era)
HISTORICAL = [
    "Pribina",
    "Ľudovít Štúr",
    "Janko Kráľ",
    "Pavol Országh Hviezdoslav",
    "Andrej Sládkovič",
]

# 20th century (1918–1989)
MODERN = [
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
CONTEMPORARY = [
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

ALL = HISTORICAL + MODERN + CONTEMPORARY

# Wikipedia article titles (where they differ from the display name)
WIKIPEDIA: dict[str, str] = {}

# Era — used as the tag
PERIODS = {
    **{p: "do roku 1918" for p in HISTORICAL},
    **{p: "20. storočie" for p in MODERN},
    **{p: "súčasnosť" for p in CONTEMPORARY},
}
