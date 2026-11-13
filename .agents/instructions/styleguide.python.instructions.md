---
applyTo: "**/*.py"
---

# Python style

Formatting and linting are enforced by ruff. Do not hand-format or restate those rules here.

Maintainability, readability and simplicity are paramount. Understandable code is preferred over compact code. It is fine to repeat yourself if that makes the code simpler.

## Libraries

-   Prefer `pathlib` over `os` / `os.path` wherever possible.
-   Use the standard library instead of reinventing the wheel (e.g. the `logging` module for logging).
-   Use `pandas` instead of the `csv` library.
-   Keep coding style and library usage consistent across the whole module (e.g. never mix `pandas` and `csv`).
-   Use regular expressions as sparingly as possible. They are hard to read and maintain and therefore error prone. Prefer string methods, `pathlib`, or `pandas` string operations.

## Structure

-   Split long files into modules.
-   Use global variables only where absolutely needed.
-   Prefer concrete `list` types for batches of items; avoid generic `Iterable` and callback `Callable` types in small scripts.
-   Use separate `match`-based functions for distinct groups of related commands.
-   Use explicit branches per category so new categories cannot fall through into unrelated behavior.
-   Avoid `try`/`except` blocks; validate inputs before operations that may fail.

## Readability

-   Use descriptive names and avoid generic ones such as `data`, `result`, `tmp` or `handle`.
-   Use named booleans instead of inline compound conditions.
-   Do not nest function calls (no `foo(bar())`). Assign the inner result to a named variable first.
-   Prefer named intermediate variables over computed values embedded in return statements.
-   Prefer explicit statements over comprehensions when working with fixed fields.
-   Use short-circuit boolean operators only to keep `if` nesting shallow, not to execute code cleverly.
-   The code should explain itself. Write comments only where needed and aim for self-explanatory code instead.
-   Keep functions and encoding steps readable rather than compressing them into dense expressions.
-   Do not impose an arbitrary 80-column width; use the project's 320-column width.

## Maintenance

-   Renames, signature changes, and changed defaults need every call site checked.
