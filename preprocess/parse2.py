import mwparserfromhell
import re

def normalize(txt):
  regex = r"[^\u0b80-\u0bffa-zA-Z]"
  return re.sub(regex," ",txt)

def wikimedia_citation_to_raw_text(citation):
    # Parse the Wikitext markup
    wikitext = mwparserfromhell.parse(citation)
    arr = []
    
    for i in wikitext.__dict__['_nodes']:
        skip_list = [
            mwparserfromhell.nodes.wikilink.Wikilink, 
            mwparserfromhell.nodes.external_link.ExternalLink,
            mwparserfromhell.nodes.template.Template
        ]
        text_list = [
            mwparserfromhell.nodes.text.Text,
            mwparserfromhell.nodes.heading.Heading
        ]
        t = type(i)
        if t in skip_list:
            continue
        
        
        if t in text_list:
            wikicode = mwparserfromhell.parse(i)
            plaintext = wikicode.strip_code().strip()
            arr.append(plaintext)
        else:
            wikicode = mwparserfromhell.parse(i)
            if wikicode.__dict__['_nodes'][0] == '*':
                  continue
            rows = (str(i).split("\n"))[1:]
            cleaned = [normalize(i) for i in rows]
            arr.extend(cleaned)
        
    combined =  " ".join(arr)
    combined = re.sub("[\`\=\~\!\@\#\$\%\^\&\*\(\)\_\+\[\]\;\'\,\.\/\\\{\}\:\"\<\>\?\s]+", " ", combined)
    return combined
    

with open("./layer3_text/1_2_0/10 ஆம் நூற்றாண்டுத் தமிழ் இலக்கிய நூல்கள்.txt", encoding='utf-8') as f:
    citation = f.read()
    text = wikimedia_citation_to_raw_text(citation)
    with open("temp.txt", "w", encoding='utf-8') as f2:
        f2.write(text)
