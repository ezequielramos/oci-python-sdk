# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DatabaseInsightsCollection(object):
    """
    Collection of database insight summary objects.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DatabaseInsightsCollection object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param items:
            The value to assign to the items property of this DatabaseInsightsCollection.
        :type items: list[DatabaseInsightSummary]

        """
        self.swagger_types = {
            'items': 'list[DatabaseInsightSummary]'
        }

        self.attribute_map = {
            'items': 'items'
        }

        self._items = None

    @property
    def items(self):
        """
        **[Required]** Gets the items of this DatabaseInsightsCollection.
        Array of database insight summary objects.


        :return: The items of this DatabaseInsightsCollection.
        :rtype: list[DatabaseInsightSummary]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this DatabaseInsightsCollection.
        Array of database insight summary objects.


        :param items: The items of this DatabaseInsightsCollection.
        :type: list[DatabaseInsightSummary]
        """
        self._items = items

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
