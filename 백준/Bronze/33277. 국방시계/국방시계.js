const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split(' ');
let a =  1440*Number(input[1])/Number(input[0]);
let h = ~~(a/60);
let m = ~~(a%60);
if (h<10) h='0'+h;
if (m<10) m='0'+m;
console.log(`${h}:${m}`);