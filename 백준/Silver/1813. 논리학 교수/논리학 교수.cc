#include <iostream>
#include <vector>
#include<map>
using namespace std;


void input(vector<int>&vec,int n){
    for ( int i = 0 ; i < n ; i ++){
        int x;
        cin>>x;
        vec.push_back(x);
    }
}

void find (map<int , int> &di, int n){
    for(int i=n ; i>=0 ; i--){
        if(di[i]==i){
            cout<<i;
            return;
        }
    }
    cout<<-1;
    return;
}


int main() {
    int N;
    cin>>N;
    vector <int> vec;
    input(vec,N);
    map<int,int> dict;
    for ( int i =0 ; i<=N ; i++){
        dict[i]=0;
    }
    for (int i : vec){
        dict[i]+=1;
    }
    find(dict,N);
    
}