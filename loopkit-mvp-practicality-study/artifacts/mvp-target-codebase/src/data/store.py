from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Optional

@dataclass
class User:
    id: int
    username: str
    password_hash: str

@dataclass
class Task:
    id: int
    owner_id: int
    title: str
    completed: bool = False

class InMemoryStore:
    def __init__(self) -> None:
        self.users: Dict[int, User] = {}
        self.tasks: Dict[int, Task] = {}
        self._next_user_id = 1
        self._next_task_id = 1

    def reset(self) -> None:
        self.__init__()

    def create_user(self, username: str, password_hash: str) -> User:
        if any(u.username == username for u in self.users.values()):
            raise ValueError("username already exists")
        user = User(self._next_user_id, username, password_hash)
        self.users[user.id] = user
        self._next_user_id += 1
        return user

    def find_user_by_username(self, username: str) -> Optional[User]:
        return next((u for u in self.users.values() if u.username == username), None)

    def get_user(self, user_id: int) -> Optional[User]:
        return self.users.get(user_id)

    def create_task(self, owner_id: int, title: str) -> Task:
        task = Task(self._next_task_id, owner_id, title)
        self.tasks[task.id] = task
        self._next_task_id += 1
        return task

    def list_tasks(self, owner_id: int) -> List[Task]:
        return [t for t in self.tasks.values() if t.owner_id == owner_id]

    def get_task(self, task_id: int, owner_id: int) -> Optional[Task]:
        task = self.tasks.get(task_id)
        if task is None or task.owner_id != owner_id:
            return None
        return task

    def update_task(self, task_id: int, owner_id: int, completed: bool) -> Optional[Task]:
        task = self.get_task(task_id, owner_id)
        if task is None:
            return None
        task.completed = completed
        return task

store = InMemoryStore()
