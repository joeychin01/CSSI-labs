#!/usr/bin/python
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Replace "pass" with your code

import time

class BankAccount(object):
    def __init__(self, label, balance):
        self.label = label
        self.balance = int(balance)
    def __str__(self):
        return "%s has a balance of %s" % (self.label, self.balance)
    def withdraw(self, amt):
        if int(amt) < self.balance and amt > 0:
            self.balance = self.balance - int(amt)
    def deposit(self, amt):
        if int(amt) > 0:
            self.balance = self.balance + int(amt)
    def rename(self, name):
        if name != "":
            self.label = name
    def transfer(self, other, amt):
        self.withdraw(amt)
        if int(amt) < self.balance and amt > 0:
            other.deposit(amt)
class Transfer(object):
    def __init__(self, type, amt, dest_account = ""):
        self.time = time.time()
        self.type = type
        self.amount = amt
        self.dest_account = dest_account

    def __str__(self):
        if type == "transfer":
            return(str(self.time)+": there was a "+self.type+" of "+self.amt+" to "+self.dest_account)
        else:
            return(str(self.time)+": there was a "+self.type+" of "+self.amount)
