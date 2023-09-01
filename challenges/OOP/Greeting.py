class English:
    def greeting(self):
        print("Hello")


class French:
    def greeting(self):
        print("Bonjour")


class Spanish:
    def greeting(self):
        print("Hola")


def greet(language):
    language.greeting()


s = Spanish()
f = French()
greet(s)
print()
greet(f)
