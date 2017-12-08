#!/usr/bin/env python
# -*- coding:utf-8 -*-
# arthur:Dear
# 2017-09-20 10:09:47

import salt.client


class LocalClient:
    def __init__(self):
        # self.master_opts = salt.config.client_config(config)
        self.client = salt.client.LocalClient()

    def cmd(self, tgt, fun, *args, **kwargs):
        return self.client.cmd(tgt, fun, *args, **kwargs)

    def cmd_async(self, tgt, fun, *args, **kwargs):
        return self.client.cmd_async(tgt, fun, *args, **kwargs)

