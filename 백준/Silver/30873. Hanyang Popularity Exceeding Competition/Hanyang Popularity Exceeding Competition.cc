#include <iostream>
using namespace std;

int dap = 0;

int abs(int a){
    if ( a > 0) return a;
    else return -a;
}

int main() {
    int n;
    cin>>n;
    for (int i = 0; i < n; i++){
        int a,b;
        cin>>a>>b;
        if (abs(dap-a)<=b){
            dap++;
        }
    }
    cout<<dap;
    
    return 0;
}