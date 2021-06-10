def foo(p, q, *args, **kwargs):
    print("p = {0}, q = {1}".format(p, q))
    for i in range(len(args)):
        print("args[{0}] = {1}".format(str(i), str(args[i])))
    
    for keyword, value in kwargs.items():
        print("keyword, value " + str((keyword, value)))


args = (2.71, [6, 28])
kwargs = {'name': 'cfg', 'rank': 1}

print("With asterisk...")
foo(1, 'euler', *args, **kwargs)

# Without asterisk (unboxing), kwargs is also considered part of args
# args sends 1 arg (the tuple) and kwargs sends another (the dict)
# foo receives 2 + 2 args
# With asterisk, all the args are opened up
# foo receives 2 + 4 args
# args sends 2 args (individual elements of tuple) and kwargs sends 2 args
# (2 elements of its dictvim )
print("Without asterisk...")
foo(1, 'euler', args, kwargs)
