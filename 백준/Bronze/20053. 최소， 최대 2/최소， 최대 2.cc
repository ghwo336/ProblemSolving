#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


void input(vector<int> &vec, int n){
    for (int i= 0 ; i<n;i++){
        int x;
        cin>>x;
        vec.push_back(x);
    }
    
    
}


void sol(){
    int n;
    cin>>n;
    vector<int>vec;
    input(vec,n);
    sort(vec.begin(),vec.end());
    cout<<vec.front()<<" "<<vec.back()<<'\n';
}


int main() {
    ios_base :: sync_with_stdio(false);
cin.tie(NULL);
cout.tie(NULL);
   int N;
    cin>>N;
    for (int i = 0; i<N ; i++){
        sol();
    }
    
    return 0;
}