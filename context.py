#!/usr/bin/env python3
import json
import os
import sys

config_path = os.path.expanduser("~/.okteto/context/config.json")

try:
    with open(config_path) as f:
        d = json.load(f)

    cur = d.get("current-context", "")
    ctx = d.get("contexts", {})

    ns = ""
    if cur in ctx:
        ns = ctx[cur].get("namespace", "")
    else:
        for key in ctx:
            if cur in key or key in cur:
                ns = ctx[key].get("namespace", "")
                cur = key
                break

    if not cur or not ns:
        print(f"current-context '{cur}' not found in contexts", file=sys.stderr)
        print("available contexts:", file=sys.stderr)
        for key in ctx:
            print(f"  {key}", file=sys.stderr)
        sys.exit(1)

    url = cur.replace("https://", "")

    if "--prompt" in sys.argv:
        print(f"%F{{cyan}}⎈ {url}%f %F{{yellow}}({ns})%f ")
    else:
        print(f"context:   {url}")
        print(f"namespace: {ns}")

except FileNotFoundError:
    print(f"config not found: {config_path}", file=sys.stderr)
    sys.exit(1)
except json.JSONDecodeError as e:
    print(f"invalid JSON: {e}", file=sys.stderr)
    sys.exit(1)