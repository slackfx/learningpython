class Book:
    def __init__(self, title, publisher, pages):
        self.title = title
        self.publisher = publisher
        self.pages = pages

class Ebook(Book):
    def __init__(self, title, publisher, pages, format_):
        #Book.__init__(self, title, publisher, pages)
        super().__init__(title, publisher, pages)
        # or
        # super(Ebook, self).__init__(title, publisher, pages)
        self.format_ = format_
