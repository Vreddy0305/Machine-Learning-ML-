def vcount(input_string):
    vowels = "aeiouAEIOU"
    vcount = 0
    ccount = 0
    for char in input_string:
        if char.isalpha():
            if char in vowels:
                vcount += 1
            else:
                ccount += 1
    return vcount, ccount

input = input("Enter a string: ")
vcount, ccount = vcount(input)
print(f"Vowels: {vcount}, Consonants: {ccount}")