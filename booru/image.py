class Image(object):

    def __init__(self, id_, image, directory, owner, rating, score, tags, height=0, width=0, hash_=None,
                 change=0, sample=False, sample_height=0, sample_width=0, parent_id=0, **kwargs):


        self.id_ = id_
        self.image = image
        self.directory = directory
        self.owner = owner
        self.rating = rating
        self.score = score
        self.tags = tags
        self.height = height
        self.width = width
        self.hash_ = hash_
        self.change = change
        self.sample = sample
        self.sample_height = sample_height
        self.sample_width = sample_width
        self.parent_id = parent_id

        self.__dict__.update(kwargs)