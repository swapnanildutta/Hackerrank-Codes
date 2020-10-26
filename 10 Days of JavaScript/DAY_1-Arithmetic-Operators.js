/*DAY-0*/
/*Objective

In this challenge, we practice using arithmetic operators. Check out the attached tutorial for resources.

Task

Complete the following functions in the editor below:

getArea(length, width): Calculate and return the area of a rectangle having sides  and .
getPerimeter(length, width): Calculate and return the perimeter of a rectangle having sides  and .
The values returned by these functions are printed to stdout by locked stub code in the editor.

Input Format

image

image

Constraints

 and  are scaled to at most three decimal places.
Output Format

image

Sample Input 0

3
4.5
Sample Output 0

13.5
15
Explanation 0

The area of the rectangle is .
The perimeter of the rectangle is .
*/

/*SOLUTION*/



/**
*   Calculate the area of a rectangle.
*
*   length: The length of the rectangle.
*   width: The width of the rectangle.
*   
*	Return a number denoting the rectangle's area.
**/
function getArea(length, width) {
    let area;
    // Write your code here
    area = length * width;
    return area;
}

/**
*   Calculate the perimeter of a rectangle.
*	
*	length: The length of the rectangle.
*   width: The width of the rectangle.
*   
*	Return a number denoting the perimeter of a rectangle.
**/
function getPerimeter(length, width) {
    let perimeter;
    // Write your code here
    perimeter = 2* (length + width);
    return perimeter;
}

