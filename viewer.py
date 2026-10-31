# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Build solutions.html: every codercise solution as a paste-ready snippet.

The snippet drops what the PennyLane site already provides or cannot run:
the uv script header, all top-level imports, and the `if __name__` demo block.
The demo block gets its own copy button, because a few codercises (such as
G.4.1b) put the answer at the top level, which these files keep under main.

Usage: uv run viewer.py  (writes solutions.html and opens it)
"""

import ast
import html
import re
import subprocess
import sys
import textwrap
from pathlib import Path

ROOT = Path(__file__).parent
OUT = ROOT / "solutions.html"
NAME_RE = re.compile(r"^([a-z])_(\d+)_(\d+)([a-z]?)_(.+)\.py$")


def is_main_guard(node):
    return (
        isinstance(node, ast.If)
        and isinstance(node.test, ast.Compare)
        and isinstance(node.test.left, ast.Name)
        and node.test.left.id == "__name__"
    )


def split_source(source):
    """Return (snippet, main_block) with the header, imports and main removed."""
    lines = source.splitlines()
    drop = set()

    if lines and lines[0].startswith("# /// script"):
        end = next(i for i, line in enumerate(lines[1:], 1) if line == "# ///")
        drop.update(range(end + 1))

    main_block = ""
    for node in ast.parse(source).body:
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            drop.update(range(node.lineno - 1, node.end_lineno))
        elif is_main_guard(node):
            drop.update(range(node.lineno - 1, node.end_lineno))
            body = lines[node.body[0].lineno - 1 : node.end_lineno]
            main_block = textwrap.dedent("\n".join(body)).strip()

    kept = "\n".join(line for i, line in enumerate(lines) if i not in drop)
    snippet = re.sub(r"\n{3,}", "\n\n\n", kept).strip()
    return snippet, main_block


def code_block(label, code):
    return (
        f'<div class="block"><div class="bar"><span>{label}</span>'
        f'<button type="button" class="copy">Copy</button></div>'
        f"<pre><code>{html.escape(code)}</code></pre></div>"
    )


def card(path):
    module, section, part, letter, slug = NAME_RE.match(path.name).groups()
    label = f"{module.upper()}.{section}.{part}{letter}"
    title = slug.replace("_", " ")
    snippet, main_block = split_source(path.read_text())

    blocks = code_block("Solution", snippet)
    if main_block:
        blocks += code_block("Main block", main_block)
    search = html.escape(f"{label} {path.stem} {title}".lower())
    return (
        f'<section class="card" id="{path.stem}" data-search="{search}">'
        f'<h2><span class="tag">{label}</span> {html.escape(title)}</h2>'
        f'<p class="file">{path.name}</p>{blocks}</section>'
    )


def sort_key(path):
    module, section, part, letter, _ = NAME_RE.match(path.name).groups()
    return module, int(section), int(part), letter


PAGE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Codercise Solutions</title>
<style>
:root {
  --bg: #f7f7f5; --card: #ffffff; --text: #1d1d1f; --muted: #6b6b70;
  --border: #e2e2de; --code: #f1f1ee; --accent: #3b5bdb; --ok: #2b8a3e;
}
@media (prefers-color-scheme: dark) {
  :root {
    --bg: #141416; --card: #1d1d20; --text: #e9e9ec; --muted: #9a9aa2;
    --border: #2e2e33; --code: #26262a; --accent: #8ea2ff; --ok: #69db7c;
  }
}
* { box-sizing: border-box; }
body {
  margin: 0; background: var(--bg); color: var(--text);
  font: 15px/1.5 system-ui, -apple-system, sans-serif;
}
header {
  position: sticky; top: 0; z-index: 1; background: var(--bg);
  border-bottom: 1px solid var(--border); padding: 12px 16px;
}
header .inner, main { max-width: 900px; margin: 0 auto; }
h1 { font-size: 18px; margin: 0 0 8px; }
input {
  width: 100%; padding: 8px 10px; font: inherit; color: var(--text);
  background: var(--card); border: 1px solid var(--border); border-radius: 6px;
}
main { padding: 16px; }
.card {
  background: var(--card); border: 1px solid var(--border);
  border-radius: 8px; padding: 14px 16px; margin-bottom: 14px;
}
.card h2 { font-size: 16px; margin: 0; text-transform: capitalize; }
.tag { color: var(--accent); font-variant-numeric: tabular-nums; }
.file { color: var(--muted); font-size: 13px; margin: 2px 0 10px; }
.block { margin-top: 8px; }
.bar {
  display: flex; justify-content: space-between; align-items: center;
  font-size: 13px; color: var(--muted); margin-bottom: 4px;
}
button {
  font: inherit; font-size: 13px; padding: 3px 12px; cursor: pointer;
  color: var(--text); background: var(--code);
  border: 1px solid var(--border); border-radius: 5px;
}
button.done { color: var(--ok); border-color: var(--ok); }
pre {
  margin: 0; padding: 10px 12px; overflow-x: auto; background: var(--code);
  border-radius: 6px; font: 13px/1.45 ui-monospace, Menlo, monospace;
}
.hidden { display: none; }
</style>
</head>
<body>
<header><div class="inner">
<h1>Codercise solutions</h1>
<input id="filter" type="search" placeholder="Filter, e.g. g.5 or diffusion" autofocus>
</div></header>
<main>
CARDS
</main>
<script>
const filter = document.getElementById("filter");
filter.addEventListener("input", () => {
  const q = filter.value.trim().toLowerCase();
  for (const card of document.querySelectorAll(".card")) {
    card.classList.toggle("hidden", !card.dataset.search.includes(q));
  }
});

async function copyText(text) {
  try {
    await navigator.clipboard.writeText(text);
  } catch {
    const area = document.createElement("textarea");
    area.value = text;
    document.body.append(area);
    area.select();
    document.execCommand("copy");
    area.remove();
  }
}

document.addEventListener("click", async (event) => {
  const button = event.target.closest("button.copy");
  if (!button) return;
  await copyText(button.closest(".block").querySelector("code").textContent);
  button.textContent = "Copied";
  button.classList.add("done");
  setTimeout(() => {
    button.textContent = "Copy";
    button.classList.remove("done");
  }, 1500);
});
</script>
</body>
</html>
"""


if __name__ == "__main__":
    files = sorted((p for p in ROOT.glob("*.py") if NAME_RE.match(p.name)), key=sort_key)
    OUT.write_text(PAGE.replace("CARDS", "\n".join(card(p) for p in files)))
    print(f"Wrote {OUT.name} with {len(files)} solutions")
    if "--no-open" not in sys.argv:
        subprocess.run(["open", str(OUT)], check=False)
