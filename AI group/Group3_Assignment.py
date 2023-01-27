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
            
            for ch in string1:
                if ch.isspace():
                    continue
                if ch in dic:
                    dic[ch] = dic[ch]+1
                else:
                    dic[ch] = 1
            sorted_chars = sorted(
                dic.items(), key=lambda x: x[1], reverse=True)
            sorted_dic = dict(sorted_chars)
            print("character", "        ", "Frequency")
            for key in sorted_dic:
                print("  ", key, "---------------->", sorted_dic[key])
            print()
            print("Top five frequently occuring characters")
            print("character", "        ", "Frequency")
            i = 1
