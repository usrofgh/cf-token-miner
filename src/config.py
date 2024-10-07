from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    model_config = SettingsConfigDict(
        # Use .env if doesn't exist .env.dev (in production for example)
        env_file=(
            Path(__file__).parent.parent.joinpath(".env"),
            Path(__file__).parent.parent.joinpath(".env.dev")
        )
    )

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.LOG_FILE = self.full_path(self.LOG_FILE)
        self.BROWSER_EXT = self.full_path(self.BROWSER_EXT)
        self.BROWSER_PROFILE = self.full_path(self.BROWSER_PROFILE)

    @staticmethod
    def full_path(*relative) -> str:
        return str(Path("src", *relative).absolute())

    MODE: str
    LOG_LEVEL: str
    LOG_FILE: str
    TESSERACT_FILE: str
    CHROME_FILE: str

    CF_TOKEN_EXP_SECONDS: int
    CF_GEN_INTERVAL: int

    BROWSER_EXT: str
    BROWSER_PROFILE: str

    REDIS_HOST: str
    REDIS_PORT: int

    PSQL_HOST: str
    PSQL_PORT: int
    PSQL_DB: str
    PSQL_USER: str
    PSQL_PASSWORD: str
    PSQL_URI: str

    SECRET_KEY: str
    JWT_ALGORITHM: str
    JWT_TTL_MIN: int

class HotKeys:
    OPEN_CONSOLE_HOTKEY: tuple = ("ctrl", "shift", "j")
    INSERT_HOTKEY: tuple = ("ctrl", "v")
    CLEAN_CONSOLE: tuple = ("ctrl", "l")
    FOCUS_CONSOLE: tuple = ("ctrl", "`")
    ZOOM_IN: tuple = ("ctrl", "+")
    ZOOM_OUT: tuple = ("ctrl", "-")


config = Config()
