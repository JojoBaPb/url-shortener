"""Tests that prove a bug exists. They are marked xfail ("expected to fail").

strict=True means: the moment someone fixes the bug, this test PASSES, pytest reports
that as an error, and reminds them to remove the xfail marker. Bugs can't be fixed
"by accident" without anyone noticing.
"""

import asyncio

import pytest


@pytest.mark.xfail(strict=True, reason="Lost updates: clicks read-then-write (fixed in stage 05)")
async def test_simultaneous_clicks_are_all_counted(client, created):
    await asyncio.gather(*(client.get(f"/{created['key']}") for _ in range(25)))

    stats = (await client.get(f"/stats/{created['secret_key']}")).json()
    assert stats["clicks"] == 25
