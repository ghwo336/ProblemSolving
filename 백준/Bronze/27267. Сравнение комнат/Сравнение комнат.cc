#include <iostream>
using namespace std;
int main() {
    int a,b,c,d;
    cin>>a>>b>>c>>d;
    int e=a*b;
    int f = c*d;
    if (e>f) cout<<'M';
    else if(e==f) cout<<'E';
    else cout<<'P';
    return 0;
}