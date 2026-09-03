"""Generate 1000 unique smoke-test goals for a git repo."""

from __future__ import annotations

import csv
from pathlib import Path

goals: list[str] = []


def add(goal: str) -> None:
    goal = " ".join(goal.split())
    if goal not in goals:
        goals.append(goal)


# --- File creation: common names ---
file_stems = [
    "hello", "test", "readme", "notes", "todo", "sample", "demo", "output",
    "input", "data", "log", "tmp", "temp", "scratch", "draft", "ping",
    "pong", "foo", "bar", "baz", "alpha", "beta", "gamma", "delta", "omega",
    "start", "end", "main", "index", "config", "settings", "manifest",
    "changelog", "license", "authors", "contributors", "credits", "status",
    "version", "info", "about", "summary", "report", "results", "metrics",
    "checklist", "agenda", "minutes", "outline", "plan", "spec", "requirements",
    "faq", "help", "usage", "guide", "howto", "tips", "hints", "examples",
    "snippet", "fragment", "piece", "blob", "payload", "message", "greeting",
    "welcome", "goodbye", "ok", "ready", "alive", "health", "probe", "smoke",
    "canary", "beacon", "marker", "flag", "token", "key", "id", "uuid",
    "count", "total", "sum", "list", "items", "names", "titles", "labels",
    "tags", "words", "lines", "numbers", "digits", "letters", "alphabet",
    "colors", "shapes", "animals", "fruits", "cities", "countries", "days",
    "months", "seasons", "weather", "quote", "poem", "story", "haiku",
    "empty", "blank", "placeholder", "dummy", "stub", "fixture", "seed",
    "bootstrap", "init", "setup", "teardown", "cleanup", "done", "finished",
    "success", "failure", "error", "warn", "debug", "trace", "verbose",
    "quiet", "silent", "echo", "print", "write", "copy", "backup", "archive",
    "snapshot", "checkpoint", "save", "cache", "buffer", "queue", "stack",
    "left", "right", "north", "south", "east", "west", "up", "down",
    "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
    "first", "second", "third", "fourth", "fifth", "last", "next", "prev",
    "old", "new", "final", "latest", "current", "original", "copy1", "copy2",
    "a", "b", "c", "x", "y", "z", "n", "m", "p", "q", "r", "s", "t", "u", "v", "w",
    "file1", "file2", "file3", "file4", "file5", "file10", "file100",
    "doc1", "doc2", "note1", "note2", "test1", "test2", "test3",
    "hello_world", "hello-world", "my_file", "my-file", "user_notes",
    "project_info", "repo_status", "git_notes", "agent_test", "smoke_test",
    "quickstart", "getting_started", "release_notes", "known_issues",
    "roadmap", "backlog", "sprint", "task", "issue", "bug", "feature",
    "idea", "brainstorm", "scratchpad", "whiteboard", "clipboard",
]

extensions = [
    "txt", "md", "csv", "json", "yml", "yaml", "toml", "ini", "cfg", "conf",
    "log", "dat", "lst", "out", "in", "tsv", "xml", "html", "css", "js",
    "py", "sh", "bat", "ps1", "sql", "rst", "adoc", "nfo", "env", "gitignore",
]

for stem in file_stems:
    add(f'Create a file called {stem}.txt')

for stem in ["hello", "test", "notes", "demo", "sample", "data", "config", "readme", "todo", "log"]:
    for ext in ["md", "csv", "json", "yml", "log", "dat"]:
        add(f"Create a file called {stem}.{ext}")

# numbered files
for i in range(1, 51):
    add(f"Create a file called file_{i:03d}.txt")

for i in range(1, 21):
    add(f"Create a file named smoke{i}.txt")
    add(f"Make a new file called probe-{i}.md")

# --- Content writes ---
contents = [
    ("hello.txt", "hello"),
    ("hello.txt", "hello world"),
    ("hello.txt", "Hello, world!"),
    ("test.txt", "ok"),
    ("test.txt", "test"),
    ("ping.txt", "pong"),
    ("status.txt", "ready"),
    ("status.txt", "ok"),
    ("alive.txt", "yes"),
    ("health.txt", "healthy"),
    ("message.txt", "smoke test"),
    ("greeting.txt", "hi"),
    ("answer.txt", "42"),
    ("count.txt", "1"),
    ("flag.txt", "true"),
    ("flag.txt", "false"),
    ("mode.txt", "test"),
    ("env.txt", "dev"),
    ("name.txt", "smoke"),
    ("title.txt", "Smoke Test"),
    ("quote.txt", "The quick brown fox jumps over the lazy dog"),
    ("abc.txt", "abcdefghijklmnopqrstuvwxyz"),
    ("digits.txt", "0123456789"),
    ("newline.txt", "line one"),
    ("blank.txt", ""),
    ("space.txt", " "),
    ("tab.txt", "a\\tb"),
    ("csv_sample.csv", "id,name"),
    ("people.csv", "name,age"),
    ("items.csv", "item,qty"),
    ("config.json", "{}"),
    ("config.json", '{"ok": true}'),
    ("settings.json", '{"mode": "test"}'),
    ("list.json", "[]"),
    ("version.txt", "1.0.0"),
    ("date.txt", "2026-09-03"),
    ("year.txt", "2026"),
    ("lang.txt", "en"),
    ("color.txt", "blue"),
    ("animal.txt", "cat"),
    ("fruit.txt", "apple"),
    ("city.txt", "Boston"),
    ("ok.md", "# OK"),
    ("readme.md", "# Smoke Test"),
    ("notes.md", "- note one"),
    ("todo.md", "- [ ] first task"),
    ("LICENSE.txt", "MIT"),
    ("AUTHORS.txt", "Smoke Tester"),
    ("echo.txt", "echo"),
    ("repeat.txt", "repeat repeat"),
]

for filename, text in contents:
    if text == "":
        add(f"Create an empty file called {filename}")
    else:
        add(f'Create a file called {filename} containing "{text}"')
        add(f'Write "{text}" to a new file named {filename}')

# extra content variants
phrases = [
    "alpha", "bravo", "charlie", "delta", "echo", "foxtrot", "golf", "hotel",
    "india", "juliet", "kilo", "lima", "mike", "november", "oscar", "papa",
    "quebec", "romeo", "sierra", "tango", "uniform", "victor", "whiskey",
    "xray", "yankee", "zulu", "red", "green", "blue", "yellow", "orange",
    "purple", "black", "white", "gray", "monday", "tuesday", "wednesday",
    "thursday", "friday", "saturday", "sunday", "spring", "summer", "autumn",
    "winter", "cat", "dog", "bird", "fish", "apple", "banana", "cherry",
    "pass", "fail", "skip", "retry", "done",
]
for phrase in phrases:
    add(f'Create a file called {phrase}.txt with the text "{phrase}"')

# --- Directories ---
dir_names = [
    "src", "lib", "bin", "tmp", "temp", "out", "output", "dist", "build",
    "docs", "doc", "notes", "data", "assets", "static", "public", "private",
    "config", "configs", "scripts", "tools", "tests", "test", "spec",
    "fixtures", "samples", "examples", "vendor", "third_party", "logs",
    "cache", "backup", "archive", "drafts", "inbox", "outbox", "misc",
    "alpha", "beta", "gamma", "one", "two", "three", "a", "b", "c",
    "folder", "dir", "directory", "workspace", "work", "scratch",
    "smoke", "probes", "canaries", "markers", "files", "stuff",
    "nested", "inner", "outer", "left", "right", "top", "bottom",
    "input", "results", "reports", "metrics", "status", "health",
]
for name in dir_names:
    add(f"Create a directory called {name}")
    add(f"Make a new folder named {name}")

# nested dirs
nested = [
    "src/utils", "src/lib", "src/app", "docs/guides", "docs/api",
    "test/unit", "test/fixtures", "data/raw", "data/processed",
    "a/b", "a/b/c", "one/two/three", "tmp/scratch", "out/logs",
    "config/local", "assets/images", "scripts/hooks", "notes/daily",
    "smoke/probes", "files/txt", "work/drafts", "archive/old",
]
for path in nested:
    add(f"Create the nested directory {path}")
    add(f"Create a folder path {path}")

# file inside directory
pairs = [
    ("src", "main.py"),
    ("src", "index.js"),
    ("src", "app.txt"),
    ("docs", "readme.md"),
    ("docs", "guide.md"),
    ("test", "test.txt"),
    ("test", "smoke.txt"),
    ("data", "sample.csv"),
    ("data", "input.json"),
    ("tmp", "scratch.txt"),
    ("notes", "today.md"),
    ("config", "settings.yml"),
    ("logs", "app.log"),
    ("output", "result.txt"),
    ("scripts", "run.sh"),
    ("assets", "info.txt"),
    ("examples", "hello.txt"),
    ("fixtures", "seed.json"),
    ("reports", "summary.md"),
    ("inbox", "message.txt"),
    ("a", "b.txt"),
    ("folder", "file.txt"),
    ("work", "draft.md"),
    ("smoke", "probe.txt"),
    ("probes", "ping.txt"),
]
for folder, filename in pairs:
    add(f"Create a directory called {folder} and put a file named {filename} inside it")
    add(f"Create the file {folder}/{filename}")
    add(f"Create {folder}/{filename} containing \"ok\"")

# --- Multiple files ---
multi = [
    "hello.txt and test.txt",
    "a.txt, b.txt, and c.txt",
    "one.txt and two.txt",
    "readme.md and notes.txt",
    "input.txt and output.txt",
    "foo.txt, bar.txt, and baz.txt",
    "ping.txt and pong.txt",
    "left.txt and right.txt",
    "start.txt and end.txt",
    "alpha.txt and beta.txt",
    "config.json and settings.yml",
    "todo.md and done.md",
    "file1.txt, file2.txt, and file3.txt",
    "sample.csv and sample.json",
    "log1.txt and log2.txt",
]
for item in multi:
    add(f"Create two or more files: {item}")
    add(f"Create the files {item}")

for i in range(2, 11):
    add(f"Create {i} empty text files named n1.txt through n{i}.txt")

# --- Simple git-repo friendly tasks ---
git_goals = [
    "Create a file called .gitignore that ignores *.log",
    "Create a file called .gitignore containing node_modules",
    "Create a file called .gitignore containing dist/",
    "Create a file called .editorconfig with indent_size = 2",
    "Create a file called .nvmrc containing 20",
    "Create a file called .python-version containing 3.12",
    "Create a file called requirements.txt containing pytest",
    "Create a file called package.json containing {}",
    "Create a file called Makefile with a hello target that echoes hi",
    "Create a file called Dockerfile containing FROM alpine",
    "Create a file called Procfile containing web: echo hi",
    "Create a file called LICENSE containing MIT",
    "Create a file called CODEOWNERS containing * @owner",
    "Create a file called CONTRIBUTING.md with the heading Contributing",
    "Create a file called SECURITY.md with the heading Security",
    "Create a README.md with the heading Smoke Test Repo",
    "Create a CHANGELOG.md with an Unreleased section",
    "Create a file called pyproject.toml containing [project]",
    "Create a file called cargo.toml containing [package]",
    "Create a file called go.mod containing module smoke",
    "Create a file called Gemfile containing source rubygems",
    "Create a file called composer.json containing {}",
    "Create a file called tsconfig.json containing {}",
    "Create a file called eslint.config.js containing export default []",
    "Create a file called .prettierrc containing {}",
    "Create a file called .eslintrc.json containing {}",
    "Create a file called jest.config.js containing module.exports = {}",
    "Create a file called vitest.config.ts containing export default {}",
    "Create a file called docker-compose.yml containing version: '3'",
    "Create a file called .dockerignore containing node_modules",
    "Create a file called .gitattributes containing * text=auto",
    "Create a file called NOTICE.txt containing Smoke Test",
    "Create a file called THIRD_PARTY_NOTICES.txt containing none",
    "Create a file called robots.txt containing User-agent: *",
    "Create a file called humans.txt containing Smoke Tester",
    "Create a file called sitemap.txt containing /",
    "Create a file called CNAME containing example.test",
    "Create a file called now.json containing {}",
    "Create a file called vercel.json containing {}",
    "Create a file called netlify.toml containing [build]",
    "Create a file called Procfile.dev containing web: echo hi",
    "Create a file called runtime.txt containing python-3.12",
    "Create a file called Aptfile containing curl",
    "Create a file called nixpacks.toml containing [phases.setup]",
    "Create a file called .tool-versions containing python 3.12",
    "Create a file called .ruby-version containing 3.3.0",
    "Create a file called .node-version containing 20",
    "Create a file called .terraform-version containing 1.8.0",
    "Create a file called .java-version containing 21",
    "Create a file called .sdkmanrc containing java=21",
]
for g in git_goals:
    add(g)

# --- Tiny code files ---
code_goals = [
    'Create a Python file called hello.py that prints "hello"',
    'Create a Python file called add.py that prints 1 + 1',
    'Create a Python file called name.py that prints __name__',
    "Create a Python file called pass.py that only contains pass",
    "Create a Python file called const.py that sets X = 1",
    'Create a JavaScript file called hello.js that logs "hello"',
    "Create a JavaScript file called add.js that logs 1 + 1",
    "Create an HTML file called index.html with a title of Smoke",
    "Create an HTML file called page.html with a single paragraph saying hi",
    "Create a CSS file called style.css that sets body color to black",
    "Create a SQL file called schema.sql that creates a table named items",
    "Create a SQL file called seed.sql that inserts one row into items",
    'Create a shell script called hello.sh that echoes "hello"',
    "Create a PowerShell script called hello.ps1 that writes hello",
    "Create a batch file called hello.bat that echoes hello",
    "Create a JSON file called users.json with an empty array",
    "Create a YAML file called config.yml with key mode set to test",
    "Create a TOML file called config.toml with key mode = test",
    "Create an INI file called app.ini with a [main] section",
    "Create a CSV file called people.csv with header name,age and one row",
    "Create a TSV file called people.tsv with header name and age",
    "Create a Markdown file called list.md with three bullet points",
    "Create a Markdown file called table.md with a two-column table",
    "Create a Markdown file called link.md that links to example.com",
    "Create a text file called numbered.txt with the numbers 1 to 5 each on their own line",
    "Create a text file called alphabet.txt with letters A to E each on their own line",
    "Create a text file called countdown.txt with the numbers 5 down to 1",
    "Create a text file called repeated.txt with the word smoke on 3 lines",
    "Create a file called mixed.txt with two lines: hello and world",
    "Create a file called indented.txt with a line that starts with two spaces",
]
for g in code_goals:
    add(g)

# --- Copy / rename / delete / append (self-contained) ---
mutate = [
    "Create a file called original.txt with the text original, then copy it to copy.txt",
    "Create a file called source.txt with the text source, then copy it to dest.txt",
    "Create a file called old.txt with the text old, then rename it to new.txt",
    "Create a file called before.txt with the text before, then rename it to after.txt",
    "Create a file called temp.txt, then delete it",
    "Create a file called disposable.txt with the text gone, then delete it",
    "Create a file called log.txt with the text start, then append the text end",
    "Create a file called notes.txt with the text first, then append the text second",
    "Create a file called counter.txt containing 1, then overwrite it with 2",
    "Create a file called draft.txt containing draft, then replace the contents with final",
    "Create files a.txt and b.txt, then delete b.txt",
    "Create a file called keep.txt and a file called drop.txt, then delete drop.txt",
    "Create a folder called tmpdir and a file tmpdir/x.txt, then delete the file",
    "Create a file called upper.txt containing hello, then change the contents to HELLO",
    "Create a file called trim.txt containing hello world, then change it to hello",
    "Create a file called swap.txt containing left, then change it to right",
    "Create a file called build.txt containing one, then append two, then append three",
    "Create a file called seed.txt containing seed, then copy it to seed.bak",
    "Create a file called data.txt containing data, then copy it to backup/data.txt",
    "Create a file called move_me.txt containing move, then move it into a folder called moved",
]
for g in mutate:
    add(g)

# --- Lists / structured data ---
structured = [
    "Create a CSV file called colors.csv with a header color and three color names",
    "Create a CSV file called fruits.csv with a header fruit and the rows apple, banana, cherry",
    "Create a CSV file called numbers.csv with a header n and the numbers 1, 2, and 3",
    "Create a JSON file called point.json with keys x and y set to 0",
    "Create a JSON file called person.json with name set to Ada and age set to 36",
    "Create a JSON file called flags.json with ok set to true",
    "Create a YAML list file called pets.yml with cat and dog",
    "Create a Markdown checklist called chores.md with two unchecked items",
    "Create a Markdown file called headings.md with an h1 and an h2",
    "Create a file called urls.txt with three example URLs, one per line",
    "Create a file called emails.txt with two example email addresses, one per line",
    "Create a file called paths.txt listing src, docs, and test, one per line",
    "Create a file called env.example containing KEY=value",
    "Create a file called .env.example containing MODE=test",
    "Create a file called secrets.example containing TOKEN=replace-me",
    "Create a file called ports.txt containing 8080",
    "Create a file called host.txt containing localhost",
    "Create a file called url.txt containing http://127.0.0.1:3000",
]
for g in structured:
    add(g)

# --- More unique create-file variants with adjectives / prefixes ---
prefixes = [
    "tmp_", "test_", "demo_", "sample_", "new_", "old_", "final_", "draft_",
    "my_", "our_", "user_", "repo_", "git_", "agent_", "smoke_", "probe_",
]
bases = [
    "note", "file", "doc", "log", "data", "list", "item", "record", "entry",
    "page", "sheet", "card", "memo", "brief", "blurb", "label", "tag",
]
for p in prefixes:
    for b in bases[:8]:
        add(f"Create a file called {p}{b}.txt")

# --- Explicit empty / whitespace / size ---
special = [
    "Create an empty file called empty.txt",
    "Create an empty file called zero.txt",
    "Create an empty file called blank.md",
    "Create an empty file called none.dat",
    "Create a file called spaces.txt that contains only a single space",
    "Create a file called newline_only.txt that contains only a newline",
    "Create a file called two_lines.txt with two empty lines",
    "Create a file called hello_nl.txt with hello followed by a newline",
    "Create a file called no_ext named LICENSE",
    "Create a file with no extension called AUTHORS",
    "Create a file with no extension called VERSION",
    "Create a hidden file called .hidden",
    "Create a hidden file called .keep",
    "Create a hidden file called .smoke",
    "Create a hidden file called .probe containing ok",
    "Create a file called file with spaces.txt",
    "Create a file called 'hello world.txt'",
    "Create a file called kebab-case-name.txt",
    "Create a file called snake_case_name.txt",
    "Create a file called CamelCaseName.txt",
    "Create a file called UPPER.txt",
    "Create a file called lower.txt",
    "Create a file called MixedCase.txt",
    "Create a file called file.with.dots.txt",
    "Create a file called 123.txt",
    "Create a file called 001.txt",
    "Create a file called 42.txt containing 42",
    "Create a file called utf8.txt containing cafe",
    "Create a file called emoji.txt containing ok",
]
for g in special:
    add(g)

# --- README / docs variants ---
docs = [
    "Create a README.md that says this is a smoke test",
    "Create a README.txt that says hello",
    "Create a docs/README.md with the heading Docs",
    "Create a file called HOWTO.md with one short instruction",
    "Create a file called FAQ.md with one question and answer",
    "Create a file called INSTALL.md with the heading Install",
    "Create a file called USAGE.md with the heading Usage",
    "Create a file called ARCHITECTURE.md with one sentence",
    "Create a file called DECISIONS.md with one bullet",
    "Create a file called OWNERS.md containing smoke",
]
for g in docs:
    add(g)

# --- Calendar / sequential names ---
months = [
    "jan", "feb", "mar", "apr", "may", "jun",
    "jul", "aug", "sep", "oct", "nov", "dec",
]
for m in months:
    add(f"Create a file called {m}.txt")
    add(f"Create a notes file called notes-{m}.md")

days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
for d in days:
    add(f"Create a file called {d}.txt")
    add(f"Create a log file called {d}.log")

# --- Remaining filler: unique numbered probes with distinct verbs ---
verbs = [
    "Create", "Make", "Add", "Write", "Generate", "Put",
]
objects = [
    "a text file", "a markdown file", "a log file", "a data file",
    "a notes file", "a sample file", "a probe file", "a marker file",
]
for i in range(1, 200):
    verb = verbs[i % len(verbs)]
    obj = objects[i % len(objects)]
    add(f"{verb} {obj} called goal_{i:04d}.txt")
    if len(goals) >= 1100:
        break

# Deduplicate while preserving order already handled by add()
assert len(goals) >= 1000, len(goals)
goals = goals[:1000]
assert len(set(goals)) == 1000


def write_csv(path: Path | None = None) -> Path:
    out = path or Path(__file__).with_name("smoke_test_goals.csv")
    with out.open("w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "goal"])
        for i, goal in enumerate(goals, start=1):
            writer.writerow([i, goal])
    return out


if __name__ == "__main__":
    out = write_csv()
    print(f"wrote {len(goals)} goals to {out}")
    print("first 5:")
    for g in goals[:5]:
        print(" -", g)
    print("last 5:")
    for g in goals[-5:]:
        print(" -", g)
