/*
An English text needs to be encrypted using the following encryption scheme.
First, the spaces are removed from the text. Let "L" be the length of this text.

Then, characters are written into a grid, whose rows and columns have the following constraints:

floor square root of "L" <= row <= column <= ceil square root of "L",

For example, "s = if man was meant to stay on the ground god would have given us roots" the sentence, after removing spaces is 54 characters long.
Squareroot of 54 is between 7 and 8, so it is written in the form of a grid with 7 rows and 8 columns.

ifmanwas  
meanttos          
tayonthe  
groundgo  
dwouldha  
vegivenu  
sroots

* Ensure that rows x columns >= "L"
* If multiple grids satisfy the above conditions, choose the one with the minimum area, i.e. .

The encoded message is obtained by displaying the characters in a column, inserting a space, and then displaying the next column and inserting a space, and so on. For example, the encoded message for the above rectangle is:

"imtgdvs fearwer mayoogo anouuio ntnnlvt wttddes aohghn sseoau"

You will be given a message to encode and print.
*/

using System;

class Encryption {

  static int Main(string[] args) {

    Console.Write("Enter the string to encrypt: ");
    string plainText = Console.ReadLine();

    if (plainText.Length == 0) {
        Console.Write("Requires a string!");
        return 0;
    }
    
    string s = plainText;
    int length = s.Length;
    double sqrt = Math.Sqrt(length);
    double floor = Math.Floor(sqrt);
    double ceil = Math.Ceiling(sqrt);
    
    while(!((floor * ceil) >= length))
    {
        if(floor > ceil)
        {
            ceil++;
        } else
        {
            floor++;
        }
    }
    int row = Convert.ToInt32(floor);
    int col = Convert.ToInt32(ceil);

    char[] chr = s.ToCharArray();
    char[,] arr = new char[row, col];
    int k = 0;
    
    for(int i=0;i<row;i++)
    {
        for(int j=0;j<col;j++)
        {
            if(!(k >= length))
            {
                arr[i, j] = chr[k++];
            } else
            {
                continue;
            }
        }
    }
    int total = (row+1)*(col+1);
    char[] fnl = new char[total];
    k = 0;
    
    for(int j=0;j<col;j++)
    {
        for(int i=0;i<row;i++)
        {
            if(! (arr[i,j] == '\0'))
            {
                if (!(k == total))
                {
                    fnl[k++] = arr[i, j];
                }
            }
        }
        if(! (k==total))
        {
            fnl[k++] = ' ';
        }
    }
    
    for(int i=0;i<total;i++)
    {
        if(fnl[i] == '\0')
        {
            fnl[i] = ' ';
        }
    }
    string cipher = new string(fnl);
    cipher = cipher.Trim();
    Console.Write("The encrypted cipher text is \n");
    Console.Write(cipher);
    return 0;
	}
}