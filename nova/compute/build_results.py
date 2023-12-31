# Copyright 2014 OpenStack Foundation
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

"""Possible results from instance build

Results represent the ultimate result of an attempt to build an instance.

Results describe whether an instance was actually built, failed to build, or
was rescheduled.
"""

ACTIVE = 'active'  # Instance is running
FAILED = 'failed'  # Instance failed to build and was not rescheduled
RESCHEDULED = 'rescheduled'  # Instance failed to build, but was rescheduled
# Instance failed by policy violation (such as affinity or anti-affinity)
# and was not rescheduled. In this case, the node's failed count won't be
# increased.
FAILED_BY_POLICY = 'failed_by_policy'
# Instance failed by policy violation (such as affinity or anti-affinity)
# but was rescheduled. In this case, the node's failed count won't be
# increased.
RESCHEDULED_BY_POLICY = 'rescheduled_by_policy'
