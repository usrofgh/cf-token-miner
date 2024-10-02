from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(
            Path(__file__).parent.parent.joinpath(".env.prod"),
            Path(__file__).parent.parent.joinpath(".env")
        )
    )

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.LOG_FILE = self.full_path(self.LOG_FILE)

    @staticmethod
    def full_path(*relative) -> str:
        return str(Path("src", *relative).absolute())

    MODE: str
    LOG_LEVEL: str
    LOG_FILE: str

    OPEN_CONSOLE_HOTKEY: tuple = ("ctrl", "shift", "j")
    CLEAN_CONSOLE: tuple = ("ctrl", "l")
    FOCUS_CONSOLE: tuple = ("ctrl", "q")

config = Config()
