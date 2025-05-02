const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim();
const n= Number(input)
dp=[1,1,1]
for (let i=2;i<n;i++){
    let k=dp[2]
    dp[2]=(dp[2]+dp[1])%1000000007
    dp[1]=k  
}
console.log(dp[2],n-2)
