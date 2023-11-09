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
show_employee("Hu")

# outer function
def outer_fun(a, b):
    square = a ** 2

    # inner function
    def addition(a, b):
        return a + b

    # call inner function from outer function
    add = addition(a, b)
    # add 5 to the result
    return add + 5

result = outer_fun(5, 10)
print(result)

def addition(num):
    if num:
        # call same function by reducing number by 1
        return num + addition(num - 1)
    else:
        return 0

res = addition(10)
print(res)

def display_student(name, age):
    print(name, age)

# call using original name
display_student("Emma", 26)

# assign new name
showStudent = display_student
# call using new name
showStudent("Emma", 26)

print(list(range(4,30,2)))

x = [4,6,8,24,12,2]
print(max(x))