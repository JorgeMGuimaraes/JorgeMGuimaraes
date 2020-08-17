import json
import io
import codecs
import urllib.parse as up

def is_header(lin: str) -> bool:
    return lin[0] == "#"

def is_content(lin: str) -> bool:
    return lin != "" and lin != '\n'

def get_shield(lin: str, label: str, color: str) -> dict:
    element = lin.rstrip().split(':')
    return {
        "schemaVersion": 1,
        "namedLogo": element[1],
        "logoColor": "FFF",
        "label": label,
        "labelColor": "000",
        "message": element[0],
        "color": color,
        "style": "flat-square"
    }

def get_shield_link(lin: str, label: str, color: str) -> str:
    shields_io_url  = "https://img.shields.io/badge/"
    element         = lin.rstrip().split(':')
    message         = element[0]
    namedLogo       = element[1]
    return f'![{up.quote(message)}]({shields_io_url}{up.quote(label)}-{up.quote(message)}-{color}?logo={up.quote(namedLogo)}&logoColor=fff&labelColor=00171f&style=flat-square) '

# Main Program
file_name = "shields.txt"
with codecs.open(file_name, mode='r', encoding='utf-8') as file:

    markdown = "## Tecnologias e Linguagens"

    for line in file:

        if is_content(line):

            if is_header(line):
                line        = line.rstrip().split(':')
                label       = line[0][2:]
                color       = line[1]
                markdown    += '\n\n'

            else:
                markdown += get_shield_link(line, label, color)

    with io.open('markdown.md', mode='w') as out_md:
        out_md.write(markdown)