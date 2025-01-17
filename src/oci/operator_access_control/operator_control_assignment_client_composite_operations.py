# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import oci  # noqa: F401
from oci.util import WAIT_RESOURCE_NOT_FOUND  # noqa: F401


class OperatorControlAssignmentClientCompositeOperations(object):
    """
    This class provides a wrapper around :py:class:`~oci.operator_access_control.OperatorControlAssignmentClient` and offers convenience methods
    for operations that would otherwise need to be chained together. For example, instead of performing an action
    on a resource (e.g. launching an instance, creating a load balancer) and then using a waiter to wait for the resource
    to enter a given state, you can call a single method in this class to accomplish the same functionality
    """

    def __init__(self, client, **kwargs):
        """
        Creates a new OperatorControlAssignmentClientCompositeOperations object

        :param OperatorControlAssignmentClient client:
            The service client which will be wrapped by this object
        """
        self.client = client

    def create_operator_control_assignment_and_wait_for_state(self, create_operator_control_assignment_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.operator_access_control.OperatorControlAssignmentClient.create_operator_control_assignment` and waits for the :py:class:`~oci.operator_access_control.models.OperatorControlAssignment` acted upon
        to enter the given state(s).

        :param oci.operator_access_control.models.CreateOperatorControlAssignmentDetails create_operator_control_assignment_details: (required)
            Details of the Operator Control Assignment.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.operator_access_control.models.OperatorControlAssignment.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.operator_access_control.OperatorControlAssignmentClient.create_operator_control_assignment`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_operator_control_assignment(create_operator_control_assignment_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_operator_control_assignment(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def delete_operator_control_assignment_and_wait_for_state(self, operator_control_assignment_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.operator_access_control.OperatorControlAssignmentClient.delete_operator_control_assignment` and waits for the :py:class:`~oci.operator_access_control.models.OperatorControlAssignment` acted upon
        to enter the given state(s).

        :param str operator_control_assignment_id: (required)
            unique OperatorControl identifier

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.operator_access_control.models.OperatorControlAssignment.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.operator_access_control.OperatorControlAssignmentClient.delete_operator_control_assignment`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        initial_get_result = self.client.get_operator_control_assignment(operator_control_assignment_id)
        operation_result = None
        try:
            operation_result = self.client.delete_operator_control_assignment(operator_control_assignment_id, **operation_kwargs)
        except oci.exceptions.ServiceError as e:
            if e.status == 404:
                return WAIT_RESOURCE_NOT_FOUND
            else:
                raise e

        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]

        try:
            waiter_result = oci.wait_until(
                self.client,
                initial_get_result,
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                succeed_on_not_found=True,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_operator_control_assignment_and_wait_for_state(self, operator_control_assignment_id, update_operator_control_assignment_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.operator_access_control.OperatorControlAssignmentClient.update_operator_control_assignment` and waits for the :py:class:`~oci.operator_access_control.models.OperatorControlAssignment` acted upon
        to enter the given state(s).

        :param str operator_control_assignment_id: (required)
            unique OperatorControl identifier

        :param oci.operator_access_control.models.UpdateOperatorControlAssignmentDetails update_operator_control_assignment_details: (required)
            Details for the new operator control assignment.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.operator_access_control.models.OperatorControlAssignment.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.operator_access_control.OperatorControlAssignmentClient.update_operator_control_assignment`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_operator_control_assignment(operator_control_assignment_id, update_operator_control_assignment_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_operator_control_assignment(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)
