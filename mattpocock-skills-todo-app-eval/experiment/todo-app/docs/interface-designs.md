# Todo App Interface Designs

This document applies the `design-an-interface` skill pattern to a small todo app domain module.

## Requirements

- Callers are tests and a possible UI layer.
- The module should support adding todos, toggling completion, editing titles, removing items, clearing completed items, and filtering by completion state.
- The module should hide id generation and immutable state updates.
- The test surface should stay behavior-focused and avoid internal data structure coupling.

## Design A: Minimal Command Surface

```js
const todos = createTodoList();
todos.dispatch({ type: "add", title: "Ship report" });
todos.dispatch({ type: "toggle", id: 1 });
todos.visible("completed");
```

This exposes one mutation method and one query method. It hides command routing and state transitions, but callers must learn command shapes and invalid command errors.

## Design B: Explicit Domain Methods

```js
const todos = createTodoList();
const item = todos.add("Ship report");
todos.toggle(item.id);
todos.list({ filter: "completed" });
```

This exposes a small set of verbs that match user behavior. It is easy to read in tests and hides id generation, normalization, and immutable update mechanics.

## Design C: Functional Reducer

```js
let state = createTodoState();
state = reduceTodos(state, { type: "add", title: "Ship report" });
selectTodos(state, { filter: "completed" });
```

This is easy to serialize and framework-friendly, but pushes state plumbing into every caller.

## Chosen Design

Design B is the best fit for this experiment because the behavior tests read like user capabilities while the implementation can remain private. It also aligns with the `tdd` skill guidance to test public behavior rather than implementation details.
