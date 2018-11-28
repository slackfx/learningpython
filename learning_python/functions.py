def separator():
    #hars = "#"
    #or i in range(100):
    #   chars += "#"
    #rint(chars)
    print('#' * 100)

def keywordArguments(a, b, c):
    print(a, b, c, sep="; ")

keywordArguments(c = "c", a = "a", b = "b")

separator()

def minimum(*n):
    if n:
        mn = n[0]
        for value in n[1:]:
            if value < mn:
                mn = value
        print(mn)

minimum(1, 3, -7, 9)
minimum(1)
minimum()

separator()

# Variable positional arguments

def func(*args):
    print(args)

values = (1, 3, -7, 9)
func(values)
func(*values) # this will unpack the tuple for the variable arguments

separator()

# Variable keyword arguments

def func2(**kwargs):
    print(kwargs)

func2(a=1, b=42)
func2(**{'a': 1, 'b': 42})
func2(**dict(a=1, b=42))

def connect(**options):
    conn_params = {
        'host': options.get('host', '127.0.0.1'),
        'port': options.get('port', 3306),
        'user': options.get('user', 'root'),
        'pwd': options.get('pwd', 'toor')
    }
    print(conn_params)

connect()
connect(host='slackvm1', port=1521)

separator()

# Python 3 only: Keyword-only arguments

def kwo(*a, b):
    print(a, b)

kwo(1, 2, 3, b=7)
kwo(b=4)
# kwo(1, 2) # Error

def kwo2(a, b=42, *, c):
    print(a, b, c)

kwo2(3, b=7, c=99)
kwo2(3, c=13)
# kwo2(3, 23) # Error

separator()

def func3(a, b, c=7, *args, **kwargs):
    print('a, b, c: ', a, b, c)
    print('args: ', args)
    print('kwargs: ', kwargs)

func3(1, 2, 3, *(5, 7, 9), **{'A': 'a', 'B': 'b'})
separator()
func3(1, 2, 3, 5, 7, 9, A='a', B='b')

separator()

# Mutables objects as default values

def func4(a=[], b={}):
    print(a)
    print(b)
    print('#' * 12)
    a.append(len(a))
    b[len(a)] = len(a)

func4()
func4()
func4()

separator()

def func5(a=[], b={}):
    print(a)
    print(b)
    print('#' * 12)
    a.append(len(a))
    b[len(a)] = len(a)

func5()
func5(a=[1, 2, 3], b={'B': 1})
func5()

separator()

# return none

def none():
    pass

none()
a = none()
print(a)

