import random
def shifr():
    shifr = ''
    first_fild = random.randint(3,20)
    print("Число в первом поле : ",first_fild)
    for i in range(1,first_fild):
        for j in range(i,first_fild):
            if i!=j:
                if first_fild %(i+j)==0:
                    pair_of_numbers = str(i)+str(j)
                    shifr+=pair_of_numbers
    return shifr
print(shifr())





