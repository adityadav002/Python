import asyncio
from jokeapi import Jokes

async def main():
    jokes = await Jokes()  # Notice the await here
    joke = await jokes.get_joke()
    print(joke["joke"] if joke["type"] == "single" else f'{joke["setup"]} ... {joke["delivery"]}')

asyncio.run(main())
