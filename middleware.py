from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject


# class CounterMiddleware(BaseMiddleware):
#     def __init__(self) -> None:
#         self.counter = 0
#
#     async def __call__(
#         self,
#         handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
#         event: TelegramObject,
#         data: Dict[str, Any]
#     ) -> Any:
#         self.counter += 1
#         data['counter'] = self.counter
#         return await handler(event, data)


class SessionMiddleware(BaseMiddleware):
    def __init__(self) -> None:
        self.data = dict()

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:
        data['session'] = self.data
        return await handler(event, data)

