class Post:
    def __init__(
        self, post_id, post_title, post_subtitle, body, img_url, author, published_date
    ):
        self.id = post_id
        self.title = post_title
        self.subtitle = post_subtitle
        self.author = author
        self.date = published_date
        self.body = body
        self.img_url = img_url
