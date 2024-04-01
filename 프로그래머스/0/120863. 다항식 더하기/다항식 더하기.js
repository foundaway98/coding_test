function solution(polynomial) {
    let ps = polynomial.split(" + ")
    let x1 = 0
    let n = 0
    for(let p of ps){
        if (p[p.length - 1] === "x"){
            if(p.length === 1){
                x1 += 1 
            } else {
                x1 += parseInt(p.slice(0, p.length-1))
            }
        } else {
            n += parseInt(p)
        }
    }
    if(x1 === 0){
        if(n === 0){
            return
        } else {
            return n.toString()
        }
    }else if(x1 === 1){
        if(n === 0){
            return "x"
        } else {
            return "x" + " + " + n
        }
    }else{
        if(n === 0){
            return x1 + "x"
        } else {
            return x1 + "x" + " + " + n
        }
    }
    
}