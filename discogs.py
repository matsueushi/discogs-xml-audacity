import discogs_client
import os
import xml.dom.minidom

d = discogs_client.Client('AudacityTagDiscogs/0.1')


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


def discogs_info_toxml(discogs_id):
    info = {}
    release = d.release(discogs_id)
    disc_info_dic = {}
    disc_info_dic['YEAR'] = release.year
    disc_info_dic['GENRE'] = release.genres[0]
    disc_info_dic['ALBUM'] = release.title
    disc_info_dic['ARTISTS'] = release.artists[0].name

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
        info[file_name] = disc_info_xml
    return info


path = '/Users/matsueushi/Documents/audacity'
discogs_id = 520337
for file_name, x in discogs_info_toxml(discogs_id).items():
    xml_string = x.toprettyxml()
    with open(os.path.join(path, file_name), 'w') as f:
        f.write(xml_string)
print('complete!')
