---
layout: default
title: Student Blog
---


# Welcome to My Blog!
Hi, my name is Arushi Pandey! I am 15 years old and I am currently a sophmore at Del Norte HS. I am an Asian-American living in San Diego, CA. Here are a few of my interests.

## Quote of the Day!
<mark>"This will all make perfect sense one day!" <mark> 

## Hobbies/Schedule:
- Playing and Creating Music 
- Water Polo and Swim for HS
- Volunteering 
- Trying New Things
- Shopping
- Watching Netflix and Youtube
- Spending time with Friends and Family

|              My School Schedule:      
| Period 1: Intro to Finance 1|
| Period 2: AP Computer Science|
| Period 3: AP Chemistry|
| Period 4: Honors Humanities 1|
| Period 5: AP Calculus 1|


I love my tools! VsCode is my bestfriend it helps me write amazing codes and helped me help you reach this blog. I love my other tools, such as GitHub. GitHub helps me store and manage my code!

## Drawing of My Life:

<img src="images/IMG_3595.jpg" alt = "drawing" width="200">

## The Plan      
      
      Monday August 21st: 
      1) Finish Installation
      2) Begin working on Blog
      3) Add Introduction to the Blog
      
      Tuesday August 22nd:
      1) Add more things about me (Schedule/Hobby)
      2) Add image I drew Last week
      3) Continue adding hacks
      4) Write out Planning for Blog
      
      Wednesday August 23rd:
      1) Find my own theme online
      2) Create a Table
      3) Add a New Page

      Thursday August 24th:
      1) Work on my pages
      2) Add a Gif and Link
      3) Create a New Page

      Friday August 25th:
      1) Add Image Carousel
      2) Add to the New Page


<div id="calculator">
    <input type="text" id="display" readonly>
    <div id="buttons">
        <button onclick="appendToDisplay('1')">1</button>
        <button onclick="appendToDisplay('2')">2</button>
        <button onclick="appendToDisplay('3')">3</button>
        <button onclick="appendToDisplay('+')">+</button>
        <button onclick="appendToDisplay('4')">4</button>
        <button onclick="appendToDisplay('5')">5</button>
        <button onclick="appendToDisplay('6')">6</button>
        <button onclick="appendToDisplay('-')">-</button>
        <button onclick="appendToDisplay('7')">7</button>
        <button onclick="appendToDisplay('8')">8</button>
        <button onclick="appendToDisplay('9')">9</button>
        <button onclick="appendToDisplay('*')">*</button>
        <button onclick="clearDisplay()">C</button>
        <button onclick="appendToDisplay('0')">0</button>
        <button onclick="calculate()">=</button>
        <button onclick="appendToDisplay('/')">/</button>
    </div>
</div>

<style>
/* Calculator Container */
#calculator {
    width: 300px;
    margin: 0 auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
    background-color: #f7f7f7;
    text-align: center;
}

/* Calculator Display */
#display {
    width: 100%;
    height: 40px;
    margin-bottom: 10px;
    font-size: 18px;
    text-align: right;
    padding: 5px;
    background-color: #fff;
    border: 1px solid #ccc;
    border-radius: 3px;
    box-shadow: inset 0 0 5px rgba(0, 0, 0, 0.2);
}

/* Calculator Buttons */
#buttons button {
    width: 50px;
    height: 50px;
    font-size: 18px;
    margin: 5px;
    cursor: pointer;
    border: 1px solid #ccc;
    border-radius: 3px;
    background-color: #fff;
}

/* Calculator Buttons (Operator Buttons) */
#buttons button:nth-child(4n-3),
#buttons button:nth-child(4n-2),
#buttons button:nth-child(4n-1),
#buttons button:last-child {
    background-color: #ff9900;
    color: #fff;
    border: 1px solid #ff9900;
}

/* Calculator Buttons (Clear and Equals) */
#buttons button:nth-child(13),
#buttons button:nth-child(16) {
    background-color: #ff3333;
    color: #fff;
    border: 1px solid #ff3333;
}
</style>

<script>
function appendToDisplay(value) {
    document.getElementById('display').value += value;
}

function clearDisplay() {
    document.getElementById('display').value = '';
}

function calculate() {
    try {
        document.getElementById('display').value = eval(document.getElementById('display').value);
    } catch (error) {
        document.getElementById('display').value = 'Error';
    }
}
</script>


<!-- ## Important Tools:

- Plans, Lists, [Scrum Boards](https://clickup.com/blog/scrum-board/) help you to track key events, show progress and record time.  Effort is a big part of your class grade.  Show plans and time spent!
- [Hacks(Todo)](https://levelup.gitconnected.com/six-ultimate-daily-hacks-for-every-programmer-60f5f10feae) enable you to stay in focus with key requirements of the class.  Each Hack will produce Tangibles.
- Tangibles or [Tangible Artifacts](https://en.wikipedia.org/wiki/Artifact_(software_development)) are things you accumulate as a learner and coder. 

 -->

[TRAVEL BLOG](http://0.0.0.0:4200/student/2023/08/23/Travel.html)




![gif](air.gif)