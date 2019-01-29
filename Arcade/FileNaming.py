""""""
"""
You are given an array of desired filenames in the order of their creation. Since two files cannot have equal names, 
the one which comes later will have an addition to its name in a form of (k), where k is the smallest positive integer 
such that the obtained name is not used yet.

Return an array of names that will be given to the files.

Example

For names = ["doc", "doc", "image", "doc(1)", "doc"], the output should be
fileNaming(names) = ["doc", "doc(1)", "image", "doc(1)(1)", "doc(2)"].
"""


def fileNaming(names):
    renamed = []
    s = set()
    for f in names:
        if f not in s:
            s.add(f)
            renamed.append(f)
        else:
            count = 1
            flag = True
            while flag:
                v = f+'('+str(count)+')'
                if v not in s:
                    s.add(v)
                    renamed.append(v)
                    flag = False
                else:
                    count+=1

    return renamed


names = ["doc", "doc", "image", "doc(1)", "doc"]
#       ["doc", "doc(1)", "image", "doc(1)(1)", "doc(2)"]
print(names)
print(fileNaming(names))

names = ["a(1)", "a(6)", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"]
#       ["a(1)", "a(6)", "a", "a(2)", "a(3)", "a(4)", "a(5)", "a(7)", "a(8)", "a(9)",  "a(10)",  "a(11)"]
print(names)
print(fileNaming(names))

names = ["dd", "dd(1)", "dd(2)", "dd", "dd(1)", "dd(1)(2)",  "dd(1)(1)", "dd",  "dd(1)"]
#       ["dd", "dd(1)", "dd(2)", "dd(3)", "dd(1)(1)", "dd(1)(2)", "dd(1)(1)(1)", "dd(4)", "dd(1)(3)"]
print(names)
print(fileNaming(names))



