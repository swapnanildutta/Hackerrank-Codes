Day11: (Divide and Conquer) 

1. 1/N-th root of an integer (use binary search) (square root, cube root, ..)
-> find perfect sqaure root using binary search.

int floorSqrt(int x)  
{     
    // Base cases 
    if (x == 0 || x == 1)  
       return x; 
  
    // Do Binary Search for floor(sqrt(x)) 
    int start = 1, end = x, ans;    
    while (start <= end)  
    {         
        int mid = (start + end) / 2; 
  
        // If x is a perfect square 
        if (mid*mid == x) 
            return mid; 
  
        // Since we need floor, we update answer when mid*mid is  
        // smaller than x, and move closer to sqrt(x) 
        if (mid*mid < x)  
        { 
            start = mid + 1; 
            ans = mid; 
        }  
        else // If mid*mid is greater than x 
            end = mid-1;         
    } 
    return ans; 
} 

-----------------------------------------------------------------------------------------
2. Matrix Median
-> find median of matrix having row sorted.

Approach 1) make 1D array sort it and find median.

Approach 2) median means n/2 number smaller then median and n/2 number bigger than number.
	find min and max of matrix. min found by first row and max found by last row.
	find mid value of min and max. and count less then mid and grater then mid numbers.
	-> count number less then mid used by uppar_bound() in each row.
	
int binaryMedian(int m[][MAX], int r ,int c) 
{ 
    int min = INT_MAX, max = INT_MIN; 
    // find min and max element here
    for (int i=0; i<r; i++) 
    { 
        // Finding the minimum element 
        if (m[i][0] < min) 
            min = m[i][0]; 
  
        // Finding the maximum element 
        if (m[i][c-1] > max) 
            max = m[i][c-1]; 
    } 
  
    int desired = (r * c + 1) / 2; 
    while (min < max) 
    { 
	// mid lies on min and max think if we sort that we take mid first and last which basically 
	// is min max.

        int mid = min + (max - min) / 2; 
        int place = 0; 
  
        // Find count of elements smaller than or equal mid 
        for (int i = 0; i < r; ++i) 
            place += upper_bound(m[i], m[i]+c, mid) - m[i]; 

        if (place < desired) 
            min = mid + 1; 
        else
            max = mid; 
    } 
    return max; 
} 

---------------------------------------------------------------------------------------------
3. Find the element that appears once in sorted array, and rest element appears twice (Binary search)

-> O(Logn) Binary search:
-> observe that number appear twice first ocuurance of number is at even index. 0,2,4 etc..
-> after single number occurance fist occur is odd pos.

void search(int a[], int left, int right){
	if(left > right) return;
	if(left==right) {
		cout << a[left]; return;
	}

	int mid = (left+right)/2;
	
	if(mid%2==0) {
	   if(a[mid]==a[mid+1])
		search(a, mid+2, right);
	   else	
		search(a, left, mid);
	} else {
	   if(a[mid]==a[mid-1])
		search(a, mid+1, right);
	   else
		search(a, left, mid-1);
	}	
}
-------------------------------------------------------------------------------------------
4. Search element in a sorted and rotated array. 
-> find pivot point sorted array.
	if both side element less than current then this is pivot point.
	
Algo ) find mid of left and right. if mid is smaller then left and right this is pivot point.
	else check if a[0] to a[mid] is sorted then move to mid+1 to right 
	else move to left to mid-1.
	once find pivot point search 0 to mid-1, mid to end.

Approach 2) one traverser: improved version.
		- find mid of array
		- check if left to mid is sorted 
		       then check key between left to mid check left to mid-1 side else mid+1 to right
		- else check key is in mid+1 to right 
		       then search mid+1 to right else left to mid-1
		
---------------------------------------------------------------------------------------------
5. K-th element of two sorted arrays 		
-> given 2 sorted array you need to find kth element in sorted array.

Approach 1) mearge array and find that index from array.
Approach 2) Divide and conqure and binary search
	take 2 array mid1, mid2

Let us assume arr1[mid1]  k, then clearly the elements after mid2 cannot be the required element. 
We then set the last element of arr2 to be arr2[mid2].

int kth(int *arr1, int *arr2, int *end1, int *end2, int k) 
{ 
    if (arr1 == end1) 
        return arr2[k]; 
    if (arr2 == end2) 
        return arr1[k]; 

    int mid1 = (end1 - arr1) / 2; 
    int mid2 = (end2 - arr2) / 2; 
    // we require more from left side so lesser move to right
    if (mid1 + mid2 < k) 
    { 
        if (arr1[mid1] > arr2[mid2]) 
            return kth(arr1, arr2 + mid2 + 1, end1, end2, 
                k - mid2 - 1); 
        else
            return kth(arr1 + mid1 + 1, arr2, end1, end2, 
                k - mid1 - 1); 
    } 
    else
    { 
        if (arr1[mid1] > arr2[mid2]) 
            return kth(arr1, arr2, arr1 + mid1, end2, k); 
        else
            return kth(arr1, arr2, end1, arr2 + mid2, k); 
    } 
} 
---------------------------------------
6. Media of an array
i) find median of unsorted array.
	use quick select algorithm. 
	O(N) time. later consider
	use logic of quick sort algorithm. find pivot point if it is middle then it is median.

ii) find median of 2 sorted array.
	At last time...

iii) STL: use nth_element of stl c++. 
-------------------------------------------------------------------------------------------
Day13: (Stack and Queue)   
1. Implement Stack / Implement Queue
-> use array for stack make top pointer.
-> for queue make 2 pointer
------------------------------------------------------------------------
2. BFS
-> BFS in tree level order traversal use queue.
------------------------------------------------------------------------
3. Implement Stack using Queue
-> we use two queue for implement stack.
we push on to stack and pop from stack. by making push operation costly.
we use q1,q2. push in to q2 and then push q1 whole in to q2 and rename q1,q2.
-> Approach 2)
	by making pop operation costly. push into q1, when pop push everything into q2 until last one and pop last one swap(q1,q2);
------------------------------------------------------------------------
4. Implement Queue using Stack 

-> using 2 stacks, s1,s2;
Approach 1) make push operation costly. when pushing to queue first all element from s1 move to s2
	add new element to s1. and again flush all s2 into s1.

Approach 2) make pop operation costly
	push data to s1. and check if s2.empty push all into s2. and remove s2.top
------------------------------------------------------------------------
5. Check for balanced parentheses 

-> balance parantheses check parantases are matches "(([]))()[]" are balanced. 
-> we use stack when open bracket push into stack.
	when close bracket comes check top of the stack if match then pop else return false.
	last if stack empty return true else return false;
------------------------------------------------------------------------
6. Next Greater Element 
-> replace current element with next greater element.
Approach 1) use two loop i for current element start j from i+1 and find element >a[i] set that val.

Approach 2) use stack. traverse from last to first.
	if stack top is <= cur pop it and if stack empty assign -1 to that index.

	for(int i=n-1; i>=0; i--){
		
		while(!s.empty() && s.top() <= arr[i])
			s.pop();
			
		if(s.empty()){
			ans[i]=-1;			
		}else{
			ans[i]=s.top();
		}
		s.push(arr[i]);
	}

----------------------------------------------------------------------------------
Day14
----------
1. Next Smaller Element
-> same as next greater element. find first element from right side which is smaller then current
-> traverse from last of array

for(int i=n-1; i>=0; i--) {
	while(!s.empty() && s.top() >= a[i])
		s.pop();
	if(s.empty())
		ans[i]=-1;
	else
		ans[i].s.top();
	s.push(a[i]);
}

------------------------------------------------------------------
2. LRU cache (vvvv. imp)
-> it is operating system paging technique to store recent accessed page in cache.
-> you have given capacity of cache and given query of pages if not available add to cache and if cache is full remove oldest page from cache and add current. if available on cahe move to recent used.

-> use map so search efficient way and use link list so swap move front is efficient.

class LRUCache { 
	// store keys of cache 
	list<int> dq; 

	// store references of key in cache 
	unordered_map<int, list<int>::iterator> ma; 
	int csize; // maximum capacity of cache 

public: 
	LRUCache(int); 
	void refer(int); 
	void display(); 
}; 

// Declare the size 
LRUCache::LRUCache(int n) { 
	csize = n; 
} 

// Refers key x with in the LRU cache 
void LRUCache::refer(int x) 
{ 
	// not present in cache 
	if (ma.find(x) == ma.end()) { 
		// cache is full 
		if (dq.size() == csize) { 
			// delete least recently used element 
			int last = dq.back(); 

			// Pops the last elmeent 
			dq.pop_back(); 

			// Erase the last 
			ma.erase(last); 
		} 
	} 

	// present in cache 
	else
		dq.erase(ma[x]); 

	// update reference 
	dq.push_front(x); 
	ma[x] = dq.begin(); 
} 

void LRUCache::display() 
{ 
	for (auto it = dq.begin(); it != dq.end(); 
		it++) 
		cout << (*it) << " "; 

	cout << endl; 
}

------------------------------------------------------------------
3. Largest rectangle in histogram
-> Makeing some observation you get max histogram is 
	find smaller from left side and right side.
	and minus both and multiply cur height
code:--

void max_histo(int a[], int n){
	stack<pair<int, int>> s1;
	int ans=0;	
	int left[n]={}, right[0]={};	
	for(int i=0; i<n; i++){
		while(!s1.empty() && s1.top().first >= a[i])
			s1.pop();
		if(s1.empty())
			left[i]=-1;
		else
			left[i]=s1.top().second;
		s1.push({a[i], i});
	}	
	while(s1.size()) s1.pop();	
	for(int i=n-1; i>=0; i--){
		while(!s1.empty() && s1.top().first >= a[i])
			s1.pop();			
		if(s1.empty())
			right[i]=n;
		else
			right[i]=s1.top().second;
		s1.push({a[i], i});
	}			
	for(int i=0; i<n; i++) 
		ans = max(ans, a[i]*(right[i]-left[i]-1));	
	cout << ans << "\n";
}
------------------------------------------------------------------
4. Sliding Window maximum (Queue)
-> Given number and K. make array that have greater element of window size k.

nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7]

Explain....
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

code :

vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        vector<int> ans;
        deque<int> dq;
        int i=0;
        
        for(i=0; i<k; i++) {
            while(!dq.empty() && nums[i] >= nums[dq.back()])
                dq.pop_back();
            
            dq.push_back(i);
        }
        
        for( ; i<nums.size(); i++) {
            ans.push_back(nums[dq.front()]);
		
	    // remove which is out side window            
            while(!dq.empty() && dq.front() <= i-k)
                dq.pop_front();
            
            while(!dq.empty() && nums[i] >= nums[dq.back()])
                dq.pop_back();
            
            dq.push_back(i);
        }
        
        ans.push_back(nums[dq.front()]);
        return ans;
    }

----------------------------------------------------------------------------------
5. Implement Min Stack
-> make new function that add fundction to getMin(). find min element from stack O(1).
-> make a new stack if empty add first element.
-> if current element <= minstack.top insert that element to minstack.
-> when getMin call return top element of min stack.

----------------------------------------------------------------------------------
6. Rotten Orange (Using BFS)

-> you given grid having 3 types of oranges.
0 - empty cell
1 - fresh orange
2 - rotten orange
-> in one minute one rotten orange make 4 side fresh orange to be rotten parally all rotten make this in different places.
-> return no of minues where all oranges rotten or if not return -1.

Approach 1) because all adj are rotten 4 side paralley all so we use BFS.
	first make structure Node{ time, row, col }. then add all rotten node to queue with time=1;
	then run BFS check 4 side if fresh then make it rotten and add with time+1.

struct Node {
   int time;
   int row, col;
};

int orangesRotting(vector<vector<int>>& grid) {
        int row=grid.size();
        int col=grid[0].size();        
        queue<Node> q;
        
        for(int i=0; i<row; i++)
            for(int j=0; j<col; j++) {
                if(grid[i][j] == 2) {
                    Node cur;
                    cur.time=0;
                    cur.row=i;
                    cur.col=j;
                    q.push(cur);
                }
            }
        
        int ans=0;
        while(!q.empty()){
            Node cur = q.front(); q.pop();
	    // check 4 side            
            if(cur.row-1 >= 0 && grid[cur.row-1][cur.col] == 1) {
                grid[cur.row-1][cur.col]=2;
                Node n; n.time=cur.time+1;
                n.row=cur.row-1, n.col=cur.col;
                q.push(n);
                ans=max(ans, n.time);
            }            
            if(cur.row+1 < row && grid[cur.row+1][cur.col] == 1) {
                grid[cur.row+1][cur.col]=2;
                Node n; n.time=cur.time+1;
                n.row=cur.row+1, n.col=cur.col;
                q.push(n);
                ans=max(ans, n.time);
            }            
            if(cur.col-1 >= 0 && grid[cur.row][cur.col-1] == 1) {
                grid[cur.row][cur.col-1]=2;
                Node n; n.time=cur.time+1;
                n.row=cur.row, n.col=cur.col-1;
                q.push(n);
                ans=max(ans, n.time);
            }            
            if(cur.col+1 < col && grid[cur.row][cur.col+1] == 1) {
                grid[cur.row][cur.col+1]=2;
                Node n; n.time=cur.time+1;
                n.row=cur.row, n.col=cur.col+1;
                q.push(n);
                ans=max(ans, n.time);
            }            
        }        
        for(int i=0; i<row; i++)
            for(int j=0; j<col; j++)
                if(grid[i][j]==1)
                    return -1; // if any fresh orange exists return -1
        return ans;        
    }
-----------------------------------------------------------------------------------------
Day15: (String) 
------------------

1. Reverse Words in a String
Ex: I am from surat.
Ans: surat from am I.

-> we can do with reverse each word inplace then reverse whole string.

// we take care of multiple space and string start with space.
void reverseWords(char* s) 
{ 
    char* word_begin = NULL; 
    char* temp = s; 
 
    while (*temp) { 

        if ((word_begin == NULL) && (*temp != ' ')) { 
            word_begin = temp; 
        } 
        if (word_begin && ((*(temp + 1) == ' ') || 
            (*(temp + 1) == '\0'))) { 
            reverse(word_begin, temp); 
            word_begin = NULL; 
        } 
        temp++; 
    }
    
    reverse(s, temp - 1); 
}

-------------------------------------------------------------------------------------
2. Longest Palindrome in a string
-> DP O(n^2)
-> it can be done normal loop as well

ex : babad ans: bab

So, approach is if pelingromic string odd than mid appear once for even middle val same
abba <= even length 2 bb.
aba <= odd length 1 b

we try to find both.

string longestPalindrome(string s) {
        if(s.size() < 1)
                return "";
        
        int start=0, end=0;
	// take each point as middle point and expand both side util it same

        for(int i=0; i<s.size(); i++){            
            int len1 = findMid(s, i, i); // odd len i, i
            int len2 = findMid(s, i, i+1); // even len i, i+1
            int len = max(len1, len2);            
            if(len > end - start){
                start = i - ((len-1)/2);
                end = i + (len / 2);
            }
        }
        return s.substr(start, end-start+1);
    }
        
    int findMid(string s, int left, int right){       
        while(left >= 0 && right < s.size() && s[left] == s[right] ){
            left--;
            right++;
        }
        return right-left-1;
    }

Approach 2) Manchar's algorithm do in O(N)
-----------------------------------------------------
3. Roman Number to Integer and vice versa

Roman to int :
int romanToInt(string s) {
	       
     	if(s.size() == 0)
            return 0;
        
        unordered_map<char, int> roman;
        
        roman['I'] = 1;
        roman['V'] = 5;
        roman['X'] = 10;
        roman['L'] = 50;
        roman['C'] = 100;
        roman['D'] = 500;
        roman['M'] = 1000;
        
        int len = s.size()-1;
        char lastChar = s[len];
        
        // store last char corresponding integer
        int result = roman[lastChar];
        
        // loop last second to first
        for(int i=len-1; i>=0; i--){
            if( roman[s[i]] >= roman[s[i+1]] ){
                result += roman[s[i]];
            } else {
                result -= roman[s[i]];
            }
        }
        return result;
    }
------
Integer to Roman

string intToRoman(int num) {
       vector<string> numrals{"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" };
       vector<int> no{ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 };        
        
	int i=0;
        string s;        
        while(num > 0){
            if(num - no[i] >= 0){
                s.append(numrals[i]);
                num -= no[i];
            } else {
                i++;    
            }        
        }
        return s;
    }
-------------------------------------------------------------------------------
4. Implement ATOI/STRSTR

ATOI
-> convert string to int "1234"
make int res;
	res = res*10 + s[i]-'0' main idea.
	there is many improvement like negative number, alphabet.
best version code:

int myAtoi(char* str) 
{ 
    if (*str == '\0') 
        return 0; 
  
    int res = 0; 
    int sign = 1; 
    int i = 0; 

    if (str[0] == '-') { 
        sign = -1; 
        i++; 
    } 
  
    for (; str[i] != '\0'; ++i) { 
  	if (isNumericChar(str[i]) == false) 
            return 0;   
        res = res * 10 + str[i] - '0'; 
    } 
    // Return result with sign 
    return sign * res; 
} 

STRSTR--------------
Very eusy bruteforce
int strStr(string haystack, string needle) {       
        int i1=0,i2=0,c=0;        
        if(needle.size() == 0)
            return 0;
        
        for(int i=0; i<haystack.size(); i++){
            i2=0; c=0;
            if(haystack[i] == needle[i2]) {
                i1=i;
                while(i1 < haystack.size() && i2 < needle.size() && haystack[i1]==needle[i2]){
                    i1++;
                    i2++;
                    c++;
                    
                    if(c == needle.size()){
                        return i;
                    }
                }
            }
            
        }
        return -1;
    }
-> use Robin karp rolling hash to do in linear time
-------------------------------------------------------------------------------------
5. Longest Common Prefix
Input: ["flower","flow","flight"]
Output: "fl"

code:
string longestCommonPrefix(vector<string>& strs) {
        string pref = "";
        if(strs.size() == 0)
            return pref; 
       
        string s = strs[0]; 

        // loop on first string
        for(int i=0; i<s.size(); i++){
            // all other string
            for(int j=1; j<strs.size(); j++){
                if(i >= strs[j].size())
                    return pref;                
                string str = strs[j];
                if(s[i] != str[i])
                    return pref;                
            }
            pref += s[i];
        }        

        return pref;
    }

----------------------------------------------------------------
6. Rabin Karp
-> Algorithm it is hashing approach called rolling hash.

-------------------------------------------------------------------------------------------
Day 16

1. Prefix Function/Z-Function
-> it is pattern matching algorithm.
-> improvement over KMP its make eusy to implement to calculate z array
-> make str=pat+"$"+s;

z[i] = means value from prefix match

void zalgo(string str, string pat){
	// main condition 1<=l<=i<=r<str.size()
	// make i in between range l,r
	// if i>r then make l=i and increase r
	
	int l=0, r=0;
	int len=str.size();
	int z[len]={0};
	
	for(int i=1; i<len; i++){
		if(i>r) {
			// naive way first time find range l to r
			l=r=i; // as we see above comment i>r make all same l=r=i, so condidtion fulfilled.			
			// starting len 2
			while(r<len && str[r]==str[r-l])
				r++;			
			z[i]=r-l;
			r--; // condidtion fulfill so r move extra 1
		}
		else  {
			int idx = i-l;
			if(i+z[idx] <= r) {
				z[i]=z[idx];
			} 
			else {
				// again condidition not fulfilled
				l=i; // make l to i and move r
				while(r<len && str[r] == str[r-l])
					r++;
				z[i]=r-l;
				r--;
			}
		}
	}
	
	for(int i=0; i<str.size(); i++)
		if(z[i] == pat.size())
			cout << "pattern find at index : "  << i - pat.size() - 1 << "\n";		
}
---------------------------------------------------------------------------
2. KMP algo 

later..........
---------------------------------------------------------------------------
3. Minimum characters needed to be inserted in the beginning to make it palindromic.
-> Different then DP you need to add at front of the array.
-> based on LPS array of KMP
	
later..........
-----------------------------------------------------------------------------
4. Check for Anagrams
-> approach 1) sort both string and check is it same 
-> Approach 2) use map count occurace of first string, minus occurance of second string.
	and check all val in map is 0.
------------------------------------------------------------------------------
5. Count and Say
-> 1, 11, 21, 1211, 111221
-- no pattern here, just read as it is and you find next pattern.

string countAndSay(int n) {
        if(n==1)
            return "1";
        if(n==2)
            return "11";
        
        string str="11";
        
        for(int i=3; i<=n; i++){
            string temp = "";
            str += "$"; // add so that s[j]!=s[j-1] condition hold true for last char
            int cnt=1;
            int len = str.size();
            
	    // just count consecutive same char in cnt, once find all and we know the char is 
	    // current mismatach means prev val = str[j-1].

            for(int j=1; j<len; j++){
                if(str[j]!=str[j-1]) {
                    temp += cnt+'0';
                    temp += str[j-1];
                    cnt=1;
                } else 
                    cnt++;
            }
            str=temp;
        }        
        return str;
    }

----------------------------------------------------------------------------
6. Compare version numbers
-> Given 2 version of system return 1 if v1 is bigger return -1 if v2 is bigger else return 0;

int compareVersion(string version1, string version2) {
        int i = 0; 
        int j = 0;
        int n1 = version1.size(); 
        int n2 = version2.size();
        int num1 = 0;
        int num2 = 0;

        while(i<n1 || j<n2)
        {
            while(i<n1 && version1[i]!='.'){
                num1 = num1*10+(version1[i]-'0');
                i++;
            }

            while(j<n2 && version2[j]!='.'){
                num2 = num2*10+(version2[j]-'0');;
                j++;
            }
            if(num1>num2) return 1;
            else if(num1 < num2) return -1;

            num1 = 0;
            num2 = 0;
            i++;
            j++;
        }
        return 0;
    }
---------------------------------------------------------------------------------------
Day17: (Binary Tree) 

1. Inorder Traversal (with recursion and without recursion) 
-> Recursion:
	void Inorder(Node* root) {
		if(!root) return;
		Inorder(root->left);
		cout << root->val << " ";
		Inorder(root->right);	
	}

-> Iterative:
	
stack<Node*> s;
Node* cur = root;

while(cur != NULL || !s.empty()) {
	while(cur != NULL) {
		s.push(cur);
		cur=cur->left;
	}
	cur=s.top(); s.pop();
	cout << cur->val << " ";
	cur=cur->right;
}

------------------------------------------------------------------------------------	
2. Preorder Traversal (with recursion and without recursion) 

Recursion: 
	void pre(Node* root) {
		if(!root) return;	
		cout << root->val << " ";
		pre(root->left);
		pre(root->right);
	}

Iterative:

stack<Node*> s;
s.push(root);

while(!s.empty()){
	Node* cur = s.top(); s.pop();
	cout << cur->val << " ";
	if(cur->right)	
		s.push(s->right);
	if(cur->left)
		s.push(s->left);
}

-----------------------------------------------------------------------------------
3. Postorder Traversal (with recursion and without recursion)  

Recursion:
	void post(Node* root) {
		if(!root) return;
		post(root->left);	
		post(root->right);
		cout << cur << " ";
	}

Iterative :
	we oberseve some pattern here. we postorder travese the tree and reverse it.
	after reverse we find that this is preorder traverse with minor diff that we process 	
	right child first then left one.
	
-> Key idea is use 2 stacks and treverse preorder and insted of printing push to 2nd stack and at the end just print 2nd stack.

code:	
stack<Node*> s1,s2;
s1.push(cur);

while(!s1.empty()){
	Node* cur = s1.top(); s1.pop();
	s2.push(cur);
	// process right child first so that push left first LIFO property.
	if(cur->left)
		s1.push(cur->left); //cur=cur->left;
	if(cur->right)	
		s2.push(cur->right); //cur=cur->right;
}
// now just print stack s1
while(!s2.empty()){
	cout << s2.top()->val << " ";
	s2.pop(); 
}

Iterative with 1 stack:
	
do {
	
	while(root) {
		if(root->right)
			s.push(root->right);
		s.push(root);
		root = root->left;
	}
	root=s.top(); s.pop();
	if(root->right && s.top()==root->right) {
		s.pop();
		s.push(root)
		root=root->right;
	} else {
		cout << root->val << " ";
		root=NULL;
	}

}while(!s.empty())

----------------------------------------------------------------------------------
4. LeftView Of Binary Tree
-> Level order traversal first occur is left view.
Recursion:

int max_lvl=0;
call: leftViewUtil(root, 1, &max_lvl);

void leftViewUtil(node* root, int level, int* max_level) 
{ 
    // Base Case 
    if (root == NULL) 
        return; 
  
    // If this is the first node of its level 
    if (*max_level < level) { 
        cout << root->data << "\t"; 
        *max_level = level; 
    } 
  
    // Recur for left and right subtrees 
    leftViewUtil(root->left, level + 1, max_level); 
    leftViewUtil(root->right, level + 1, max_level); 
} 
  
--------
Iterative:

-> Do BFS when first node at each level print it.	
queue<Node*> q;
q.push(root);

while(!q.empty()) {
	Node* cur=q.front();
	cout << cur->val << " ";
	int size=q.size();
	
	for(int i=0; i<size; i++) {
		cur=q.front(); q.pop();
		if(cur->left)	
			q.push(cur->left);
		if(cur->right)
			q.push(cur->right);
	}

}
------------------------------------------------------------------------------------
5. Right View of Binary Tree
-> level order traversal with last node each lvl;

queue<Node*> q;
q.push(root);

while(!q.empty()) {
	int len = q.size();
	for(int i=1; i<=len; i++) {
		auto cur = q.top(); q.pop();

		if(i==len)
			cout << cur->val << " ";

		if(cur->left)
			q.push(cur->left);
		if(cur->right)	
			q.push(cur->right);

	}
}

----------------------------------------------------------------------------
6. Bottom View of Binary Tree
-> make map maintain hd horizontal diamention so updated val each hd is ans.

void bottomview(Node* root){
	int hd=0;
	map<int, int> mp;
	queue<pair<Node*, int>> q;
	q.push({root, hd});

	while(!q.empty()) {
		auto cur = q.top();
		Node* temp = cur.first;
		hd = cur.second;

		mp[hd]=temp->val; // last added is ans at each hd
		
		if(temp->left)
			q.push({temp->left, hd-1});

		if(temp->right)
			q.push({temp->right, hd+1});
		
	}
	for(auto m : mp)	
		cout << m.second << " ";
}

----------------------------------------------------------------------------
7. Top View of Binary Tree 

void topView(Node* root){
	int hd=0;
	map<int, int> mp;
	queue<pair<Node*, int>> q;
	q.push({root, hd});

	while(!q.empty()) {
		auto cur = q.top();
		Node* temp = cur.first;
		hd = cur.second;
		
		// just 1 change is this
		if(mp.count(hd)==0)
			mp[hd]=temp->val; // For first only consider
		
		if(temp->left)
			q.push({temp->left, hd-1});

		if(temp->right)
			q.push({temp->right, hd+1});
		
	}
	for(auto m : mp)	
		cout << m.second << " ";
}

---------------------------------------------------------------------------------------
Day 18
-------
1. Level order Traversal / Level order traversal in spiral form

-> Level order use queue.
queue<Node*> q;
q.push(root);
while(!q.empty()) {
	auto cur = q.top(); q.pop();
	cout << cur->val << " ";
	if(cur->left) q.push(q->left);
	if(cur->right) q.push(q->right);
}

-> spiral form level order traversal
- take 2 stack s1,s2. start with s1. push root to s1.
when s1 !empty push right -> left to s2.
when s2 !empty push left -> right to s1.

stack<Node*> s1,s2;
s1.push(root);

while(!s1.empty() || !s2.empty()) {

	while(!s1.empty()) {
		Node* cur=s1.top(); s1.pop();
		cout << cur->val << " ";
		if(cur->right) s2.push(cur->right);
		if(cur->left) s2.push(cur->left);
	}

	while(!s2.empty()) {
		Node* cur = s2.top(); s2.pop();
		cout << cur->val << " ";  
		if(cur->left) s1.push(cur->left);
		if(cur->right) s1.push(cur->right);
	}	
}

---------------------------------------------------------------------
2. Height of a Binary Tree

int height(Node* root){
	if(root==NULL)
		return 0;
	return 1 + max(height(root->left), height(root->right));
}

---------------------------------------------------------------------
3. Diameter of Binary Tree

// O(N^2) : all time height called
int diameter(Node* root){
	if(root == NULL)	
		return 0;
	int l=height(root->left);
	int r=height(root->right);
	int ld = diameter(root->left);
	int rd = diameter(root->right);
	
	// max Diameter passes through root means "root+left+right"=>(1+l+r)
	// or it just left side or right side => (ld, rd) | max of both
	return max( l+r+1, max(ld, rd) );
}

--> here we all time calculate height so we reduce that and optimize it.

/ O(N)
int diameter(Node* root, int* height){
	int lh=0, rh=0;
	int ld=0, rd=0;
	
	if(root==NULL) {
		*height=0;
		return 0;
	}

	ld = diameter(root, &lh);
	rd = diameter(root, &rh);	
		
	*height = max(lh, rh) + 1;
	
	return max(lh+rh+1, max(ld, rd));
}
--------------------------------------------------------------------------
4. Check if Binary tree is height balanced or not
-> Tree is called height Balanced iff:	
-> left height and right height abs diff <= 1
-> left is balanced and right is balanced.

// O(N^2) : all time called height function
bool isBal(Node* root) {
	if(root==NULL)
		return true;

	int lh = height(root->left);
	int rh = height(root->right);
	
	if(abs(lh-rh) <= 1 && isBal(root->left) && isBal(root->right))
		return true;

	return false;
}

- we optimize this as we calculate height parallely.

bool isBal(Node* root, int* height){
	if(root==NULL) {
		*height=0;
		return true;
	}
	
	int lh=0, rh=0;		
	bool left, right;
	
	left = isBal(root, &lh);
	right = isBal(root, &rh);
	
	*height = 1 + max(lh, rh);	
	
	if(abs(lh-rh) > 1)	
		return false;
	else
		return left && right;
}
-------------------------------------------------------------
5. LCA in Binary Tree 

-> longest common ancestor(LCA) of BST is common parent from where both child divides left, right side.
given 2 node find LCA of that node.

// a, b is val we find LCA of a,b.
Node* lca(Node* root, int a, int b){
	if( a < root->val && b < root->val )
		return lca(root->left, a, b);
	else if(a > root->val && b > root->val)
		return lca(root->right, a, b);
	else
		return root;
}

--------------------------------------------------------------
6. Check if two trees are identical or not

bool isSame(Node* root1, Node* root2){
	if(root1==NULL && root2==NULL)
		return true;
	if(root1==NULL || root2==NULL)
		return false;
	if(root1->val != root2->val)
		return false;

	return isSame(root1->left, root2->left) && isSame(root1->right, root2->right);
}

----------------------------------------------------------------------------------------
Day 19: (Binary Tree) 

1. Maximum path sum 
-> many variation of this question.

i) max sum root to leaf :
int ans=0;
	
void treesum(Node* root, int cur){
	if(!root) return;
	if(root->left == NULL && root->right == NULL) {
		ans=max(ans, cur);
		return;
	}
	treesum(root->left, cur + root->val);
	treesum(root->right, cur + root->val);
}

ii) max path leaf to leaf.

int res=0;	
int solve(Node* root){
	if(root==NULL) return 0;	
	int ls = solve(root->left);
	int rs = solve(root->right);
	
	// we move upward so either take left or right and add cur val and return to above
	int temp = max(ls, rs) + root->val;

	// if current node become turning point
	// left <-> curr <-> right
	// if this is case then take both left and right
	int ans = max(temp, ls+rs+root->val);
	res=max(temp, ans);
	return temp;
}

iii) max path from any node to any node (actual question is this)

int ans=INT_MIN;

int maxpath(Node* root) {
	if(!root) return 0;
	int l = maxpath(root->left);
	int r = maxpath(root->right);
	
	// choose max left, right add current or choose only cur and return upward.
	int temp = max( max(l, r) + root->val, root->val );
	int cur = max(temp, l + r + root->val);
	ans=max(ans, cur);
	return temp;
}

-----------------------------------------------------------------------------
2. Construct Binary Tree from inorder and preorder

int search(int in[], int start, int end, int val) {

	for(int i=start; i<=end; i++)
		if(in[i]==val)
			return i;
	return -1;
}

Node* buildTree(int in[], int pre[], int instart, int inend){
	static int preIndex=0;

	if(instart > inend)
		return NULL;
	
	Node* root = New Node(pre[preIndex++]);
	
	// no child
	if(instart == inend)
		return root;
	
	// we get index of root here we assume it always return valid index not -1.
	int rootindex = search(in, instart, inend, root->val);
	
	// find root index so left side is left subtree and right side is right subtree
	root->left = buildTree(in, pre, instart, rooindex-1);
	root->right = buildTree(in, pre, rootindex+1, inend);
	return root;
}

-------------------------------------------------------------------------
3. Construct Binary Tree from Inorder and Postorder
-> we know postorder right is root and find root in Inorder we get left right subtree.

int search(int arr[], int start, int end, int val){
	for(int i=start, i<=end; i++)	
		if(arr[i] == val)
			return i;
	return -1;
}

Node* buildTree(int in[], int post[], int start, int end, int& postIndex){
	if(start > end)
		return NULL;

	Node* root = new Node(post[postIndex]);
	postIndex--;

	if(start == end)
		return root;

	int rootindex = search(in, start, end, root->val);

	root->right = buildTree(in, post, rootindex+1, end, postIndex);
	root->left = buildTree(in, post, start, rootindex-1, postIndex);

	return root;
}

----------------------------------------------------------------------------------------
4. Symmetric Binary Tree (check binary tree is mirror of it self)

bool solve(TreeNode* root1, TreeNode* root2){
        if(root1==NULL && root2==NULL)
            return true;
        
        if(root1==NULL || root2 == NULL)
            return false;
        
        if(root1->val != root2->val)
            return false;
        
        return solve(root1->left, root2->right) && solve(root1->right, root2->left);
}

--------------------------------------------------------------------------------------------
5. Flatten Binary Tree to LinkedList

-> Tree Question:
    1
   / \
  2   5
 / \   \
3   4   6

Ans : 

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6

-> make it inplace so basically we rearrange it and make left child null
-> use stack 
void flatten(TreeNode* root) {
        if(!root) return; stack<TreeNode*> s; s.push(root);       
        while(!s.empty()){
            auto cur = s.top(); s.pop();            
            if(cur->right)
                s.push(cur->right);            
            if(cur->left)
                s.push(cur->left);            
            if(!s.empty()) 
                cur->right=s.top();                     
            cur->left=NULL;
        }
}

---------------------------------------------------------------------------------------
6. Check if Binary Tree is mirror of itself or not
-> for 1 tree its same as questio 4.
-> even for 2 tree its again same as question 4.

---------------------------------------------------------------------------------------

Day 20: (Binary Search Tree) 
------
1. Populate Next Right pointers of Tree
-> do level order traversal and add next pointer to queue.front();

Node* connect(Node* root) {
        if(root==NULL)
            return root;
        queue<Node*> q;
        Node* cur = root;
        q.push(cur);
        
        while(!q.empty()){
            int size=q.size();
            
            for(int i=0; i<size-1; i++){
                cur = q.front(); q.pop();
                cur->next = q.front();
                if(cur->left)
                    q.push(cur->left);
                if(cur->right)
                    q.push(cur->right);
            }
            if(!q.empty()) {
                cur=q.front(); q.pop();
                if(cur->left)
                    q.push(cur->left);
                if(cur->right)
                    q.push(cur->right);
            }
        }        
        return root;
    }

------------------------------------------------------------------------------------
2. Search given Key in BST
->BST have propety small number left side big number right side.

bool findKey(Node* root, int key){
	if(root==NULL)
		return false;
	if(root->val == key)
		return false;
	if(key < root->val)
		return findkey(root->left, key);
	else	
		return findkey(root->right, key);
}

-----------------------------------------------------------------------------------
3. Construct BST from given keys. (Insert in BST)

Node* insert(Node* root, int key){
	if(root==NULL) {
		root=new Node(key);
		return root;
	}
	if(key < root->val)
		root->left = insert(root->left, key);
	else
		root->right = insert(root->right, key);
	return root;
}
------------------------------------------------------------------------------------
4. Check is a BT is BST or not  (check given tree is BST or not)
-> in BST all left side less then root and all right side greater then root.

bool checkBST(Node* root, int mx, int mn){
	if(root==NULL)	
		return true;
	if(root->val > mx || root->val < mn)
		return false;

	return checkBST(root->left, root->val, mn) && checkBST(root->left, mx, root->val);
}
// for caling mn=INT_MIN, mx=INT_MAX
-------------------------------------------------------------------------------------
5. Find LCA of two nodes in BST
-> longest comman ancester.
-- if present in tree both node

Node* findLCA(Node* root, Node* a, Node* b){
	if(root==NULL) return root;
	
	if(root->val == a->val || root->val == b->val)
		return root;

	Node* left = findLCA(root->left, a, b);
	Node* right = findLCA(root->right, a, b);
	
	if(left==NULL)	
		return right;
	if(right==NULL)
		return left;
	return root;	
}

--------------------------------------------------------------------------
6. Find the inorder predecessor/successor of a given Key in BST.
-> predecessor:
	left side bigger numner. in BST left side right most
-> successor:
	right side left most value.

-- there are 2 possibility that key is present or key not present.
	
void findboth(Node* root, Node*& pre, Node*& suc, int key){
	if(root==NULL)
		return;

	// case when we found key.
	if(root->val == key) {
		if(root->left) {
			Node* temp = root->left;
			while(temp->right)	
				temp=temp->right;
			pre=temp;
		}
		if(root->right) {
			Node* temp = root->right;
			while(temp->left)	
				temp=temp->left;
			suc=temp;
		}
		return;
	}

	// if key < cur this may suc., pre
	if(key < root->val) {
		suc=root;
		findboth(root->left, pre, suc, key);
	}
	else {
		pre=root;
		findboth(root->right, pre, suc, key);
	}
}

--------------------------------------------------------------------------
7. print path given sum
-> given sum find sum in BST. sum is in root to leaf.
-> find is there exist sum.

bool hasPathSum(TreeNode* root, int sum) {
        if(root==NULL)
            return false;
        if(root->left == NULL && root->right == NULL && sum-root->val == 0)
            return true;
        else
           return hasPathSum(root->left, sum - root->val) || hasPathSum(root->right, sum - root->val);
}


=> print sum
- do preorder traversal and add to sum then backtrack

int sum=0;
stack<int> s;
int k=20; // target sum

void solve(Node* root){
	if(root==NULL)
		return;
	sum += root->val;
	s.push(root->val);
	if(sum == k) {
		print satck path.
	}
	solve(root->left);	
	solve(root->right);
	sum=sum - root->val;
	s.pop();
}
