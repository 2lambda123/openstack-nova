# Copyright 2016 Cloudbase Solutions Srl
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from oslo_policy import policy

from nova.policies import base


POLICY_ROOT = 'os_compute_api:os-migrate-server:%s'


migrate_server_policies = [
    policy.DocumentedRuleDefault(
        name=POLICY_ROOT % 'migrate',
        check_str=base.ADMIN,
        description="Cold migrate a server without specifying a host",
        operations=[
            {
                'method': 'POST',
                'path': '/servers/{server_id}/action (migrate)'
            }
        ],
        scope_types=['project']),
    policy.DocumentedRuleDefault(
        name=POLICY_ROOT % 'migrate:host',
        check_str=base.ADMIN,
        description="Cold migrate a server to a specified host",
        operations=[
            {
                'method': 'POST',
                'path': '/servers/{server_id}/action (migrate)'
            }
        ],
        scope_types=['project']),
    policy.DocumentedRuleDefault(
        name=POLICY_ROOT % 'migrate_live',
        check_str=base.ADMIN,
        description="Live migrate a server to a new host without a reboot",
        operations=[
            {
                'method': 'POST',
                'path': '/servers/{server_id}/action (os-migrateLive)'
            }
        ],
        scope_types=['project']),
]


def list_rules():
    return migrate_server_policies
