from pydantic_ai_skills import CallableSkillScriptExecutor, LocalSkillScriptExecutor

from .container import run_script as run_script_via_container
from .sandbox import run_script as run_script_via_opensandbox

SkillScriptExecutor = CallableSkillScriptExecutor | LocalSkillScriptExecutor


OPENSANDBOX_SCRIPT_EXECUTOR = CallableSkillScriptExecutor(run_script_via_opensandbox)
CONTAINER_SCRIPT_EXECUTOR = CallableSkillScriptExecutor(run_script_via_container)
HOST_SCRIPT_EXECUTOR = LocalSkillScriptExecutor()


def create_script_executor() -> SkillScriptExecutor: ...
