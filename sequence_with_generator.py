def reg_number(upto):
    for i in range(26):
        for j in range(26):
            for k in range(26):
                for l in range(upto):
                    yield ("{}{}{}-{:03d}".format(chr(i + ord('A')), chr(j + ord('A')), chr(k + ord('A')), l))

for number in reg_number(5):
  print(number)