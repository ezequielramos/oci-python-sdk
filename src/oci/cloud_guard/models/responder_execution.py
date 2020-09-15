# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ResponderExecution(object):
    """
    Responder Execution Object.
    """

    #: A constant which can be used with the responder_rule_type property of a ResponderExecution.
    #: This constant has a value of "REMEDIATION"
    RESPONDER_RULE_TYPE_REMEDIATION = "REMEDIATION"

    #: A constant which can be used with the responder_rule_type property of a ResponderExecution.
    #: This constant has a value of "NOTIFICATION"
    RESPONDER_RULE_TYPE_NOTIFICATION = "NOTIFICATION"

    #: A constant which can be used with the responder_execution_status property of a ResponderExecution.
    #: This constant has a value of "STARTED"
    RESPONDER_EXECUTION_STATUS_STARTED = "STARTED"

    #: A constant which can be used with the responder_execution_status property of a ResponderExecution.
    #: This constant has a value of "AWAITING_CONFIRMATION"
    RESPONDER_EXECUTION_STATUS_AWAITING_CONFIRMATION = "AWAITING_CONFIRMATION"

    #: A constant which can be used with the responder_execution_status property of a ResponderExecution.
    #: This constant has a value of "AWAITING_INPUT"
    RESPONDER_EXECUTION_STATUS_AWAITING_INPUT = "AWAITING_INPUT"

    #: A constant which can be used with the responder_execution_status property of a ResponderExecution.
    #: This constant has a value of "SUCCEEDED"
    RESPONDER_EXECUTION_STATUS_SUCCEEDED = "SUCCEEDED"

    #: A constant which can be used with the responder_execution_status property of a ResponderExecution.
    #: This constant has a value of "FAILED"
    RESPONDER_EXECUTION_STATUS_FAILED = "FAILED"

    #: A constant which can be used with the responder_execution_status property of a ResponderExecution.
    #: This constant has a value of "SKIPPED"
    RESPONDER_EXECUTION_STATUS_SKIPPED = "SKIPPED"

    #: A constant which can be used with the responder_execution_status property of a ResponderExecution.
    #: This constant has a value of "ALL"
    RESPONDER_EXECUTION_STATUS_ALL = "ALL"

    #: A constant which can be used with the responder_execution_mode property of a ResponderExecution.
    #: This constant has a value of "MANUAL"
    RESPONDER_EXECUTION_MODE_MANUAL = "MANUAL"

    #: A constant which can be used with the responder_execution_mode property of a ResponderExecution.
    #: This constant has a value of "AUTOMATED"
    RESPONDER_EXECUTION_MODE_AUTOMATED = "AUTOMATED"

    #: A constant which can be used with the responder_execution_mode property of a ResponderExecution.
    #: This constant has a value of "ALL"
    RESPONDER_EXECUTION_MODE_ALL = "ALL"

    def __init__(self, **kwargs):
        """
        Initializes a new ResponderExecution object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ResponderExecution.
        :type id: str

        :param responder_rule_id:
            The value to assign to the responder_rule_id property of this ResponderExecution.
        :type responder_rule_id: str

        :param responder_rule_type:
            The value to assign to the responder_rule_type property of this ResponderExecution.
            Allowed values for this property are: "REMEDIATION", "NOTIFICATION", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type responder_rule_type: str

        :param responder_rule_name:
            The value to assign to the responder_rule_name property of this ResponderExecution.
        :type responder_rule_name: str

        :param problem_id:
            The value to assign to the problem_id property of this ResponderExecution.
        :type problem_id: str

        :param region:
            The value to assign to the region property of this ResponderExecution.
        :type region: str

        :param target_id:
            The value to assign to the target_id property of this ResponderExecution.
        :type target_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ResponderExecution.
        :type compartment_id: str

        :param resource_type:
            The value to assign to the resource_type property of this ResponderExecution.
        :type resource_type: str

        :param resource_name:
            The value to assign to the resource_name property of this ResponderExecution.
        :type resource_name: str

        :param time_created:
            The value to assign to the time_created property of this ResponderExecution.
        :type time_created: datetime

        :param time_completed:
            The value to assign to the time_completed property of this ResponderExecution.
        :type time_completed: datetime

        :param responder_execution_status:
            The value to assign to the responder_execution_status property of this ResponderExecution.
            Allowed values for this property are: "STARTED", "AWAITING_CONFIRMATION", "AWAITING_INPUT", "SUCCEEDED", "FAILED", "SKIPPED", "ALL", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type responder_execution_status: str

        :param responder_execution_mode:
            The value to assign to the responder_execution_mode property of this ResponderExecution.
            Allowed values for this property are: "MANUAL", "AUTOMATED", "ALL", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type responder_execution_mode: str

        :param message:
            The value to assign to the message property of this ResponderExecution.
        :type message: str

        :param responder_rule_execution_details:
            The value to assign to the responder_rule_execution_details property of this ResponderExecution.
        :type responder_rule_execution_details: ResponderRuleExecutionDetails

        """
        self.swagger_types = {
            'id': 'str',
            'responder_rule_id': 'str',
            'responder_rule_type': 'str',
            'responder_rule_name': 'str',
            'problem_id': 'str',
            'region': 'str',
            'target_id': 'str',
            'compartment_id': 'str',
            'resource_type': 'str',
            'resource_name': 'str',
            'time_created': 'datetime',
            'time_completed': 'datetime',
            'responder_execution_status': 'str',
            'responder_execution_mode': 'str',
            'message': 'str',
            'responder_rule_execution_details': 'ResponderRuleExecutionDetails'
        }

        self.attribute_map = {
            'id': 'id',
            'responder_rule_id': 'responderRuleId',
            'responder_rule_type': 'responderRuleType',
            'responder_rule_name': 'responderRuleName',
            'problem_id': 'problemId',
            'region': 'region',
            'target_id': 'targetId',
            'compartment_id': 'compartmentId',
            'resource_type': 'resourceType',
            'resource_name': 'resourceName',
            'time_created': 'timeCreated',
            'time_completed': 'timeCompleted',
            'responder_execution_status': 'responderExecutionStatus',
            'responder_execution_mode': 'responderExecutionMode',
            'message': 'message',
            'responder_rule_execution_details': 'responderRuleExecutionDetails'
        }

        self._id = None
        self._responder_rule_id = None
        self._responder_rule_type = None
        self._responder_rule_name = None
        self._problem_id = None
        self._region = None
        self._target_id = None
        self._compartment_id = None
        self._resource_type = None
        self._resource_name = None
        self._time_created = None
        self._time_completed = None
        self._responder_execution_status = None
        self._responder_execution_mode = None
        self._message = None
        self._responder_rule_execution_details = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ResponderExecution.
        The unique identifier of the responder execution


        :return: The id of this ResponderExecution.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ResponderExecution.
        The unique identifier of the responder execution


        :param id: The id of this ResponderExecution.
        :type: str
        """
        self._id = id

    @property
    def responder_rule_id(self):
        """
        **[Required]** Gets the responder_rule_id of this ResponderExecution.
        Responder Rule id for the responder execution


        :return: The responder_rule_id of this ResponderExecution.
        :rtype: str
        """
        return self._responder_rule_id

    @responder_rule_id.setter
    def responder_rule_id(self, responder_rule_id):
        """
        Sets the responder_rule_id of this ResponderExecution.
        Responder Rule id for the responder execution


        :param responder_rule_id: The responder_rule_id of this ResponderExecution.
        :type: str
        """
        self._responder_rule_id = responder_rule_id

    @property
    def responder_rule_type(self):
        """
        **[Required]** Gets the responder_rule_type of this ResponderExecution.
        Rule Type for the responder execution

        Allowed values for this property are: "REMEDIATION", "NOTIFICATION", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The responder_rule_type of this ResponderExecution.
        :rtype: str
        """
        return self._responder_rule_type

    @responder_rule_type.setter
    def responder_rule_type(self, responder_rule_type):
        """
        Sets the responder_rule_type of this ResponderExecution.
        Rule Type for the responder execution


        :param responder_rule_type: The responder_rule_type of this ResponderExecution.
        :type: str
        """
        allowed_values = ["REMEDIATION", "NOTIFICATION"]
        if not value_allowed_none_or_none_sentinel(responder_rule_type, allowed_values):
            responder_rule_type = 'UNKNOWN_ENUM_VALUE'
        self._responder_rule_type = responder_rule_type

    @property
    def responder_rule_name(self):
        """
        **[Required]** Gets the responder_rule_name of this ResponderExecution.
        Rule name for the responder execution


        :return: The responder_rule_name of this ResponderExecution.
        :rtype: str
        """
        return self._responder_rule_name

    @responder_rule_name.setter
    def responder_rule_name(self, responder_rule_name):
        """
        Sets the responder_rule_name of this ResponderExecution.
        Rule name for the responder execution


        :param responder_rule_name: The responder_rule_name of this ResponderExecution.
        :type: str
        """
        self._responder_rule_name = responder_rule_name

    @property
    def problem_id(self):
        """
        **[Required]** Gets the problem_id of this ResponderExecution.
        Problem id associated with the responder execution


        :return: The problem_id of this ResponderExecution.
        :rtype: str
        """
        return self._problem_id

    @problem_id.setter
    def problem_id(self, problem_id):
        """
        Sets the problem_id of this ResponderExecution.
        Problem id associated with the responder execution


        :param problem_id: The problem_id of this ResponderExecution.
        :type: str
        """
        self._problem_id = problem_id

    @property
    def region(self):
        """
        **[Required]** Gets the region of this ResponderExecution.
        region where the problem is found


        :return: The region of this ResponderExecution.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """
        Sets the region of this ResponderExecution.
        region where the problem is found


        :param region: The region of this ResponderExecution.
        :type: str
        """
        self._region = region

    @property
    def target_id(self):
        """
        **[Required]** Gets the target_id of this ResponderExecution.
        targetId of the problem for the responder execution


        :return: The target_id of this ResponderExecution.
        :rtype: str
        """
        return self._target_id

    @target_id.setter
    def target_id(self, target_id):
        """
        Sets the target_id of this ResponderExecution.
        targetId of the problem for the responder execution


        :param target_id: The target_id of this ResponderExecution.
        :type: str
        """
        self._target_id = target_id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ResponderExecution.
        compartment id of the responder execution for the problem


        :return: The compartment_id of this ResponderExecution.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ResponderExecution.
        compartment id of the responder execution for the problem


        :param compartment_id: The compartment_id of this ResponderExecution.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def resource_type(self):
        """
        **[Required]** Gets the resource_type of this ResponderExecution.
        resource type of the problem for the responder execution


        :return: The resource_type of this ResponderExecution.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """
        Sets the resource_type of this ResponderExecution.
        resource type of the problem for the responder execution


        :param resource_type: The resource_type of this ResponderExecution.
        :type: str
        """
        self._resource_type = resource_type

    @property
    def resource_name(self):
        """
        **[Required]** Gets the resource_name of this ResponderExecution.
        resource name of the problem for the responder execution. TODO-DOC link to resource definition doc


        :return: The resource_name of this ResponderExecution.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """
        Sets the resource_name of this ResponderExecution.
        resource name of the problem for the responder execution. TODO-DOC link to resource definition doc


        :param resource_name: The resource_name of this ResponderExecution.
        :type: str
        """
        self._resource_name = resource_name

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this ResponderExecution.
        The date and time the responder execution was created. Format defined by RFC3339.


        :return: The time_created of this ResponderExecution.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ResponderExecution.
        The date and time the responder execution was created. Format defined by RFC3339.


        :param time_created: The time_created of this ResponderExecution.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_completed(self):
        """
        Gets the time_completed of this ResponderExecution.
        The date and time the responder execution was updated. Format defined by RFC3339.


        :return: The time_completed of this ResponderExecution.
        :rtype: datetime
        """
        return self._time_completed

    @time_completed.setter
    def time_completed(self, time_completed):
        """
        Sets the time_completed of this ResponderExecution.
        The date and time the responder execution was updated. Format defined by RFC3339.


        :param time_completed: The time_completed of this ResponderExecution.
        :type: datetime
        """
        self._time_completed = time_completed

    @property
    def responder_execution_status(self):
        """
        **[Required]** Gets the responder_execution_status of this ResponderExecution.
        current execution status of the responder

        Allowed values for this property are: "STARTED", "AWAITING_CONFIRMATION", "AWAITING_INPUT", "SUCCEEDED", "FAILED", "SKIPPED", "ALL", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The responder_execution_status of this ResponderExecution.
        :rtype: str
        """
        return self._responder_execution_status

    @responder_execution_status.setter
    def responder_execution_status(self, responder_execution_status):
        """
        Sets the responder_execution_status of this ResponderExecution.
        current execution status of the responder


        :param responder_execution_status: The responder_execution_status of this ResponderExecution.
        :type: str
        """
        allowed_values = ["STARTED", "AWAITING_CONFIRMATION", "AWAITING_INPUT", "SUCCEEDED", "FAILED", "SKIPPED", "ALL"]
        if not value_allowed_none_or_none_sentinel(responder_execution_status, allowed_values):
            responder_execution_status = 'UNKNOWN_ENUM_VALUE'
        self._responder_execution_status = responder_execution_status

    @property
    def responder_execution_mode(self):
        """
        **[Required]** Gets the responder_execution_mode of this ResponderExecution.
        execution mode of the responder

        Allowed values for this property are: "MANUAL", "AUTOMATED", "ALL", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The responder_execution_mode of this ResponderExecution.
        :rtype: str
        """
        return self._responder_execution_mode

    @responder_execution_mode.setter
    def responder_execution_mode(self, responder_execution_mode):
        """
        Sets the responder_execution_mode of this ResponderExecution.
        execution mode of the responder


        :param responder_execution_mode: The responder_execution_mode of this ResponderExecution.
        :type: str
        """
        allowed_values = ["MANUAL", "AUTOMATED", "ALL"]
        if not value_allowed_none_or_none_sentinel(responder_execution_mode, allowed_values):
            responder_execution_mode = 'UNKNOWN_ENUM_VALUE'
        self._responder_execution_mode = responder_execution_mode

    @property
    def message(self):
        """
        Gets the message of this ResponderExecution.
        Message about the responder execution.


        :return: The message of this ResponderExecution.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this ResponderExecution.
        Message about the responder execution.


        :param message: The message of this ResponderExecution.
        :type: str
        """
        self._message = message

    @property
    def responder_rule_execution_details(self):
        """
        Gets the responder_rule_execution_details of this ResponderExecution.

        :return: The responder_rule_execution_details of this ResponderExecution.
        :rtype: ResponderRuleExecutionDetails
        """
        return self._responder_rule_execution_details

    @responder_rule_execution_details.setter
    def responder_rule_execution_details(self, responder_rule_execution_details):
        """
        Sets the responder_rule_execution_details of this ResponderExecution.

        :param responder_rule_execution_details: The responder_rule_execution_details of this ResponderExecution.
        :type: ResponderRuleExecutionDetails
        """
        self._responder_rule_execution_details = responder_rule_execution_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
