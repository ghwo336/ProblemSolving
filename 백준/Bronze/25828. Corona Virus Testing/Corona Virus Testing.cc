#include <iostream>
using namespace std;
int main() {
    int g,t,p;
    cin>>g>>p>>t;
    int num1 = g*p;
    int num2 = g+(t*p);
    if (num1<num2) cout<<1;
    if (num1>num2) cout<<2;
    if (num1==num2) cout<<0;
    return 0;
}