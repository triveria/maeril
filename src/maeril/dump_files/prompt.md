# Introduction

Please review the following project files thoroughly.
You will be assigned a related task afterward.

# Project Snapshot

## Directory Structure

[command: tree -I ".github|.git|tmp|*.egg-info|__pycache__|build|.pytest_cache" -af]

## File Contents

[codefile: prompt.py]

# Work Guidelines

-   Output the changed files in full to ensure your response can be compiled as is.
-   If requested to remove components, don't just comment them out but remove them. They are still available to the developer through git.
-   Don't add line numbers to your output. They are only here for the reader's guidance
-   Files must end with a newline
-   Don't use lambda functions. Use named functions
-   Always try to use best practises. Ask in case of uncertainty. Feel free to modify other parts of the existing code so that it adheres to best practises
-   When working on code: Focus on maintainability, clean code and the SOLID principle. Since we are working on this project for a long time, maintainability and readability is paramount!
-   Apply modern Coding practises and tech standards
-   Explain your work afterwards.

# Code Style Guidelines "Pragmatic Clarity"

**Philosophy:**
This guideline prioritizes code that is straightforward to read, understand, and maintain. It values explicitness, direct feedback on errors (in appropriate contexts), and focused commenting. The ultimate goal is to produce robust and efficient software by minimizing ambiguity and cognitive overhead for developers.

**I. Code Structure and Organization**

1.  **Modularity and Single Responsibility:**

    -   Functions, methods, and classes should aim to do one thing well.
    -   Break down complex logic into smaller, well-defined, and testable units.

2.  **Configuration Management:**

    -   **Avoid Global Mutable State for Configuration:** Configuration values should not be stored in global mutable variables.
    -   **Explicit Configuration Passing:** Prefer passing configuration explicitly to functions or classes that need it (e.g., via parameters, constructors).
    -   **Localized Configuration:** If configuration is specific to a module or a small set of functions, keep it localized within that scope (e.g., constants defined at the top of a module or within a class).
    -   **Immutable Constants:** Use named constants for fixed values.

3.  **Dependency Management:**
    -   Clearly define and manage dependencies.
    -   Minimize coupling between modules where possible.

**II. Clarity and Explicitness**

1.  **Readability Over Premature Optimization:** Write code that is easy to understand first. Optimize only when necessary and with clear profiling data.
2.  **Explicit is Better Than Implicit:**
    -   Avoid "magic" that obscures control flow or data origin.
    -   For a small, fixed number of distinct operations, explicit sequential calls can be clearer than a loop abstracting them, especially if the parameters or context for each call differ meaningfully. (e.g., setting up multiple distinct pipeline stages).
3.  **Naming Conventions:**
    -   Use clear, descriptive, and unambiguous names for variables, functions, classes, etc.
    -   Follow language-specific conventions (e.g., `snake_case` for Python, `camelCase` for JavaScript/Java) consistently.
    -   The name should reflect the entity's purpose and scope.

**III. Error Handling Philosophy**

1.  **Context-Dependent Error Handling:** The strategy for error handling depends on the nature of the software component.
    -   **Libraries, Frameworks, Long-Running Services:** Implement robust error handling. Catch specific exceptions, log detailed information, and attempt recovery or graceful degradation where appropriate. Provide clear error information to callers.
    -   **Scripts, Command-Line Tools, Internal Automation:**
        -   **"Crash Early, Crash Loudly" for Critical/Unexpected Errors:** For unrecoverable errors or unexpected states that indicate a bug or misconfiguration, allow the program to terminate immediately. Unhandled exceptions provide direct feedback and a full stack trace, which is invaluable for debugging.
        -   **Avoid Overly Broad Exception Catching:** Do not use generic `try-catch` blocks (e.g., `except: pass` or catching a base `Exception` type without specific reason) that can hide bugs or make debugging difficult. If an error is caught, it should be for a specific, understood reason (e.g., retrying a network request, providing a user-friendly message for expected failures).
    -   **Validate Inputs:** Validate inputs at boundaries (e.g., public API functions, user input processing) to fail fast if preconditions are not met.

**IV. Commenting and Documentation**

1.  **Purposeful Comments:**
    -   Comments should explain _why_ something is done or clarify complex, non-obvious logic.
    -   Document design decisions, trade-offs, or workarounds that aren't evident from the code itself.
2.  **Avoid Redundant Comments:**
    -   Do not comment on what the code clearly expresses. For example, `x = x + 1 // Increment x` is redundant.
    -   Well-named variables and functions reduce the need for comments.
3.  **Maintain Comments:** Ensure comments are kept up-to-date with code changes. Outdated comments are worse than no comments.
4.  **API Documentation:** Public APIs (functions, classes, modules intended for external use) should be clearly documented, explaining their purpose, parameters, return values, and any exceptions they might raise.

**V. Simplicity and Maintainability**

1.  **Keep It Simple, Stupid (KISS):** Prefer the simplest solution that effectively solves the problem. Avoid unnecessary complexity.
2.  **Don't Repeat Yourself (DRY):** Consolidate common logic into reusable functions or modules. Balance DRY with clarity; sometimes a little repetition is clearer than a convoluted abstraction.
3.  **Consistency:** Strive for a consistent coding style throughout the codebase. This makes the code easier to read and understand for everyone on the team.
4.  **Version Control:** Use version control (e.g., Git) effectively with clear, conventional commit messages.

**VI. Language-Specific Guidelines**

-   This guide provides general principles. Always adhere to established language-specific style guides (e.g., PEP 8 for Python, Google Style Guides for C++/Java/Go, etc.) for formatting, naming conventions, and idiomatic usage, unless a principle here explicitly suggests a higher-level deviation for a stated reason (like the "Crash Early" philosophy in specific contexts).

# Assignment

Fix all bugs
