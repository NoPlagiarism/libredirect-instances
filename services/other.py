import requests
import json
from .utils import fetchJsonList, fetchRegexList, fetchCache
from colorama import Fore, Style
import logging
import traceback
import re


def tent(mightyList):
    fetchJsonList(
        'tent',
        'https://forgejo.sny.sh/sun/Tent/raw/branch/main/instances.json',
        'url',
        False,
        mightyList
    )


def ruralDictionary(mightyList):
    fetchJsonList(
        'ruralDictionary',
        'https://codeberg.org/zortazert/rural-dictionary/raw/branch/master/instances.json',
        {
            'clearnet': 'clearnet',
            'tor': 'tor',
            'i2p': 'i2p',
            'loki': None
        },
        False,
        mightyList
    )


def laboratory(mightyList):
    fetchRegexList(
        'laboratory',
        'https://git.vitali64.duckdns.org/utils/laboratory.git/plain/README.md',
        r"\| (https:\/{2}.*?) \|",
        mightyList
    )


def gothub(mightyList):
    fetchJsonList(
        'gothub',
        'https://codeberg.org/gothub/gothub-instances/raw/branch/master/instances.json',
        {
            'clearnet': 'link',
            'tor': None,
            'i2p': None,
            'loki': None
        },
        False,
        mightyList
    )


def biblioReads(mightyList):
    fetchJsonList(
        'biblioReads',
        'https://raw.githubusercontent.com/nesaku/BiblioReads/main/instances.json',
        {
            'clearnet': 'url',
            'tor': 'onion',
            'i2p': 'i2p',
            'loki': None
        },
        False,
        mightyList
    )


def libremdb(mightyList):
    fetchJsonList(
        'libremdb',
        'https://raw.githubusercontent.com/zyachel/libremdb/main/instances.json',
        {
            'clearnet': 'clearnet',
            'tor': 'tor',
            'i2p': 'i2p',
            'loki': None
        },
        False,
        mightyList
    )


def breezeWiki(mightyList):
    fetchJsonList(
        'breezeWiki',
        'https://docs.breezewiki.com/files/instances.json',
        'instance',
        False,
        mightyList
    )


def binternet(mightyList):
    fetchRegexList(
        'binternet',
        'https://raw.githubusercontent.com/Ahwxorg/Binternet/main/README.md',
        r"\| \[[\w\.]+!?\]\((https?:\/{2}(?:\S+\.)+[a-zA-Z0-9]*)\/?\)",
        mightyList
    )


def dumb(mightyList):
    fetchJsonList(
        'dumb',
        'https://raw.githubusercontent.com/rramiachraf/dumb/main/instances.json',
        {
            'clearnet': 'clearnet',
            'tor': 'tor',
            'i2p': 'i2p',
            'loki': None
        },
        False,
        mightyList
    )


def suds(mightyList):
    fetchJsonList(
        'suds', 'https://git.vern.cc/cobra/Suds/raw/branch/main/instances.json',
        {
            'clearnet': 'clearnet',
            'tor': 'tor',
            'i2p': 'i2p',
            'loki': None
        },
        False,
        mightyList
    )


def proxigram(mightyList):
    fetchRegexList(
        'proxigram',
        'https://codeberg.org/ThePenguinDev/Proxigram/wiki/raw/Instances.md',
        r"\[(https?:\/{2}(?:[^\s\/]+\.)+[a-zA-Z0-9]+)\/?\]",
        mightyList
    )


def rimgo(mightyList):
    try:
        r = requests.get('https://rimgo.codeberg.page/api.json')
        rJson = json.loads(r.text)
        _list = {
            'clearnet': [],
            'tor': [],
        }
        for instance in rJson['clearnet']:
            _list['clearnet'].append(instance['url'])

        for instance in rJson['tor']:
            _list['tor'].append(instance['url'])

        mightyList['rimgo'] = _list
        print(Fore.GREEN + 'Fetched ' + Style.RESET_ALL + 'rimgo')
    except Exception:
        fetchCache('rimgo')
        logging.error(traceback.format_exc())


def jiti(mightyList):
    fetchRegexList(
        'jitsi',
        "https://raw.githubusercontent.com/jitsi/handbook/master/docs/community/instances.md",
        r"\|(?:(?: |	)+)+((?:[a-z]+\.)+[a-z]+)(?:(?: |	)+)+\|",
        mightyList
    )
    mightyList['jitsi']['clearnet'] = list(
        map(
            lambda x: "https://"+x,
            mightyList['jitsi']['clearnet']
        )
    )
    mightyList['jitsi']['clearnet'].insert(0, 'https://8x8.vc')
    mightyList['jitsi']['clearnet'].insert(0, 'https://meet.jit.si')


def anonymousOverflow(mightyList):
    fetchRegexList(
        'anonymousOverflow',
        'https://raw.githubusercontent.com/httpjamesm/AnonymousOverflow/main/README.md',
        r"\| \[(?:[^\s\/]+\.)+[a-zA-Z0-9]+\]\((https?:\/{2}(?:[^\s\/]+\.)+[a-zA-Z0-9]+)\/?\) +\|",
        mightyList
    )


def proxitok(mightyList):
    fetchRegexList(
        'proxiTok',
        'https://raw.githubusercontent.com/wiki/pablouser1/ProxiTok/Public-instances.md',
        r"\| \[.*\]\(([-a-zA-Z0-9@:%_\+.~#?&//=]{2,}\.[a-z]{2,}\b(?:\/[-a-zA-Z0-9@:%_\+.~#?&//=]*)?)\)(?: \(Official\))? +\|(?:(?: [A-Z]*.*\|.*\|)|(?:$))",
        mightyList
    )


def priviblur(mightyList):
    fetchRegexList(
        'priviblur',
        'https://raw.githubusercontent.com/syeopite/priviblur/master/instances.md',
        r"\| ?\[.*\]\((https?:\/{2}(?:[^\s\/]+\.)+[a-zA-Z0-9]+)\) ?|",
        mightyList
    )


def safetwitch(mightyList):
    fetchRegexList(
        'safetwitch',
        'https://codeberg.org/dragongoose/safetwitch/raw/branch/master/README.md',
        re.compile(
            r"^\| \[.*?\]\((https?:\/{2}(?:[^\s\/]+\.)*(?:[^\s\/]+\.)+[a-zA-Z0-9]+)\/?\)",
            re.MULTILINE
        ),
        mightyList
    )


def nitter(mightyList):
    frontend = 'nitter'
    try:
        r = requests.get(
            'https://raw.githubusercontent.com/wiki/zedeus/nitter/Instances.md')
        _list = {}

        _list['clearnet'] = []
        public = re.findall(r"## Public((?:\n|.*)+?)##", r.text)
        if public:
            for line in public[0].split('\n'):
                result = re.findall(r"^\| \[.*?\]\((https.*?)\)", line)
                if len(result) > 0:
                    _list['clearnet'].append(result[0])

        _list['tor'] = []
        public = re.findall(r"## Tor((?:\n|.*)+?)##", r.text)
        if public:
            for line in public[0].split('\n'):
                result = re.findall(r"^\| <(http.*?)\/?>", line)
                if len(result) > 0:
                    _list['tor'].append(result[0])

        _list['i2p'] = []
        public = re.findall(r"## I2P((?:\n|.*)+?)##", r.text)
        if public:
            for line in public[0].split('\n'):
                result = re.findall(r"^- <(http.*?)\/?>", line)
                if len(result) > 0:
                    _list['i2p'].append(result[0])

        _list['loki'] = []
        public = re.findall(r"## Lokinet((?:\n|.*)+?)##", r.text)
        if public:
            for line in public[0].split('\n'):
                result = re.findall(r"^- <(http.*?)\/?>", line)
                if len(result) > 0:
                    _list['loki'].append(result[0])

        mightyList[frontend] = _list
        print(Fore.GREEN + 'Fetched ' + Style.RESET_ALL + frontend)

    except Exception:
        fetchCache(frontend, mightyList)
        logging.error(traceback.format_exc())


def send(mightyList):
    fetchRegexList(
        'send',
        'https://gitlab.com/timvisee/send-instances/-/raw/master/README.md',
        r"(https.*?) \|.*?\n",
        mightyList
    )


def quetre(mightyList):
    fetchJsonList(
        'quetre',
        'https://raw.githubusercontent.com/zyachel/quetre/main/instances.json',
        {
            'clearnet': 'clearnet',
            'tor': 'tor',
            'i2p': 'i2p',
            'loki': None
        },
        False,
        mightyList
    )


def privateBin(mightyList):
    fetchJsonList(
        'privateBin',
        'https://privatebin.info/directory/api?top=100&https_redirect=true&min_rating=A&csp_header=true&min_uptime=100&attachments=true',
        'url',
        False,
        mightyList
    )