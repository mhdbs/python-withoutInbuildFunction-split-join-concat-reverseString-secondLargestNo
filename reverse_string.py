def reverse_string(s): 
    if len(s) == 0: 
        return s 
    else: 
        return reverse_string(s[1:]) + s[0]

s = "String"
  
print ("Reversed string is : ") 
print (reverse_string(s))