import re
print("Enter 1 for English")
print("Enter 2 for Amharic")
print("Enter 3 to Exit")
choice = int(input())
match choice:
    case 1:
        file = open("Group3.txt", "r")
        string = file.read()
        newstring = re.sub('[^a-zA-Z0-9\n\\s]', '', string)
        print(newstring)
        file.close()
        file1 = open("Group3.txt", "w")
        file1.write(newstring)
        file1.close()

        def charfreq():
            dic = {}
            file2 = open("Group3.txt", "r")
            string1 = file2.read()
