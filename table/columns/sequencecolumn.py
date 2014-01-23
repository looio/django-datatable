#!/usr/bin/env python
# coding: utf-8

from .base import Column

class SequenceColumn(Column):
    def __init__(self, field, headers, **kwargs):
        self.headers = headers
        super(SequenceColumn, self).__init__(field, **kwargs)

    @property
    def columns(self):
        return [self.get_column(key) for key in self.__len__()]

    def __len__(self):
        return len(self.headers)

    def __getitem__(self, key):
        return self.columns[key]

    def __setitem__(self, key, value):
        self.columns[key] = value

    def get_column(self, key):
        return Column(field=self.get_field(key),
                      header=self.get_header(key),
                      **kwargs)

    def get_field(self, key):
        return ".".join([self.field, str(key)])

    def get_header(self, key):
        return self.headers[key]
