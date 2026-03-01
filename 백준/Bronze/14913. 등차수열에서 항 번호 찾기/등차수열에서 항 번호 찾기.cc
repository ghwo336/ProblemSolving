#include <iostream>
using namespace std;
int main() {
    int a,b,c;
    cin>>a>>b>>c;
    if ((c-a)%b ==0 && (c-a)*b>=0){
        cout<<(c-a)/b+1;
            return 0;
    }
    cout<<'X';
    return 0;
}