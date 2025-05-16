fs=require("fs");
input = fs.readFileSync("/dev/stdin").toString().trim().split(" ");
let lv= Number(input[0])
let pan = input[1]
if (pan=="miss") console.log(0);
else if (pan=="bad") console.log(lv*200);
else if (pan=="cool") console.log(lv*400);
else if (pan=="great") console.log(lv*600);
else console.log(lv*1000);