#include <algorithm>
#include <deque>
#include <iostream>
#include <queue>
#include <vector>

using namespace std;

class Solution {
public:
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
};

int main() {
    Solution solver;
    // vector<vector<int>> tasks = {{19, 13}, {16, 9}, {21, 10}, {32, 25}, {37, 4}, {49, 24}, {2, 15}, {38, 41}, {37, 34}, {33, 6}, {45, 4}, {18, 18}, {46, 39}, {12, 24}};
    vector<vector<int>> tasks = {{1, 2}, {2, 4}, {3, 2}, {4, 1}};
    auto result = solver.getOrderMinHeap(tasks);
    for (auto const& time : result) {
        cout << time << " ";
    }
    cout << endl;
    return 0;
}