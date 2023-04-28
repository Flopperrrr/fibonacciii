n_terms = int(input("Enter a number : "))

n_1 = 0
n_2 = 1
count= 0
if n_terms <= 0 :
    print("Please enter a positive number!")
if n_terms == 1:
    print(n_1)
else:
    while count < n_terms:
        print(n_1)
        nth = n_1 + n_2
        n_1 = n_2
        n_2 = nth
        count += 1

