#include <iostream>
using namespace std;
int main() {
    int n,k,a,b;
    cin>>n>>k>>a>>b;
    int dap2= (n-1)*a;
    int dap1=(n+k-2)*b;
    cout<<dap1<<' '<<dap2;
    return 0;
}