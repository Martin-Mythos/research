# QA Session Output

This artifact applies the `qa` skill's user-facing issue template to the todo app experiment. No real GitHub issues were created because this is a self-contained research project.

## Issue 1: Empty todo list accepts an unknown filter

## What happened

When the todo list had no items, requesting an unsupported filter such as `archived` returned an empty list instead of reporting that the filter was invalid.

## What I expected

Unsupported filters should always be rejected, regardless of whether the todo list currently has items.

## Steps to reproduce

1. Create a new todo list.
2. Ask for todos with the `archived` filter.
3. Observe that the app returns an empty list instead of an error.

## Additional context

This was found by the behavior test `todo list rejects invalid user actions`. The fix was to validate the filter before applying it to the current item collection.

## Issue 2: No persistence boundary exists yet

## What happened

The experiment implements only an in-memory todo list. A user interface or CLI would lose todos when the process reloads.

## What I expected

A product-grade todo app should define whether persistence is local storage, a file, a database, or intentionally out of scope.

## Steps to reproduce

1. Create a todo list.
2. Add several todos.
3. Dispose of the todo list instance.
4. Create a new todo list instance.
5. Observe that previous todos are not available.

## Additional context

This is not a bug in the experiment scope. It is a product boundary that should be made explicit before expanding beyond a domain-module demo.
