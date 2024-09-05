from farcaster import Warpcast

async def main():
    client = Warpcast()

    user = await client.get_user(username="ayomide.eth")
    print(f"User: {user}")

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())

