from json import dumps
from pocket_structuring import extract_articles_from_html_file, write_articles_to_csv_file
import unittest
from unittest.mock import patch, mock_open

MOCK_HTML = \
    '<!DOCTYPE html>\n' + \
    '<html>\n' + \
    '	<!--So long and thanks for all the fish-->\n' + \
    '	<head>\n' + \
    '		<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />\n' + \
    '		<title>Pocket Export</title>\n' + \
    '	</head>\n' + \
    '	<body>\n' + \
    '		<h1>Unread</h1>\n' + \
    '		<ul>\n' + \
    '			<li><a href="https://openai.com/research/scaling-kubernetes-to-7500-nodes" time_added="1695851847" tags="software">Scaling Kubernetes to 7,500 nodes</a></li>\n' + \
    '<li><a href="https://openai.com/research/scaling-kubernetes-to-2500-nodes" time_added="1695851686" tags="software">Scaling Kubernetes to 2,500 nodes</a></li>\n' + \
    '		</ul>\n' + \
    '		\n' + \
    '		<h1>Read Archive</h1>\n' + \
    '		<ul>\n' + \
    '			<li><a href="https://samcurry.net/filling-in-the-blanks-exploiting-null-byte-buffer-overflow-for-a-40000-bounty/?utm_source=firefox_pocket_save_button" time_added="1669162039" tags="cyber">Exploiting Null Byte Buffer Overflow for a ,000 bounty | Sam Curry</a></li>\n' + \
    '		</ul>\n' + \
    '	</body>\n' + \
    '</html>'

MOCK_STRUCTURED = [
    {'Title': 'Scaling Kubernetes to 7,500 nodes', 'URL': 'https://openai.com/research/scaling-kubernetes-to-7500-nodes', 'Time Added': '2023-09-27 21:57:27', 'Tags': ['software']},
    {'Title': 'Scaling Kubernetes to 2,500 nodes', 'URL': 'https://openai.com/research/scaling-kubernetes-to-2500-nodes', 'Time Added': '2023-09-27 21:54:46', 'Tags': ['software']},
    {'Title': 'Exploiting Null Byte Buffer Overflow for a ,000 bounty | Sam Curry', 'URL': 'https://samcurry.net/filling-in-the-blanks-exploiting-null-byte-buffer-overflow-for-a-40000-bounty/?utm_source=firefox_pocket_save_button', 'Time Added': '2022-11-23 00:07:19', 'Tags': ['cyber']}
]

# Fuller output:
# {'Title': 'Scaling Kubernetes to 7,500 nodes', 'URL': 'https://openai.com/research/scaling-kubernetes-to-7500-nodes', 'Time Added': '2023-09-27 21:57:27', 'Tags': ['software']},
# {'Title': 'Scaling Kubernetes to 2,500 nodes', 'URL': 'https://openai.com/research/scaling-kubernetes-to-2500-nodes', 'Time Added': '2023-09-27 21:54:46', 'Tags': ['software']},
# {'Title': 'CodeQL zero to hero part 1: the fundamentals of static analysis for vulnera', 'URL': 'https://github.blog/2023-03-31-codeql-zero-to-hero-part-1-the-fundamentals-of-static-analysis-for-vulnerability-research/', 'Time Added': '2023-09-15 16:17:33', 'Tags': ['cyber', 'software']},
# {'Title': '(4) An Engineer&#039;s Guide to Data Contracts - Pt. 1', 'URL': 'https://dataproducts.substack.com/p/an-engineers-guide-to-data-contracts', 'Time Added': '2023-09-07 18:17:13', 'Tags': ['software']},
# {'Title': 'JSX was a Mistake | Kyle Shevlin', 'URL': 'https://kyleshevlin.com/jsx-was-a-mistake', 'Time Added': '2023-06-17 17:47:16', 'Tags': ['software']},
# {'Title': 'Neuralink and the Brain&#039;s Magical Future — Wait But Why', 'URL': 'https://waitbutwhy.com/2017/04/neuralink.html', 'Time Added': '2023-04-12 22:48:17', 'Tags': ['']},
# {'Title': 'The Three Internets | Council on Foreign Relations', 'URL': 'https://www.cfr.org/podcasts/three-internets', 'Time Added': '2023-04-12 17:16:56', 'Tags': ['']},
# {'Title': '17 Open Source Projects at AWS Written in Rust - DZone', 'URL': 'https://dzone.com/articles/17-open-source-projects-at-aws-written-in-rust', 'Time Added': '2023-04-07 14:25:22', 'Tags': ['software']},
# {'Title': 'Fog of war: how the Ukraine conflict transformed the cyber threat landscape', 'URL': 'https://blog.google/threat-analysis-group/fog-of-war-how-the-ukraine-conflict-transformed-the-cyber-threat-landscape/', 'Time Added': '2023-04-03 02:12:44', 'Tags': ['cyber']},
# {'Title': '“The Door Problem” – Liz England', 'URL': 'https://lizengland.com/blog/2014/04/the-door-problem/', 'Time Added': '2023-04-03 02:08:05', 'Tags': ['software']},
# {'Title': '&quot;Reverse Engineering for Beginners&quot; free book', 'URL': 'https://beginners.re/', 'Time Added': '2023-01-11 04:36:00', 'Tags': ['cyber', 'project']},
# {'Title': 'Rooms and Mazes: A Procedural Dungeon Generator – journal.stuffwithstuff.co', 'URL': 'https://journal.stuffwithstuff.com/2014/12/21/rooms-and-mazes/', 'Time Added': '2023-01-08 17:18:07', 'Tags': ['project', 'software']},
# {'Title': 's1r1us - Prototype Pollution', 'URL': 'https://blog.s1r1us.ninja/research/PP', 'Time Added': '2022-11-08 19:40:12', 'Tags': ['cyber']},
# {'Title': 'No internet connection', 'URL': 'https://hackernoon.com/domain-fronting-101-what-is-domain-fronting-and-how-does-it-work-es2v37pr', 'Time Added': '2022-11-06 22:55:18', 'Tags': ['cyber', 'project']},
# {'Title': 'manoelt/50M_CTF_Writeup: $50 Million CTF from Hackerone - Writeup', 'URL': 'https://github.com/manoelt/50M_CTF_Writeup', 'Time Added': '2022-11-06 19:51:39', 'Tags': ['cyber']},
# {'Title': 'Exploiting Null Byte Buffer Overflow for a ,000 bounty | Sam Curry', 'URL': 'https://samcurry.net/filling-in-the-blanks-exploiting-null-byte-buffer-overflow-for-a-40000-bounty/?utm_source=firefox_pocket_save_button', 'Time Added': '2022-11-23 00:07:19', 'Tags': ['cyber']},
# {'Title': 'Project Zero: A deep dive into an NSO zero-click iMessage exploit: Remote C', 'URL': 'https://googleprojectzero.blogspot.com/2021/12/a-deep-dive-into-nso-zero-click.html', 'Time Added': '2022-11-19 21:32:06', 'Tags': ['cyber']},
# {'Title': 'Hidden OAuth attack vectors | PortSwigger Research', 'URL': 'https://portswigger.net/research/hidden-oauth-attack-vectors', 'Time Added': '2022-11-19 21:19:54', 'Tags': ['cyber']},
# {'Title': 'I tried to write about containers, but realized I needed to understand imag', 'URL': 'https://www.lacework.com/blog/i-tried-to-write-about-containers-but-realized-i-needed-to-understand-images-docker-and-kubernetes-first/', 'Time Added': '2022-11-19 21:19:46', 'Tags': ['cyber']},
# {'Title': 'XSS via a spoofed React element', 'URL': 'http://danlec.com/blog/xss-via-a-spoofed-react-element', 'Time Added': '2022-11-14 07:54:08', 'Tags': ['cyber']},
# {'Title': 'What you need to know about the latest critical OpenSSL vulnerability | Lac', 'URL': 'https://www.lacework.com/blog/what-you-need-to-know-about-the-latest-critical-openssl-vulnerability/', 'Time Added': '2022-11-14 03:58:48', 'Tags': ['cyber']}

class TestExtractArticles(unittest.TestCase):

    #mock_file.assert_called_with("path/to/open")
    #@patch('builtins.open')
    @patch("builtins.open", new_callable=mock_open, read_data=MOCK_HTML)
    def test_extract_articles_from_html(self, mock_open):
        # Call the function
        html_filename = "sample-pocket-export.html"
        articles = extract_articles_from_html_file(html_filename)
        print(articles)
        # Check the result
        mock_open.assert_called_with(html_filename, 'r')
        self.assertEqual(dumps(articles), dumps(MOCK_STRUCTURED))

if __name__ == "__main__":
    unittest.main()
