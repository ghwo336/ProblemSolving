fs=require("fs");
input=fs.readFileSync("/dev/stdin").toString().trim().split("\n");
let f = input[0].split(" ").map(Number);
let e = input[1].split(" ").map(Number);
if (f[1]<e[1] || (e[1]==f[1]&&e[2]>=f[2])) console.log(e[0]-f[0]);
else console.log(e[0]-f[0]-1);
console.log(e[0]-f[0]+1);
console.log(e[0]-f[0])