# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .activity_time_series_metrics import ActivityTimeSeriesMetrics
from .add_managed_database_to_managed_database_group_details import AddManagedDatabaseToManagedDatabaseGroupDetails
from .allowed_parameter_value import AllowedParameterValue
from .associated_database_collection import AssociatedDatabaseCollection
from .associated_database_summary import AssociatedDatabaseSummary
from .awr_db_collection import AwrDbCollection
from .awr_db_cpu_usage_collection import AwrDbCpuUsageCollection
from .awr_db_cpu_usage_summary import AwrDbCpuUsageSummary
from .awr_db_metric_collection import AwrDbMetricCollection
from .awr_db_metric_summary import AwrDbMetricSummary
from .awr_db_parameter_change_collection import AwrDbParameterChangeCollection
from .awr_db_parameter_change_summary import AwrDbParameterChangeSummary
from .awr_db_parameter_collection import AwrDbParameterCollection
from .awr_db_parameter_summary import AwrDbParameterSummary
from .awr_db_report import AwrDbReport
from .awr_db_snapshot_collection import AwrDbSnapshotCollection
from .awr_db_snapshot_range_collection import AwrDbSnapshotRangeCollection
from .awr_db_snapshot_range_summary import AwrDbSnapshotRangeSummary
from .awr_db_snapshot_summary import AwrDbSnapshotSummary
from .awr_db_sql_report import AwrDbSqlReport
from .awr_db_summary import AwrDbSummary
from .awr_db_sysstat_collection import AwrDbSysstatCollection
from .awr_db_sysstat_summary import AwrDbSysstatSummary
from .awr_db_top_wait_event_collection import AwrDbTopWaitEventCollection
from .awr_db_top_wait_event_summary import AwrDbTopWaitEventSummary
from .awr_db_wait_event_bucket_collection import AwrDbWaitEventBucketCollection
from .awr_db_wait_event_bucket_summary import AwrDbWaitEventBucketSummary
from .awr_db_wait_event_collection import AwrDbWaitEventCollection
from .awr_db_wait_event_summary import AwrDbWaitEventSummary
from .awr_query_result import AwrQueryResult
from .change_database_parameter_details import ChangeDatabaseParameterDetails
from .change_database_parameters_details import ChangeDatabaseParametersDetails
from .change_db_management_private_endpoint_compartment_details import ChangeDbManagementPrivateEndpointCompartmentDetails
from .change_job_compartment_details import ChangeJobCompartmentDetails
from .change_managed_database_group_compartment_details import ChangeManagedDatabaseGroupCompartmentDetails
from .child_database import ChildDatabase
from .clone_sql_tuning_task_details import CloneSqlTuningTaskDetails
from .cluster_cache_metric import ClusterCacheMetric
from .consumer_group_privilege_collection import ConsumerGroupPrivilegeCollection
from .consumer_group_privilege_summary import ConsumerGroupPrivilegeSummary
from .cpu_utilization_aggregate_metrics import CpuUtilizationAggregateMetrics
from .create_db_management_private_endpoint_details import CreateDbManagementPrivateEndpointDetails
from .create_job_details import CreateJobDetails
from .create_managed_database_group_details import CreateManagedDatabaseGroupDetails
from .create_sql_job_details import CreateSqlJobDetails
from .data_access_container_collection import DataAccessContainerCollection
from .data_access_container_summary import DataAccessContainerSummary
from .database_credentials import DatabaseCredentials
from .database_fleet_health_metrics import DatabaseFleetHealthMetrics
from .database_home_metric_definition import DatabaseHomeMetricDefinition
from .database_home_metrics import DatabaseHomeMetrics
from .database_io_aggregate_metrics import DatabaseIOAggregateMetrics
from .database_instance_home_metrics_definition import DatabaseInstanceHomeMetricsDefinition
from .database_parameter_summary import DatabaseParameterSummary
from .database_parameter_update_status import DatabaseParameterUpdateStatus
from .database_parameters_collection import DatabaseParametersCollection
from .database_storage_aggregate_metrics import DatabaseStorageAggregateMetrics
from .database_time_aggregate_metrics import DatabaseTimeAggregateMetrics
from .database_usage_metrics import DatabaseUsageMetrics
from .datafile import Datafile
from .db_management_private_endpoint import DbManagementPrivateEndpoint
from .db_management_private_endpoint_collection import DbManagementPrivateEndpointCollection
from .db_management_private_endpoint_summary import DbManagementPrivateEndpointSummary
from .drop_sql_tuning_task_details import DropSqlTuningTaskDetails
from .execution_plan_stats_comparision import ExecutionPlanStatsComparision
from .failed_connections_aggregate_metrics import FailedConnectionsAggregateMetrics
from .fleet_metric_definition import FleetMetricDefinition
from .fleet_metric_summary_definition import FleetMetricSummaryDefinition
from .fleet_status_by_category import FleetStatusByCategory
from .fleet_summary import FleetSummary
from .instance_details import InstanceDetails
from .job import Job
from .job_collection import JobCollection
from .job_database import JobDatabase
from .job_execution import JobExecution
from .job_execution_collection import JobExecutionCollection
from .job_execution_result_details import JobExecutionResultDetails
from .job_execution_result_location import JobExecutionResultLocation
from .job_execution_summary import JobExecutionSummary
from .job_executions_status_summary import JobExecutionsStatusSummary
from .job_executions_status_summary_collection import JobExecutionsStatusSummaryCollection
from .job_run import JobRun
from .job_run_collection import JobRunCollection
from .job_run_summary import JobRunSummary
from .job_schedule_details import JobScheduleDetails
from .job_summary import JobSummary
from .managed_database import ManagedDatabase
from .managed_database_collection import ManagedDatabaseCollection
from .managed_database_group import ManagedDatabaseGroup
from .managed_database_group_collection import ManagedDatabaseGroupCollection
from .managed_database_group_summary import ManagedDatabaseGroupSummary
from .managed_database_summary import ManagedDatabaseSummary
from .memory_aggregate_metrics import MemoryAggregateMetrics
from .metric_data_point import MetricDataPoint
from .metric_dimension_definition import MetricDimensionDefinition
from .object_privilege_collection import ObjectPrivilegeCollection
from .object_privilege_summary import ObjectPrivilegeSummary
from .object_storage_job_execution_result_details import ObjectStorageJobExecutionResultDetails
from .object_storage_job_execution_result_location import ObjectStorageJobExecutionResultLocation
from .parent_group import ParentGroup
from .pdb_metrics import PdbMetrics
from .pdb_status_details import PdbStatusDetails
from .proxied_for_user_collection import ProxiedForUserCollection
from .proxied_for_user_summary import ProxiedForUserSummary
from .proxy_user_collection import ProxyUserCollection
from .proxy_user_summary import ProxyUserSummary
from .remove_managed_database_from_managed_database_group_details import RemoveManagedDatabaseFromManagedDatabaseGroupDetails
from .reset_database_parameters_details import ResetDatabaseParametersDetails
from .role_collection import RoleCollection
from .role_summary import RoleSummary
from .sql_job import SqlJob
from .sql_tuning_advisor_task_collection import SqlTuningAdvisorTaskCollection
from .sql_tuning_advisor_task_finding_collection import SqlTuningAdvisorTaskFindingCollection
from .sql_tuning_advisor_task_finding_summary import SqlTuningAdvisorTaskFindingSummary
from .sql_tuning_advisor_task_recommendation_collection import SqlTuningAdvisorTaskRecommendationCollection
from .sql_tuning_advisor_task_recommendation_summary import SqlTuningAdvisorTaskRecommendationSummary
from .sql_tuning_advisor_task_sql_execution_plan import SqlTuningAdvisorTaskSqlExecutionPlan
from .sql_tuning_advisor_task_summary import SqlTuningAdvisorTaskSummary
from .sql_tuning_advisor_task_summary_finding_benefits import SqlTuningAdvisorTaskSummaryFindingBenefits
from .sql_tuning_advisor_task_summary_finding_counts import SqlTuningAdvisorTaskSummaryFindingCounts
from .sql_tuning_advisor_task_summary_report import SqlTuningAdvisorTaskSummaryReport
from .sql_tuning_advisor_task_summary_report_index_finding_summary import SqlTuningAdvisorTaskSummaryReportIndexFindingSummary
from .sql_tuning_advisor_task_summary_report_object_stat_finding_summary import SqlTuningAdvisorTaskSummaryReportObjectStatFindingSummary
from .sql_tuning_advisor_task_summary_report_statement_counts import SqlTuningAdvisorTaskSummaryReportStatementCounts
from .sql_tuning_advisor_task_summary_report_statistics import SqlTuningAdvisorTaskSummaryReportStatistics
from .sql_tuning_advisor_task_summary_report_task_info import SqlTuningAdvisorTaskSummaryReportTaskInfo
from .sql_tuning_task_credential_details import SqlTuningTaskCredentialDetails
from .sql_tuning_task_password_credential_details import SqlTuningTaskPasswordCredentialDetails
from .sql_tuning_task_plan_stats import SqlTuningTaskPlanStats
from .sql_tuning_task_return import SqlTuningTaskReturn
from .sql_tuning_task_secret_credential_details import SqlTuningTaskSecretCredentialDetails
from .sql_tuning_task_sql_detail import SqlTuningTaskSqlDetail
from .sql_tuning_task_sql_execution_plan_step import SqlTuningTaskSqlExecutionPlanStep
from .start_sql_tuning_task_details import StartSqlTuningTaskDetails
from .statements_aggregate_metrics import StatementsAggregateMetrics
from .system_privilege_collection import SystemPrivilegeCollection
from .system_privilege_summary import SystemPrivilegeSummary
from .tablespace import Tablespace
from .tablespace_collection import TablespaceCollection
from .tablespace_summary import TablespaceSummary
from .time_series_metric_data_point import TimeSeriesMetricDataPoint
from .time_series_metric_definition import TimeSeriesMetricDefinition
from .update_database_parameters_result import UpdateDatabaseParametersResult
from .update_db_management_private_endpoint_details import UpdateDbManagementPrivateEndpointDetails
from .update_job_details import UpdateJobDetails
from .update_managed_database_group_details import UpdateManagedDatabaseGroupDetails
from .update_sql_job_details import UpdateSqlJobDetails
from .user import User
from .user_collection import UserCollection
from .user_summary import UserSummary
from .work_request import WorkRequest
from .work_request_collection import WorkRequestCollection
from .work_request_error import WorkRequestError
from .work_request_error_collection import WorkRequestErrorCollection
from .work_request_log_entry import WorkRequestLogEntry
from .work_request_log_entry_collection import WorkRequestLogEntryCollection
from .work_request_resource import WorkRequestResource
from .work_request_summary import WorkRequestSummary

# Maps type names to classes for database_management services.
database_management_type_mapping = {
    "ActivityTimeSeriesMetrics": ActivityTimeSeriesMetrics,
    "AddManagedDatabaseToManagedDatabaseGroupDetails": AddManagedDatabaseToManagedDatabaseGroupDetails,
    "AllowedParameterValue": AllowedParameterValue,
    "AssociatedDatabaseCollection": AssociatedDatabaseCollection,
    "AssociatedDatabaseSummary": AssociatedDatabaseSummary,
    "AwrDbCollection": AwrDbCollection,
    "AwrDbCpuUsageCollection": AwrDbCpuUsageCollection,
    "AwrDbCpuUsageSummary": AwrDbCpuUsageSummary,
    "AwrDbMetricCollection": AwrDbMetricCollection,
    "AwrDbMetricSummary": AwrDbMetricSummary,
    "AwrDbParameterChangeCollection": AwrDbParameterChangeCollection,
    "AwrDbParameterChangeSummary": AwrDbParameterChangeSummary,
    "AwrDbParameterCollection": AwrDbParameterCollection,
    "AwrDbParameterSummary": AwrDbParameterSummary,
    "AwrDbReport": AwrDbReport,
    "AwrDbSnapshotCollection": AwrDbSnapshotCollection,
    "AwrDbSnapshotRangeCollection": AwrDbSnapshotRangeCollection,
    "AwrDbSnapshotRangeSummary": AwrDbSnapshotRangeSummary,
    "AwrDbSnapshotSummary": AwrDbSnapshotSummary,
    "AwrDbSqlReport": AwrDbSqlReport,
    "AwrDbSummary": AwrDbSummary,
    "AwrDbSysstatCollection": AwrDbSysstatCollection,
    "AwrDbSysstatSummary": AwrDbSysstatSummary,
    "AwrDbTopWaitEventCollection": AwrDbTopWaitEventCollection,
    "AwrDbTopWaitEventSummary": AwrDbTopWaitEventSummary,
    "AwrDbWaitEventBucketCollection": AwrDbWaitEventBucketCollection,
    "AwrDbWaitEventBucketSummary": AwrDbWaitEventBucketSummary,
    "AwrDbWaitEventCollection": AwrDbWaitEventCollection,
    "AwrDbWaitEventSummary": AwrDbWaitEventSummary,
    "AwrQueryResult": AwrQueryResult,
    "ChangeDatabaseParameterDetails": ChangeDatabaseParameterDetails,
    "ChangeDatabaseParametersDetails": ChangeDatabaseParametersDetails,
    "ChangeDbManagementPrivateEndpointCompartmentDetails": ChangeDbManagementPrivateEndpointCompartmentDetails,
    "ChangeJobCompartmentDetails": ChangeJobCompartmentDetails,
    "ChangeManagedDatabaseGroupCompartmentDetails": ChangeManagedDatabaseGroupCompartmentDetails,
    "ChildDatabase": ChildDatabase,
    "CloneSqlTuningTaskDetails": CloneSqlTuningTaskDetails,
    "ClusterCacheMetric": ClusterCacheMetric,
    "ConsumerGroupPrivilegeCollection": ConsumerGroupPrivilegeCollection,
    "ConsumerGroupPrivilegeSummary": ConsumerGroupPrivilegeSummary,
    "CpuUtilizationAggregateMetrics": CpuUtilizationAggregateMetrics,
    "CreateDbManagementPrivateEndpointDetails": CreateDbManagementPrivateEndpointDetails,
    "CreateJobDetails": CreateJobDetails,
    "CreateManagedDatabaseGroupDetails": CreateManagedDatabaseGroupDetails,
    "CreateSqlJobDetails": CreateSqlJobDetails,
    "DataAccessContainerCollection": DataAccessContainerCollection,
    "DataAccessContainerSummary": DataAccessContainerSummary,
    "DatabaseCredentials": DatabaseCredentials,
    "DatabaseFleetHealthMetrics": DatabaseFleetHealthMetrics,
    "DatabaseHomeMetricDefinition": DatabaseHomeMetricDefinition,
    "DatabaseHomeMetrics": DatabaseHomeMetrics,
    "DatabaseIOAggregateMetrics": DatabaseIOAggregateMetrics,
    "DatabaseInstanceHomeMetricsDefinition": DatabaseInstanceHomeMetricsDefinition,
    "DatabaseParameterSummary": DatabaseParameterSummary,
    "DatabaseParameterUpdateStatus": DatabaseParameterUpdateStatus,
    "DatabaseParametersCollection": DatabaseParametersCollection,
    "DatabaseStorageAggregateMetrics": DatabaseStorageAggregateMetrics,
    "DatabaseTimeAggregateMetrics": DatabaseTimeAggregateMetrics,
    "DatabaseUsageMetrics": DatabaseUsageMetrics,
    "Datafile": Datafile,
    "DbManagementPrivateEndpoint": DbManagementPrivateEndpoint,
    "DbManagementPrivateEndpointCollection": DbManagementPrivateEndpointCollection,
    "DbManagementPrivateEndpointSummary": DbManagementPrivateEndpointSummary,
    "DropSqlTuningTaskDetails": DropSqlTuningTaskDetails,
    "ExecutionPlanStatsComparision": ExecutionPlanStatsComparision,
    "FailedConnectionsAggregateMetrics": FailedConnectionsAggregateMetrics,
    "FleetMetricDefinition": FleetMetricDefinition,
    "FleetMetricSummaryDefinition": FleetMetricSummaryDefinition,
    "FleetStatusByCategory": FleetStatusByCategory,
    "FleetSummary": FleetSummary,
    "InstanceDetails": InstanceDetails,
    "Job": Job,
    "JobCollection": JobCollection,
    "JobDatabase": JobDatabase,
    "JobExecution": JobExecution,
    "JobExecutionCollection": JobExecutionCollection,
    "JobExecutionResultDetails": JobExecutionResultDetails,
    "JobExecutionResultLocation": JobExecutionResultLocation,
    "JobExecutionSummary": JobExecutionSummary,
    "JobExecutionsStatusSummary": JobExecutionsStatusSummary,
    "JobExecutionsStatusSummaryCollection": JobExecutionsStatusSummaryCollection,
    "JobRun": JobRun,
    "JobRunCollection": JobRunCollection,
    "JobRunSummary": JobRunSummary,
    "JobScheduleDetails": JobScheduleDetails,
    "JobSummary": JobSummary,
    "ManagedDatabase": ManagedDatabase,
    "ManagedDatabaseCollection": ManagedDatabaseCollection,
    "ManagedDatabaseGroup": ManagedDatabaseGroup,
    "ManagedDatabaseGroupCollection": ManagedDatabaseGroupCollection,
    "ManagedDatabaseGroupSummary": ManagedDatabaseGroupSummary,
    "ManagedDatabaseSummary": ManagedDatabaseSummary,
    "MemoryAggregateMetrics": MemoryAggregateMetrics,
    "MetricDataPoint": MetricDataPoint,
    "MetricDimensionDefinition": MetricDimensionDefinition,
    "ObjectPrivilegeCollection": ObjectPrivilegeCollection,
    "ObjectPrivilegeSummary": ObjectPrivilegeSummary,
    "ObjectStorageJobExecutionResultDetails": ObjectStorageJobExecutionResultDetails,
    "ObjectStorageJobExecutionResultLocation": ObjectStorageJobExecutionResultLocation,
    "ParentGroup": ParentGroup,
    "PdbMetrics": PdbMetrics,
    "PdbStatusDetails": PdbStatusDetails,
    "ProxiedForUserCollection": ProxiedForUserCollection,
    "ProxiedForUserSummary": ProxiedForUserSummary,
    "ProxyUserCollection": ProxyUserCollection,
    "ProxyUserSummary": ProxyUserSummary,
    "RemoveManagedDatabaseFromManagedDatabaseGroupDetails": RemoveManagedDatabaseFromManagedDatabaseGroupDetails,
    "ResetDatabaseParametersDetails": ResetDatabaseParametersDetails,
    "RoleCollection": RoleCollection,
    "RoleSummary": RoleSummary,
    "SqlJob": SqlJob,
    "SqlTuningAdvisorTaskCollection": SqlTuningAdvisorTaskCollection,
    "SqlTuningAdvisorTaskFindingCollection": SqlTuningAdvisorTaskFindingCollection,
    "SqlTuningAdvisorTaskFindingSummary": SqlTuningAdvisorTaskFindingSummary,
    "SqlTuningAdvisorTaskRecommendationCollection": SqlTuningAdvisorTaskRecommendationCollection,
    "SqlTuningAdvisorTaskRecommendationSummary": SqlTuningAdvisorTaskRecommendationSummary,
    "SqlTuningAdvisorTaskSqlExecutionPlan": SqlTuningAdvisorTaskSqlExecutionPlan,
    "SqlTuningAdvisorTaskSummary": SqlTuningAdvisorTaskSummary,
    "SqlTuningAdvisorTaskSummaryFindingBenefits": SqlTuningAdvisorTaskSummaryFindingBenefits,
    "SqlTuningAdvisorTaskSummaryFindingCounts": SqlTuningAdvisorTaskSummaryFindingCounts,
    "SqlTuningAdvisorTaskSummaryReport": SqlTuningAdvisorTaskSummaryReport,
    "SqlTuningAdvisorTaskSummaryReportIndexFindingSummary": SqlTuningAdvisorTaskSummaryReportIndexFindingSummary,
    "SqlTuningAdvisorTaskSummaryReportObjectStatFindingSummary": SqlTuningAdvisorTaskSummaryReportObjectStatFindingSummary,
    "SqlTuningAdvisorTaskSummaryReportStatementCounts": SqlTuningAdvisorTaskSummaryReportStatementCounts,
    "SqlTuningAdvisorTaskSummaryReportStatistics": SqlTuningAdvisorTaskSummaryReportStatistics,
    "SqlTuningAdvisorTaskSummaryReportTaskInfo": SqlTuningAdvisorTaskSummaryReportTaskInfo,
    "SqlTuningTaskCredentialDetails": SqlTuningTaskCredentialDetails,
    "SqlTuningTaskPasswordCredentialDetails": SqlTuningTaskPasswordCredentialDetails,
    "SqlTuningTaskPlanStats": SqlTuningTaskPlanStats,
    "SqlTuningTaskReturn": SqlTuningTaskReturn,
    "SqlTuningTaskSecretCredentialDetails": SqlTuningTaskSecretCredentialDetails,
    "SqlTuningTaskSqlDetail": SqlTuningTaskSqlDetail,
    "SqlTuningTaskSqlExecutionPlanStep": SqlTuningTaskSqlExecutionPlanStep,
    "StartSqlTuningTaskDetails": StartSqlTuningTaskDetails,
    "StatementsAggregateMetrics": StatementsAggregateMetrics,
    "SystemPrivilegeCollection": SystemPrivilegeCollection,
    "SystemPrivilegeSummary": SystemPrivilegeSummary,
    "Tablespace": Tablespace,
    "TablespaceCollection": TablespaceCollection,
    "TablespaceSummary": TablespaceSummary,
    "TimeSeriesMetricDataPoint": TimeSeriesMetricDataPoint,
    "TimeSeriesMetricDefinition": TimeSeriesMetricDefinition,
    "UpdateDatabaseParametersResult": UpdateDatabaseParametersResult,
    "UpdateDbManagementPrivateEndpointDetails": UpdateDbManagementPrivateEndpointDetails,
    "UpdateJobDetails": UpdateJobDetails,
    "UpdateManagedDatabaseGroupDetails": UpdateManagedDatabaseGroupDetails,
    "UpdateSqlJobDetails": UpdateSqlJobDetails,
    "User": User,
    "UserCollection": UserCollection,
    "UserSummary": UserSummary,
    "WorkRequest": WorkRequest,
    "WorkRequestCollection": WorkRequestCollection,
    "WorkRequestError": WorkRequestError,
    "WorkRequestErrorCollection": WorkRequestErrorCollection,
    "WorkRequestLogEntry": WorkRequestLogEntry,
    "WorkRequestLogEntryCollection": WorkRequestLogEntryCollection,
    "WorkRequestResource": WorkRequestResource,
    "WorkRequestSummary": WorkRequestSummary
}
