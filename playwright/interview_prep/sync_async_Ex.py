import asyncio
import time


def task(name):
    print(f"starting {name}")
    time.sleep(2)
    print(f"finished {name}")


# task("Ghanika")
# task("Hamsika")


async def task(name):
    print(f"starting {name}")
    await asyncio.sleep(2)
    print(f"finished {name}")


async def main():
    await asyncio.gather((task("First")), (task("Second")))


asyncio.run(main())
