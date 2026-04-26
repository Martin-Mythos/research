export function createTodoList() {
  let nextId = 1;
  let items = [];

  const snapshot = () => items.map((item) => ({ ...item }));
  const findExisting = (id) => {
    const item = items.find((candidate) => candidate.id === id);
    if (!item) {
      throw new Error(`Todo ${id} does not exist`);
    }
    return item;
  };

  return {
    add(title) {
      const normalizedTitle = normalizeTitle(title);
      const item = { id: nextId++, title: normalizedTitle, completed: false };
      items = [...items, item];
      return { ...item };
    },

    toggle(id) {
      findExisting(id);
      items = items.map((item) =>
        item.id === id ? { ...item, completed: !item.completed } : item,
      );
      return snapshot().find((item) => item.id === id);
    },

    rename(id, title) {
      findExisting(id);
      const normalizedTitle = normalizeTitle(title);
      items = items.map((item) =>
        item.id === id ? { ...item, title: normalizedTitle } : item,
      );
      return snapshot().find((item) => item.id === id);
    },

    remove(id) {
      findExisting(id);
      items = items.filter((item) => item.id !== id);
    },

    clearCompleted() {
      const removed = items.filter((item) => item.completed).length;
      items = items.filter((item) => !item.completed);
      return removed;
    },

    list({ filter = "all" } = {}) {
      if (!["all", "active", "completed"].includes(filter)) {
        throw new Error(`Unknown todo filter: ${filter}`);
      }

      const filtered = items.filter((item) => {
        if (filter === "all") return true;
        if (filter === "active") return !item.completed;
        return item.completed;
      });

      return filtered.map((item) => ({ ...item }));
    },
  };
}

function normalizeTitle(title) {
  if (typeof title !== "string") {
    throw new Error("Todo title must be a string");
  }

  const normalizedTitle = title.trim();
  if (!normalizedTitle) {
    throw new Error("Todo title is required");
  }

  return normalizedTitle;
}
