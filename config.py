from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    kafka_bootstrap: str = "localhost:9092"

    kafka_input_topic: str = "monitoring-input"

    kafka_output_topic: str = "monitoring-output"

    ssh_username: str

    ssh_password: str

    ollama_url: str = "http://localhost:11434"

    class Config:
        env_file = ".env"


settings = Settings()