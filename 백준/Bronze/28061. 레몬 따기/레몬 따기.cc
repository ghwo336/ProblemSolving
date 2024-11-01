#include <iostream>
using namespace std;
int main() {
    int N;
    int dap = 0;
    cin>>N;
    for(int i = 0 ; i <N ; i ++){
        int x;
        cin>>x;
        if (dap<x+i-N){
            dap=x+i-N;
        }
    }

    cout<<dap;

    
    return 0;
}