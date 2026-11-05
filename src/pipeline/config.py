from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.parent
ENV_PATH = BASE_DIR / ".env"

class DbSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=ENV_PATH, env_prefix="PG_")

    host: str
    port: int
    user: str
    password: SecretStr
    db: str

    @property
    def url(self) -> str:
        return f"postgresql://{self.user}:{self.password.get_secret_value()}@{self.host}:{self.port}/{self.db}"

if __name__ == "__main__":
    settings = DbSettings()

    print(f"PostgreSQL Host: {settings.host}")
    print(f"PostgreSQL Port: {settings.port}")
    print(f"PostgreSQL User: {settings.user}")
    print(f"PostgreSQL Database: {settings.db}")