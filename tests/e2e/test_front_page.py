# -*- coding: utf-8 -*-
#
# Swiss Open Access Repository
# Copyright (C) 2019 RERO
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, version 3 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""E2E test of the front page."""

from flask import url_for


def test_frontpage(live_server, browser):
    """Test retrieval of front page."""
    browser.get(url_for('invenio_theme_frontpage.index', _external=True))
    assert (browser.find_element_by_tag_name('img').get_attribute('alt') ==
            'Swiss Open Access Repository')
