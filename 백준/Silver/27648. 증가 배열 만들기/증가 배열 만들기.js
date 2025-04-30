const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split(' ');
let n=Number(input[0]);
let m=Number(input[1]);
let k=Number(input[2]);
if(n+m-1<=k){
    console.log("YES");
    for (let i=1; i<=n;i++){
        let row= [];
        for (let j=1;j<=m;j++){
            row.push(j+i-1);
        }
        console.log(row.join(" "));
    }
}
else{
    console.log("NO")
}