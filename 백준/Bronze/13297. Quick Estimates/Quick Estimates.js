fs= require("fs");
input=fs.readFileSync("/dev/stdin").toString().split("\n");
let n = Number(input[0]);
for (let i = 1; i<=n;i++){
    let t = input[i];
    console.log(t.length)
}