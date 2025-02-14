from wraptext import indent, dedent

ROUNDTRIP_CASES = [
    # basic test case
    "Hi.\nThis is a test.\nTesting.",
    # include a blank line
    "Hi.\nThis is a test.\n\nTesting.",
    # include leading and trailing blank lines
    "\nHi.\nThis is a test.\nTesting.\n",
]

WINDOWS_CASES = [
    # use windows line endings
    "Hi.\r\nThis is a test.\r\nTesting.",
    # pathological case
    "Hi.\r\nThis is a test.\n\r\nTesting.\r\n\n",
]


def test_indent_nomargin_default() -> None:
    # indent should do nothing if 'prefix' is empty.
    for text in ROUNDTRIP_CASES:
        assert indent(text, "") == text
    for text in WINDOWS_CASES:
        assert indent(text, "") == text


def test_roundtrip_spaces() -> None:
    # A whitespace prefix should roundtrip with dedent
    for text in ROUNDTRIP_CASES:
        assert dedent(indent(text, "    ")) == text


def test_roundtrip_tabs() -> None:
    # A whitespace prefix should roundtrip with dedent
    for text in ROUNDTRIP_CASES:
        assert dedent(indent(text, "\t\t")) == text


def test_roundtrip_mixed() -> None:
    # A whitespace prefix should roundtrip with dedent
    for text in ROUNDTRIP_CASES:
        assert dedent(indent(text, " \t  \t ")) == text


def test_indent_default() -> None:
    # Test default indenting of lines that are not whitespace only
    prefix = "  "
    expected = [
        # Basic test case
        "  Hi.\n  This is a test.\n  Testing.",
        # Include a blank line
        "  Hi.\n  This is a test.\n\n  Testing.",
        # Include leading and trailing blank lines
        "\n  Hi.\n  This is a test.\n  Testing.\n",
    ]
    for text, expect in zip(ROUNDTRIP_CASES, expected):
        assert indent(text, prefix) == expect
    expected = [
        # Use Windows line endings
        "  Hi.\r\n  This is a test.\r\n  Testing.",
        # Pathological case
        "  Hi.\r\n  This is a test.\n\r\n  Testing.\r\n\n",
    ]
    for text, expect in zip(WINDOWS_CASES, expected):
        assert indent(text, prefix) == expect


def indented_text_should_have_the_same_number_of_lines_as_the_original_text() -> None:
    texts = ["foo\nbar", "foo\nbar\n", "foo\nbar\nbaz"]
    for original in texts:
        indented = indent(original, "")
        assert indented == original
