# Single-Threaded CPU problem
![image](https://user-images.githubusercontent.com/25105806/170844851-c0495cf8-933f-4654-bc37-d17b81618028.png)

Leetcode link: https://leetcode.com/problems/single-threaded-cpu/

<br />


### Approach 1: Brute Force, getOrderBruteForce()

The idea is pretty simple: we simply simulate the whole process and find out the order. There are several things to keep in mind that the tasks might not come in order of the `enqueueTime` so we have to sort the `tasks` list. The final result is the index of the task in original unsorted `tasks` list, so we have to find a away to perserve the original indices.

In this solution, the original indices of tasks are appended to each task so we can know the index even after sorting. We use `time` variable to represent the current time and add all tasks with smaller `enqueueTime` to `availableTasks` list, which means tasks are waiting to be executed. 

```cpp
vector<int> getOrderBruteForce(vector<vector<int>>& tasks) {
    // perserve the original index
    for (int i = 0; i < tasks.size(); i++) {
        tasks[i].push_back(i);
    }
    sort(tasks.begin(),
         tasks.end(),
         [](const std::vector<int>& a, const std::vector<int>& b) {
             return a[0] < b[0];
         });

    deque<int> newTasks;
    for (int i = 0; i < tasks.size(); i++) {
        newTasks.push_back(i);
    }
    vector<int> result;
    vector<int> availableTasks;
    long time = tasks[0][0];
    while (newTasks.size() != 0 || availableTasks.size() != 0) {
        // add all available tasks to list
        while (newTasks.size() != 0 && time >= tasks.at(newTasks.front()).at(0)) {
            availableTasks.push_back(newTasks.front());
            newTasks.pop_front();
        }

        if (availableTasks.size() != 0) {
            // find the execution order of the available tasks
            int nextTask = -1;
            int minProcessingTime = INT_MAX;
            int index = 0;
            int taskIndex = INT_MAX;
            for (int i = 0; i < availableTasks.size(); i++) {
                if (tasks[availableTasks[i]][1] <= minProcessingTime) {
                    if (tasks[availableTasks[i]][1] < minProcessingTime) {
                        taskIndex = tasks[availableTasks[i]][2];
                        minProcessingTime = tasks[availableTasks[i]][1];
                        nextTask = tasks[availableTasks[i]][2];
                        index = i;
                    } else {
                        if (tasks[availableTasks[i]][2] < taskIndex) {
                            taskIndex = tasks[availableTasks[i]][2];
                            minProcessingTime = tasks[availableTasks[i]][1];
                            nextTask = tasks[availableTasks[i]][2];
                            index = i;
                        }
                    }
                }
            }
            time = time + tasks[availableTasks[index]][1];
            availableTasks.erase(availableTasks.begin() + index); // remove the executed task
            result.push_back(nextTask);
        } else {
            // advance time directly to the enqueue time of next task
            time = tasks[newTasks[0]][0];
        }
    }

    return result;
}
```

The brute force solution will lead to TLE, no surprise.

<br />

### Approach 2: Min-Heap, getOrderMinHeap()

Reference: https://www.youtube.com/watch?v=RR1n-d4oYqE

The most time consuming part of the first approach is the part of deciding the next task to execute. In the brute force solution we looped through all tasks every time we need to find a new task to execute. However, we can achieve this by using a min-heap(priority queue), which will automatically put the min value on top of the tree structure so that we can get that value quickly. 

In c++, the min-heap can be built by providing a customized comparator function to a priority queue. 
```cpp
// customized comparator for min heap:
// first compare processing time
// if processing time are equal, then compare index
struct twoDimComparator {
    bool operator()(const vector<int>& v1, const vector<int>& v2) {
        if (v1[0] == v2[0]) {
            return v1[1] > v2[1];
        } else {
            return v1[0] > v2[0];
        }
    }
};
```

We are comparing to values instead of one because we need to find the task first by the minimum processin time and if the processing time are equal, we need to compare the task index and pick the smaller one. 

Notice that we don't push the `enqueueTime` of a task to the heap because we don't need the `enqueueTime` once we added the task to heap. So the first element of a task becomes the `processingTime` and second element is the `taskID`.

Full code:
```cpp
vector<int> getOrderMinHeap(vector<vector<int>>& tasks) {
    // perserve the original index
    for (int i = 0; i < tasks.size(); i++) {
        tasks[i].push_back(i);
    }
    // sort the tasks based on enqueue time
    sort(tasks.begin(),
         tasks.end(),
         [](const std::vector<int>& a, const std::vector<int>& b) {
             return a[0] < b[0];
         });

    // customized comparator for min heap:
    // first compare processing time
    // if processing time are equal, then compare index
    struct twoDimComparator {
        bool operator()(const vector<int>& v1, const vector<int>& v2) {
            if (v1[0] == v2[0]) {
                return v1[1] > v2[1];
            } else {
                return v1[0] > v2[0];
            }
        }
    };
    vector<int> result;
    priority_queue<vector<int>, vector<vector<int>>, twoDimComparator> availTasks;
    int i = 0;
    long time = tasks[0][0]; // address overflow
    while (availTasks.size() != 0 or i < tasks.size()) {
        // add all available tasks to min heap
        while (i < tasks.size() && time >= tasks[i][0]) {
            // no need to push enqueue time to the heap
            // so {taskDuration, taskID}
            availTasks.push({tasks[i][1], tasks[i][2]});
            i++;
        }

        if (availTasks.size() == 0) {
            // advance time directly to the enqueue time of next task
            time = tasks[i][0];
        } else {
            // pop the task with min processing time
            int procTime = availTasks.top()[0];
            int taskID = availTasks.top()[1];
            availTasks.pop();
            time += procTime;
            result.push_back(taskID);
        }
    }

    return result;
}
```

Time complexity is O(nlogn) where sorting takes O(nlogn) and heap take O(logn):\
![image](https://user-images.githubusercontent.com/25105806/170845145-190c7468-1342-45e5-ba32-9bd8e4a9a9b6.png)
