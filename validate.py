#!/usr/bin/env python3
"""Check that index.html is well-formed: every opened tag is closed in order.

Usage: python3 validate.py [path ...]   (defaults to index.html)
Exits non-zero on the first mismatched or unclosed tag.
"""
import html.parser
import sys

VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input",
        "link", "meta", "source", "track", "wbr"}


class Checker(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.errors = []

    def handle_starttag(self, tag, attrs):
        if tag not in VOID:
            self.stack.append((tag, self.getpos()))

    def handle_startendtag(self, tag, attrs):
        pass

    def handle_endtag(self, tag):
        if not self.stack or self.stack[-1][0] != tag:
            expected = self.stack[-1][0] if self.stack else "nothing"
            line, col = self.getpos()
            self.errors.append(
                f"line {line}, col {col}: closing </{tag}> but expected </{expected}>")
            return
        self.stack.pop()


def check(path):
    c = Checker()
    with open(path, encoding="utf-8") as f:
        c.feed(f.read())
    c.close()
    for tag, (line, col) in c.stack:
        c.errors.append(f"line {line}, col {col}: <{tag}> never closed")
    return c.errors


def main(argv):
    paths = argv[1:] or ["index.html"]
    failed = False
    for p in paths:
        errors = check(p)
        if errors:
            failed = True
            print(f"{p}: NOT well-formed")
            for e in errors:
                print(f"  {e}")
        else:
            print(f"{p}: well-formed")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
