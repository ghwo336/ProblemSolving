#include <iostream>
using namespace std;
int main() {
    int N;
    int dap=0;
    cin>>N;
    for( int i = 0 ; i < N ; i++){
        int x;
        cin>>x;
        if (x%2==1) dap+=1;
    }
    cout<<dap;
    return 0;
}