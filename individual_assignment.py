def char_frequency(string):
 # Create a dictionary to store the frequency count
    count={}
    for char in string:
        if char in count:
          count[char]=count[char]+1
        else:
          count[char]=1
# Print the frequency count of each character
    for key in count:
        print(" There are ",count[key],"  ",key)    
string = input("Enter a string: ")
char_frequency(string)