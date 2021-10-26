# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .association import Association
from .association_collection import AssociationCollection
from .association_summary import AssociationSummary
from .ca_bundle import CaBundle
from .ca_bundle_collection import CaBundleCollection
from .ca_bundle_summary import CaBundleSummary
from .certificate import Certificate
from .certificate_authority import CertificateAuthority
from .certificate_authority_collection import CertificateAuthorityCollection
from .certificate_authority_issuance_expiry_rule import CertificateAuthorityIssuanceExpiryRule
from .certificate_authority_rule import CertificateAuthorityRule
from .certificate_authority_summary import CertificateAuthoritySummary
from .certificate_authority_version import CertificateAuthorityVersion
from .certificate_authority_version_collection import CertificateAuthorityVersionCollection
from .certificate_authority_version_summary import CertificateAuthorityVersionSummary
from .certificate_collection import CertificateCollection
from .certificate_renewal_rule import CertificateRenewalRule
from .certificate_revocation_list_details import CertificateRevocationListDetails
from .certificate_rule import CertificateRule
from .certificate_subject import CertificateSubject
from .certificate_subject_alternative_name import CertificateSubjectAlternativeName
from .certificate_summary import CertificateSummary
from .certificate_version import CertificateVersion
from .certificate_version_collection import CertificateVersionCollection
from .certificate_version_summary import CertificateVersionSummary
from .change_ca_bundle_compartment_details import ChangeCaBundleCompartmentDetails
from .change_certificate_authority_compartment_details import ChangeCertificateAuthorityCompartmentDetails
from .change_certificate_compartment_details import ChangeCertificateCompartmentDetails
from .create_ca_bundle_details import CreateCaBundleDetails
from .create_certificate_authority_config_details import CreateCertificateAuthorityConfigDetails
from .create_certificate_authority_details import CreateCertificateAuthorityDetails
from .create_certificate_by_importing_config_details import CreateCertificateByImportingConfigDetails
from .create_certificate_config_details import CreateCertificateConfigDetails
from .create_certificate_details import CreateCertificateDetails
from .create_certificate_issued_by_internal_ca_config_details import CreateCertificateIssuedByInternalCaConfigDetails
from .create_certificate_managed_externally_issued_by_internal_ca_config_details import CreateCertificateManagedExternallyIssuedByInternalCaConfigDetails
from .create_root_ca_by_generating_internally_config_details import CreateRootCaByGeneratingInternallyConfigDetails
from .create_subordinate_ca_issued_by_internal_ca_config_details import CreateSubordinateCaIssuedByInternalCaConfigDetails
from .object_storage_bucket_config_details import ObjectStorageBucketConfigDetails
from .revocation_status import RevocationStatus
from .revoke_certificate_authority_version_details import RevokeCertificateAuthorityVersionDetails
from .revoke_certificate_version_details import RevokeCertificateVersionDetails
from .schedule_certificate_authority_deletion_details import ScheduleCertificateAuthorityDeletionDetails
from .schedule_certificate_authority_version_deletion_details import ScheduleCertificateAuthorityVersionDeletionDetails
from .schedule_certificate_deletion_details import ScheduleCertificateDeletionDetails
from .schedule_certificate_version_deletion_details import ScheduleCertificateVersionDeletionDetails
from .update_ca_bundle_details import UpdateCaBundleDetails
from .update_certificate_authority_config_details import UpdateCertificateAuthorityConfigDetails
from .update_certificate_authority_details import UpdateCertificateAuthorityDetails
from .update_certificate_by_importing_config_details import UpdateCertificateByImportingConfigDetails
from .update_certificate_config_details import UpdateCertificateConfigDetails
from .update_certificate_details import UpdateCertificateDetails
from .update_certificate_issued_by_internal_ca_config_details import UpdateCertificateIssuedByInternalCaConfigDetails
from .update_certificate_managed_externally_issued_by_internal_ca_config_details import UpdateCertificateManagedExternallyIssuedByInternalCaConfigDetails
from .update_root_ca_by_generating_internally_config_details import UpdateRootCaByGeneratingInternallyConfigDetails
from .update_subordinate_ca_issued_by_internal_ca_config_details import UpdateSubordinateCaIssuedByInternalCaConfigDetails
from .validity import Validity

# Maps type names to classes for certificates_management services.
certificates_management_type_mapping = {
    "Association": Association,
    "AssociationCollection": AssociationCollection,
    "AssociationSummary": AssociationSummary,
    "CaBundle": CaBundle,
    "CaBundleCollection": CaBundleCollection,
    "CaBundleSummary": CaBundleSummary,
    "Certificate": Certificate,
    "CertificateAuthority": CertificateAuthority,
    "CertificateAuthorityCollection": CertificateAuthorityCollection,
    "CertificateAuthorityIssuanceExpiryRule": CertificateAuthorityIssuanceExpiryRule,
    "CertificateAuthorityRule": CertificateAuthorityRule,
    "CertificateAuthoritySummary": CertificateAuthoritySummary,
    "CertificateAuthorityVersion": CertificateAuthorityVersion,
    "CertificateAuthorityVersionCollection": CertificateAuthorityVersionCollection,
    "CertificateAuthorityVersionSummary": CertificateAuthorityVersionSummary,
    "CertificateCollection": CertificateCollection,
    "CertificateRenewalRule": CertificateRenewalRule,
    "CertificateRevocationListDetails": CertificateRevocationListDetails,
    "CertificateRule": CertificateRule,
    "CertificateSubject": CertificateSubject,
    "CertificateSubjectAlternativeName": CertificateSubjectAlternativeName,
    "CertificateSummary": CertificateSummary,
    "CertificateVersion": CertificateVersion,
    "CertificateVersionCollection": CertificateVersionCollection,
    "CertificateVersionSummary": CertificateVersionSummary,
    "ChangeCaBundleCompartmentDetails": ChangeCaBundleCompartmentDetails,
    "ChangeCertificateAuthorityCompartmentDetails": ChangeCertificateAuthorityCompartmentDetails,
    "ChangeCertificateCompartmentDetails": ChangeCertificateCompartmentDetails,
    "CreateCaBundleDetails": CreateCaBundleDetails,
    "CreateCertificateAuthorityConfigDetails": CreateCertificateAuthorityConfigDetails,
    "CreateCertificateAuthorityDetails": CreateCertificateAuthorityDetails,
    "CreateCertificateByImportingConfigDetails": CreateCertificateByImportingConfigDetails,
    "CreateCertificateConfigDetails": CreateCertificateConfigDetails,
    "CreateCertificateDetails": CreateCertificateDetails,
    "CreateCertificateIssuedByInternalCaConfigDetails": CreateCertificateIssuedByInternalCaConfigDetails,
    "CreateCertificateManagedExternallyIssuedByInternalCaConfigDetails": CreateCertificateManagedExternallyIssuedByInternalCaConfigDetails,
    "CreateRootCaByGeneratingInternallyConfigDetails": CreateRootCaByGeneratingInternallyConfigDetails,
    "CreateSubordinateCaIssuedByInternalCaConfigDetails": CreateSubordinateCaIssuedByInternalCaConfigDetails,
    "ObjectStorageBucketConfigDetails": ObjectStorageBucketConfigDetails,
    "RevocationStatus": RevocationStatus,
    "RevokeCertificateAuthorityVersionDetails": RevokeCertificateAuthorityVersionDetails,
    "RevokeCertificateVersionDetails": RevokeCertificateVersionDetails,
    "ScheduleCertificateAuthorityDeletionDetails": ScheduleCertificateAuthorityDeletionDetails,
    "ScheduleCertificateAuthorityVersionDeletionDetails": ScheduleCertificateAuthorityVersionDeletionDetails,
    "ScheduleCertificateDeletionDetails": ScheduleCertificateDeletionDetails,
    "ScheduleCertificateVersionDeletionDetails": ScheduleCertificateVersionDeletionDetails,
    "UpdateCaBundleDetails": UpdateCaBundleDetails,
    "UpdateCertificateAuthorityConfigDetails": UpdateCertificateAuthorityConfigDetails,
    "UpdateCertificateAuthorityDetails": UpdateCertificateAuthorityDetails,
    "UpdateCertificateByImportingConfigDetails": UpdateCertificateByImportingConfigDetails,
    "UpdateCertificateConfigDetails": UpdateCertificateConfigDetails,
    "UpdateCertificateDetails": UpdateCertificateDetails,
    "UpdateCertificateIssuedByInternalCaConfigDetails": UpdateCertificateIssuedByInternalCaConfigDetails,
    "UpdateCertificateManagedExternallyIssuedByInternalCaConfigDetails": UpdateCertificateManagedExternallyIssuedByInternalCaConfigDetails,
    "UpdateRootCaByGeneratingInternallyConfigDetails": UpdateRootCaByGeneratingInternallyConfigDetails,
    "UpdateSubordinateCaIssuedByInternalCaConfigDetails": UpdateSubordinateCaIssuedByInternalCaConfigDetails,
    "Validity": Validity
}
