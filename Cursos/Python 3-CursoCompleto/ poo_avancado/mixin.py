#!/usr/bin/python3
class HtmlToStringMixin:
    def __str__(self):
        #Conversão para html
        html = super().__str__() \
            .replace('(', '<strong>(') \
            .replace(')', ')</strong>')
        return f',<span>{html}</span>'