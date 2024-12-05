from dataclasses import dataclass

import environs
from environs import Env


@dataclass
class TgBot:
    token: str

@dataclass
class Config:
    bot: TgBot


def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path=path)
    return Config(TgBot(token=env('BOT_TOKEN')))

