from reserved_commands import is_reserved_for_codex


def test_exact_x_approval_commands_are_reserved():
    assert is_reserved_for_codex("APPROVE X-20260608-004")
    assert is_reserved_for_codex("HOLD X-20260608-004")
    assert is_reserved_for_codex("REJECT X-20260608-004: wrong tone")


def test_natural_language_is_not_reserved():
    assert not is_reserved_for_codex("please approve X-20260608-004")
    assert not is_reserved_for_codex("APPROVE this")
