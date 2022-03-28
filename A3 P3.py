string = input ("Enter String : ")
upp = low = 0
for letter in string :
   if ord(letter) in range (65,91):
       upp = upp + 1
   elif ord(letter) in range (97,123):
       low = low + 1
print("upper-case letter are : ",upp,"\nlower-case letter are : ",low)