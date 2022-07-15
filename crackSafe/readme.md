# Decode Ways problem
![image](https://user-images.githubusercontent.com/25105806/179154083-3c55d53d-5612-4d11-b5e6-579c695ba20c.png)

Leetcode link: https://leetcode.com/problems/cracking-the-safe/

<br />

### Approach 1: Backtracking, backtrack()

The idea is to use backtrack to explore all possible ways of appending new characters. However, we need to make sure we don't add duplicate passwords in our path, so we have to maintain a hashset of seen passwords. When certain path does not contain all passwords, we backtrack.

The stopping condition for the recursion function is when the size of seen hashset contains `pow(k, n)` number of unique passwords.

```cpp
string crackSafeBacktrack(int n, int k) {
    string result(n, '0');
    set<string> seen = {result};
    bakctrack(n, k, result, seen);
    return result;
}

bool bakctrack(int n, int k, string& cur, set<string>& seen) {
    if (seen.size() == pow(k, n)) {
        return true;
    }

    for (int i = 0; i < k; i++) {
        cur.append(to_string(i));                          // append the new char
        string password = cur.substr(cur.length() - n, n); // get the newly formed password
        if (seen.count(password) == 0) {
            // newly formed password is not seen before, we can add it to the set and append next one recursively
            seen.insert(password);
            if (bakctrack(n, k, cur, seen)) {
                return true;
            }
            cur.pop_back();       // backtrack
            seen.erase(password); // backtrack
        } else {
            // the newly formed password is seen, we should try appending another char
            cur.pop_back();
        }
    }
    return false;
}
```

<br />

### Approach 2: hierholzer Algorithm, hierholzer()
