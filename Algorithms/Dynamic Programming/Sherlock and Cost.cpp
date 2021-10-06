/** question Name : Sherlock and Cost
    question link : https://www.hackerrank.com/challenges/sherlock-and-cost/problem
*/

#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);
vector<string> split(const string &);

/*
 * Complete the 'cost' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts INTEGER_ARRAY B as parameter.
 */

int mod (int a) {
    return a > 0 ? a : -1 * a;
}

int max (int a, int b) {
    return a > b ? a : b;
}

int cost(vector<int> B) {
    int maxx = 0;
    int dp[B.size () + 1][2];
    dp[0][0] = dp[0][1] = 0;
    for (int i = 1; i < B.size (); ++i) {
        dp[i][0] = max ((1 - 1) + dp[i-1][0], (B[i-1] - 1) + dp[i-1][1]);
        dp[i][1] = max ((B[i] - 1) + dp[i-1][0], mod(B[i-1] - B[i]) + dp[i-1][1]);
    }
    maxx =  max (dp[B.size () - 1][0], dp[B.size () - 1][1]);
    return maxx;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string t_temp;
    getline(cin, t_temp);

    int t = stoi(ltrim(rtrim(t_temp)));

    for (int t_itr = 0; t_itr < t; t_itr++) {
        string n_temp;
        getline(cin, n_temp);

        int n = stoi(ltrim(rtrim(n_temp)));

        string B_temp_temp;
        getline(cin, B_temp_temp);

        vector<string> B_temp = split(rtrim(B_temp_temp));

        vector<int> B(n);

        for (int i = 0; i < n; i++) {
            int B_item = stoi(B_temp[i]);

            B[i] = B_item;
        }

        int result = cost(B);

        fout << result << "\n";
    }

    fout.close();

    return 0;
}

string ltrim(const string &str) {
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
    );

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end()
    );

    return s;
}

vector<string> split(const string &str) {
    vector<string> tokens;

    string::size_type start = 0;
    string::size_type end = 0;

    while ((end = str.find(" ", start)) != string::npos) {
        tokens.push_back(str.substr(start, end - start));

        start = end + 1;
    }

    tokens.push_back(str.substr(start));

    return tokens;
}
