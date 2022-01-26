#exercise 3
import pdb
#pdb.set_trace()

def is_prime(x):
    if x < 2:
        result = False
        return result
    elif x == 2 or x == 3:
        result = True
        return result
    else:
        for n in range(2, x-1):
            if (x % n) == 0:
                result = False
                return result
        else:
            result = True
            return result


Uinput = int(input("Enter a number to check if its Prime: "))
print ("Is " + str(Uinput) + " a prime number: " + str(is_prime(Uinput)))

#exercise 4

item_list = ["Burger", "Hotdog", "Bun", "Ketchup", "Cheese"]
n = 0

while n < 5:
    for i in item_list:
        print(i)
    n = n + 1

print (item_list[4])