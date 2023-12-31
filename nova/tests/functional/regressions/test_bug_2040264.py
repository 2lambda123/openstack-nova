# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from nova.tests import fixtures as nova_fixtures
from nova.tests.functional import integrated_helpers


class ComputeVersion6xPinnedRpcTests(integrated_helpers._IntegratedTestBase):

    compute_driver = 'fake.MediumFakeDriver'
    ADMIN_API = True
    api_major_version = 'v2.1'
    microversion = 'latest'

    def setUp(self):
        super(ComputeVersion6xPinnedRpcTests, self).setUp()
        self.useFixture(nova_fixtures.CastAsCallFixture(self))

        self.compute1 = self._start_compute(host='host1')

    def _test_rebuild_instance_with_compute_rpc_pin(self, version_cap):
        # Since passing the latest microversion (>= 2.93) passes
        # the 'reimage_boot_volume' parameter as True and it is
        # not acceptable with compute RPC version (required 6.1)
        # These tests fail, so assigning microversion to 2.92
        self.api.microversion = '2.92'
        self.flags(compute=version_cap, group='upgrade_levels')

        server_req = self._build_server(networks='none')
        server = self.api.post_server({'server': server_req})
        server = self._wait_for_state_change(server, 'ACTIVE')

        self.api.post_server_action(server['id'], {'rebuild': {
            'imageRef': '155d900f-4e14-4e4c-a73d-069cbf4541e6'
        }})

    # We automatically pin to 6.0 if old computes are Yoga or older.
    def test_rebuild_instance_6_0(self):
        self._test_rebuild_instance_with_compute_rpc_pin('6.0')

    # We automatically pin to 6.1 if old computes are Zed.
    def test_rebuild_instance_6_1(self):
        self._test_rebuild_instance_with_compute_rpc_pin('6.1')

    # We automatically pin to 6.2 if old computes are 2023.1.
    def test_rebuild_instance_6_2(self):
        self._test_rebuild_instance_with_compute_rpc_pin('6.2')
