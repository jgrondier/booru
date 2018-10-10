from urllib.parse import urlparse, ParseResult, urljoin
from .request_manager import GelBooru2RequestManager
from .boards import Boards


class Booru(object):

    def __init__(self, url, type=Boards.GELBOORU2, https=True, rating=None, mandatory_tags=None, ignored_tags=None):

        parse = urlparse(url)

        scheme = "https" if https else "http"

        if parse.netloc is not '':
            netloc = parse.netloc
        else:
            netloc = parse.path

        self.url = ParseResult(scheme=scheme, netloc=netloc, params='',
                               query='', fragment='', path='').geturl()

        if mandatory_tags is None:
            self.mandatory_tags = []
        else:
            self.mandatory_tags = mandatory_tags

        if ignored_tags is None:
            self.ignored_tags = []
        else:
            self.ignored_tags = [t if t.startswith(
                "-") else "-{}".format(t) for t in ignored_tags]

        self.rating = rating

        if type is not Boards.GELBOORU2:
            raise ValueError("Currently, only Gelbooru 2 is supported !")

        self.request_manager = GelBooru2RequestManager(
            url=self.url, rating=rating, mandatory_tags=self.mandatory_tags, ignored_tags=self.ignored_tags)

    def generate_image_url(self, image, url_attribute=None):

        if url_attribute is not None and hasattr(image, url_attribute):
            return getattr(image, url_attribute)

        return "/".join([self.url, "images", image.directory, image.image])
