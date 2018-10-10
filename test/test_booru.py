import requests
from booru import Booru


def test_booru_url_parsing():
    assert Booru(
        "http://safebooru.org/index.php?page=dapi&s=post&q=index&pid=1&limit=5&json=1&tags=1boy"
    ).url == "https://safebooru.org"

    assert Booru("safebooru.org", https=False).url == "http://safebooru.org"

    assert Booru("//gelbooru.com").url == "https://gelbooru.com"


def test_request_most_recent():

    tags = "1girl"

    booru = Booru("gelbooru.com")

    booru_manager = booru.request_manager

    img = booru_manager.most_recent(tags=tags)

    print(img.tags)

    assert tags in img.tags


def test_image_url_gen():

    tags = "bowsette"

    gbooru = Booru("gelbooru.com")
    gbooru_manager = gbooru.request_manager
    gimg = gbooru_manager.most_recent(tags=tags)
    assert requests.get(gbooru.generate_image_url(gimg)).status_code == 200

    sbooru = Booru("safebooru.org")
    sbooru_manager = sbooru.request_manager
    simg = sbooru_manager.most_recent(tags=tags)
    assert requests.get(sbooru.generate_image_url(simg)).status_code == 200

    assert requests.get(gbooru.generate_image_url(simg)).status_code != 200


def test_mandatory_tags():

    tags = "bowsette"

    mandatory_tags = ["1boy", "1girl"]

    booru = Booru("safebooru.org", mandatory_tags=mandatory_tags)
    booru_manager = booru.request_manager

    img = booru_manager.most_recent(tags=tags)

    print(img.tags)

    for tag in mandatory_tags:
        assert tag in img.tags


def test_ignored_tags():

    tags = "bowsette 1boy"

    ignored_tags = ["bowsette"]

    booru = Booru("safebooru.org", ignored_tags=ignored_tags)
    booru_manager = booru.request_manager

    img = booru_manager.most_recent(tags=tags)

    print(img.tags)

    for tag in ignored_tags:
        assert tag not in img.tags


def test_range():
	
	tags = "bowsette"

	br = Booru("safebooru.org")
	manager = br.request_manager

	imgs = manager.range(tags, limit=5)

	assert len(imgs) is 5

	for img in imgs:
		assert tags in img.tags
