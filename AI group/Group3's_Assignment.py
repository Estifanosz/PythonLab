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
            for key in sorted_dic:
                if i <= 5:
                    print("  ", key, "---------------->", sorted_dic[key])
                i = i+1
        charfreq()

        def stat_info():
            file3 = open("Group3.txt", "r")
            stringc = file3.read()
            number_char = 0
            number_lines = 0
            number_words = 0
            file3.seek(0)
            for line in file3:
                word_list = line.split()
                number_lines += 1
                number_words += len(word_list)
            stringn = re.sub('[^a-zA-Z0-9]', '', stringc)
            number_char += len(stringn)
            print("Total number of lines is = ", number_lines)
            print("Total number of words is = ", number_words)
            print("Total number of characters is = ", number_char)
            file3.close()
        stat_info()
    case 2:
        afile = open("Group3Amharic.txt", "r", encoding="UTF-8")
        Amharic_String = afile.read()
        newA_string = re.sub('[^\u1200-\u137F\n\\s]', '', Amharic_String)
        afile.close()
        file1 = open("Group3Amharic.txt", "w", encoding="UTF-8")
        file1.write(newA_string)
        file1.close()

        def charfreq():
            dic = {}
            file2 = open("Group3Amharic.txt", "r", encoding="UTF-8")
            string1 = file2.read()

            for ch in string1:
                if ch.isspace() or (not (0x1200 <= ord(ch) <= 0x137F)):
                    continue
                if ch in dic:
                    dic[ch] = dic[ch]+1
                else:
                    dic[ch] = 1
            sorted_chars = sorted(
                dic.items(), key=lambda x: x[1], reverse=True)
            sorted_dic = dict(sorted_chars)
            print("characters", "           ", "Frequency")
            for key in sorted_dic:
                print("  ", key, "---------------->", sorted_dic[key])
            print()
            print("Top five frequently occuring characters")
            print("Characters", "           ", "Frequency")
            i = 1    
            for key in sorted_dic:
                if i <= 5:
                    print("  ", key, "---------------->", sorted_dic[key])
            i = i+1
        charfreq()

        def stat_info():
            file3 = open("Group3Amharic.txt", "r", encoding="UTF-8")
            stringc = file3.read()
            number_char = 0
            number_lines = 0
            number_words = 0
            file3.seek(0)
            for line in file3:
                word_list = line.split()
                number_lines += 1
                number_words += len(word_list)
            stringn = re.sub('[^\u1200-\u137F]', '', stringc)
            number_char += len(stringn)
            print("Total number of Lines =", number_lines)
            print("Total number of Words =", number_words)
            print("Total number of characters =", number_char)
            file3.close()
        stat_info()

    case 3:
        exit(0)
    case _:
        print("Invalid key, Please try Again!")
