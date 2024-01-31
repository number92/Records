from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    DB_HOST: str
    DB_PORT: int
    BOT_TOKEN: str

    @property
    def DATABASE_URL_asyncpg(self):
        # DSN postgresql+asyncpg://postgres:@localhost:5433/postgres
        url = (
            "postgresql+asyncpg://"
            + f"{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
            + f"@{self.DB_HOST}:{self.DB_PORT}/{self.POSTGRES_DB}"
        )
        return url

    @property
    def DATABASE_URL_psycopg(self):
        # DSN postgresql+psycopg://postgres:@localhost:5433/postgres
        url = (
            "postgresql+psycopg://"
            + f"{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
            + f"@{self.DB_HOST}:{self.DB_PORT}/{self.POSTGRES_DB}"
        )
        return url

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
