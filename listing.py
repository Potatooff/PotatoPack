f = open("list.txt", "a")
f.write("Chathistory_2\n")
f.close()


f = open("list.txt", "r")

for lines in f:
    print(lines)