#include <iostream>
#include <vector>
using namespace std;

int main() {
    int N;
    cin>>N;
    int dap=0;
    for (int i = 0 ; i <N ; i++){
        int x;
        cin>>x;
        if (x<=0){
            dap+=(-x);
        }else dap+=x;
    }

    for (int i = 0 ; i <N ; i++){
        int x;
        cin>>x;
        if (x<=0){
            dap+=(-x);
        }else dap+=x;
    }
    cout<<dap;
    
    return 0;
}