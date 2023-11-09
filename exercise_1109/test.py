# demo is the function name
def demo(name, age):
    # print value
    print(name, age)

# call function
demo("Ben", 25)

def func1(*args):
    for i in args:
        print(i)

func1(20, 40, 60)
func1(80, 100)

def calculation(a, b):
    return a + b, a - b

# get result in tuple format
# unpack tuple
add, sub = calculation(40, 10)
print(add, sub)

def show_employee(name,salary=80000):
    print("Name:",name,"salary:",salary)
show_employee("Ben",12000)
show_employee("Jessa")
show_employee("hu")