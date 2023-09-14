# This file is part of the Trezor project.
#
# Copyright (C) 2012-2019 SatoshiLabs and contributors
#
# This library is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License version 3
# as published by the Free Software Foundation.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the License along with this library.
# If not, see <https://www.gnu.org/licenses/lgpl-3.0.html>.

import pytest

from trezorlib.debuglink import TrezorClientDebugLink as Client
from trezorlib.tezos import get_address
from trezorlib.tools import parse_path


@pytest.mark.altcoin
@pytest.mark.tezos
@pytest.mark.skip_t1
@pytest.mark.parametrize("chunkify", (True, False))
def test_tezos_get_address(client: Client, chunkify: bool):
    path = parse_path("m/44h/1729h/0h")
    address = get_address(client, path, show_display=True, chunkify=chunkify)
    assert address == "tz1Kef7BSg6fo75jk37WkKRYSnJDs69KVqt9"

    path = parse_path("m/44h/1729h/1h")
    address = get_address(client, path, show_display=True, chunkify=chunkify)
    assert address == "tz1ekQapZCX4AXxTJhJZhroDKDYLHDHegvm1"
