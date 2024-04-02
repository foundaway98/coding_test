const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];
let result = ""
rl.on('line', function (line) {
    input = line.split("")
}).on('close',function(){
    for(let item of input){
        if(item.toUpperCase() === item){
            result += item.toLowerCase()
        } else {
            result += item.toUpperCase()
        }
    }
    console.log(result)
    
});