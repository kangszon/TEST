x = open('fintest.txt', 'r')
a = x.read()
if input() in a:
    print("True")
x.close()