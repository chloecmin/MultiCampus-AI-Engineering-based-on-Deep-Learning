file = open("../txt/gugudan.txt", "w")

for i in range(2, 10):
    for j in range(1, 10):
        file.write("{} x {} = {}\n".format(i, j, i*j))

file.close()
