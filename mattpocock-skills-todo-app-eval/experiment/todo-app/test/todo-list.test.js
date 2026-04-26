import assert from "node:assert/strict";
import test from "node:test";
import { createTodoList } from "../src/todo-list.js";

test("user can add todos and see active work", () => {
  const todos = createTodoList();

  const first = todos.add(" Ship research report ");
  const second = todos.add("Review skill design");

  assert.deepEqual(todos.list(), [
    { id: first.id, title: "Ship research report", completed: false },
    { id: second.id, title: "Review skill design", completed: false },
  ]);
  assert.deepEqual(todos.list({ filter: "active" }), [
    { id: first.id, title: "Ship research report", completed: false },
    { id: second.id, title: "Review skill design", completed: false },
  ]);
});

test("user can complete and filter todos", () => {
  const todos = createTodoList();
  const first = todos.add("Write tests");
  const second = todos.add("Refactor module");

  todos.toggle(first.id);

  assert.deepEqual(todos.list({ filter: "completed" }), [
    { id: first.id, title: "Write tests", completed: true },
  ]);
  assert.deepEqual(todos.list({ filter: "active" }), [
    { id: second.id, title: "Refactor module", completed: false },
  ]);
});

test("user can rename, remove, and clear completed todos", () => {
  const todos = createTodoList();
  const first = todos.add("Draft");
  const second = todos.add("Delete me");
  const third = todos.add("Done soon");

  todos.rename(first.id, "Final draft");
  todos.remove(second.id);
  todos.toggle(third.id);

  assert.equal(todos.clearCompleted(), 1);
  assert.deepEqual(todos.list(), [
    { id: first.id, title: "Final draft", completed: false },
  ]);
});

test("todo list rejects invalid user actions", () => {
  const todos = createTodoList();

  assert.throws(() => todos.add("   "), /title is required/);
  assert.throws(() => todos.add(123), /title must be a string/);
  assert.throws(() => todos.toggle(999), /does not exist/);
  assert.throws(() => todos.list({ filter: "archived" }), /Unknown todo filter/);
});
