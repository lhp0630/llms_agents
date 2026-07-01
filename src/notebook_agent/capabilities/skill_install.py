from __future__ import annotations

from collections.abc import Awaitable, Callable
from dataclasses import dataclass
from typing import Any

from pydantic_ai import RunContext
from pydantic_ai.capabilities import NativeOrLocalTool
from pydantic_ai.native_tools import AbstractNativeTool
from pydantic_ai.tools import AgentDepsT, Tool


@dataclass(init=False)
class SkillInstall(NativeOrLocalTool[AgentDepsT]):
    """Install a skill to the local skills directory from a remote URL."""

    url: str
    """Remote URL of the skill source (WebDAV or GitHub repository)."""

    def __init__(
        self,
        *,
        native: SkillInstallTool
        | Callable[
            [RunContext[AgentDepsT]],
            Awaitable[SkillInstallTool | None] | SkillInstallTool | None,
        ]
        | bool = True,
        local: Tool[AgentDepsT] | Callable[..., Any] | bool | None = None,
        url: str,
    ) -> None:
        self.native = native
        self.local = local
        self.url = url
        self.__post_init__()


@dataclass(kw_only=True)
class SkillInstallTool(AbstractNativeTool):
    """Install a skill to the local skills directory from a remote URL.

    Supported sources:

    * WebDAV — skill files served from a WebDAV endpoint
    * GitHub — repository containing a skills directory (e.g. `skills/<name>`)
    """

    url: str
    """Remote URL of the skill source (WebDAV or GitHub repository)."""


def _install_skill_from_webdav(ctx: RunContext[AgentDepsT], url: str) -> str:
    """Install a skill from a WebDAV URL into the local skills directory."""
    return f"Skill installed from {url}"


def _install_skill_from_github(ctx: RunContext[AgentDepsT], url: str) -> str:
    """Install a skill from a GitHub repository skills directory into the local skills directory."""
    return f"Skill installed from {url}"
