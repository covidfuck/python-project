class Book:
    title = ''
    author = ''
    price = 0

    def __str__(self):
        return f'{self.title} / {self.author} / {self.price}원'


a = Book()
b = Book()
a.title = '제목1'
a.author = '홍길동'
a.price = 1000

b.title = '제목2'
b.author = '고길동'
b.price = 2000

print(a)
print(b)