from typing import Optional

from nonebot import get_plugin_config
from pydantic import BaseModel


class ConfigModel(BaseModel):
    proxy: Optional[str] = None

    akinator_child_mode: bool = False
    akinator_language: str = "cn"
    akinator_text_mode: bool = False


config = get_plugin_config(ConfigModel)
