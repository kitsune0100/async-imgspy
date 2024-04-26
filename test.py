import asyncio
import textwrap
import imgspy
import asyncimgspy
import os
import time


async def main():
    items_to_process = [
        'http://via.placeholder.com/500x500.png',
        'http://via.placeholder.com/500x500.jpg',
        textwrap.dedent('''data:image/png;base64,
         iVBORw0KGgoAAAANSUhEUgAAAAIAAAABCAYAAAD0In+
         KAAAAD0lEQVR42mNk+M9QzwAEAAmGAYCF+yOnAAAAAElFTkSuQmCC''')
    ]
    os_items = [f"fixtures/{i}" for i in os.listdir("fixtures")]
    items_to_process = items_to_process + os_items
    # sync test
    print(f"Sync Benchmark Test Start")
    start_time = time.time()
    results = [imgspy.info(item) for item in items_to_process]
    end_time = time.time()
    print(f"Sync Benchmark Test End : {end_time - start_time}s")
    print(f"Sync Results : {results}")
    # async test
    print(f"Async Benchmark Test Start")
    start_time = time.time()
    async_results = await asyncimgspy.info(items_to_process)
    end_time = time.time()
    print(f"Async Results : {async_results}")
    print(f"Async Benchmark Test End : {end_time - start_time}s")


if __name__ == "__main__":
    asyncio.run(main())
