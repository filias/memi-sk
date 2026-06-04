"""Slovak category providers."""

from memi_engine import CategoryProvider, register
from memi_engine import images

from memi_sk.categories.regions import REGIONS, WIKIPEDIA as REGION_WIKI
from memi_sk.categories.cities import (
    CITIES,
    WIKIPEDIA as CITY_WIKI,
    REGIONS as CITY_REGIONS,
)
from memi_sk.categories.rivers import (
    RIVERS,
    WIKIPEDIA as RIVER_WIKI,
    LENGTHS as RIVER_LENGTHS,
)
from memi_sk.categories.landmarks import (
    LANDMARKS,
    WIKIPEDIA as LANDMARK_WIKI,
    CITIES as LANDMARK_CITIES,
)
from memi_sk.categories.dishes import DISHES, WIKIPEDIA as DISH_WIKI
from memi_sk.categories.animals import (
    ANIMALS,
    WIKIPEDIA as ANIMAL_WIKI,
    LATIN_NAMES as ANIMAL_LATIN,
)
from memi_sk.categories.plants import (
    PLANTS,
    WIKIPEDIA as PLANT_WIKI,
    LATIN_NAMES as PLANT_LATIN,
)
from memi_sk.categories.people import (
    HISTORICAL,
    MODERN,
    CONTEMPORARY,
    ALL as PEOPLE_ALL,
    WIKIPEDIA as PEOPLE_WIKI,
    PERIODS as PEOPLE_PERIODS,
)


class RegionsProvider(CategoryProvider):
    key = "geografia:kraje"
    items = REGIONS
    override_name = True

    def get_image(self, item):
        wiki = REGION_WIKI.get(item, item)
        return images.get_wikipedia_image(wiki)


class CitiesProvider(CategoryProvider):
    key = "geografia:mestá"
    items = CITIES
    override_name = True

    def get_image(self, item):
        wiki = CITY_WIKI.get(item, item)
        return images.get_wikipedia_image(wiki)

    def get_tag(self, item):
        return CITY_REGIONS.get(item)


class RiversProvider(CategoryProvider):
    key = "geografia:rieky"
    items = RIVERS
    override_name = True

    def get_image(self, item):
        wiki = RIVER_WIKI.get(item, item)
        return images.get_wikipedia_image(wiki)

    def get_tag(self, item):
        return RIVER_LENGTHS.get(item)


class LandmarksProvider(CategoryProvider):
    key = "kultúra:pamiatky"
    items = LANDMARKS
    override_name = True

    def get_image(self, item):
        wiki = LANDMARK_WIKI.get(item, item)
        return images.get_wikipedia_image(wiki)

    def get_tag(self, item):
        return LANDMARK_CITIES.get(item)


class DishesProvider(CategoryProvider):
    key = "kultúra:jedlá"
    items = DISHES
    override_name = True

    def get_image(self, item):
        wiki = DISH_WIKI.get(item, item)
        return images.get_wikipedia_image(wiki)


class AnimalsProvider(CategoryProvider):
    key = "príroda:zvieratá"
    items = ANIMALS
    override_name = True

    def get_image(self, item):
        wiki = ANIMAL_WIKI.get(item, item)
        return images.get_wikipedia_image(wiki)

    def get_tag(self, item):
        return ANIMAL_LATIN.get(item)


class PlantsProvider(CategoryProvider):
    key = "príroda:rastliny"
    items = PLANTS
    override_name = True

    def get_image(self, item):
        wiki = PLANT_WIKI.get(item, item)
        return images.get_wikipedia_image(wiki)

    def get_tag(self, item):
        return PLANT_LATIN.get(item)


class PeopleProvider(CategoryProvider):
    """All people across all eras."""
    key = "ľudia:všetci"
    items = PEOPLE_ALL
    override_name = True

    def get_image(self, item):
        wiki = PEOPLE_WIKI.get(item, item)
        return images.get_wikipedia_image(wiki)

    def get_tag(self, item):
        return PEOPLE_PERIODS.get(item)


class PeopleHistoricalProvider(PeopleProvider):
    key = "ľudia:do roku 1918"
    items = HISTORICAL


class PeopleModernProvider(PeopleProvider):
    key = "ľudia:20. storočie"
    items = MODERN


class PeopleContemporaryProvider(PeopleProvider):
    key = "ľudia:súčasnosť"
    items = CONTEMPORARY


register(RegionsProvider())
register(CitiesProvider())
register(RiversProvider())
register(LandmarksProvider())
register(DishesProvider())
register(AnimalsProvider())
register(PlantsProvider())
register(PeopleProvider())
register(PeopleHistoricalProvider())
register(PeopleModernProvider())
register(PeopleContemporaryProvider())
