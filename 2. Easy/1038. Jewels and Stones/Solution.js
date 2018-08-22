const numJewelsInStones = function (J, S) {
    let [jewels, cnt] = [new Set(J), 0]
    for (let i in S) {
        if (jewels.has(S[i])) cnt++
    }
    return cnt
}
