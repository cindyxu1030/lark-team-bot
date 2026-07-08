import re


_X_APPROVAL_COMMAND = re.compile(
    r"^(?:APPROVE\s+X-\d{8}-\d{3}|HOLD\s+X-\d{8}-\d{3}|"
    r"REJECT\s+X-\d{8}-\d{3}(?::\s*.+)?)$",
    re.IGNORECASE,
)


def is_reserved_for_codex(text: str) -> bool:
    """Commands that have a single deterministic owner in the shared Lark group."""
    return bool(_X_APPROVAL_COMMAND.fullmatch((text or "").strip()))
