const fs = require ('fs');
const input = fs.readFileSync("/dev/stdin").toString().trim();
const di = {
    1996:'SPbSU',
    1997:'SPbSU',
    2000:'SPbSU',
    2006:'PetrSU, ITMO',
    2007:'SPbSU',
    2008:'SPbSU',
    2013:'SPbSU',
    2018:'SPbSU',
}

if (input in di){
    console.log(di[input])
}else{
    console.log("ITMO")
}