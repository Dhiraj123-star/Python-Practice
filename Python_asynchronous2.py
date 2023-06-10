import asyncio

async def perform_io_operation(number):
    await asyncio.sleep(1)  # Simulate I/O operation
    print(f"IO operation {number} completed")

async def main():
    tasks = []

    for i in range(1, 6):
        tasks.append(perform_io_operation(i))

    await asyncio.gather(*tasks)

asyncio.run(main())