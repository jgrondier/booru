import requests
from abc import ABC, abstractmethod
from .image import Image


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
    def most_recent(self, tags):
        pass

    def __build_tags__(self, tags):

        tmp = [x for x in tags.split(" ") if "-{}".format(x) not in self.ignored_tags]

        tmp = list(set(tmp + self.mandatory_tags + self.ignored_tags))

        return " ".join(tmp)



class GelBooru2RequestManager(RequestManager):

    API_PARAMS = {
        "page": "dapi",
        "s": "post",
        "q": "index",
        "json": 1
    }


    def __init__(self, url, rating, mandatory_tags, ignored_tags):

        super(GelBooru2RequestManager, self).__init__(rating, mandatory_tags, ignored_tags)

        self.url = "/".join([url, "index.php"])

    def most_recent(self, tags=''):

        payload = self.API_PARAMS.copy()

        payload["tags"] = self.__build_tags__(tags)
        payload["limit"] = 1

        rjson = requests.get(self.url, params=payload).json()[0]

        rjson["id_"] = rjson.pop("id")
        rjson["hash_"] = rjson.pop("hash")

        return Image(**rjson)
