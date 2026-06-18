import asyncio

async def worker(name, fail=False):
    await asyncio.sleep(1)

    if fail:
        raise Exception(f"{name} failed")

    return f"{name} success"

async def main():
    results = await asyncio.gather(
        worker("Task1", fail=True),
        worker("Task2", fail=True),
        worker("Task3", fail=True),
        worker("Task4"),
        return_exceptions=True
    )

    success_count = 0
    failure_count = 0

    for result in results:
        if isinstance(result, Exception):
            failure_count += 1
        else:
            success_count += 1

    print("Success:", success_count)
    print("Failure:", failure_count)

    if success_count >= 2:
        print("Overall PASS")
    else:
        print("Overall FAIL")

asyncio.run(main())
