import asyncio

async def background_task():
    while True:
        print("Running in the background...")
        await asyncio.sleep(1)

async def main():
    task = asyncio.create_task(background_task())
    # ... do other tasks ...
    await asyncio.sleep(5)  # Run the background task for 5 seconds
    task.cancel()

asyncio.run(main())

