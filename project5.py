
List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

def split(x):
   even = []
   odd = []
   for i in x:
      if (i % 2 == 0):
         even.append(i)
      else:
         odd.append(i)
   print("list with even numbers:", even)
   print("list with odd numbers:", odd)
def verify():

    if List[0] == List[len(List)-1]:
        return True
    else:
        return False

print ("Checking if the  first and last number are equivalent: ", verify())
split(List)