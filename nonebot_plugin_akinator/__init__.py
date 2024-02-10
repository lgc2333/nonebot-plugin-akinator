from nonebot.plugin import PluginMetadata, inherit_supported_adapters, require

require("nonebot_plugin_saa")
require("nonebot_plugin_session")

from . import __main__ as __main__  # noqa: E402
from .config import ConfigModel  # noqa: E402

__version__ = "0.1.3"
__plugin_meta__ = PluginMetadata(
    name="Akinator",
    description="网络天才",
    usage="使用 `akinator` 指令开始让我猜人物吧！",
    homepage="https://github.com/lgc-NB2Dev/nonebot-plugin-akinator",
    type="application",
    config=ConfigModel,
    supported_adapters=inherit_supported_adapters("nonebot_plugin_saa"),
    extra={"License": "MIT", "Author": "student_2333"},
)
