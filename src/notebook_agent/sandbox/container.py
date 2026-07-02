from typing import Any

from pydantic_ai_skills import SkillScript


def run_script(
    script: SkillScript,
    args: dict[str, Any] | None = None,
    ctx: Any | None = None,
) -> Any: ...
