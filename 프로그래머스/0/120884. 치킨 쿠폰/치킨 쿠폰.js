function solution(chicken) {
    let coupon = chicken
    let answer = 0
    while(coupon > 9){
        let sc = parseInt(coupon/10)
        answer += sc
        coupon = sc + coupon % 10
    }
    return answer
}