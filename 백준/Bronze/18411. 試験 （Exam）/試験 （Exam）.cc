#include <iostream>
using namespace std;

int min(int x, int y){
    if (x>y) return y;
    return x;
}

int main() {
    int a,b,c;
    cin>>a>>b>>c;
    int sum= a+b+c;
    int mi=10000;
    mi=min(mi,a);
    mi=min(mi,b);
    mi=min(mi,c);
    cout<<sum-mi;
    return 0;
}