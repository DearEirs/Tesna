#!/usr/bin/env python
# -*- coding:utf-8 -*-
# arthur:Dear
# 2017-09-20 10:09:47

import salt.config
import salt.client


class Salt:
    def __init__(self, config='/etc/salt/master'):
        self.master_opts = salt.config.client_config(config)
        self.client = salt.client.LocalClient()

    def cmd_async(self, tgt, fun, arg=(), tgt_type='glob', ret='', jid='', kwarg=None, **kwargs):
        return self.client.cmd_async(tgt, fun, arg=(), tgt_type='glob', ret='', jid='', kwarg=None, **kwargs)
