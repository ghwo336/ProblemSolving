#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int dap=0;
int want=0;
int n =0 ;
vector<int> vec;
void input(int n, vector<int>&vec){
    for ( int i = 0 ; i < n ; i ++ ){
        int x;
        cin>>x;
        vec.push_back(x);
    }
}

void backtracking(int now , int sum,bool check){
    if (sum==want && check ) dap+=1;
    if (now ==n) return;
    backtracking(now+1,sum,false);
    backtracking(now+1,sum+vec[now],true);
}





int main() {
    int N,S;
    cin>>N>>S;
    want=S;
    n=N;

    input(N,vec);
    backtracking(0,0,true);
    if (S==0){
        dap-=1;
    }
    cout<<dap;
    
   
    }