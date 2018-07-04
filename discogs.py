import discogs_client
import re
import os
import urllib
import xml.dom.minidom
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

SAVE_PATH = os.getenv('SAVE_PATH')
USER_TOKEN = os.getenv('USER_TOKEN')

d = discogs_client.Client('AudacityTagDiscogs/0.1', user_token=USER_TOKEN)


def audacity_tag(name, val):
    disc_info_xml = xml.dom.minidom.Document()
    subnode = disc_info_xml.createElement('tag')
    subnode_attr = disc_info_xml.createAttribute('name')
    subnode_attr.value = name
    subnode.setAttributeNode(subnode_attr)
    subnode_attr = disc_info_xml.createAttribute('value')
    subnode_attr.value = str(val)
    subnode.setAttributeNode(subnode_attr)
    return subnode


def discogs_info_toxml(release):
    info = {}
    disc_info_dic = {}
    disc_info_dic['YEAR'] = release.year
    disc_info_dic['GENRE'] = release.genres[0]
    # remove " (*)" of "artist name (*)"
    disc_info_dic['ARTIST'] = re.sub(' \(\d\)$', '', release.artists[0].name)
    disc_info_dic['ALBUM'] = release.title

    for i, t in enumerate(release.tracklist):
        disc_info_xml = xml.dom.minidom.Document()
        tags = disc_info_xml.createElement('tags')
        disc_info_xml.appendChild(tags)
        tags.appendChild(audacity_tag('TITLE', t.title))
        tags.appendChild(audacity_tag('TRACKNUMBER', i + 1))
        for name, val in disc_info_dic.items():
            tags.appendChild(audacity_tag(name, val))

        # print('%s - %02d %s.xml' % (release.title, i, t.title))
        # print(disc_info_xml.toprettyxml())
        file_name = '%s - %02d %s.xml' % (release.title, i, t.title)
        file_name = re.sub('/', '_', file_name)
        info[file_name] = disc_info_xml
    return info


def download_album_info(discogs_id):
    release = d.release(discogs_id)
    image_url = release.images[0]['uri']

    for file_name, x in discogs_info_toxml(release).items():
        xml_string = x.toprettyxml()
        with open(os.path.join(SAVE_PATH, file_name), 'w') as f:
            f.write(xml_string)

    try:
        image_name = '%s.jpg' % release.title
        urllib.request.urlretrieve(
            image_url, os.path.join(SAVE_PATH, image_name))
    except:
        sys.exit('Unable to download image')

    print('complete!')


discogs_id = 1147938
download_album_info(discogs_id)
