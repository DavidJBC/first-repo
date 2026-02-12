#include <iostream>
using namespace std;
int main() {
  // Write code here
  for (int i = 1; i < 101; i++)
  {
    if (i % 3 == 0 and i % 5 == 0)
    {
      cout<<"FizzBuzz\n";
    } else if (i % 3 == 0 and i % 5 != 0)
    {
      cout<<"Fizz\n";
    } else if (i % 5 == 0 and i % 3 != 0)
    {
      cout<<"Buzz\n";
    } else
    {
      cout<<i<<" \n";
    }

  }
}

