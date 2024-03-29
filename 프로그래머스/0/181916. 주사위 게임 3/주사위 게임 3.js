function solution(a, b, c, d) {
    let dp = {}
    dp[a] = dp[a] > 0 ? dp[a] + 1 : 1 
    dp[b] = dp[b] > 0 ? dp[b] + 1 : 1
    dp[c] = dp[c] > 0 ? dp[c] + 1 : 1
    dp[d] = dp[d] > 0 ? dp[d] + 1 : 1
    const dpk = Object.keys(dp)
    if(dpk.length === 1){
        return dpk[0] * 1111
    } else if(dpk.length === 2){
        let isThree = false
        let threeIdx = 0
        for(let i = 0; i<dpk.length;i++){
            if (dp[dpk[i]] == 3){
                isThree = true
                threeIdx = i
                break
            }
        }
        if(isThree){
            return (10 * parseInt(dpk[threeIdx]) + parseInt(dpk[1-threeIdx])) * (10 * parseInt(dpk[threeIdx]) + parseInt(dpk[1-threeIdx]))
        } else {
            return (parseInt(dpk[0]) + parseInt(dpk[1])) * Math.abs(parseInt(dpk[0]) - parseInt(dpk[1]))
        }
    } else if(dpk.length === 3){
        let ones = []
        for(let i = 0; i<dpk.length; i++){
            if(dp[dpk[i]] === 1){
                ones.push(i)
            }
        }
        return (parseInt(dpk[ones[0]]) * parseInt(dpk[ones[1]]))
    } else {
        return parseInt(dpk[0])
        
    }
}