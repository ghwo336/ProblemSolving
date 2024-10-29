#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


int main() {
    vector<int> vec;
    for (int i = 0 ; i < 4 ; i++){
        int n;
        cin>>n;
        vec.push_back(n);
    }
    sort(vec.begin(),vec.end());
    cout<<vec[0]*vec[2];
    return 0;
}