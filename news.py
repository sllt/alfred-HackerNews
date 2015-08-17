#!/usr/bin/python
# encoding: utf-8

import sys

from workflow import Workflow, ICON_WEB
from workflow import web

import json

url = "https://hacker-news.firebaseio.com/v0/item/%s.json?print=pretty"

topic = "https://news.ycombinator.com/item?id=%s"

def item_title(item):
    return json.loads(web.get(url % item).content)["title"].decode("utf-8")

def main(wf):

    args = wf.args
    a = web.get("https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty")

    items = json.loads(a.content.decode("utf-8"))[:8]
    for i in items:
        wf.add_item(item_title(i), arg=(topic % i), icon = "icon.png", valid= True)

    # Send output to Alfred
    wf.send_feedback()


if __name__ == '__main__':
    wf = Workflow()
    sys.exit(wf.run(main))