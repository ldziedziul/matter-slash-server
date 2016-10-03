#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# coding=utf-8
import json
import urllib


class SlashCommandHandler(object):
    def handle(self, request):
        raise NotImplementedError("Implement me!")


class EuroCommandHandler(SlashCommandHandler):
    def format_latest_rate(self):
        url = "http://stooq.pl/q/l/?s=eurpln&f=sd2t2ohlc&h&e=csv"
        response = urllib.urlopen(url)
        data = response.read()
        rate = data.split("\r\n")[1].split(",")[-1]
        date = data.split("\r\n")[1].split(",")[1]
        return "![Euro](http://stooq.pl/c/?s=eurpln&c=3d&t=l&a=lg)\n\n" + self.format_rate_by_date(date, rate)

    def handle(self, request):
        if request.text:
            date = request.text[0].encode("utf8")
            rate = self.get_euro_rate_by_date(date)
            stripped_date = date.replace("-", "")
            formatted = self.format_rate_by_date(date, rate)
            return ("![Euro](http://stooq.pl/c/?s=eurpln&d=%s&c=3d&t=l&a=lg)\n\n" % stripped_date) + formatted
        else:
            return self.format_latest_rate()

    def get_euro_rate_by_date(sefl, date):
        url = "http://api.fixer.io/%s?symbols=PLN" % date
        response = urllib.urlopen(url)
        data = response.read()
        rate = json.loads(data)["rates"]["PLN"]
        return rate

    def format_rate_by_date(self, date, rate):
        formatted = """|Data       |      Kurs |
    |:----------|----------:|
    |%s | %s PLN|""" % (date, rate)
        return formatted
