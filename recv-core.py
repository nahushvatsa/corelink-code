import corelink
import asyncio

async def on_data(message: bytes, stream_id: int, header: dict):
    # message is bytes per the API; decode for printing
    try:
        text = message.decode("utf-8", errors="replace")
    except Exception:
        text = repr(message)
    print(f"RECV from stream {stream_id}: {text} | header={header}")

async def on_server(msg: dict, key: str):
    print(f"SERVER[{key}] -> {msg}")

async def main():
    await corelink.connect("Testuser", "Testpassword", "corelink.hpc.nyu.edu", "20012")
    await corelink.set_data_callback(on_data)
    await corelink.set_server_callback(on_server, "update")
    await corelink.set_server_callback(on_server, "stale")

    streamID = await corelink.create_receiver("Holodeck", "udp", alert=True, echo=True)

    await corelink.processing.connect_receiver(streamID)
    print("connected")
    await asyncio.Event().wait();

corelink.run(main())
