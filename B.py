#!/usr/bin/python3


class test:
    def __init__(self, keyword):
        self.keyword = 'mr.' + keyword + 'ed'
    def prints(self, s):
        print(test.inner(self) , " and " , s)
    def inner(self):
        return 'hhasHellos' , self.keyword

