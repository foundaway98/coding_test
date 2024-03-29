function solution(numer1, denom1, numer2, denom2) {
    var answer = [];
    
    let u = numer1 * denom2 + numer2 * denom1
    let d = denom1 * denom2
    
    let max = Math.max(u,d)
    for (let i = max; max > 1; max--){
        if(u%max === 0 && d%max === 0){
            return[u/max, d/max]
        }
    }
    
    return [u,d];
}