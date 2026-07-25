from src.data.store import Task, store

def serialize_task(task: Task) -> dict:
    return {"id": task.id, "title": task.title, "completed": task.completed}

def create_task(owner_id: int, title: str) -> dict:
    if not title or len(title) > 120:
        raise ValueError("title must be 1-120 characters")
    return serialize_task(store.create_task(owner_id, title))
