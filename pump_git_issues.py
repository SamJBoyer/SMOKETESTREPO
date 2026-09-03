"""Create GitHub issues from generate_goals.py smoke-test goals."""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
import time

from generate_goals import goals as ALL_GOALS

DEFAULT_REPO = "SamJBoyer/SMOKETESTREPO"
DEFAULT_LABEL = "agent-ready"
DEFAULT_COUNT = 100


def ensure_gh() -> None:
    if shutil.which("gh") is None:
        sys.exit("gh CLI is required and was not found on PATH")


def run_gh(args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["gh", *args],
        capture_output=True,
        text=True,
        encoding="utf-8",
    )


def ensure_label(repo: str, label: str) -> None:
    listed = run_gh(["label", "list", "--repo", repo, "--json", "name", "--jq", ".[].name"])
    if listed.returncode != 0:
        sys.exit(listed.stderr.strip() or "failed to list labels")
    names = {line.strip() for line in listed.stdout.splitlines() if line.strip()}
    if label in names:
        return
    created = run_gh(
        [
            "label",
            "create",
            label,
            "--repo",
            repo,
            "--description",
            "ready for autonomous implementation",
            "--color",
            "2939bc",
        ]
    )
    if created.returncode != 0:
        sys.exit(created.stderr.strip() or f"failed to create label {label}")


def create_issue(repo: str, title: str, body: str, label: str) -> str:
    last_error = ""
    for attempt in range(1, 6):
        result = run_gh(
            [
                "issue",
                "create",
                "--repo",
                repo,
                "--title",
                title,
                "--body",
                body,
                "--label",
                label,
            ]
        )
        if result.returncode == 0:
            return result.stdout.strip()
        last_error = (result.stderr or result.stdout).strip()
        time.sleep(min(2 ** attempt, 16))
    raise RuntimeError(last_error or "gh issue create failed")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Pump generate_goals.py tasks into GitHub issues with the agent-ready label."
    )
    parser.add_argument("--count", type=int, default=DEFAULT_COUNT, help="Number of issues to create")
    parser.add_argument("--offset", type=int, default=0, help="Skip this many goals from the start")
    parser.add_argument("--repo", default=DEFAULT_REPO, help="owner/name of the GitHub repo")
    parser.add_argument("--label", default=DEFAULT_LABEL, help="Label to apply to each issue")
    parser.add_argument("--dry-run", action="store_true", help="Print issues without creating them")
    args = parser.parse_args()

    selected = ALL_GOALS[args.offset : args.offset + args.count]
    if len(selected) < args.count:
        sys.exit(
            f"only {len(selected)} goals available after offset {args.offset} "
            f"(need {args.count})"
        )

    if args.dry_run:
        for i, goal in enumerate(selected, start=1):
            print(f"[dry-run] {i}/{args.count}: {goal}")
        return

    ensure_gh()
    ensure_label(args.repo, args.label)

    created = 0
    for i, goal in enumerate(selected, start=1):
        body = (
            f"{goal}\n\n"
            "This is an agent-ready smoke-test task generated from generate_goals.py."
        )
        url = create_issue(args.repo, goal, body, args.label)
        created += 1
        print(f"{i}/{args.count}: {url}")

    print(f"created {created} issues on {args.repo} with label {args.label}")


if __name__ == "__main__":
    main()
