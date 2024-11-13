#include <iostream>
using namespace std;
int main() {
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int dap=0;
    int N;
    cin>>N;
    for(int i =0; i<N; i++){
        int a,b;
        cin>>a>>b;
        dap+=a;
        dap-=b;
        cout<<dap<<'\n';
    }
}