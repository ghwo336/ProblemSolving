#include <iostream>
using namespace std;
int main() {
    int a,b;
    int dap=0;
    cin>>a>>b;
    for (int i=a;i<=b;i++){
        if (i%2==0){
            dap+=1;
        }
    }
    if(b%2) dap+=1;
    cout<<dap;
}