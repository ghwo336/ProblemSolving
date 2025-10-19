#include <iostream>
using namespace std;
int main() {
    long long a,b;
    cin>>a>>b;
    long long dap = 0;
    if (a%2==1) a++;
    if (b%2==1) b--;
    if (b<4){
        cout<<0;
        return 0;
    }
    if (a==2) a=4;
    if (a==b) {
        cout<<a;
        return 0;
    }
    cout<<((a+b)*((b-a)/2+1))/2;
    
    
    return 0;
}