function solution(a, b) {
    //31 29 31 30 31 30 31 31 30 31 30 31
    // 금 토 일 월 화 수 목
    let days = [31,29,31,30,31,30,31,31,30,31,30,31]
    let dow = ["THU","FRI","SAT","SUN","MON","TUE","WED"]
    let date = 0
    for(let i = 0; i<a-1; i++){
        date += days[i]
    }
    date += b
    return dow[date%7]
}