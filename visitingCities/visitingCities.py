def minCost(red, blue, blueCost):
    ans = [0]
    
    dp_r = [0 for i in range(len(red)+1)]
    dp_b = [0 for i in range(len(blue)+1)]
    dp_b[0] = blueCost
    for i in range(1, len(red)+1):
        dp_r[i] = min(dp_r[i-1] + red[i-1], dp_b[i-1] + red[i-1]) # r2r, b2r
        dp_b[i] = min(dp_b[i-1] + blue[i-1], dp_r[i-1] + blue[i-1] + blueCost) # b2b, r2b
        ans.append(min(dp_r[i], dp_b[i]))
            
    return ans


if __name__ == "__main__":
    red = [2, 1, 4, 5]
    blue = [3, 2, 1, 2]
    blueCost = 2

    ans = minCost(red, blue, blueCost)
    print(ans)





