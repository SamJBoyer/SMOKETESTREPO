This is a worktest for agents to implement simple git smoketests.

## Usage

`pump_git_issues.py` imports smoke-test goals from `generate_goals.py` and creates a GitHub issue for each selected goal.

**Prerequisites**

- Python 3
- GitHub CLI (`gh`) on `PATH` and authenticated

**Examples**

Dry run first (prints issues, does not create them or call `gh`):

```bash
python3 pump_git_issues.py --dry-run
```

Create issues for real:

```bash
python3 pump_git_issues.py
```

**Flags**

| Flag | Default | Meaning |
| --- | --- | --- |
| `--count` | `100` | Number of issues to create |
| `--offset` | `0` | Skip this many goals from the start of the list |
| `--repo` | `SamJBoyer/SMOKETESTREPO` | Target GitHub repo (`owner/name`) |
| `--label` | `agent-ready` | Label applied to each issue (created if missing) |
| `--dry-run` | off | Print the selected issues without creating them |

The script exits if fewer goals remain after `--offset` than `--count`. A real run requires `gh`, creates the label when it is missing, then creates one labeled issue per selected goal.
