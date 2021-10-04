# Scramble String problem
![image](https://user-images.githubusercontent.com/25105806/133915286-055196bc-6451-4624-817e-142c576b81d4.png)


### Approach 1: Recursion, isScramble()
The key here is to cut both `s1` and `s2` at the same length and compare the same part to see if they are equal. We use recursion to cut the left and right part recursively to exhuast all possible cuttings and permutations.
```
For example s1=great and s2=rgeat

cut at index 1, we have
g reat    r geat
since g!=r, so it is not possible

cut at index 2, we have
gr eat    rg eat
    cut at index 1, we have
    g r, r g and g g, r r
    so gr = rg
since eat = eat, so this is valid
```


```
For example s1=great and s2=rgtea

cut at index 1, we have
g reat    r gtea
since g!=r, it is not possible

cut at index 2, we have
gr eat    rg tea
    for gr and rg
      cut at index 1, we have
      g r, r g and g g, r r
      so gr = rg
    for eat and tea
      cut at index 1, we have
      e t and at ea
      since e!=t, this is not valid
      e a and at te is not not valid
      
      cut at index 2, we have
      ea te and t a OR ea ea and t t
      ea ea and t t is valid
      so eat=tea
since gr = rg and eat = tea, this is valid
```
To speed up, we use memorization to avoid checking already checked pairs of (s1, s2)


Actual running time:\
![image](https://user-images.githubusercontent.com/25105806/133915499-a87786d8-a3dc-4d11-a006-9758c2d6a036.png)


