def likes(names):
    l = names
    str_main = ""
    str_s = ""
    str_end = "{} like{} this"

    if len(l) == 0:
        str_main = "no one"
        str_s = "s"
    elif len(l) == 1:
        str_main = l[0]
        str_s = "s"
    elif len(l) == 2:
        str_main = l[0] + " and " + l[1]
    elif len(l) == 3:
        str_main = "{}"l[0] + ", " + l[1] + " and " + l[2]
    else:
        str_main = "{}, {} and {} others".format(l[0], l[1], str(len(l) - 2))

    return str_end.format(str_main, str_s)

print(likes([]))
