// C++ program to count number of 2 x 2
// squares in a right isosceles triangle
#include<bits/stdc++.h>
using namespace std;

int numberOfSquares(int base)
{
// removing the extra part we would
// always need
base = (base - 2);

// Since each square has base of
// length of 2
base = floor(base / 2);

return base * (base + 1)/2;
}

// Driver code
int main()
{
int base = 8;
cout << numberOfSquares(base);
return 0;
}
