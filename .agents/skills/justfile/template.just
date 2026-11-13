# Project task runner. Run `just` to list recipes.
#
# Conventions:
#   - One-line comment above every recipe; `just --list` prints it.
#   - `check` is the commit gate and mirrors .pre-commit-config.yaml.
#   - `all` is the push gate: `check` plus the slow suite.
#   - Recipes are non-interactive so agents and CI can run them.

set shell := ["bash", "-uc"]

mod some-subdir-with-justfile

# Show available recipes (default).
[private]
default:
    @just --list --list-submodules

# Install toolchains and dependencies (one-time setup).
setup:
    # TODO: install dependencies, e.g. `pnpm install`, `cargo fetch`
    @true

# Build the shippable artifact.
build:
    # TODO: invoke the build script or toolchain
    @true

# Format sources in place.
fmt:
    # TODO: e.g. `cargo fmt --all`, `dprint fmt`
    @true

# Check formatting and lint without modifying sources.
lint:
    # TODO: e.g. `cargo fmt --all --check` then `cargo clippy --all-targets -- -D warnings`
    @true

# Run the fast unit test suite.
test-unit:
    # TODO: e.g. `cargo test -p <crate>`
    @true

# Run the integration or browser test suite.
test-integration:
    # TODO: e.g. `./scripts/test-integration.sh`
    @true

# Run all commit gates: lint and the fast test layers.
check: lint test-unit

# Run every check and the slow suite.
all: check test-integration

# Remove generated outputs.
clean:
    # TODO: e.g. `cargo clean`, `rm -rf dist`
    @true
