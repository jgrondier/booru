import requests
from abc import ABC, abstractmethod
from .image import Image
import random as rnd


class RequestManager(ABC):

    API_PARAMS = {
        "page": "dapi",
        "s": "post",
        "q": "index",
        "json": 1
    }

    def __init__(self, rating, mandatory_tags, ignored_tags):
        self.mandatory_tags = mandatory_tags
        self.ignored_tags = ignored_tags
        self.rating = rating

    @abstractmethod
    def most_recent(self, tags, **additional_params):
        pass

    @abstractmethod
    def random(self, tags, limit, **additional_params):
        pass

    def __build_tags__(self, tags):

        tmp = [x for x in tags.split(
            " ") if "-{}".format(x) not in self.ignored_tags]

        tmp = list(set(tmp + self.mandatory_tags + self.ignored_tags))

        return " ".join(tmp)

    def __init_payload__(self, additional_params):
        pl = self.API_PARAMS.copy()
        pl.update(additional_params)
        return pl


class GelBooru2RequestManager(RequestManager):

    def __init__(self, url, rating, mandatory_tags, ignored_tags):

        super(GelBooru2RequestManager, self).__init__(
            rating, mandatory_tags, ignored_tags)

        self.url = "/".join([url, "index.php"])

    def __range__(self, tags, limit, additional_params):
        payload = self.API_PARAMS.copy()

        payload["tags"] = self.__build_tags__(tags)
        payload["limit"] = limit

        try:
            rjson = requests.get(self.url, params=payload).json()
        except ConnectionError as e:
            print("The Booru could not be reached.")
            raise e
        except ValueError as e:
            print("No json could be retrieved from the Booru.")
            raise e

        if len(rjson) < 1:
            raise ValueError(
                "No result could be find corresponding to the tags")

        for i in rjson:
            i["id_"] = i.pop("id")
            i["hash_"] = i.pop("hash")

        return rjson

    def most_recent(self, tags='', **additional_params):

        selected = self.__range__(tags, 1, additional_params)[0]

        return Image(**selected)

    def range(self, tags='', limit=500, **additional_params):

        r = self.__range__(tags, limit, additional_params)

        return [Image(**selected) for selected in r]

    def random(self, tags='', limit=500, **additional_params):

        selected = rnd.choice(self.__range__(tags, limit, additional_params))

        return Image(**selected)
