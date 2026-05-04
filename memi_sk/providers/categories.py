"""Slovak category providers."""

from memi_engine import CategoryProvider, register
from memi_engine import images

from memi_sk.categories.kraje import KRAJE, WIKIPEDIA as KRAJ_WIKI
from memi_sk.categories.mesta import (
    MESTA,
    WIKIPEDIA as MESTO_WIKI,
    KRAJE as MESTO_KRAJE,
)
from memi_sk.categories.rieky import (
    RIEKY,
    WIKIPEDIA as RIEKA_WIKI,
    DLZKY as RIEKA_DLZKY,
)
from memi_sk.categories.pamiatky import (
    PAMIATKY,
    WIKIPEDIA as PAMIATKA_WIKI,
    MESTA as PAMIATKA_MESTA,
)
from memi_sk.categories.jedla import JEDLA, WIKIPEDIA as JEDLO_WIKI
from memi_sk.categories.zvierata import (
    ZVIERATA,
    WIKIPEDIA as ZVIERA_WIKI,
    LATINSKE as ZVIERA_LAT,
)
from memi_sk.categories.rastliny import (
    RASTLINY,
    WIKIPEDIA as RASTLINA_WIKI,
    LATINSKE as RASTLINA_LAT,
)
from memi_sk.categories.ludia import (
    HISTORICKE,
    MODERNE,
    SUCASNI,
    ALL as LUDIA_ALL,
    WIKIPEDIA as LUDIA_WIKI,
    OBDOBIA as LUDIA_OBDOBIA,
)


class KrajeProvider(CategoryProvider):
    key = "geografia:kraje"
    items = KRAJE
    override_name = True

    def get_image(self, item):
        wiki = KRAJ_WIKI.get(item, item)
        return images.get_wikipedia_image(wiki)


class MestaProvider(CategoryProvider):
    key = "geografia:mestá"
    items = MESTA
    override_name = True

    def get_image(self, item):
        wiki = MESTO_WIKI.get(item, item)
        return images.get_wikipedia_image(wiki)

    def get_tag(self, item):
        return MESTO_KRAJE.get(item)


class RiekyProvider(CategoryProvider):
    key = "geografia:rieky"
    items = RIEKY
    override_name = True

    def get_image(self, item):
        wiki = RIEKA_WIKI.get(item, item)
        return images.get_wikipedia_image(wiki)

    def get_tag(self, item):
        return RIEKA_DLZKY.get(item)


class PamiatkyProvider(CategoryProvider):
    key = "kultúra:pamiatky"
    items = PAMIATKY
    override_name = True

    def get_image(self, item):
        wiki = PAMIATKA_WIKI.get(item, item)
        return images.get_wikipedia_image(wiki)

    def get_tag(self, item):
        return PAMIATKA_MESTA.get(item)


class JedlaProvider(CategoryProvider):
    key = "kultúra:jedlá"
    items = JEDLA
    override_name = True

    def get_image(self, item):
        wiki = JEDLO_WIKI.get(item, item)
        return images.get_wikipedia_image(wiki)


class ZvierataProvider(CategoryProvider):
    key = "príroda:zvieratá"
    items = ZVIERATA
    override_name = True

    def get_image(self, item):
        wiki = ZVIERA_WIKI.get(item, item)
        return images.get_wikipedia_image(wiki)

    def get_tag(self, item):
        return ZVIERA_LAT.get(item)


class RastlinyProvider(CategoryProvider):
    key = "príroda:rastliny"
    items = RASTLINY
    override_name = True

    def get_image(self, item):
        wiki = RASTLINA_WIKI.get(item, item)
        return images.get_wikipedia_image(wiki)

    def get_tag(self, item):
        return RASTLINA_LAT.get(item)


class LudiaProvider(CategoryProvider):
    """All people across all eras."""
    key = "ľudia:všetci"
    items = LUDIA_ALL
    override_name = True

    def get_image(self, item):
        wiki = LUDIA_WIKI.get(item, item)
        return images.get_wikipedia_image(wiki)

    def get_tag(self, item):
        return LUDIA_OBDOBIA.get(item)


class LudiaHistorickeProvider(LudiaProvider):
    key = "ľudia:do roku 1918"
    items = HISTORICKE


class LudiaModerneProvider(LudiaProvider):
    key = "ľudia:20. storočie"
    items = MODERNE


class LudiaSucasniProvider(LudiaProvider):
    key = "ľudia:súčasnosť"
    items = SUCASNI


register(KrajeProvider())
register(MestaProvider())
register(RiekyProvider())
register(PamiatkyProvider())
register(JedlaProvider())
register(ZvierataProvider())
register(RastlinyProvider())
register(LudiaProvider())
register(LudiaHistorickeProvider())
register(LudiaModerneProvider())
register(LudiaSucasniProvider())
