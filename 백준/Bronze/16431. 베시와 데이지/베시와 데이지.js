fs=require("fs");
input=fs.readFileSync("/dev/stdin").toString().trim().split("\n");
let bessie=input[0].split(' ').map(Number);
let daisy=input[1].split(' ').map(Number);
let john=input[2].split(' ').map(Number);
let b = Math.max(Math.abs(bessie[0]-john[0]),Math.abs(bessie[1]-john[1]));
let d = Math.abs(daisy[0]-john[0])+Math.abs(daisy[1]-john[1])
if (b==d) console.log("tie");
else if (b>d) console.log("daisy")
else console.log("bessie")

