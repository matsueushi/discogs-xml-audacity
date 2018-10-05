# xml-for-audacity

Download metadata xml for [Audacity matadata editor](https://manual.audacityteam.org/man/metadata_editor.html) and album artwork using discogs API
![screenshot](https://user-images.githubusercontent.com/28841596/46452843-063f3080-c76c-11e8-91c4-1823e768a7de.png)
![audacity_metadata_screenshot](https://user-images.githubusercontent.com/28841596/46511727-3e06b080-c81e-11e8-9e21-c45f6b7671a0.png)

## Usage

**Setup**
1. [Get your personal access token of Discogs](https://www.discogs.com/settings/developers)
2. Rename *.env.sample* as *.env* and set your user token 
```
USER_TOKEN=(your access token)
```

**Fetching Data**
1. Find URL for a release. If the URL is <https://www.discogs.com/New-Order-Blue-Monday/release/20755>, the unique id of this release is 20755.
2. Run the command
```
$ python main.py unique_id
```

## Requirement

- Python 3+
- [Discogs API Client](https://github.com/discogs/discogs_client)
- [python-dotenv](https://github.com/theskumar/python-dotenv)

## Auther

[@matsueushi](https://twitter.com/matsueushi)

## License

[MIT](/LICENSE)
