import json
import io
import codecs

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

# Main Program
file_name = "shields.txt"
shields_io_url = "https://img.shields.io/endpoint?url="
git_url = "https://github.com/JorgeMGuimaraes/JorgeMGuimaraes/shields/"
with codecs.open(
    file_name,
    mode='r',
    encoding='utf-8') as file:

    markdown = "## Tecnologias e Linguagens"
    for line in file:
        if is_content(line):
            if is_header(line):
                line = line.rstrip().split(':')
                label = line[0][2:]
                color = line[1]
                markdown += '\n\n'
            else:
                shield = get_shield(line, label, color)
                markdown += f'![{shield["message"]}]({shields_io_url}{git_url}{shield["namedLogo"]}.json) '
                with codecs.open(
                    f'{shield["namedLogo"]}.json',
                    mode='w',
                    encoding='utf-8') as out_json:
                    out_json.write(json.dumps(shield, indent=4, ensure_ascii=False))

    with io.open('markdown.md', mode='w') as out_md:
        out_md.write(markdown)