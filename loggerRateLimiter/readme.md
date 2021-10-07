# Logger Rate Limiter problem
![image](https://user-images.githubusercontent.com/25105806/136318512-8151eb55-3899-4c29-a504-ded82f258063.png)

<br />

### Approach 1: shouldPrintMessage()
The idea is simple, use a dict to store the message and its timestamp, then update the timestamp if the message is printed otherwise do nothing:

```python
class Logger:
    def __init__(self):
        self.timestampMap = dict()
       
    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.timestampMap:
            result = timestamp >= self.timestampMap[message]
            if result==True:
                self.timestampMap[message] = timestamp + 10
            return result
        else:
            self.timestampMap[message] = timestamp+10
            return True

```

Time complexity is O(n):\
![image](https://user-images.githubusercontent.com/25105806/136318664-6fed88f6-ef6d-4e02-b693-1161400d03a6.png)
