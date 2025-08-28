#include <iostream>
using namespace std;
int main() {
    int a,b,c;
    cin>>a>>b>>c;
    int s,v;
    cin>>s>>v;
    s*=30;
    v*=30;
    int l;
    cin>>l;
    int dap=0;
    int exp = (250-l)*100;
    if (exp<=c*v){
        if (exp%c==0) {
            cout<<exp/c;
        }
        else{
            cout<<exp/c+1;
        }
    }
    else{
        exp-=(c*v);
        dap+=v;
        if (exp<=b*s){
            if(exp%b==0){
                cout<<dap+exp/b;
            }
            else{
                cout<<dap+exp/b+1;
            }
        }
        else{
            dap+=s;
            exp-=(b*s);
            if  (exp%a==0){
                cout<<dap+exp/a;
            }
            else{
                cout<<dap+exp/a+1;
            }
        }
    }
    return 0;
}