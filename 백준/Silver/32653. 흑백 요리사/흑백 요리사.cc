#include<bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin>>n;
    long long dap =1;
    for (int i = 0 ; i< n; i++){
        long long a;
        cin>>a;
        dap=lcm(dap,a);
    }

    cout<<dap*2;
    return 0;
}