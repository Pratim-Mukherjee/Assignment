



my_str =input('enter a string')
print("Reversed string: ", my_str[::-1])
my_str = my_str.casefold()

rev_str = reversed(my_str)

if list(my_str) == list(rev_str):
   print("The string is a palindrome.")
   strn = my_str
   print(" ".join(strn))

else:
   print("The string is not a palindrome.")
   strn = my_str
   print(" ".join(strn))





