s="Tops Technologies"
print(s)
print("----------------------------")
'capitalize converts only first letter of an entire string(no matter the space) to capital'
print(s.capitalize())
print("----------------------------")
'casefold converts all letters to lowercase , lower does the same'
print(s.casefold())
print(s.lower())
print("----------------------------")
'upper converts all letters to uppercase'
print(s.upper())
print("----------------------------")
'swapcase converts lowercase letters to uppercase and uppercase letters to lowercase'
print(s.swapcase())
print("----------------------------")
' title converts any words first letter to Uppercase'
print("blah blah".title())
print(s.title())
print("----------------------------")
'Checks for lower and upper case'
print("blah".islower())
print("BLAH".isupper())
print("----------------------------")
'Checks if String has space'
print(" ".isspace())
print("----------------------------")
'isalnum checks if String has either alphabetic characters , numeric characters or both'
print("tops123".isalnum())
print("----------------------------")
'But as alnum function checks for either alpha or num , returns true if  even one is found'
print("tops".isalnum())
print("123".isalnum())
print("----------------------------")
'isalnum returns false if a space is found in String'
print("tops 123".isalnum())
print("----------------------------")
'isnumeric checks if String has only numbers'
print("123".isnumeric())
print("----------------------------")
'isalpha checks if a String has only alphabetic characters'
print("tops".isalpha())
print("----------------------------")
'center has 2 arguments . center takes first argument of how many spaces to occupy , second argument as to what to put beside the center (which is the String)'
print(s.center(40,"*"))

