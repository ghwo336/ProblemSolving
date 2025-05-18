fs=require("fs");
input=fs.readFileSync("/dev/stdin").toString()
let li =input.split(' ').map(Number);
li.sort((a,b)=>a-b);
console.log(li[1])