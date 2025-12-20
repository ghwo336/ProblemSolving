#include <bits/stdc++.h>
using namespace std;
int main() {
    int n;
    cin>>n;
    int arr[1001]={0};
    vector<int> v;
    int dap=0;
    for (int i =0 ; i < n ; i++){
        int a;
        cin>>a;
        dap+=a;
        arr[a]+=a;
        v.push_back(a);
    }
    sort(v.begin(),v.end());
    int fiv=0;
    for (int i =0 ; i<=1000;i++){
        fiv=max(fiv,arr[i]);
    }
    cout<<dap+fiv<<'\n';
    for (int i = 0; i < n ; i++){
        cout<<v[i]<<' ';
    }
    
    
    return 0;
}