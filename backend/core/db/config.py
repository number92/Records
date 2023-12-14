from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DB_USER: str
    DB_PASS: str
    DB_NAME: str
    DB_HOST: str
    DB_PORT: int

    @property
    def DATABASE_URL_asyncpg(self):
        # DSN postgresql+asyncpg://postgres:@localhost:5433/postgres
        url = (
            f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}"
            f"@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )
        return url

    @property
    def DATABASE_URL_psycopg(self):
        # DSN postgresql+psycopg://postgres:@localhost:5433/postgres
        url = (
            f"postgresql+psycopg://{self.DB_USER}:{self.DB_PASS}"
            f"@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )
        return url

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
