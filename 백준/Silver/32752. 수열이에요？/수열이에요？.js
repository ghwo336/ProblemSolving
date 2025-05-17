fs=require("fs");
input=fs.readFileSync("/dev/stdin").toString().split("\n");
let [n,l,r]=input[0].split(" ").map(Number);
let li = input[1].split(" ").map(Number);
let liF = li.slice(0,l-1);
let liE = li.slice(r,n);
li.sort((a,b)=>a-b);
let liM = li.slice(l-1,r);
li=[...liF,...liM,...liE];
let pandan = 1;
 for (let i =1; i<li.length;i++){
     if (li[i-1]>li[i]) pandan=0
 }
console.log(pandan)
