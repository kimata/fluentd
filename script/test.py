#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import fluent.sender

HOST = "192.168.4.5"

sender = fluent.sender.FluentSender("test", host=HOST)
sender.emit("test", {"message": "This is test"})
