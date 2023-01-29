# Simplify Path problem
* Given a string `path`, which is an absolute path (starting with a slash `'/'`) to a file or directory in a Unix-style file system, convert it to the simplified canonical path.
* In a Unix-style file system, a period `'.'` refers to the current directory, a double period `'..'` refers to the directory up a level, and any multiple consecutive slashes (i.e. `'//'`) are treated as a single slash `'/'`. For this problem, any other format of periods such as `'...'` are treated as file/directory names.
* The canonical path should have the following format:
  1. The path starts with a single slash `'/'`.
  2. Any two directories are separated by a single slash `'/'`.
  3. The path does not end with a trailing `'/'`.
  4. The path only contains the directories on the path from the root directory to the target file or directory (i.e., no period `'.'` or double period `'..'`)
* Return the simplified canonical path.


### Approach 1: Str Traversal, simplifyPath()
First observation is that the slash `'/'` does not mean anything in the path, it is just a separator, so we can remove it by using `.split('\')`. We can use stack to represent the canonical path. Then there are several cases to consider:
1. `'..'`: we need to pop the last element out of the stack
2. directory: simply append this directory to the result stack
3. `''` or `'.'`: do nothing

Actual running time:\
![76f239b542b051121a38f9754311ef1](https://user-images.githubusercontent.com/25105806/130373435-dc553b1b-c557-47d0-98bb-402d61ad033a.png)
