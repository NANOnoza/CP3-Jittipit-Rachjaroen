"""
     *
    ***
   *****
  *******
 *********
"""
Number_input = int(input("Please Enter The Number: "))
for Number in range(Number_input):
 print(" " * (Number_input - Number) + "*" * (Number*2+1))
