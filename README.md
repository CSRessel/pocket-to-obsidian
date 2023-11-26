# Pocket to Obsidian

Quick data extraction from [Pocket exports](https://getpocket.com/export), so the full database of saved articles can be used in other contexts.
This repos is a small toy to play around with the
[Data Analysis GPT](https://help.openai.com/en/articles/8555545-file-uploads-with-gpts-and-advanced-data-analysis-in-chatgpt?q=data+analysis),
and with the [ChatGPT.nvim plugin](https://github.com/jackmort/chatgpt.nvim) commands for documentation and unit testing.

## Getting Started

Setup and activate a venv as needed.

Run tests:

```
python -m tests.test_pocket_structuring
```

Run full script:

```
python pocket_structuring.py
```

## Sample Input

[A sample export is available in this repo](sample-pocket-export.html)

[Your own data can be generated from the Pocket webapp](https://getpocket.com/export)

## Sample Output

| Title | URL | Time Added | Tags |
| --- | --- | --- | --- |
| Scaling Kubernetes to 7,500 nodes | [Link](https://openai.com/research/scaling-kubernetes-to-7500-nodes) | 2023-09-27 21:57:27 | software |
| Scaling Kubernetes to 2,500 nodes | [Link](https://openai.com/research/scaling-kubernetes-to-2500-nodes) | 2023-09-27 21:54:46 | software |
| CodeQL zero to hero part 1: the fundamentals of static analysis for vulnera | [Link](https://github.blog/2023-03-31-codeql-zero-to-hero-part-1-the-fundamentals-of-static-analysis-for-vulnerability-research/) | 2023-09-15 16:17:33 | cyber,software |
| The AI Power Paradox: Can States Learn to Govern Artificial Intelligence—Be | [Link](https://www.foreignaffairs.com/world/artificial-intelligence-power-paradox) | 2023-09-07 18:59:12 | politics |
| (4) An Engineer's Guide to Data Contracts - Pt. 1 | [Link](https://dataproducts.substack.com/p/an-engineers-guide-to-data-contracts) | 2023-09-07 18:17:13 | software |
| JSX was a Mistake | Kyle Shevlin | [Link](https://kyleshevlin.com/jsx-was-a-mistake) | 2023-06-17 17:47:16 | software |
| Neuralink and the Brain's Magical Future — Wait But Why | [Link](https://waitbutwhy.com/2017/04/neuralink.html) | 2023-04-12 22:48:17 |  |
| The Three Internets | Council on Foreign Relations | [Link](https://www.cfr.org/podcasts/three-internets) | 2023-04-12 17:16:56 |  |
| 17 Open Source Projects at AWS Written in Rust - DZone | [Link](https://dzone.com/articles/17-open-source-projects-at-aws-written-in-rust) | 2023-04-07 14:25:22 | software |
| A Walkthrough Of My Obsidian Setup | HeyMichelleMac | [Link](https://heymichellemac.com/obsidian-setup-sep-2021) | 2023-04-07 14:09:22 |  |
| Meditations On Moloch | Slate Star Codex | [Link](https://slatestarcodex.com/2014/07/30/meditations-on-moloch/) | 2023-04-05 14:12:04 |  |
| http://www.skyhunter.com/marcs/GentleSeduction.html | [Link](http://www.skyhunter.com/marcs/GentleSeduction.html) | 2023-04-05 14:11:55 |  |
| The Last Question by Isaac Asimov | [Link](http://www.thelastquestion.net/) | 2023-04-05 10:39:27 |  |
| Exploiting Null Byte Buffer Overflow for a $40,000 bounty | Sam Curry | [Link](https://samcurry.net/filling-in-the-blanks-exploiting-null-byte-buffer-overflow-for-a-40000-bounty/?utm_source=firefox_pocket_save_button) | 2022-11-23 00:07:19 | cyber |
| Project Zero: A deep dive into an NSO zero-click iMessage exploit: Remote C | [Link](https://googleprojectzero.blogspot.com/2021/12/a-deep-dive-into-nso-zero-click.html) | 2022-11-19 21:32:06 | cyber |
| Hidden OAuth attack vectors | PortSwigger Research | [Link](https://portswigger.net/research/hidden-oauth-attack-vectors) | 2022-11-19 21:19:54 | cyber |
| I tried to write about containers, but realized I needed to understand imag | [Link](https://www.lacework.com/blog/i-tried-to-write-about-containers-but-realized-i-needed-to-understand-images-docker-and-kubernetes-first/) | 2022-11-19 21:19:46 | cyber |
| XSS via a spoofed React element | [Link](http://danlec.com/blog/xss-via-a-spoofed-react-element) | 2022-11-14 07:54:08 | cyber |
| What you need to know about the latest critical OpenSSL vulnerability | Lac | [Link](https://www.lacework.com/blog/what-you-need-to-know-about-the-latest-critical-openssl-vulnerability/) | 2022-11-14 03:58:48 | cyber |

