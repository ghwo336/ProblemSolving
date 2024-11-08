#include <iostream>
using namespace std;

long long min (long long x, long long y){
    if (x>y) return y;
    return x;
}
int main() {
    long long a,b;
    cin>>a>>b;
    cout<<min(a+1,b);
    return 0;
}