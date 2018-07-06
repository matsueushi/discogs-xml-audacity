# -*- coding: utf-8 -*-
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


def trim_artist_name(name):
    return re.sub(' \(\d\)$', '', name)


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
    disc_info_dic['ARTIST'] = trim_artist_name(release.artists[0].name)
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
        file_name = '%s - %02d %s.xml' % (release.title, i + 1, t.title)
        file_name = re.sub('/', '_', file_name)
        info[file_name] = disc_info_xml
    return info


def download_album_info(discogs_id):
    release = d.release(discogs_id)
    image_url = release.images[0]['uri']
    artist_name = trim_artist_name(release.artists[0].name)
    sub_save_path = os.path.join(SAVE_PATH, artist_name)
    if not os.path.exists(sub_save_path):
        os.makedirs(sub_save_path)

    for file_name, x in discogs_info_toxml(release).items():
        xml_string = x.toprettyxml()
        with open(os.path.join(sub_save_path, file_name), 'w') as f:
            f.write(xml_string)

    try:
        image_name = '%s.jpg' % release.title
        urllib.request.urlretrieve(
            image_url, os.path.join(sub_save_path, image_name))
    except:
        sys.exit('Unable to download image')

    print('complete!')
