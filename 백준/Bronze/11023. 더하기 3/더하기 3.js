fs=require("fs");
input=fs.readFileSync("/dev/stdin").toString().split(" ").map(Number);
console.log(input.reduce((acc,cur)=>acc+cur,0));