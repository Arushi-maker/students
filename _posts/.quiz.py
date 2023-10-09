
import getpass, sys

def question_with_response(prompt):
    print("Question: " + prompt)
    msg = input()
    return msg

questions = 3
correct = 0

print('Hello, ' + getpass.getuser() + " running " + sys.executable)
print("You will be asked " + str(questions) + " questions.")
print("Are you ready to take a test?")

rsp = question_with_response("What period # does Arushi have Comp Sci?")
if rsp == "2":
    print(rsp + " is correct!")
    correct += 1
else:
    print(rsp + " is incorrect!")

rsp = question_with_response("What is Arushi's quote of the day?")
if rsp == "This will all make perfect sense one day":
    print(rsp + " is correct!")
    correct += 1
else:
    print(rsp + " is incorrect!")

rsp = question_with_response("Is Arushi your friend?")
if rsp == "yes":
    print(rsp + " is correct!")
    correct += 1
else:
    print(rsp + " is incorrect!")

print(getpass.getuser() + " you scored " + str(correct) +"/" + str(questions))
