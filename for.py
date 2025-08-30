# abhi = [3, 5, 4, 7, 8]
# print(abhi[0:2])

# for i in range(12):
#     if (i == 10):
#         break
#     print(5*(i+1))
    
# ----------------------------------------
# lst = [i for i in range(10)]
# print(lst)
# if 9 in lst:
#     print("yes it is present")
# --------------------------------
# def factorial(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n*factorial(n-1)

# print(factorial(5))

# pintu = {}
# print(type(pintu))
# --------------------------------
# info = {'name':'pintu', 'age':19, 'gender':'male', 'eligable':True}

# # for key , value in info.items():
# #     print(key)
# for key  in info.keys():
#     print(key)
# -----------------------------
# a = input("Enter your Table number")
# print(f"The multiplication of {a} is ")

# try:
#     for i in range(1,11):
#         print(f"{int(a)}*{i}={int(a)*i}")
# except:
#     print("Sorry it is not working")
# ----------------------------------
# try:
#     num = int(input("Enter your Random number: "))
#     print(f"Your Number is {num}")
# except ValueError:
#     print("ValueError is occuring")
# except IndexError:
#     print("this is index base error")

# ----------------------------------------------

a = int(input("Enter your Number Between 5 and 9: "))

if (a<5 or a>9):
    raise ValueError ("Value should be between 5 and 9")
else:
    print(f"Thanks your correct choosed number is {a}")