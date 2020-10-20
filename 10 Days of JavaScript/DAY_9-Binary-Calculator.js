/*DAY-9*/
/*Objective

In this challenge, we implement a calculator that uses binary numbers. Check out the attached tutorial for learning materials.

Task

Implement a simple calculator that performs the following operations on binary numbers: addition, subtraction, multiplication, and division. Note that division operation must be integer division only; for example, , , and .

The calculator's initial state must look like this:

image

Element IDs. Each element in the document must have an id, specified below:

innerHTML	id	Description/Behavior
res	Contains the result of button presses.
btns	A button container that displays all eight calculator buttons.
0	btn0	A button expressing binary digit .
1	btn1	A button expressing binary digit .
C	btnClr	A button to clear the contents of .
=	btnEql	A button to evaluate the contents of the expression in .
+	btnSum	A button for the addition operation.
-	btnSub	A button for the subtraction operation.
*	btnMul	A button for the multiplication operation.
/	btnDiv	A button for the integer division operation.
Styling. The document's elements must have the following styles:

body has a width of 33%.
res has a background-color of lightgray, a border that is solid, a height of 48px, and a font-size of 20px.
btn0 and btn1 have a background-color of lightgreen and a color of brown.
btnClr and btnEql have a background-color of darkgreen and a color of white.
btnSum, btnSub, btnMul, and btnDiv have a background-color of black, a color of red.
All the buttons in btns have a width of 25%, a height of 36px, a font-size of 18px, margin of 0px, and float value left.
The .js and .css files are in different directories, so use the link tag to provide the CSS file path and the script tag to provide the JS file path:

<!DOCTYPE html>
<html>
    <head>
        <link rel="stylesheet" href="css/binaryCalculator.css" type="text/css">
    </head>
    
    <body>
    	<script src="js/binaryCalculator.js" type="text/javascript"></script>
    </body>
</html>
Constraints

All expressions in the test dataset are entered in the form , where  is the first binary number,  is the second binary number, and  is in the set .
Both operands will always be positive integers when converted from base- to base-.
All expressions will be valid.
Explanation

Consider the following sequence of button clicks:

Before pressing the  button, the result div looks like this:

27+8

After pressing the  button to evaluate our expression, the result div looks like this:

27+8eval

Notice that , , and , so our calculator evaluated the expression correctly.

Now, let's consider our next sequence of button clicks as:

Before pressing the  button, the result div looks like this:

141x7

After pressing the  button to evaluate our expression, the result div looks like this:

141x7eval

Consider the next sequence of button clicks as:

The result div looks like this:

clear3
*/

/*SOLUTION*/

/HTML/
<!-- Enter your HTML code here -->
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <link rel="stylesheet" href="css/binaryCalculator.css" type="text/css">
        <title>Binary Calculator</title>
    </head>
    <body>
        <div id="res"></div>
        <div id="btns">
            <button id="btn0">0</button>
            <button id="btn1">1</button>
            <button id="btnClr">C</button>
            <button id="btnEql">=</button>
            <button id="btnSum">+</button>
            <button id="btnSub">-</button>
            <button id="btnMul">*</button>
            <button id="btnDiv">/</button>
        </div>
        <script src="js/binaryCalculator.js" type="text/javascript"></script>
    </body>
</html>

/*CSS*/
 body {
    width: 33%;
}
#res {
    display: block;
    font-size: 20px;
height: 48px;
    background-color: lightgray;      
border: 2px solid black;
    box-sizing: border-box;
}
#btns {
    display: block;
    overflow: hidden;
}
#btns button {
    display: block;
    float: left;
    width: 25%;
    height: 36px;
    font-size: 18px;
    background: black;
    color: red;
}
#btns #btn0, #btns #btn1 {
    background-color: lightgreen;
    color: brown;
}
#btns #btnClr, #btns #btnEql {
    background-color: darkgreen;
    color: white;
}
