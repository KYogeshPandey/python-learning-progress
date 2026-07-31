def greet (fx):
    def mfx(*args, **kwargs):
        print("Good morning")
        fx(*args, **kwargs)
        print("thanks for using this function")
    return mfx

# @greet
def hello():
    print("Hello world!")

@greet
def add(a,b):
    print(f"The sum of {a} and {b} is {a+b}")

add(4,5)

greet(hello())