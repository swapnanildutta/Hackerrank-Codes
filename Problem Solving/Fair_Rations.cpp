/* problem-statement
You are the benevolent ruler of Rankhacker Castle, and today you're distributing bread. Your subjects are in a line, and some of them already have some loaves.
Times are hard and your castle's food stocks are dwindling, so you must distribute as few loaves as possible according to the following rules:
Every time you give a loaf of bread to some person,i, you must also give a loaf of bread to the person immediately in front of or behind them in the line (i.e., persons(i+1) or (i-1)
After all the bread is distributed, each person must have an even number of loaves.
Given the number of loaves already held by each citizen, find and print the minimum number of loaves you must distribute to satisfy the two rules above. If this is not possible, print NO.

For example, the people in line have loaves, B=[4,5,6,7]. We can first give a loaf to i=3 and i=4 so B=[4,5,7,8] .
Next we give a loaf to i=2 and i=3 and have B=[4,6,8,8] which satisfies our conditions. We had to distribute 4 loaves.

Function Description
Complete the fairRations function in the editor below. It should return an integer that represents the minimum number of loaves required.
fairRations has the following parameter(s):
    B: an array of integers that represent the number of loaves each persons starts with .
    
Input Format

The first line contains an integer,N, the number of subjects in the bread line.
The second line contains N space-separated integers B[i] .

Output Format
Print a single integer taht denotes the minimum number of loaves that must be distributed so that every person has an even number of loaves. If it's not possible to do this, print NO.

Sample Input 0
5
2 3 4 5 6
Sample Output 0
4 
Explanation 0
The initial distribution is(2,3,4,5,6). The requirements can be met as follows:
Given 1 loaf of bread each to the second and third people so that the distribution becomes (2,4,5,5,6).
Give 1 loaf of bread each to the third and fourth people so that the distribution becomes (2,4,6,6,6)
Each of the N subjects has an even number of loaves after 4 loaves were distributed. */

#include <bits/stdc++.h>
using namespace std;
vector<string> split_string(string);
// Complete the fairRations function below.
int fairRations(vector<int> b) {
int count=0;
for(int i=0;i<b.size();i++)
{
 if(b[i]%2!=0)
 count++;
}
if(count%2!=0)
{
    return -1;
}
else
{ count=0;
    for(int i=0;i<b.size();i++)
    {
        if(b[i]%2!=0)
        {   count++;
            b[i]=b[i]+1;
            b[i+1]=b[i+1]+1;
        }
    }
    return count*2;
}

}
//auto-generated code
int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));
    int N;
    cin >> N;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');
    string B_temp_temp;
    getline(cin, B_temp_temp);
    vector<string> B_temp = split_string(B_temp_temp);
    vector<int> B(N);
    for (int i = 0; i < N; i++) {
        int B_item = stoi(B_temp[i]);
        B[i] = B_item;
    }
int result = fairRations(B);      
        if(result==-1)
            fout<<"NO"<<"\n";
        else
            fout<<result<<"\n";
    fout.close();
    return 0;
}
vector<string> split_string(string input_string) {
    string::iterator new_end = unique(input_string.begin(), input_string.end(), [] (const char &x, const char &y) {
        return x == y and x == ' ';
    });
    input_string.erase(new_end, input_string.end());
    while (input_string[input_string.length() - 1] == ' ') {
        input_string.pop_back();
    }
    vector<string> splits;
    char delimiter = ' ';
    size_t i = 0;
    size_t pos = input_string.find(delimiter);
    while (pos != string::npos) {
        splits.push_back(input_string.substr(i, pos - i));
        i = pos + 1;
        pos = input_string.find(delimiter, i);
    }
    splits.push_back(input_string.substr(i, min(pos, input_string.length()) - i + 1));
    return splits;
}

