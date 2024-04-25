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
    for item in items_to_process:
        imgspy.info(item)
    end_time = time.time()
    print(f"Sync Benchmark Test End : {end_time - start_time}s")
    # async test
    print(f"Async Benchmark Test Start")
    start_time = time.time()
    results = await asyncimgspy.info(items_to_process)
    end_time = time.time()
    print(f"Async Benchmark Test End : {end_time - start_time}s")


if __name__ == "__main__":
    asyncio.run(main())
