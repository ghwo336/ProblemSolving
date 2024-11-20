#include <iostream>
using namespace std;
int main() {
    int n;
    cin>>n;
    int dap=0;
    for (int i =0 ; i<n;i++){
        int x;
        cin>>x;
        dap+=x;
    }
    if (dap>0) cout<<"Right";
    if (dap==0) cout<<"Stay";
    if (dap<0) cout<<"Left";
    return 0;
}