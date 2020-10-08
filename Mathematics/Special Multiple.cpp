/*
Link : https://www.hackerrank.com/challenges/special-multiple/problem
You are given an integer N. Can you find the least positive integer X made up of only 9's and 0's, such that, X is a multiple of N?

Update
X is made up of one or more occurences of 9 and zero or more occurences of 0.

Input Format
The first line contains an integer T which denotes the number of test cases. T lines follow.
Each line contains the integer N for which the solution has to be found.

Output Format
Print the answer X to STDOUT corresponding to each test case. The output should not contain any leading zeroes.

Constraints
1 <= T <= 104
1 <= N <= 500

Sample Input

3
5
7
1
Sample Output

90
9009
9

Explanation
90 is the smallest number made up of 9's and 0's divisible by 5. Similarly, you can derive for other cases.
*/

// author: @akashksinghal
#include <bits/stdc++.h>
using namespace std;

string solve(int n) {
    queue<string> q; 
    q.push("9"); 
    while (true) 
    { 
        string s1 = q.front(); 
        q.pop(); 
        cout << s1 << "\n";
        if(stol(s1)%n==0){
            return s1;
        } 
        string s2 = s1; 
        q.push(s1.append("0")); 
        q.push(s2.append("9")); 
    } 
    return "";
}

int main()
{
    int t;
    cin >> t;
    for (int t_itr = 0; t_itr < t; t_itr++) {
        int n;
        cin >> n;
        string result = solve(n);

        cout << result << "\n";
    }
    return 0;
}