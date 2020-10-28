// hackerrank
/* Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Follow up:

Could you solve this problem without using the library's sort function?
Could you come up with a one-pass algorithm using only O(1) constant space?  */


#include <iostream>
using namespace std;

int main() {
	int n; cin>>n;
	int freq[101]={0};
	for(int i=0;i<n;i++){
	    int c; 
	    cin>>c;
	    freq[c]++;
	}
	int result=0;
	for(int i=0;i<n;i++){
	    result+=freq[i]/2;
	}
	cout<<result<<endl;
	
	return 0;
}
