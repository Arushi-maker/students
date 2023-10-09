---
toc: true
comments: false
layout: post
title: Jupyter Notebook
<p style="padding: 20px;">This is a paragraph with padding.</p>
description: Jupyter Notebook is another way to edit live code on my browser. It is a tool like VsCode. I created my own quiz about myself. After speaking with Mr.Mortensen I learned that I can not run this on HTML code in my blog. However, the code still runs in my terminal and I also checked with ChatGPT to analyze it.
type: tangibles
courses: { csp: {week: 0}}
---
---

    ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~

# Quiz About Me
Here's the code for a quiz I made after learning from the files on Jupyter Notebook.

```
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
```
<!-- <img src="images/IMG_3595.jpg" alt = "drawing" width="200">
<img src="images/IMG_3595.jpg" alt = "drawing" width="200"> -->