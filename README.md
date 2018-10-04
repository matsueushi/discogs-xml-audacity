# xml-for-audacity

Download metadata xml for [Audacity matadata editor](https://manual.audacityteam.org/man/metadata_editor.html) and album artwork using discogs API
![screenshot](https://user-images.githubusercontent.com/28841596/46452843-063f3080-c76c-11e8-91c4-1823e768a7de.png)

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
