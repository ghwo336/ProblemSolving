#include <iostream>
using namespace std;
int main() {
    long long dap = 0;
    int n;
    cin>>n;
    for (int x =1 ; x<=n/3 ; x++){
        for (int y = 0 ; y < n; y++){
            int first=x;
            int second=x+y;
            int third=n-(first+second);
            if (second>third) break;
            if (first+second>third) dap++;
        }
    }
cout<<dap;
    
    return 0;
}