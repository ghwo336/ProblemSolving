#include <iostream>
using namespace std;
int main() {
    int a = 0;
    int b = 0;
    int c = 0;
    cin>>c;
    a+=3*c;
    cin>>c;
    a+=2*c;
    cin>>c;
    a+=c;
    cin>>c;
    b+=3*c;
    cin>>c;
    b+=2*c;
    cin>>c;
    b+=c;
    if (a>b) cout<<'A';
    else if (a<b) cout<<'B';
    else cout<<'T';
    
}