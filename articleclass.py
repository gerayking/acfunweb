import time


class user:
    userId: int
    username: str

    def __init__(self, userId, username):
        self.userId = userId
        self.username = username


class article:
    commentCount = 0
    title: str
    author: user
    readCount: int
    date: str
    id: int


    def __init__(self, commentCount=0, title=None, author=None, readCount=0, date=None, id=0):
        self.commentCount = commentCount
        self.title = title
        self.author = author
        self.readCount = readCount
        self.date = date
        self.id = id
