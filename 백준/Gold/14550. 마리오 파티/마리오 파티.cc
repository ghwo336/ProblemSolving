#include <iostream>
#include <vector>
using namespace std;
// 최대 최소 함수
int min (int a , int b){
    if (a<b) return a;
    else return b;
}
int max (int a , int b){
    if (a<b) return b;
    else return a;
}

//main solution
void sol(int n, int s, int t){
    //2차원 
    vector<int>v;
    v.push_back(0);
    vector<vector<int>> dp(t+1,vector<int>(n+2,-2000000000));
    dp[0][0]=0;
    for (int i = 1; i <= n; i++){
        int k;
        cin>>k;
        v.push_back(k);
        dp[0][i]=0;
    };
    v.push_back(0);
    for (int i = 1 ; i <= t; i++){
        dp[i][0]=0;
        for (int j = 1 ; j<= s; j++ ){
            for (int k = j ; k <= min(n+1,i*s) ; k++){
                dp[i][k]=max(dp[i][k],dp[i-1][k-j]+v[k]);
            }
        }
    }
    cout<<dp[t][n+1]<<'\n';
    
    
    
}



int main() {
    while(true){
        int n,s,t;
        cin>>n;
        if (n==0) break;
        cin>>s;
        cin>>t;
        sol(n,s,t);
    }
    return 0;
}