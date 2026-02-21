from hello_world import hello

x = "awesome"


def myfunc():
    global x
    x = "Mayank Srivastava"
    print("Python is " + x)
    hello("This is hello")


myfunc()
