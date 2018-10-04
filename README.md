# xml-for-audacity

[Audacity matadata tags xml](https://manual.audacityteam.org/man/metadata_editor.html) generator using discogs API

## Usage

**Setup**
1. [Get your personal access token of Discogs](https://www.discogs.com/settings/developers)
2. Rename *.env.sample* as *.env* and edit
```
USER_TOKEN=(your access token)
SAVE_PATH=(save folder)
```

**Fetching Data**
1. Find URL for a release (e.g. <https://www.discogs.com/New-Order-Blue-Monday/release/20755>)
2. Run
```
$ python main.py id (e.g. 20755) 
```

## Requirement

- Python 3+
- [Discogs API Client](https://github.com/discogs/discogs_client)
- [python-dotenv](https://github.com/theskumar/python-dotenv)

## Auther

[@matsueushi](https://twitter.com/matsueushi)

## License

[MIT](/LICENSE) 
