# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BlockVolumeReplicaInfo(object):
    """
    Information about the block volume replica in the destination availability domain.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new BlockVolumeReplicaInfo object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this BlockVolumeReplicaInfo.
        :type display_name: str

        :param block_volume_replica_id:
            The value to assign to the block_volume_replica_id property of this BlockVolumeReplicaInfo.
        :type block_volume_replica_id: str

        :param availability_domain:
            The value to assign to the availability_domain property of this BlockVolumeReplicaInfo.
        :type availability_domain: str

        """
        self.swagger_types = {
            'display_name': 'str',
            'block_volume_replica_id': 'str',
            'availability_domain': 'str'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'block_volume_replica_id': 'blockVolumeReplicaId',
            'availability_domain': 'availabilityDomain'
        }

        self._display_name = None
        self._block_volume_replica_id = None
        self._availability_domain = None

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this BlockVolumeReplicaInfo.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this BlockVolumeReplicaInfo.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this BlockVolumeReplicaInfo.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this BlockVolumeReplicaInfo.
        :type: str
        """
        self._display_name = display_name

    @property
    def block_volume_replica_id(self):
        """
        **[Required]** Gets the block_volume_replica_id of this BlockVolumeReplicaInfo.
        The block volume replica's Oracle ID (OCID).


        :return: The block_volume_replica_id of this BlockVolumeReplicaInfo.
        :rtype: str
        """
        return self._block_volume_replica_id

    @block_volume_replica_id.setter
    def block_volume_replica_id(self, block_volume_replica_id):
        """
        Sets the block_volume_replica_id of this BlockVolumeReplicaInfo.
        The block volume replica's Oracle ID (OCID).


        :param block_volume_replica_id: The block_volume_replica_id of this BlockVolumeReplicaInfo.
        :type: str
        """
        self._block_volume_replica_id = block_volume_replica_id

    @property
    def availability_domain(self):
        """
        **[Required]** Gets the availability_domain of this BlockVolumeReplicaInfo.
        The availability domain of the block volume replica.

        Example: `Uocm:PHX-AD-1`


        :return: The availability_domain of this BlockVolumeReplicaInfo.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this BlockVolumeReplicaInfo.
        The availability domain of the block volume replica.

        Example: `Uocm:PHX-AD-1`


        :param availability_domain: The availability_domain of this BlockVolumeReplicaInfo.
        :type: str
        """
        self._availability_domain = availability_domain

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
