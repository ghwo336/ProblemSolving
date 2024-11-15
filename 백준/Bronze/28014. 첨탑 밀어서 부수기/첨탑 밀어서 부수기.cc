#include <iostream>
#include <vector>
using namespace std;
int main() {
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int N;
    cin>>N;
    vector<int> vec;
    for (int i = 0 ; i < N ;i++){
        int x;
        cin>>x;
        vec.push_back(x);
    }
    int dap=1;
    for (int i =1 ; i<N;i++){
        if (vec[i]>=vec[i-1]) dap+=1;
    }
    cout<<dap;


    return 0;
}