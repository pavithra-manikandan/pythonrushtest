import importlib.util, sys, io

def load_rush(path):
    spec = importlib.util.spec_from_file_location("rush", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.rush

rush1 = load_rush("rush-1-1/rush.py")
rush2 = load_rush("rush-1-2/rush.py")
rush3 = load_rush("rush-1-3/rush.py")
rush4 = load_rush("rush-1-4/rush.py")
rush5 = load_rush("rush-1-5/rush.py")
# ── Helpers ────────────────────────────────────────────────────────────────
passed = 0
failed = 0

def capture_stdout(fn, x, y):
    buf = io.StringIO()
    old = sys.stdout; sys.stdout = buf
    fn(x, y)
    sys.stdout = old
    return buf.getvalue().strip()

def capture_stderr(fn, x, y):
    buf = io.StringIO()
    old = sys.stderr; sys.stderr = buf
    fn(x, y)
    sys.stderr = old
    return buf.getvalue().strip()

def test(label, fn, x, y, expected):
    global passed, failed
    result = capture_stdout(fn, x, y)
    if result == expected:
        print(f"  ✅  rush({x},{y}) — {label}")
        passed += 1
    else:
        print(f"  ❌  rush({x},{y}) — {label}")
        print(f"       Expected : {repr(expected)}")
        print(f"       Got      : {repr(result)}")
        failed += 1

def test_invalid(label, fn, x, y):
    global passed, failed
    err = capture_stderr(fn, x, y)
    out = capture_stdout(fn, x, y)
    if "Invalid size" in err and out == "":
        print(f"  ✅  rush({x},{y}) — {label}")
        passed += 1
    else:
        print(f"  ❌  rush({x},{y}) — {label}")
        print(f"       stderr : {repr(err)}")
        print(f"       stdout : {repr(out)}")
        failed += 1

def section(title):
    print(f"\n{'─'*50}")
    print(f"  {title}")
    print(f"{'─'*50}")

# ══════════════════════════════════════════════════════════════════════════
#  ASSIGNMENT 1  —  o - |
# ══════════════════════════════════════════════════════════════════════════
section("ASSIGNMENT 1  (o, -, |)")

# From the spec
test("spec: 5x3",          rush1, 5, 3, "o---o\n|   |\no---o")
test("spec: 5x1",          rush1, 5, 1, "o---o")
test("spec: 1x1",          rush1, 1, 1, "o")
test("spec: 1x5",          rush1, 1, 5, "o\n|\n|\n|\no")
test("spec: 4x4",          rush1, 4, 4, "o--o\n|  |\n|  |\no--o")

# Edge cases
test("2x2 tiny square",    rush1, 2, 2, "oo\noo")
test("2x1 wide single row",rush1, 2, 1, "oo")
test("1x2 tall single col",rush1, 1, 2, "o\no")
test("3x2 short wide",     rush1, 3, 2, "o-o\no-o")
test("10x1 long single row",rush1,10, 1, "o--------o")
test("1x10 tall single col",rush1, 1,10, "o\n|\n|\n|\n|\n|\n|\n|\n|\no")
test("large 8x5",          rush1, 8, 5, "o------o\n|      |\n|      |\n|      |\no------o")

# Invalid inputs
test_invalid("zero width",       rush1, 0, 5)
test_invalid("zero height",      rush1, 5, 0)
test_invalid("both zero",        rush1, 0, 0)
test_invalid("negative width",   rush1, -1, 3)
test_invalid("negative height",  rush1, 3, -1)
test_invalid("both negative",    rush1, -5, -5)

# ══════════════════════════════════════════════════════════════════════════
#  ASSIGNMENT 2  —  / \ *
# ══════════════════════════════════════════════════════════════════════════
section("ASSIGNMENT 2  (/, \\, *)")

# From the spec
test("spec: 5x3",          rush2, 5, 3, "/***\\\n*   *\n\\***/")
test("spec: 5x1",          rush2, 5, 1, "*****")
test("spec: 1x1",          rush2, 1, 1, "*")
test("spec: 1x5",          rush2, 1, 5, "*\n*\n*\n*\n*")
test("spec: 4x4",          rush2, 4, 4, "/**\\\n*  *\n*  *\n\\**/")

# Edge cases
test("2x2 tiny square",    rush2, 2, 2, "/\\\n\\/")
test("2x1 single row",     rush2, 2, 1, "**")
test("1x2 tall single col",rush2, 1, 2, "*\n*")
test("3x2 short wide",     rush2, 3, 2, "/*\\\n\\*/")
test("10x1 long single row",rush2,10, 1, "**********")
test("large 8x5",          rush2, 8, 5, "/******\\\n*      *\n*      *\n*      *\n\\******/")

# Invalid inputs
test_invalid("zero width",       rush2, 0, 5)
test_invalid("zero height",      rush2, 5, 0)
test_invalid("negative width",   rush2, -3, 3)
test_invalid("negative height",  rush2, 3, -3)

# ══════════════════════════════════════════════════════════════════════════
#  ASSIGNMENT 3  —  A top corners, C bottom corners, B edges
# ══════════════════════════════════════════════════════════════════════════
section("ASSIGNMENT 3  (A top, C bottom, B edges)")

# From the spec
test("spec: 5x3",          rush3, 5, 3, "ABBBA\nB   B\nCBBBC")
test("spec: 5x1",          rush3, 5, 1, "BBBBB")
test("spec: 1x1",          rush3, 1, 1, "B")
test("spec: 1x5",          rush3, 1, 5, "B\nB\nB\nB\nB")
test("spec: 4x4",          rush3, 4, 4, "ABBA\nB  B\nB  B\nCBBC")

# Edge cases
test("2x2",                rush3, 2, 2, "AA\nCC")
test("2x1",                rush3, 2, 1, "BB")
test("1x2",                rush3, 1, 2, "B\nB")
test("3x2",                rush3, 3, 2, "ABA\nCBC")
test("large 8x5",          rush3, 8, 5, "ABBBBBA\nB      B\nB      B\nB      B\nCBBBBBC")

# Invalid inputs
test_invalid("zero width",       rush3, 0, 5)
test_invalid("zero height",      rush3, 5, 0)
test_invalid("negative width",   rush3, -2, 2)
test_invalid("negative height",  rush3, 2, -2)

# ══════════════════════════════════════════════════════════════════════════
#  ASSIGNMENT 4  —  A left corners, C right corners (same top & bottom)
# ══════════════════════════════════════════════════════════════════════════
section("ASSIGNMENT 4  (A left, C right — mirrored rows)")

# From the spec
test("spec: 5x3",          rush4, 5, 3, "ABBBC\nB   B\nABBBC")
test("spec: 5x1",          rush4, 5, 1, "BBBBB")
test("spec: 1x1",          rush4, 1, 1, "B")
test("spec: 1x5",          rush4, 1, 5, "B\nB\nB\nB\nB")
test("spec: 4x4",          rush4, 4, 4, "ABBC\nB  B\nB  B\nABBC")

# Edge cases
test("2x2",                rush4, 2, 2, "AC\nAC")
test("2x1",                rush4, 2, 1, "BB")
test("1x2",                rush4, 1, 2, "B\nB")
test("3x2",                rush4, 3, 2, "ABC\nABC")
test("large 8x5",          rush4, 8, 5, "ABBBBC\nB      B\nB      B\nB      B\nABBBBC")

# Invalid inputs
test_invalid("zero width",       rush4, 0, 5)
test_invalid("zero height",      rush4, 5, 0)
test_invalid("negative width",   rush4, -2, 2)
test_invalid("negative height",  rush4, 2, -2)

# ══════════════════════════════════════════════════════════════════════════
#  ASSIGNMENT 5  —  A top-left & bottom-right, C top-right & bottom-left
# ══════════════════════════════════════════════════════════════════════════
section("ASSIGNMENT 5  (A↖ C↗ / C↙ A↘ — diagonal corners)")

# From the spec
test("spec: 5x3",          rush5, 5, 3, "ABBBC\nB   B\nCBBBA")
test("spec: 5x1",          rush5, 5, 1, "BBBBB")
test("spec: 1x1",          rush5, 1, 1, "B")
test("spec: 1x5",          rush5, 1, 5, "B\nB\nB\nB\nB")
test("spec: 4x4",          rush5, 4, 4, "ABBC\nB  B\nB  B\nCBBA")

# Edge cases
test("2x2",                rush5, 2, 2, "AC\nCA")
test("2x1",                rush5, 2, 1, "BB")
test("1x2",                rush5, 1, 2, "B\nB")
test("3x2",                rush5, 3, 2, "ABC\nCBA")
test("large 8x5",          rush5, 8, 5, "ABBBBC\nB      B\nB      B\nB      B\nCBBBBA")

# Invalid inputs
test_invalid("zero width",       rush5, 0, 5)
test_invalid("zero height",      rush5, 5, 0)
test_invalid("negative width",   rush5, -2, 2)
test_invalid("negative height",  rush5, 2, -2)

# ── Summary ────────────────────────────────────────────────────────────────
total = passed + failed
print(f"\n{'═'*50}")
print(f"  Results: {passed}/{total} passed", "🎉" if failed == 0 else "⚠️  fix the ❌ cases above")
print(f"{'═'*50}\n")