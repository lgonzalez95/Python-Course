class Course:
    def __init__(self, name, duration, *books):
        self.name = name
        self.duration = duration
        self.books = [self.Book(x) for x in books]

    def show_details(self):
        books = [x.title for x in self.books]
        print('Course name: ' + self.name)
        print('Course duration: ' + self.duration)
        print('Books: ' + ', '.join(books))

    class Book:
        def __init__(self, title):
            self.title = title

        def __str__(self):
            print('Book name: ' + self.title)


c = Course('Intro to python', '50 hours', 'Book 1', 'Book 2')
c.show_details()
