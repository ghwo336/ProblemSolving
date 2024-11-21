#include <iostream>
#include <vector>
using namespace std;
int main() {
    int dap1 = 0;
    int dap2 = 0;
    vector<int> vec1;
    vector<int> vec2;

    for (int i =0 ; i<6 ; i++){
        int x;
        cin>>x;
        vec1.push_back(x);
    }
    for (int i =0 ; i<6 ; i++){
        int x;
        cin>>x;
        vec2.push_back(x);
    }
    dap1+=(vec1[0]*13+vec1[1]*7+vec1[2]*5+vec1[3]*3+vec1[4]*3+vec1[5]*2);
    dap2+=(vec2[0]*13+vec2[1]*7+vec2[2]*5+vec2[3]*3+vec2[4]*3+vec2[5]*2);
    if (dap1-dap2>1) cout<<"cocjr0208";
    else cout <<"ekwoo";

    
    return 0;
}