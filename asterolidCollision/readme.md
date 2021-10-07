# Asteroid Collision problem
![image](https://user-images.githubusercontent.com/25105806/136440943-364a841c-4b73-46d3-9e61-bcd1b5d45fac.png)

Leetcode link: https://leetcode.com/problems/asteroid-collision/

<br />

### Approach 1: Stack, asteroidCollision()
The idea is simply, we use stack to simulate the collision with incoming asteroid. If both asteroids are the same size, pop the top asteroid from stack and break the loop, if incoming asteroid is bigger, pop the top asteroid from stack and check the new top asteroid from the stack, if incoming asteroid is smaller, simply break the loop to simulate the exploded incoming asteroid.

```python
def asteroidCollision(self, asteroids: List[int]) -> List[int]:
    stack = list()
    for asteroid in asteroids:
        if len(stack)==0:
            stack.append(asteroid)
        else:
            # same dir
            if (stack[-1] > 0 and asteroid > 0) or (stack[-1] < 0 and asteroid < 0):
                stack.append(asteroid)
            else:
                # different dir
                if stack[-1]<0 and asteroid>0:
                    # will not meet
                    stack.append(asteroid)
                else:
                    asteroidExploded = False
                    while len(stack)>0 and asteroidExploded==False and stack[-1]>0 and asteroid<0:
                        if stack[-1] == abs(asteroid):
                            stack.pop()
                            asteroidExploded = True
                        elif stack[-1] < abs(asteroid):
                            stack.pop()
                        else:
                            asteroidExploded = True

                    if not asteroidExploded:
                        stack.append(asteroid)
    return stack
```


Time complexity is O(n):\
![image](https://user-images.githubusercontent.com/25105806/136441278-84495b2b-044b-41ff-9220-ed016b4429e6.png)
