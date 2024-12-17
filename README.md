# Lab 🧪


### Setup

Install dependencies:
```
uv sync
```

### Generate a problem directory

```bash
uv run problems/generate.py <problem_name>
```

<details>
    <summary>Example</summary>

```bash
uv run python problems/generate.py merge-sorted-array
```
</details>

### Run a problem approach

```bash
uv run python problems/runner.py <problem_name> <approach_number>
```

<details>
    <summary>Example</summary>

```bash
uv run python problems/runner.py merge-sorted-array 3
```
</details>
