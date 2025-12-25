#include <iostream>
using namespace std;
int main() {
    int n;
    cin>>n;
    bool f = true;
    for (int i = 0 ; i < n; i++ ){
        int a;
        cin>>a;
        if (a<48) f=false;
    }
    if (f) cout<<"True";
    else cout<<"False";
    return 0;
}