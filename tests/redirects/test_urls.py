# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

"""Test redirects from the global.conf file."""

import pytest
import requests

from .base import assert_valid_url
from .map_410 import URLS_410


@pytest.mark.headless
@pytest.mark.nondestructive
@pytest.mark.django_db
@pytest.mark.parametrize("url", URLS_410)
def test_410_url(url, base_url):
    assert_valid_url(url, base_url=base_url, status_code=requests.codes.gone)


@pytest.mark.headless
@pytest.mark.nondestructive
@pytest.mark.django_db
def test_404_url(base_url):
    assert_valid_url(
        "/en-US/jozxyqk",
        base_url=base_url,
        final_status_code=requests.codes.not_found,
        follow_redirects=True,
    )


@pytest.mark.headless
@pytest.mark.nondestructive
@pytest.mark.django_db
@pytest.mark.parametrize(
    "url",
    [
        "/firefox/",
        "/firefox/new/",
        "/firefox/all/",
        "/firefox/android/",
        "/firefox/android/faq/",
        "/firefox/channel/",
        "/firefox/developer/",
        "/firefox/desktop/",
        "/firefox/mobile/",
        "/firefox/notes/",
        "/firefox/releasenotes/",
        "/firefox/latest/releasenotes/",
        "/firefox/android/releasenotes/",
        "/firefox/ios/releasenotes/",
        "/firefox/releases/",
        "/firefox/system-requirements/",
        "/firefox/installer-help/",
        "/firefox/unsupported/EOL/",
        "/firefox/unsupported-systems/",        
        "/firefox/nightly/whatsnew/",
        # Legacy URLs (Bug 1110927)
        "/firefox/start/central.html",
        "/firefox/sync/firstrun.html",
    ],
)
def test_301_urls(url, base_url, follow_redirects=False):
    assert_valid_url(url, base_url=base_url, follow_redirects=follow_redirects)


@pytest.mark.headless
@pytest.mark.nondestructive
@pytest.mark.django_db
@pytest.mark.parametrize(
    "url",
    [
        "/firefox/nightly/firstrun/",
    ],
)
def test_302_urls(url, base_url, follow_redirects=False):
    assert_valid_url(url, base_url=base_url, follow_redirects=follow_redirects, status_code=requests.codes.found)
