#include <iostream>
using namespace std;
int main() {
    int N;
    cin>>N;
    int dap=0;
    for (int i=0;i<N;i++){
        int a,b;
        cin>>a>>b;
        if (a==136){
            dap+=1000;
        } else if(a==142){
            dap+=5000;
        } else if(a==148){
            dap+=10000;
        }else{
            dap+=50000;
        }   
    }
    cout<<dap;
}