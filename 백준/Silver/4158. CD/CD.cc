#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int dap=0;

void input(int n , vector<int>& vec){
    for (int i = 0; i < n ; i ++){
        int x;
        cin>>x;
        vec.push_back(x);
    }
}


void binarySearch(int start, int end,int want,vector<int> & vec){
    if (start>end){
        return;
    }
    int mid = (start+end)/2;
    if (vec[mid]==want){
        dap+=1;
        return;  
    }
    if (vec[mid]>want){
        return binarySearch(start,mid-1,want,vec);
    }else return binarySearch(mid+1,end,want,vec);

    
}


int main() {
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    while(true){
        
    
    int n,m;
    vector<int> vec1;
    vector<int> vec2;
    cin>>n>>m;
        
    if (n==0 && m==0) break;
    input(n,vec1);
    input(m,vec2);
    sort(vec1.begin(),vec1.end());
    for (int i = 0 ; i < m ; i ++){
        binarySearch(0,n-1,vec2[i],vec1);
    }
    cout<<dap<<'\n';
    dap=0;
    }
}