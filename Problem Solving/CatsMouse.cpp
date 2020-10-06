/* Question

Two cats and a mouse are at various positions on a line.
You will be given their starting positions. Your task is to determine which cat 
will reach the mouse first, assuming the mouse does not move and the cats travel
at equal speed. If the cats arrive at the same time, the mouse will be allowed to
move and it will escape while they fight.

You are given q queries in the form of x, y and z representing the respective positions
for cats A and B, and for mouse C. Complete the function

to return the appropriate answer to each query, which will be printed on a new line.

    *If cat A  catches the mouse first, print Cat A.
    *If cat B catches the mouse first, print Cat B.
    *If both cats reach the mouse at the same time, print Mouse C as the two cats fight and mouse escapes.

Example

*x=2
*y=5
*z=4

The cats are at positions 2(Cat A) and 5(Cat B), and the mouse is at position 4. Cat B, at position 5 will arrive first since it is only 1 unit away while the other is

2 units away. Return 'Cat B'.

Function Description

Complete the catAndMouse function in the editor below.

catAndMouse has the following parameter(s):

    *int x: Cat A's position
    *int y: Cat B's position
    *int z: Mouse C's position

Returns

    string: Either 'Cat A', 'Cat B', or 'Mouse C'

Input Format

The first line contains a single integer,q, denoting the number of queries.
Each of the q subsequent lines contains three space-separated integers describing the respective values of x(cat A's location), y(cat B's location), and z(mouse C's location).

Constraints

    *1<=q<=100
    *1<=x,y,z<=100

Sample Input 0

2
1 2 3
1 3 2

Sample Output 0

Cat B
Mouse C

*/




 /* Solution:*/

#include <bits/stdc++.h>

using namespace std;

vector<string> split_string(string);

// Complete the catAndMouse function below.
string catAndMouse(int x, int y, int z) {
    int dist_x = abs(x-z);
    int dist_y = abs(y-z);
    if(dist_x < dist_y)
        return "Cat A";
    if(dist_y<dist_x)
        return "Cat B";
    return "Mouse C";


}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    int q;
    cin >> q;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    for (int q_itr = 0; q_itr < q; q_itr++) {
        string xyz_temp;
        getline(cin, xyz_temp);

        vector<string> xyz = split_string(xyz_temp);

        int x = stoi(xyz[0]);

        int y = stoi(xyz[1]);

        int z = stoi(xyz[2]);

        string result = catAndMouse(x, y, z);

        fout << result << "\n";
    }

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
