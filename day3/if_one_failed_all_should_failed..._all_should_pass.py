import asyncio

async def worker(name, fail=False):
    await asyncio.sleep(1)

    if fail:
        raise Exception(f"{name} failed")

    return f"{name} completed"

async def main():
    try:
        results = await asyncio.gather(
            worker("Task1"),
            worker("Task2"),
            worker("Task3", fail=True),  # This task will fail
            worker("Task4")
        )

        # This line runs only if ALL tasks succeed
        print("All tasks passed")
        print(results)

    except Exception as e:
        # If ANY task fails, we come here
        print("All tasks failed")
        print("Reason:", e)

asyncio.run(main())
