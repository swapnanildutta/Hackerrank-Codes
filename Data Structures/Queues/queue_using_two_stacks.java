/*A queue is an abstract data type that maintains the order in which elements were added to it, allowing the oldest elements to be removed from the front and new elements to be added to the rear. This is called a First-In-First-Out (FIFO) data structure because the first element added to the queue (i.e., the one that has been waiting the longest) is always the first one to be removed.

A basic queue has the following operations:

Enqueue: add a new element to the end of the queue.
Dequeue: remove the element from the front of the queue and return it.
In this challenge, you must first implement a queue using two stacks. Then process  queries, where each query is one of the following  types:

1 x: Enqueue element  into the end of the queue.
2: Dequeue the element at the front of the queue.
3: Print the element at the front of the queue.
Input Format

The first line contains a single integer, , denoting the number of queries.
Each line  of the  subsequent lines contains a single query in the form described in the problem statement above. All three queries start with an integer denoting the query , but only query  is followed by an additional space-separated value, , denoting the value to be enqueued.

Constraints

It is guaranteed that a valid answer always exists for each query of type .
Output Format

For each query of type , print the value of the element at the front of the queue on a new line.

Sample Input

10
1 42
2
1 14
3
1 28
3
1 60
1 78
2
2
Sample Output

14
14
Explanation

We perform the following sequence of actions:

Enqueue ; .
Dequeue the value at the head of the queue, ; .
Enqueue ; .
Print the value at the head of the queue, ; .
Enqueue ; .
Print the value at the head of the queue, ; .
Enqueue ; .
Enqueue ; .
Dequeue the value at the head of the queue, ; .
Dequeue the value at the head of the queue, ; .*/
import java.io.*;
import java.util.*;

class queue_using_two_stacks {

public static void main(String[] args) {
	Scanner sc = new Scanner(System.in);
	Stack<Integer> stack_insert = new Stack<>();
	Stack<Integer> stack_delete = new Stack<>();		
	int q = sc.nextInt();
	while(q-- > 0) {
		int type = sc.nextInt();
		if(type == 1) {
			int x = sc.nextInt();
			stack_insert.push(x);
		} else if(type == 2) {
			if( stack_delete.isEmpty() ) {
				while( !stack_insert.isEmpty() ) {
					stack_delete.push( stack_insert.pop() );
				}
			}
			stack_delete.pop();
		} else {
			if( stack_delete.isEmpty() ) {
				while( !stack_insert.isEmpty() ) {
					stack_delete.push( stack_insert.pop() );
				}
			}
			System.out.println( stack_delete.peek() );
		}
	}
}
}
