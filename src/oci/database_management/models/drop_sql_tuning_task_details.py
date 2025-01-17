# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DropSqlTuningTaskDetails(object):
    """
    Request to drop a SQL tuning task.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DropSqlTuningTaskDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param task_id:
            The value to assign to the task_id property of this DropSqlTuningTaskDetails.
        :type task_id: int

        :param credential_details:
            The value to assign to the credential_details property of this DropSqlTuningTaskDetails.
        :type credential_details: oci.database_management.models.SqlTuningTaskCredentialDetails

        """
        self.swagger_types = {
            'task_id': 'int',
            'credential_details': 'SqlTuningTaskCredentialDetails'
        }

        self.attribute_map = {
            'task_id': 'taskId',
            'credential_details': 'credentialDetails'
        }

        self._task_id = None
        self._credential_details = None

    @property
    def task_id(self):
        """
        **[Required]** Gets the task_id of this DropSqlTuningTaskDetails.
        The identifier of the task being dropped. This is not the `OCID`__.
        It can be retrieved from the following endpoint
        :func:`list_sql_tuning_advisor_tasks`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The task_id of this DropSqlTuningTaskDetails.
        :rtype: int
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """
        Sets the task_id of this DropSqlTuningTaskDetails.
        The identifier of the task being dropped. This is not the `OCID`__.
        It can be retrieved from the following endpoint
        :func:`list_sql_tuning_advisor_tasks`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param task_id: The task_id of this DropSqlTuningTaskDetails.
        :type: int
        """
        self._task_id = task_id

    @property
    def credential_details(self):
        """
        **[Required]** Gets the credential_details of this DropSqlTuningTaskDetails.

        :return: The credential_details of this DropSqlTuningTaskDetails.
        :rtype: oci.database_management.models.SqlTuningTaskCredentialDetails
        """
        return self._credential_details

    @credential_details.setter
    def credential_details(self, credential_details):
        """
        Sets the credential_details of this DropSqlTuningTaskDetails.

        :param credential_details: The credential_details of this DropSqlTuningTaskDetails.
        :type: oci.database_management.models.SqlTuningTaskCredentialDetails
        """
        self._credential_details = credential_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
