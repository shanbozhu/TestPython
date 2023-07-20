import re, os


def alter(file, old_str, new_str):
    str = file + ".bak"
    print(str)
    with open(file, "r", encoding="utf-8") as f1, open("%s.bak" % file, "w", encoding="utf-8") as f2:
        for line in f1:
            print(line, end="")
            f2.write(re.sub(old_str, new_str, line))
    os.remove(file)
    os.rename("%s.bak" % file, file)

alter("my_file.txt", "aa", "password")