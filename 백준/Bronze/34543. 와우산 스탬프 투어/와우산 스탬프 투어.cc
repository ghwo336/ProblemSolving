#include <iostream>
using namespace std;
int main() {
    int n,w;
    cin>>n>>w;
    int dap=n*10;
    if (w>1000) dap-=15;
    if (n>=3) dap+=20;
    if (n==5) dap+=50;
    if (dap<0) cout<<0;
    else cout<<dap;
    return 0;
}