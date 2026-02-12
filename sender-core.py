import corelink
import time
import asyncio

async def on_server(msg: dict, key: str):
    print(f"SERVER[{key}] -> {msg}")

async def main():
    await corelink.connect("Testuser", "Testpassword", "corelink.hpc.nyu.edu", "20012")

    senderID = await corelink.create_sender("Holodeck", "udp", "testing")
    await corelink.set_server_callback(on_server, "subscriber")
    await corelink.set_server_callback(on_server, "dropped")
    
    print("created sender")
    counter = 0

    while counter <= 10:
        await corelink.send(senderID, "hello world")
        await asyncio.sleep(1)
        counter += 1

corelink.run(main())
