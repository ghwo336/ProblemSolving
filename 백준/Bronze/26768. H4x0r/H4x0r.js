const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim();
const di = {
    'a':'4',
    'e':'3',
    'i':'1',
    'o':'0',
    's':'5'
}
let dap=''
const n = input.length;
for (let i = 0 ; i < n; i++){
    if (input[i] in di){
        dap+=di[input[i]]
    }
    else dap+=input[i]
}

console.log(dap)