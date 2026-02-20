from hello_world import hello

x = "awesome"


def myfunc():
    global x
    x = "fantastic"
    print("Python is " + x)
    hello("This is hello")


myfunc()
