def solution(sizes):
    walletMax = max(sizes[0])
    walletMin = min(sizes[0])
    for cardSize in sizes:
        cardMax = max(cardSize)
        cardMin = min(cardSize)
        if cardMax <= walletMax and cardMin <= walletMin:
            continue
        elif cardMax <= walletMax and cardMin > walletMin:
            walletMin = cardMin
        elif cardMax > walletMax and cardMin <= walletMin:
            walletMax = cardMax
        elif cardMax > walletMax and cardMin > walletMin:
            walletMax = cardMax
            walletMin = cardMin
    
    
    return walletMax*walletMin