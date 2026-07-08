import os
import shutil
from dotenv import load_dotenv

load_dotenv()

FEISHU_APP_ID = os.environ["FEISHU_APP_ID"]
FEISHU_APP_SECRET = os.environ["FEISHU_APP_SECRET"]

def _resolve_cli(env_name: str, binary_name: str) -> str:
    configured = os.getenv(env_name)
    if configured:
        expanded = os.path.expanduser(configured)
        if os.path.exists(expanded):
            return expanded
        detected = shutil.which(binary_name)
        if detected:
            print(
                f"[config] {env_name} points to missing path {expanded}; using {detected}",
                flush=True,
            )
            return detected
        return expanded
    return shutil.which(binary_name) or binary_name


CLAUDE_CLI = _resolve_cli("CLAUDE_CLI_PATH", "claude")
CODEX_CLI = _resolve_cli("CODEX_CLI_PATH", "codex")
CODEX_HOME = os.path.expanduser(os.getenv("CODEX_HOME", "~/.codex"))

DEFAULT_MODEL = os.getenv("DEFAULT_MODEL", "claude-opus-4-6")
DEFAULT_CWD = os.path.expanduser(os.getenv("DEFAULT_CWD", "~"))
PERMISSION_MODE = os.getenv("PERMISSION_MODE", "bypassPermissions")

SESSIONS_DIR = os.path.expanduser(os.getenv("SESSIONS_DIR", "~/.lark-claude"))
PROJECTS_ROOT = os.path.expanduser(os.getenv("PROJECTS_ROOT", "~/projects"))
AGENT_HUB_ROOT = os.path.expanduser(os.getenv("AGENT_HUB_ROOT", os.path.join(PROJECTS_ROOT, "_agent-hub")))

# 访客分级：不在 OWNER_OPEN_IDS 里的发送者只能用受限只读 Claude。
# OWNER_OPEN_IDS 为空 = 所有人都是 owner（向后兼容）。
OWNER_OPEN_IDS = [v.strip() for v in os.getenv("OWNER_OPEN_IDS", "").split(",") if v.strip()]
GUEST_CWD = os.path.expanduser(os.getenv("GUEST_CWD", PROJECTS_ROOT))
GUEST_ALLOWED_TOOLS = [v.strip() for v in os.getenv("GUEST_ALLOWED_TOOLS", ",".join([
    "WebSearch",
    "WebFetch",
    "Bash(lark-cli calendar +freebusy:*)",
    "Bash(lark-cli calendar +agenda:*)",
    "Bash(lark-cli calendar +suggestion:*)",
])).split(",") if v.strip()]


def is_owner(open_id: str) -> bool:
    return not OWNER_OPEN_IDS or open_id in OWNER_OPEN_IDS


# 群聊里是否只在被 @ 时回复（默认开）。设 GROUP_REQUIRE_MENTION=false 恢复全量回复。
GROUP_REQUIRE_MENTION = os.getenv("GROUP_REQUIRE_MENTION", "true").strip().lower() in ("1", "true", "yes")


BOT_MENTION_OPEN_IDS = [v.strip() for v in os.getenv("BOT_MENTION_OPEN_IDS", "").split(",") if v.strip()]
OTHER_BOT_MENTION_OPEN_IDS = [v.strip() for v in os.getenv("OTHER_BOT_MENTION_OPEN_IDS", "").split(",") if v.strip()]

COLLAB_COORDINATOR_AGENT = os.getenv("COLLAB_COORDINATOR_AGENT", "codex").strip().lower()
COLLAB_CLAUDE_MODEL = os.getenv("COLLAB_CLAUDE_MODEL", "claude-sonnet-4-6")
COLLAB_CODEX_MODEL = os.getenv("COLLAB_CODEX_MODEL", "gpt-5.4")

# 卡片按钮回调 HTTP 端口（需 ngrok 暴露）
CALLBACK_PORT = int(os.getenv("CALLBACK_PORT", "9981"))

# 流式卡片更新：每积累多少字符推送一次
STREAM_CHUNK_SIZE = int(os.getenv("STREAM_CHUNK_SIZE", "20"))
