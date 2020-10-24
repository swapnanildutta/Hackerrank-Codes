/*
Objective
Welcome to the last day! Today, we're discussing bitwise operations. Check out the Tutorial tab for learning materials and an instructional video!

Task
Given set S of integers .Find two integers A and B (where A<s, from set S such that the value of A&B is the maximum possible and also less than a given integer K, . In this case, & represents the bitwise AND operator.

Input Format
The first line contains an integer,T, the number of test cases.
Each of the T subsequent lines defines a test case as 2-space-separated integers, N and K, respectively.


Output Format
For each test case, print the maximum possible value of A&B on a new line.

Sample Input
3
5 2
8 5
2 2

Sample Output
1
4
0
*/

#include <bits/stdc++.h>

using namespace std;

vector<string> split_string(string);

int main()
{
    int t;
    cin >> t;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    for (int t_itr = 0; t_itr < t; t_itr++) {
        string nk_temp;
        getline(cin, nk_temp);

        vector<string> nk = split_string(nk_temp);

        int n = stoi(nk[0]);

        int k = stoi(nk[1]);
     
        int max=-1;
        for(int i=1;i<n;i++)
            for(int j=i+1;j<=n;j++)
            {
                int ans=i&j;
                if(ans>max && ans<k)
                    max=ans;
            }
        cout<<max<<endl;
    }

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
