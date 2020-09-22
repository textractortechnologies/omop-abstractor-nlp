import time


async def make_burgers(number: int) -> str:
    time.sleep(number)
    return f"Enjoy your {number} burgers"


async def get_burgers(number: int) -> str:
    return await make_burgers(number)