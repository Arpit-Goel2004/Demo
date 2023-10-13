//write a cpp program to check if a number is fibonacci number or not//

#include<iostream>
using namespace std;
int main()
{
    int n,a=0,b=1,c=0;
    cout<<"Enter a number: ";
    cin>>n;
    while(c<n)
    {
        c=a+b;
        a=b;
        b=c;
    }
    if(c==n)
    {
        cout<<n<<" is a fibonacci number";
    }
    else
    {
        cout<<n<<" is not a fibonacci number";
    }
    return 0;
}

// Path: Demo/sample.cpp