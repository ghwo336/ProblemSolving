#include <iostream>
#include <vector>
using namespace std;

void sol(){
    vector<int> v;
    for (int i =0; i<3; i++){
        int a;
        cin>>a;
        v.push_back(a);
    }
    int dap =0;
    for(int i = 0 ; i < 3; i++){
        if (v[i]>=10) dap++;
        cout<<v[i]<<' ';
    }
    cout<<'\n';
    if (dap==0) cout << "zilch";
    else if (dap==1) cout <<"double";
    else if (dap==2) cout << "double-double";
    else cout << "triple-double";
    cout<<'\n';
}

int main(){
    int n;
    cin>>n;
    for (int i = 0; i<n; i++){
        sol();
        if (i!=n-1) cout<<'\n';
    }
}