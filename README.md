# DiscordPlays
Simple bot for playing games with Discord, a la TwitchPlaysPokemon 🎮

## Dependencies
DiscordPlays works with Python 3.7+ has two dependencies:
* [discord.py](https://github.com/Rapptz/discord.py/)
* [keyboard](https://github.com/boppreh/keyboard)

## Configuration
This is the default configuration
```json
{
    "token": "BOT_TOKEN_GOES_HERE",
    "server": SERVER_ID_GOES_HERE,
    "channel": CHANNEL_ID_GOES_HERE,
    "allowed_keys": {
        "KEY_NAME": "ACTION",
    },
    "game": "(OPTIONAL) NAME_OF_GAME_GOES_HERE"
}
```

To get a bot token, check out [this guide](https://discordpy.readthedocs.io/en/latest/discord.html#discord-intro)!

The `server` and `channel` values should both be **integers**, not strings!

For `allowed_keys`, each *key* should be the *name of the key/keybind*, such as `a`, `space`, or `attack`, while the *value* should be the *actual key/keybind executed*, such as `a`, `space`, or `enter`.

Finally, `game` is optional but should be a string that will show in the bot's "Now Playing" part of their profile.

## Usage
*Note: Due to how the `keyboard` library works, Linux users will need to run as sudo/root*

`python3 discord_plays.py`

By default, it will load its configuration from `config.json` in its relative path, but you can set the environment variable `DISCORD_PLAYS_CONFIG` if you wish to load from a different location.
