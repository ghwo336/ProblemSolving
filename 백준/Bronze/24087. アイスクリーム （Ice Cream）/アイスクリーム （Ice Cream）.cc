#include <iostream>
using namespace std;
int main() {
   int s{0};
    int a{0};
    int b{0};
    cin>>s>>a>>b;
    int dap{250};
    s-=a;
    if (s>0){
        if (s%b!=0){
            dap+=100*(s/b+1);
        }
        else{
            dap+=100*(s/b);
        }
    }
    cout<<dap;
}