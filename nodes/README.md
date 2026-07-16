# n8n Python Nodes

# Morpheus Nodes

This folder contains the Python implementation of the custom workflow nodes used by Morpheus.

The files are designed to run inside the n8n Python execution environment rather than as standalone Python scripts.

## Development notes

When opening these files in VS Code, Pylance may report warnings such as:

- `_item is not defined`
- `return outside function`

These warnings are expected.

Objects such as `_item` are injected by the n8n runtime and therefore are not available during static analysis.

The source code is intentionally kept compatible with the production workflow so each file can be copied directly into its corresponding n8n Python Code node.

## Available nodes

| Node | Description | Status |
|------|-------------|--------|
| detect_source.py | Detect the originating job board from an incoming email | ✅ |
| inspect_wttj_email.py | Extract the main fields from Welcome to the Jungle emails | ✅ |