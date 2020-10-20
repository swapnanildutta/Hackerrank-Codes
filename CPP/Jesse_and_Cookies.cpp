/*
Problem

Jesse loves cookies. He wants the sweetness of all his cookies to be greater than value K.
To do this, Jesse repeatedly mixes two cookies with the least sweetness.
He creates a special combined cookie with:

	sweetness = (1 x Least sweet cookie + 2 x 2nd least sweet cookie).

He repeats this procedure until all the cookies in his collection have a sweetness >= K.
You are given Jesse's cookies. Print the number of operations required to give the cookies a sweetness >= K.
Print -1 if this isn't possible.

Input Format

The first line consists of integers N, the number of cookies and K, the minimum required sweetness, separated by a space.
The next line contains N integers describing the array A where A[i] is the sweetness of the i-th cookie in Jesse's collection.

Constraints

	1 <= N <= 10^6
	0 <= K <= 10^9
	0 <= A[i] <= 10^6

Output Format

Output the number of operations that are needed to increase the cookie's sweetness >= K.
Output -1 if this isn't possible.

Sample Input

	6 7
	1 2 3 9 10 12

Sample Output

	2

Explanation

Combine the first two cookies to create a cookie with sweetness = 1 x 1 + 2 x 2 = 5
After this operation, the cookies are 3, 5, 9, 10, 12.
Then, combine the cookies with sweetness 3 and sweetness 5, to create a cookie with resulting sweetness = 1 x 3 + 2 x 5 = 13
Now, the cookies are 9, 10, 12, 13.
All the cookies have a sweetness >= 7.

Thus, 2 operations are required to increase the sweetness.
*/

#include <bits/stdc++.h>

using namespace std;

vector<string> split_string(string);

/*
 * Complete the cookies function below.
 */
int cookies(int k, vector<int> A)
{
	priority_queue<int, vector<int>, greater<int>> pq;
	for (int i = 0; i < A.size(); ++i)
	{
		pq.push(A[i]);
	}
	int op = 0;
	while (pq.top() < k)
	{
		if (pq.size() < 2)
			return -1;
		op++;
		int sml = pq.top();
		pq.pop();
		int sml2 = pq.top();
		pq.pop();
		pq.push(sml + sml2 * 2);
	}
	return op;
}

int main()
{
	ofstream fout(getenv("OUTPUT_PATH"));

	string nk_temp;
	getline(cin, nk_temp);

	vector<string> nk = split_string(nk_temp);

	int n = stoi(nk[0]);

	int k = stoi(nk[1]);

	string A_temp_temp;
	getline(cin, A_temp_temp);

	vector<string> A_temp = split_string(A_temp_temp);

	vector<int> A(n);

	for (int A_itr = 0; A_itr < n; A_itr++) {
		int A_item = stoi(A_temp[A_itr]);

		A[A_itr] = A_item;
	}

	int result = cookies(k, A);

	fout << result << "\n";

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