# -*- coding: utf-8 -*-

#  Licensed under the Apache License, Version 2.0 (the 'License'); you may
#  not use this file except in compliance with the License. You may obtain
#  a copy of the License at
#
#       https://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an 'AS IS' BASIS, WITHOUT
#  WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#  License for the specific language governing permissions and limitations
#  under the License.

from __future__ import unicode_literals, absolute_import

import unittest

from linebot.models import TextMessage
from linebot.models.sticon import Sticon
from tests.models.serialize_test_case import SerializeTestCase


class TestTextMessage(SerializeTestCase):
    def test_sticon(self):
        arg = {
            "type": "text",
            "text": "$ LINE emoji $",
            'sticon': [
                Sticon(
                    index=0,
                    product_id='5ac1bfd5040ab15980c9b435',
                    sticon_id='001'
                ),
                Sticon(
                    index=13,
                    product_id='5ac1bfd5040ab15980c9b435',
                    sticon_id='002'
                ),
            ]
        }
        self.assertEqual(
            self.serialize_as_dict(arg, type=self.TEXT),
            TextMessage(**arg).as_json_dict()
        )

    def test_null_sticon(self):
        arg = {
            "type": "text",
            "text": "\uDBC0\uDC84 LINE original emoji"
        }
        self.assertEqual(
            self.serialize_as_dict(arg, type=self.TEXT),
            TextMessage(**arg).as_json_dict()
        )


if __name__ == '__main__':
    unittest.main()