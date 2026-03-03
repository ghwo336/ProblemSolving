#include <iostream>
using namespace std;
int main() {
    int n,m;
    cin >> n >> m;
    int j ; 
    cin >> j;
    int left = 1;
    int right = m;
    int dap = 0;
    for (int i = 0 ; i < j; i++){
        int want;
        cin >> want;
        if (want>=left && want<=right) continue;
        else if (want < left){
            int move = left-want;
            left -= move;
            right -= move;
            dap+=move;
        }else{
            int move = want-right;
            left+=move;
            right+=move;
            dap+=move;
        }
    }
    cout << dap;
    
    return 0;
}