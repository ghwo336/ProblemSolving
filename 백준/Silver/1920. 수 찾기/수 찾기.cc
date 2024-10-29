#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

void input(int n, vector<int>& vec){
    for (int i = 0 ; i < n ; i++){
        int x;
        cin >>x;
        vec.push_back(x);
    }
}


void binarySearch(int start, int end , int want, vector<int>& vec){
    if (start>end){
        cout<<0<<'\n';
        return;
    }
    int mid=(start+end)/2;
    if (vec[mid]==want){
        cout<<1<<'\n';
        return;
    }
    else if (vec[mid]>want){
        binarySearch(start,mid-1,want,vec);
    }
    else{
        binarySearch(mid+1,end,want,vec);
    }
    
    
}




int main() {
    int N;
    vector<int>vec1;

    int M;
    vector<int>vec2;
    
    
    cin>>N;
    input(N,vec1);
    
    cin>>M;
    input(M,vec2);

    sort(vec1.begin(),vec1.end());

    for(int i = 0 ; i < M ; i ++){
        binarySearch(0,N-1,vec2[i],vec1);
    }

    
    return 0;
}