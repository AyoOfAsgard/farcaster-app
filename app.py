from farcaster import Warpcast

async def main():
    client = Warpcast(access_token="")

    user = client.get_user(fid=15255)
    print(f"User: {user}")

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())

