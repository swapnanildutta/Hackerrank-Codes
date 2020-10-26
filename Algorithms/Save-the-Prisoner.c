/*
Problem:
A jail has a number of prisoners and a number of treats to pass out to them. Their jailer decides the fairest way to divide the treats is to seat the prisoners around a circular table in sequentially numbered chairs. A chair number will be drawn from a hat. Beginning with the prisoner in that chair, one candy will be handed to each prisoner sequentially around the table until all have been distributed.

The jailer is playing a little joke, though. The last piece of candy looks like all the others, but it tastes awful. Determine the chair number occupied by the prisoner who will receive that candy.

For example, there are  prisoners and  pieces of candy. The prisoners arrange themselves in seats numbered  to . Let's suppose two is drawn from the hat. Prisoners receive candy at positions . The prisoner to be warned sits in chair number .

Function Description

Complete the saveThePrisoner function in the editor below. It should return an integer representing the chair number of the prisoner to warn.

saveThePrisoner has the following parameter(s):

n: an integer, the number of prisoners
m: an integer, the number of sweets
s: an integer, the chair number to begin passing out sweets from
Input Format

Problem:

The first line contains an integer, , denoting the number of test cases.
The next  lines each contain  space-separated integers:
- : the number of prisoners
- : the number of sweets
- : the chair number to start passing out treats at

Constraints

Output Format

For each test case, print the chair number of the prisoner who receives the awful treat on a new line.

Sample Input 0

2
5 2 1
5 2 2
Sample Output 0

2
3
Explanation 0

In first query, there are  prisoners and  sweets. Distribution starts at seat number . Prisoners in seats numbered  and  get sweets. Warn prisoner .
In the second query, distribution starts at seat  so prisoners in seats  and  get sweets. Warn prisoner .

Sample Input 1

2
7 19 2
3 7 3
Sample Output 1

6
3
Explanation 1

In the first test case, there are  prisoners,  sweets and they are passed out starting at chair . The candies go all around twice and there are  more candies passed to each prisoner from seat  to seat .

In the second test case, there are  prisoners,  candies and they are passed out starting at seat . They go around twice, and there is one more to pass out to the prisoner at seat .
*/

#include <assert.h>
#include <limits.h>
#include <math.h>
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* readline();
char** split_string(char*);

// Complete the saveThePrisoner function below.
/*int saveThePrisoner(int n, int m, int s) {


}

int main()
{
    FILE* fptr = fopen(getenv("OUTPUT_PATH"), "w");

    char* t_endptr;
    char* t_str = readline();
    int t = strtol(t_str, &t_endptr, 10);

    if (t_endptr == t_str || *t_endptr != '\0') { exit(EXIT_FAILURE); }

    for (int t_itr = 0; t_itr < t; t_itr++) {
        char** nms = split_string(readline());

        char* n_endptr;
        char* n_str = nms[0];
        int n = strtol(n_str, &n_endptr, 10);

        if (n_endptr == n_str || *n_endptr != '\0') { exit(EXIT_FAILURE); }

        char* m_endptr;
        char* m_str = nms[1];
        int m = strtol(m_str, &m_endptr, 10);

        if (m_endptr == m_str || *m_endptr != '\0') { exit(EXIT_FAILURE); }

        char* s_endptr;
        char* s_str = nms[2];
        int s = strtol(s_str, &s_endptr, 10);

        if (s_endptr == s_str || *s_endptr != '\0') { exit(EXIT_FAILURE); }

        int result = saveThePrisoner(n, m, s);

        fprintf(fptr, "%d\n", result);
    }

    fclose(fptr);

    return 0;
}*/
int main()
{
    long int t;
    scanf("%ld",&t);
    while(t!=0)
    {
        long int n,m,s,d,ans;
        scanf("%ld%ld%ld",&n,&m,&s);
        if(m>=n)
        {
             d=m%n;
             ans=s+d-1;

        }
        else
        {
            ans=m+s-1;
        }
        if(ans<=n&&ans>=1)
        {
            printf("%ld\n",ans);
        }
        if(ans<1)
        {
             printf("%ld\n",n);
        }
        if(ans>n)
        {
            printf("%ld\n",(ans-n));
        }
        t--;
    } 
    return 0;
}
char* readline() {
    size_t alloc_length = 1024;
    size_t data_length = 0;
    char* data = malloc(alloc_length);

    while (true) {
        char* cursor = data + data_length;
        char* line = fgets(cursor, alloc_length - data_length, stdin);

        if (!line) { break; }

        data_length += strlen(cursor);

        if (data_length < alloc_length - 1 || data[data_length - 1] == '\n') { break; }

        size_t new_length = alloc_length << 1;
        data = realloc(data, new_length);

        if (!data) { break; }

        alloc_length = new_length;
    }

    if (data[data_length - 1] == '\n') {
        data[data_length - 1] = '\0';
    }

    data = realloc(data, data_length);

    return data;
}

char** split_string(char* str) {
    char** splits = NULL;
    char* token = strtok(str, " ");

    int spaces = 0;

    while (token) {
        splits = realloc(splits, sizeof(char*) * ++spaces);
        if (!splits) {
            return splits;
        }

        splits[spaces - 1] = token;

        token = strtok(NULL, " ");
    }

    return splits;
}
