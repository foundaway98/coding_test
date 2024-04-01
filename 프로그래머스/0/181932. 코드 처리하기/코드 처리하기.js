function solution(code) {
    let ret = []
    let mode = false
    for(let idx in code){
        if (code[idx] === "1"){
            mode = !mode
        } else if(mode){
            if(idx % 2 === 1){
                ret.push(code[idx])
            }
        } else if(!mode){
            if(idx%2 === 0){
                ret.push(code[idx])
            }
        }
    }
    return ret.length === 0 ? "EMPTY" : ret.join("")
    
}