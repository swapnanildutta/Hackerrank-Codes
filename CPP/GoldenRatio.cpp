#include <iostream>
using namespace std;

void main()
{
    int n, t1 = 0, t2 = 1, nextTerm = 0;
    float ratio=0;

    cout << "Enter the number of terms: ";
    cin >> n;

    cout << "Fibonacci Series: ";

    for (int i = 1; i <= n; ++i)
    {
	ratio=0;
        // Prints the first two terms.
        if(i == 1)
        {
            cout << " " << t1;
            continue;
        }
        if(i == 2)
        {
            cout << t2 << " ";
            continue;
        }
        nextTerm = t1 + t2;
        t1 = t2;
        t2 = nextTerm;
        ratio = t2/t1;

        cout << nextTerm << " ";
    }
  cout<<"\nRatio:  "<<ratio
}
