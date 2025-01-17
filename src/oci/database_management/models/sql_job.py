# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .job import Job
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SqlJob(Job):
    """
    The details of the SQL job.
    """

    #: A constant which can be used with the sql_type property of a SqlJob.
    #: This constant has a value of "QUERY"
    SQL_TYPE_QUERY = "QUERY"

    #: A constant which can be used with the sql_type property of a SqlJob.
    #: This constant has a value of "DML"
    SQL_TYPE_DML = "DML"

    #: A constant which can be used with the sql_type property of a SqlJob.
    #: This constant has a value of "DDL"
    SQL_TYPE_DDL = "DDL"

    #: A constant which can be used with the sql_type property of a SqlJob.
    #: This constant has a value of "PLSQL"
    SQL_TYPE_PLSQL = "PLSQL"

    #: A constant which can be used with the operation_type property of a SqlJob.
    #: This constant has a value of "EXECUTE_SQL"
    OPERATION_TYPE_EXECUTE_SQL = "EXECUTE_SQL"

    #: A constant which can be used with the role property of a SqlJob.
    #: This constant has a value of "NORMAL"
    ROLE_NORMAL = "NORMAL"

    #: A constant which can be used with the role property of a SqlJob.
    #: This constant has a value of "SYSDBA"
    ROLE_SYSDBA = "SYSDBA"

    def __init__(self, **kwargs):
        """
        Initializes a new SqlJob object with values from keyword arguments. The default value of the :py:attr:`~oci.database_management.models.SqlJob.job_type` attribute
        of this class is ``SQL`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this SqlJob.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this SqlJob.
        :type compartment_id: str

        :param name:
            The value to assign to the name property of this SqlJob.
        :type name: str

        :param description:
            The value to assign to the description property of this SqlJob.
        :type description: str

        :param managed_database_group_id:
            The value to assign to the managed_database_group_id property of this SqlJob.
        :type managed_database_group_id: str

        :param managed_database_id:
            The value to assign to the managed_database_id property of this SqlJob.
        :type managed_database_id: str

        :param managed_databases_details:
            The value to assign to the managed_databases_details property of this SqlJob.
        :type managed_databases_details: list[oci.database_management.models.JobDatabase]

        :param database_sub_type:
            The value to assign to the database_sub_type property of this SqlJob.
            Allowed values for this property are: "CDB", "PDB", "NON_CDB", "ACD", "ADB", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type database_sub_type: str

        :param schedule_type:
            The value to assign to the schedule_type property of this SqlJob.
            Allowed values for this property are: "IMMEDIATE", "LATER", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type schedule_type: str

        :param job_type:
            The value to assign to the job_type property of this SqlJob.
            Allowed values for this property are: "SQL", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type job_type: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this SqlJob.
            Allowed values for this property are: "ACTIVE", "INACTIVE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param timeout:
            The value to assign to the timeout property of this SqlJob.
        :type timeout: str

        :param result_location:
            The value to assign to the result_location property of this SqlJob.
        :type result_location: oci.database_management.models.JobExecutionResultLocation

        :param schedule_details:
            The value to assign to the schedule_details property of this SqlJob.
        :type schedule_details: oci.database_management.models.JobScheduleDetails

        :param submission_error_message:
            The value to assign to the submission_error_message property of this SqlJob.
        :type submission_error_message: str

        :param time_created:
            The value to assign to the time_created property of this SqlJob.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this SqlJob.
        :type time_updated: datetime

        :param sql_type:
            The value to assign to the sql_type property of this SqlJob.
            Allowed values for this property are: "QUERY", "DML", "DDL", "PLSQL", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type sql_type: str

        :param sql_text:
            The value to assign to the sql_text property of this SqlJob.
        :type sql_text: str

        :param operation_type:
            The value to assign to the operation_type property of this SqlJob.
            Allowed values for this property are: "EXECUTE_SQL", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type operation_type: str

        :param user_name:
            The value to assign to the user_name property of this SqlJob.
        :type user_name: str

        :param role:
            The value to assign to the role property of this SqlJob.
            Allowed values for this property are: "NORMAL", "SYSDBA", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type role: str

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'name': 'str',
            'description': 'str',
            'managed_database_group_id': 'str',
            'managed_database_id': 'str',
            'managed_databases_details': 'list[JobDatabase]',
            'database_sub_type': 'str',
            'schedule_type': 'str',
            'job_type': 'str',
            'lifecycle_state': 'str',
            'timeout': 'str',
            'result_location': 'JobExecutionResultLocation',
            'schedule_details': 'JobScheduleDetails',
            'submission_error_message': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'sql_type': 'str',
            'sql_text': 'str',
            'operation_type': 'str',
            'user_name': 'str',
            'role': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'name': 'name',
            'description': 'description',
            'managed_database_group_id': 'managedDatabaseGroupId',
            'managed_database_id': 'managedDatabaseId',
            'managed_databases_details': 'managedDatabasesDetails',
            'database_sub_type': 'databaseSubType',
            'schedule_type': 'scheduleType',
            'job_type': 'jobType',
            'lifecycle_state': 'lifecycleState',
            'timeout': 'timeout',
            'result_location': 'resultLocation',
            'schedule_details': 'scheduleDetails',
            'submission_error_message': 'submissionErrorMessage',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'sql_type': 'sqlType',
            'sql_text': 'sqlText',
            'operation_type': 'operationType',
            'user_name': 'userName',
            'role': 'role'
        }

        self._id = None
        self._compartment_id = None
        self._name = None
        self._description = None
        self._managed_database_group_id = None
        self._managed_database_id = None
        self._managed_databases_details = None
        self._database_sub_type = None
        self._schedule_type = None
        self._job_type = None
        self._lifecycle_state = None
        self._timeout = None
        self._result_location = None
        self._schedule_details = None
        self._submission_error_message = None
        self._time_created = None
        self._time_updated = None
        self._sql_type = None
        self._sql_text = None
        self._operation_type = None
        self._user_name = None
        self._role = None
        self._job_type = 'SQL'

    @property
    def sql_type(self):
        """
        Gets the sql_type of this SqlJob.
        The type of SQL. This is a mandatory field for the EXECUTE_SQL operationType.

        Allowed values for this property are: "QUERY", "DML", "DDL", "PLSQL", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The sql_type of this SqlJob.
        :rtype: str
        """
        return self._sql_type

    @sql_type.setter
    def sql_type(self, sql_type):
        """
        Sets the sql_type of this SqlJob.
        The type of SQL. This is a mandatory field for the EXECUTE_SQL operationType.


        :param sql_type: The sql_type of this SqlJob.
        :type: str
        """
        allowed_values = ["QUERY", "DML", "DDL", "PLSQL"]
        if not value_allowed_none_or_none_sentinel(sql_type, allowed_values):
            sql_type = 'UNKNOWN_ENUM_VALUE'
        self._sql_type = sql_type

    @property
    def sql_text(self):
        """
        Gets the sql_text of this SqlJob.
        The SQL text to be executed in the job. This is a mandatory field for the EXECUTE_SQL operationType.


        :return: The sql_text of this SqlJob.
        :rtype: str
        """
        return self._sql_text

    @sql_text.setter
    def sql_text(self, sql_text):
        """
        Sets the sql_text of this SqlJob.
        The SQL text to be executed in the job. This is a mandatory field for the EXECUTE_SQL operationType.


        :param sql_text: The sql_text of this SqlJob.
        :type: str
        """
        self._sql_text = sql_text

    @property
    def operation_type(self):
        """
        **[Required]** Gets the operation_type of this SqlJob.
        The SQL operation type.

        Allowed values for this property are: "EXECUTE_SQL", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The operation_type of this SqlJob.
        :rtype: str
        """
        return self._operation_type

    @operation_type.setter
    def operation_type(self, operation_type):
        """
        Sets the operation_type of this SqlJob.
        The SQL operation type.


        :param operation_type: The operation_type of this SqlJob.
        :type: str
        """
        allowed_values = ["EXECUTE_SQL"]
        if not value_allowed_none_or_none_sentinel(operation_type, allowed_values):
            operation_type = 'UNKNOWN_ENUM_VALUE'
        self._operation_type = operation_type

    @property
    def user_name(self):
        """
        Gets the user_name of this SqlJob.
        The database user name used to execute the SQL job. If the job is being executed on a Managed Database Group,
        then the user name should exist on all the databases in the group with the same password.


        :return: The user_name of this SqlJob.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """
        Sets the user_name of this SqlJob.
        The database user name used to execute the SQL job. If the job is being executed on a Managed Database Group,
        then the user name should exist on all the databases in the group with the same password.


        :param user_name: The user_name of this SqlJob.
        :type: str
        """
        self._user_name = user_name

    @property
    def role(self):
        """
        Gets the role of this SqlJob.
        The role of the database user. Indicates whether the database user is a normal user or sysdba.

        Allowed values for this property are: "NORMAL", "SYSDBA", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The role of this SqlJob.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """
        Sets the role of this SqlJob.
        The role of the database user. Indicates whether the database user is a normal user or sysdba.


        :param role: The role of this SqlJob.
        :type: str
        """
        allowed_values = ["NORMAL", "SYSDBA"]
        if not value_allowed_none_or_none_sentinel(role, allowed_values):
            role = 'UNKNOWN_ENUM_VALUE'
        self._role = role

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
