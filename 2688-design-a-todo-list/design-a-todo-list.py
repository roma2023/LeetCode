class TodoList:

    def __init__(self):
        self.tasks = defaultdict(list)
        self.users = defaultdict(list)
        self.tags = defaultdict(list)
        self.taskId = 1

    def addTask(self, userId: int, taskDescription: str, dueDate: int, tags: List[str]) -> int:
        self.tasks[self.taskId] = (taskDescription, dueDate, False)
        self.users[userId].append(self.taskId)
        self.tags[self.taskId].extend(tags)
        self.taskId += 1
        return self.taskId - 1

    def getAllTasks(self, userId: int) -> List[str]:
        tasks = self.users[userId]
        result = []
        for task in tasks:
            if task in self.tasks:
                desc, date, complete = self.tasks[task]
                if not complete:
                    result.append((date, task, desc))
        sorted_tasks = sorted(result, key = lambda x:x[0])
        return [desc for date, task, desc in sorted_tasks]

    def getTasksForTag(self, userId: int, tag: str) -> List[str]:
        tasks = self.users[userId]
        result = []
        for task in tasks:
            if task in self.tasks and tag in self.tags[task]:
                desc, date, complete = self.tasks[task]
                if not complete:
                    result.append((date, task, desc))
        sorted_tasks = sorted(result, key = lambda x:x[0])
        return [desc for date, task, desc in sorted_tasks]

    def completeTask(self, userId: int, taskId: int) -> None:
        tasks = self.users[userId]
        if taskId in tasks:
            desc, date, complete = self.tasks[taskId]
            self.tasks[taskId] = (desc, date, True)

# Time complexity:
# O(nlogn) (Sorting)

# Space complexity:
# O(n)
# Your TodoList object will be instantiated and called as such:
# obj = TodoList()
# param_1 = obj.addTask(userId,taskDescription,dueDate,tags)
# param_2 = obj.getAllTasks(userId)
# param_3 = obj.getTasksForTag(userId,tag)
# obj.completeTask(userId,taskId)