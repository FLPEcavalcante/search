from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    response_obj = {}

    def handle_starttag(self, tag, attrs):
        if tag == 'p' and attrs[0][0] == 'linkname':
            MyHTMLParser.response_obj['linkname'] = attrs[0][1]
        if tag == 'a' and attrs[0][0] == 'href':
            MyHTMLParser.response_obj['link'] = attrs[0][1]
        if MyHTMLParser.response_obj.get('link') and MyHTMLParser.response_obj.get('linkname'):
            print(MyHTMLParser.response_obj)

    def get():
        return MyHTMLParser.response_obj


parser = MyHTMLParser()
href = """<p linkname="art43_incVI" style="text-align:justify" class=""><a class="linkname" id="art43_incVI" name="art43_incVI"></a>VI - incorporar informações ambientais relevantes e validadas, produzidas pelas instituições superiores de ensino e pesquisa e órgãos do governo federal.\xa0<a href="/sinj/Norma/e67d3109ad0b41748e3e8f322ab17f43/exec_dec_44087_2022.html#txt_90b944df8b744e47f2aab70dc1dcc224">(Regulamentado(a) pelo(a) Decreto 44087 de 30/12/2022)</a></p>"""
parser.feed(href)
