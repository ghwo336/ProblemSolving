fs=require("fs")
input=fs.readFileSync("/dev/stdin").toString().split("\n");
let n = Number(input[0])
for (let i=1;i<=n;i++){
    Number(input[i][input[i].length-1])%2==0?console.log("even"):console.log("odd")
}