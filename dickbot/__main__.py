import argparse
from discord import Intents

from .bot import DickBot

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('token', type=str)

    args = parser.parse_args()

    intents = Intents.default()
    intents.message_content = True
    
    DickBot(intents=intents).run(args.token)
    return

if __name__ == '__main__':
    main()
