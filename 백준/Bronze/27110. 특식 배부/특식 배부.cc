#include <iostream>
using namespace std;

int max(int a, int b){
    if (a<b) return a;
    return b;
}



int main() {
    int N;
    cin>>N;
    int x,y,z;
    cin>>x>>y>>z;
    int dap=0;
    dap+=max(N,x);
    dap+=max(N,y);
    dap+=max(N,z);
    cout<<dap;
    
    return 0;
}