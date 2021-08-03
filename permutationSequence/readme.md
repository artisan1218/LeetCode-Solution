# Permutation Sequence problem
* The set `[1, 2, 3, ..., n]` contains a total of `n!` unique permutations.
* By listing and labeling all of the permutations in order, we get the following sequence for `n = 3`:
  ```
  "123"
  "132"
  "213"
  "231"
  "312"
  "321"
  ```
* Given `n` and `k`, return the `kth` permutation sequence.

### Approach 1: Brute Force, getPermutationPackage()
The easiest way to do is simply generate all possible permutations of the `n` in order and get the `kth` element of permutations. I do this by using the `itertools` package.\
Since it will generate all possible permutations which are not necessary, it's very slow and very inefficient

Running time:\
![0a50fc232004c86f23afa788416331c](https://user-images.githubusercontent.com/25105806/128086830-d1897e6a-ca69-41a6-ab1a-4839d37bc5fa.png)


### Approach 2: Work Outside In, getPermutationOutsideIn()
By observing the permutations, we can find that each permutation can be divided into the form of `digit + permutations(rest digits)` and they are all in order. 
For example, if we have `n = 4`, we have `{1, 2, 3, 4}`, if you were to list out all the permutations you have:
```
1 + (permutations of 2, 3, 4)
2 + (permutations of 1, 3, 4)
3 + (permutations of 1, 2, 4)
4 + (permutations of 1, 2, 3)
```
we can first get the outer digit of the permutation, then work outside in.
```
e.g. 
solving 1 + (permutations of 2, 3, 4) 
solving 2 + (permutations of 3, 4) 
solving 4 + (permutations of 3)
solving 3
```

How do we decide the which outer digit to append to `result`? We use `(k-1)/(number of outer digits permutation)`\
If `n=4, k=2` and we are solving the outer most digit, which means we need to know which digit does the result start with. \
There are `factorial(n-1)` permutations that start with same digit, so we calcualte `(k-1)//factorial(n-1)` to get the ith number of permutations, which is the outer digit. Then remove the added digit from digit set, update `k` with `k = k % factorial(n-1)` and calculate again until we've added all `n` numbers.

Running time:
![3ef5bdb91c83a39ab5b5e40bb5d1e30](https://user-images.githubusercontent.com/25105806/128087973-627b8357-33d5-4319-9eda-fd03cd0e222a.png)
