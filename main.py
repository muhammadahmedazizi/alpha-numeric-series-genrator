# https://www.digitalocean.com/community/tutorials/python-ord-chr

for i in range(26):
    for j in range(26):
        for k in range(26):
            for l in range(9):
                print("{}{}{}-{:03d}".format(chr(i + ord('A')), chr(j + ord('A')), chr(k + ord('A')), l))


