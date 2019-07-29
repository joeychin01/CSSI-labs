print("Welcome to this Mad Libs!")
noun1 = raw_input("Please enter a singular noun: ")
adj1 = raw_input("please enter an adjective: ")
noun2 = raw_input("Please enter another singular noun: ")
verb1 = raw_input("Please enter a verb")
print(
    "The %s jumped over a %s %s.  Then the %s decided to stop being so %s and take up a hobby: %s" % (noun1, adj1, noun2, noun2, adj1, verb1+"ing")
)
