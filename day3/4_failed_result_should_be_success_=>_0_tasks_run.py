import asyncio

async def worker(name):
    try:
        raise Exception("Something went wrong")
    except Exception:
        return f"{name} => SUCCESS (handled failure)"

async def main():
    results = await asyncio.gather(
        worker("Task1"),
        worker("Task2"),
        worker("Task3"),
        worker("Task4")
    )

    for result in results:
        print(result)

asyncio.run(main())
