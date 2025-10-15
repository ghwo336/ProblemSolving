#include <iostream>
using namespace std;
int main() {
    int a;
    cin>>a;
    if (a<4) cout<<0;
    else cout<<a*(a-1)*(a-2)*(a-3)/24;
    return 0;
}