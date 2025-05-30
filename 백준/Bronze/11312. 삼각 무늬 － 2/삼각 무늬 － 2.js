fs=require("fs");
input=fs.readFileSync("/dev/stdin").toString().split("\n");
let n =Number(input[0])
for (let i = 1; i <=n; i++){
    let li= input[i].split(" ").map(Number);
    let m= li[0]/li[1];
    console.log(m*m);
}