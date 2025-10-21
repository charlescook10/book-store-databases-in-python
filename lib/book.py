class Book:
    def __init__(self, id, title, author_name):
        self.id = id
        self.title = title
        self.author_name = author_name
    
    def __repr__(self):
        return f"{self.id} - {self.title} - {self.author_name}"
    
    def __eq__(self, value):
        return self.__dict__ == value.__dict__