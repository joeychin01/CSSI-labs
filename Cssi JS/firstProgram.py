print "Hello World!"
age = raw_input("Please insert your age:")
print age
if age > 10:
    print "shouldn't you be in school right now?"
elif age > 8:
    print "Go to school"
else:
    print age
def helloThere(name):
    print ("hello there %s" % name)
helloThere(raw_input("Insert your name:"))
