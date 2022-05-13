#vo
class Board:
    def __init__(self, num:int = 0, writer:str=None, w_date=None, title:str=None, content:str=None):
        self.num = num
        self.writer = writer
        self.w_date = w_date
        self.title = title
        self.content = content

    def __str__(self):
        return 'num:' + str(self.num) + ' / writer:' + self.writer + ' / w_date:' + str(self.w_date) + \
               ' / title:' + self.title + ' / content:' + self.content