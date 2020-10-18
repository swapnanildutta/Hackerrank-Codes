// A string is said to be a child of a another string if it can be formed by deleting 0 or more characters from the other string. Given two strings of equal length, what's the longest string that can be constructed such that it is a child of both?

// For example, ABCD and ABDC have two children with maximum length 3, ABC and ABD. They can be formed by eliminating either the D or C from both strings. Note that we will not consider ABCD as a common child because we can't rearrange characters and ABCD  ABDC.



#include <bits/stdc++.h>

using namespace std;

static int T[5001][5001];
int commonChild(string s1, string s2) {
    int m = s1.size();
    int n = s2.size();
    
    for(int i = 0; i <= m; i++ ){
        for(int j = 0; j <= n; j++ ){
            if(i == 0 || j == 0){
                T[i][j] = 0;
            }else if(s1[i-1]==s2[j-1]){
                T[i][j] = 1+T[i-1][j-1];
            }else{
                T[i][j] = max(T[i][j-1], T[i-1][j]);
            }
        }
    }
    
    return T[m][n];
    
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string s1;
    getline(cin, s1);

    string s2;
    getline(cin, s2);

    int result = commonChild(s1, s2);

    fout << result << "\n";

    fout.close();

    return 0;
}
