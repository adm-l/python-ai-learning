"""Minimal asyncio TCP echo server/client on localhost."""
import asyncio


async def handle(reader: asyncio.StreamReader, writer: asyncio.StreamWriter) -> None:
    try:
        data = await reader.readline()
        if len(data) > 1024:
            writer.write(b"ERROR: line too long\\n")
        else:
            writer.write(b"echo: " + data)
        await writer.drain()
    finally:
        writer.close()
        await writer.wait_closed()


async def main() -> None:
    server = await asyncio.start_server(handle, "127.0.0.1", 8888, limit=1024)
    async with server:
        async with asyncio.timeout(3):
            reader, writer = await asyncio.open_connection("127.0.0.1", 8888)
            writer.write(b"hello\\n")
            await writer.drain()
            print((await reader.readline()).decode().rstrip())
            writer.close()
            await writer.wait_closed()


if __name__ == "__main__":
    asyncio.run(main())
