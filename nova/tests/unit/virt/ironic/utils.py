# Copyright 2014 Red Hat, Inc.
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

from openstack.baremetal.v1 import node as _node
from openstack.baremetal.v1 import port as _port
from openstack.baremetal.v1 import port_group as _port_group
from openstack.baremetal.v1 import volume_connector as _volume_connector
from openstack.baremetal.v1 import volume_target as _volume_target

from nova import objects
from nova.virt.ironic import ironic_states


def get_test_validation(**kw):
    result = {
        'power': _node.ValidationResult(result=True, reason=None),
        'deploy': _node.ValidationResult(result=True, reason=None),
        'console': _node.ValidationResult(result=True, reason=None),
        'rescue': _node.ValidationResult(result=True, reason=None),
        'storage': _node.ValidationResult(result=True, reason=None),
    }
    result.update(kw)
    return result


def get_test_node(fields=None, **kw):
    # NOTE(stephenfin): Prevent invalid properties making their way through
    if 'uuid' in kw or 'instance_uuid' in kw or 'maintenance' in kw:
        raise Exception('Invalid property provided')

    node = {
        'id': kw.get('id', 'eeeeeeee-dddd-cccc-bbbb-aaaaaaaaaaaa'),
        'chassis_uuid': kw.get('chassis_uuid'),
        'power_state': kw.get('power_state', ironic_states.NOSTATE),
        'target_power_state': kw.get('target_power_state',
                                     ironic_states.NOSTATE),
        'provision_state': kw.get('provision_state', ironic_states.AVAILABLE),
        'target_provision_state': kw.get('target_provision_state',
                                         ironic_states.NOSTATE),
        'last_error': kw.get('last_error'),
        'instance_id': kw.get('instance_id'),
        'instance_info': kw.get('instance_info'),
        'driver': kw.get('driver', 'fake'),
        'driver_info': kw.get('driver_info', {}),
        'properties': kw.get('properties', {}),
        'reservation': kw.get('reservation'),
        'is_maintenance': kw.get('is_maintenance'),
        'network_interface': kw.get('network_interface'),
        'resource_class': kw.get('resource_class'),
        'traits': kw.get('traits', []),
        'extra': kw.get('extra', {}),
        'updated_at': kw.get('created_at'),
        'created_at': kw.get('updated_at'),
    }

    if fields is not None:
        node = {key: value for key, value in node.items() if key in fields}

    return _node.Node(**node)


def get_test_port(**kw):
    # NOTE(stephenfin): Prevent invalid properties making their way through
    if 'uuid' in kw or 'node_uuid' in kw or 'portgroup_uuid' in kw:
        raise Exception('Invalid property provided')

    port = {
        'id': kw.get('id', 'gggggggg-uuuu-qqqq-ffff-llllllllllll'),
        'node_id': kw.get('node_id', get_test_node().id),
        'address': kw.get('address', 'FF:FF:FF:FF:FF:FF'),
        'extra': kw.get('extra', {}),
        'internal_info': kw.get('internal_info', {}),
        'port_group_id': kw.get('port_group_id'),
        'created_at': kw.get('created_at'),
        'updated_at': kw.get('updated_at'),
    }

    return _port.Port(**port)


def get_test_portgroup(**kw):
    # NOTE(stephenfin): Prevent invalid properties making their way through
    if 'uuid' in kw or 'node_uuid' in kw:
        raise Exception('Invalid property provided')

    port_group = {
        'id': kw.get('id', 'deaffeed-1234-5678-9012-fedcbafedcba'),
        'node_id': kw.get('node_id', get_test_node().id),
        'address': kw.get('address', 'EE:EE:EE:EE:EE:EE'),
        'extra': kw.get('extra', {}),
        'internal_info': kw.get('internal_info', {}),
        'properties': kw.get('properties', {}),
        'mode': kw.get('mode', 'active-backup'),
        'name': kw.get('name'),
        'is_standalone_ports_supported': kw.get(
            'is_standalone_ports_supported', True,
        ),
        'created_at': kw.get('created_at'),
        'updated_at': kw.get('updated_at'),
    }

    return _port_group.PortGroup(**port_group)


def get_test_vif(**kw):
    return {
        'profile': kw.get('profile', {}),
        'ovs_interfaceid': kw.get('ovs_interfaceid'),
        'preserve_on_delete': kw.get('preserve_on_delete', False),
        'network': kw.get('network', {}),
        'devname': kw.get('devname', 'tapaaaaaaaa-00'),
        'vnic_type': kw.get('vnic_type', 'baremetal'),
        'qbh_params': kw.get('qbh_params'),
        'meta': kw.get('meta', {}),
        'details': kw.get('details', {}),
        'address': kw.get('address', 'FF:FF:FF:FF:FF:FF'),
        'active': kw.get('active', True),
        'type': kw.get('type', 'ironic'),
        'id': kw.get('id', 'aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee'),
        'qbg_params': kw.get('qbg_params'),
    }


def get_test_volume_connector(**kw):
    # NOTE(stephenfin): Prevent invalid properties making their way through
    if 'uuid' in kw or 'node_uuid' in kw:
        raise Exception('Invalid property provided')

    volume_connector = {
        'id': kw.get('id', 'hhhhhhhh-qqqq-uuuu-mmmm-bbbbbbbbbbbb'),
        'node_id': kw.get('node_id', get_test_node().id),
        'type': kw.get('type', 'iqn'),
        'connector_id': kw.get('connector_id', 'iqn.test'),
        'extra': kw.get('extra', {}),
        'created_at': kw.get('created_at'),
        'updated_at': kw.get('updated_at'),
    }

    return _volume_connector.VolumeConnector(**volume_connector)


def get_test_volume_target(**kw):
    # NOTE(stephenfin): Prevent invalid properties making their way through
    if 'uuid' in kw or 'node_uuid' in kw:
        raise Exception('Invalid property provided')

    volume_target = {
        'id': kw.get('id', 'aaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee'),
        'node_id': kw.get('node_id', get_test_node().id),
        'volume_type': kw.get('volume_type', 'iscsi'),
        'properties': kw.get('properties', {}),
        'boot_index': kw.get('boot_index', 0),
        'volume_id': kw.get(
            'volume_id', 'fffffff-gggg-hhhh-iiii-jjjjjjjjjjjj',
        ),
        'extra': kw.get('extra', {}),
        'created_at': kw.get('created_at'),
        'updated_at': kw.get('updated_at'),
    }

    return _volume_target.VolumeTarget(**volume_target)


def get_test_flavor(**kw):
    default_extra_specs = {
        'baremetal:deploy_kernel_id': 'aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa',
        'baremetal:deploy_ramdisk_id': 'bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb',
    }
    flavor = {
        'name': kw.get('name', 'fake.flavor'),
        'extra_specs': kw.get('extra_specs', default_extra_specs),
        'swap': kw.get('swap', 0),
        'root_gb': 1,
        'memory_mb': 1,
        'vcpus': 1,
        'ephemeral_gb': kw.get('ephemeral_gb', 0),
    }

    return objects.Flavor(**flavor)


def get_test_image_meta(**kw):
    return objects.ImageMeta.from_dict(
        {'id': kw.get('id', 'cccccccc-cccc-cccc-cccc-cccccccccccc')},
    )
