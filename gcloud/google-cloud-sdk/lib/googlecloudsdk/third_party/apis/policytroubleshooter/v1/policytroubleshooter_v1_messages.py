"""Generated message classes for policytroubleshooter version v1.

"""
# NOTE: This file is autogenerated and should not be edited by hand.

from apitools.base.protorpclite import messages as _messages
from apitools.base.py import encoding


package = 'policytroubleshooter'


class GoogleCloudPolicytroubleshooterV1AccessTuple(_messages.Message):
  r"""Information about the member, resource, and permission to check.

  Fields:
    fullResourceName: Required. The full resource name that identifies the
      resource. For example, `//compute.googleapis.com/projects/my-
      project/zones/us-central1-a/instances/my-instance`.  For examples of
      full resource names for Google Cloud services, see
      https://cloud.google.com/iam/help/troubleshooter/full-resource-names.
    permission: Required. The IAM permission to check for the specified member
      and resource.  For a complete list of IAM permissions, see
      https://cloud.google.com/iam/help/permissions/reference.  For a complete
      list of predefined IAM roles and the permissions in each role, see
      https://cloud.google.com/iam/help/roles/reference.
    principal: Required. The member, or principal, whose access you want to
      check, in the form of the email address that represents that member. For
      example, `alice@example.com` or `my-service-account@my-
      project.iam.gserviceaccount.com`.  The member must be a Google Account
      or a service account. Other types of members are not supported.
  """

  fullResourceName = _messages.StringField(1)
  permission = _messages.StringField(2)
  principal = _messages.StringField(3)


class GoogleCloudPolicytroubleshooterV1BindingExplanation(_messages.Message):
  r"""Details about how a binding in a policy affects a member's ability to
  use a permission.

  Enums:
    AccessValueValuesEnum: Required. Indicates whether _this binding_ provides
      the specified permission to the specified member for the specified
      resource.  This field does _not_ indicate whether the member actually
      has the permission for the resource. There might be another binding that
      overrides this binding. To determine whether the member actually has the
      permission, use the `access` field in the TroubleshootIamPolicyResponse.
    RelevanceValueValuesEnum: The relevance of this binding to the overall
      determination for the entire policy.
    RolePermissionValueValuesEnum: Indicates whether the role granted by this
      binding contains the specified permission.
    RolePermissionRelevanceValueValuesEnum: The relevance of the permission's
      existence, or nonexistence, in the role to the overall determination for
      the entire policy.

  Messages:
    MembershipsValue: Indicates whether each member in the binding includes
      the member specified in the request, either directly or indirectly. Each
      key identifies a member in the binding, and each value indicates whether
      the member in the binding includes the member in the request.  For
      example, suppose that a binding includes the following members:  *
      `user:alice@example.com` * `group:product-eng@example.com`  You want to
      troubleshoot access for `user:bob@example.com`. This user is a member of
      the group `group:product-eng@example.com`.  For the first member in the
      binding, the key is `user:alice@example.com`, and the `membership` field
      in the value is set to `MEMBERSHIP_NOT_INCLUDED`.  For the second member
      in the binding, the key is `group:product-eng@example.com`, and the
      `membership` field in the value is set to `MEMBERSHIP_INCLUDED`.

  Fields:
    access: Required. Indicates whether _this binding_ provides the specified
      permission to the specified member for the specified resource.  This
      field does _not_ indicate whether the member actually has the permission
      for the resource. There might be another binding that overrides this
      binding. To determine whether the member actually has the permission,
      use the `access` field in the TroubleshootIamPolicyResponse.
    condition: A condition expression that prevents access unless the
      expression evaluates to `true`.  To learn about IAM Conditions, see
      http://cloud.google.com/iam/help/conditions/overview.
    memberships: Indicates whether each member in the binding includes the
      member specified in the request, either directly or indirectly. Each key
      identifies a member in the binding, and each value indicates whether the
      member in the binding includes the member in the request.  For example,
      suppose that a binding includes the following members:  *
      `user:alice@example.com` * `group:product-eng@example.com`  You want to
      troubleshoot access for `user:bob@example.com`. This user is a member of
      the group `group:product-eng@example.com`.  For the first member in the
      binding, the key is `user:alice@example.com`, and the `membership` field
      in the value is set to `MEMBERSHIP_NOT_INCLUDED`.  For the second member
      in the binding, the key is `group:product-eng@example.com`, and the
      `membership` field in the value is set to `MEMBERSHIP_INCLUDED`.
    relevance: The relevance of this binding to the overall determination for
      the entire policy.
    role: The role that this binding grants. For example,
      `roles/compute.serviceAgent`.  For a complete list of predefined IAM
      roles, as well as the permissions in each role, see
      https://cloud.google.com/iam/help/roles/reference.
    rolePermission: Indicates whether the role granted by this binding
      contains the specified permission.
    rolePermissionRelevance: The relevance of the permission's existence, or
      nonexistence, in the role to the overall determination for the entire
      policy.
  """

  class AccessValueValuesEnum(_messages.Enum):
    r"""Required. Indicates whether _this binding_ provides the specified
    permission to the specified member for the specified resource.  This field
    does _not_ indicate whether the member actually has the permission for the
    resource. There might be another binding that overrides this binding. To
    determine whether the member actually has the permission, use the `access`
    field in the TroubleshootIamPolicyResponse.

    Values:
      ACCESS_STATE_UNSPECIFIED: Reserved for future use.
      GRANTED: The member has the permission.
      NOT_GRANTED: The member does not have the permission.
      UNKNOWN_CONDITIONAL: The member has the permission only if a condition
        expression evaluates to `true`.
      UNKNOWN_INFO_DENIED: The sender of the request does not have access to
        all of the policies that Policy Troubleshooter needs to evaluate.
    """
    ACCESS_STATE_UNSPECIFIED = 0
    GRANTED = 1
    NOT_GRANTED = 2
    UNKNOWN_CONDITIONAL = 3
    UNKNOWN_INFO_DENIED = 4

  class RelevanceValueValuesEnum(_messages.Enum):
    r"""The relevance of this binding to the overall determination for the
    entire policy.

    Values:
      HEURISTIC_RELEVANCE_UNSPECIFIED: Reserved for future use.
      NORMAL: The data point has a limited effect on the result. Changing the
        data point is unlikely to affect the overall determination.
      HIGH: The data point has a strong effect on the result. Changing the
        data point is likely to affect the overall determination.
    """
    HEURISTIC_RELEVANCE_UNSPECIFIED = 0
    NORMAL = 1
    HIGH = 2

  class RolePermissionRelevanceValueValuesEnum(_messages.Enum):
    r"""The relevance of the permission's existence, or nonexistence, in the
    role to the overall determination for the entire policy.

    Values:
      HEURISTIC_RELEVANCE_UNSPECIFIED: Reserved for future use.
      NORMAL: The data point has a limited effect on the result. Changing the
        data point is unlikely to affect the overall determination.
      HIGH: The data point has a strong effect on the result. Changing the
        data point is likely to affect the overall determination.
    """
    HEURISTIC_RELEVANCE_UNSPECIFIED = 0
    NORMAL = 1
    HIGH = 2

  class RolePermissionValueValuesEnum(_messages.Enum):
    r"""Indicates whether the role granted by this binding contains the
    specified permission.

    Values:
      ROLE_PERMISSION_UNSPECIFIED: Reserved for future use.
      ROLE_PERMISSION_INCLUDED: The permission is included in the role.
      ROLE_PERMISSION_NOT_INCLUDED: The permission is not included in the
        role.
      ROLE_PERMISSION_UNKNOWN_INFO_DENIED: The sender of the request is not
        allowed to access the binding.
    """
    ROLE_PERMISSION_UNSPECIFIED = 0
    ROLE_PERMISSION_INCLUDED = 1
    ROLE_PERMISSION_NOT_INCLUDED = 2
    ROLE_PERMISSION_UNKNOWN_INFO_DENIED = 3

  @encoding.MapUnrecognizedFields('additionalProperties')
  class MembershipsValue(_messages.Message):
    r"""Indicates whether each member in the binding includes the member
    specified in the request, either directly or indirectly. Each key
    identifies a member in the binding, and each value indicates whether the
    member in the binding includes the member in the request.  For example,
    suppose that a binding includes the following members:  *
    `user:alice@example.com` * `group:product-eng@example.com`  You want to
    troubleshoot access for `user:bob@example.com`. This user is a member of
    the group `group:product-eng@example.com`.  For the first member in the
    binding, the key is `user:alice@example.com`, and the `membership` field
    in the value is set to `MEMBERSHIP_NOT_INCLUDED`.  For the second member
    in the binding, the key is `group:product-eng@example.com`, and the
    `membership` field in the value is set to `MEMBERSHIP_INCLUDED`.

    Messages:
      AdditionalProperty: An additional property for a MembershipsValue
        object.

    Fields:
      additionalProperties: Additional properties of type MembershipsValue
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a MembershipsValue object.

      Fields:
        key: Name of the additional property.
        value: A
          GoogleCloudPolicytroubleshooterV1BindingExplanationAnnotatedMembersh
          ip attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('GoogleCloudPolicytroubleshooterV1BindingExplanationAnnotatedMembership', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  access = _messages.EnumField('AccessValueValuesEnum', 1)
  condition = _messages.MessageField('GoogleTypeExpr', 2)
  memberships = _messages.MessageField('MembershipsValue', 3)
  relevance = _messages.EnumField('RelevanceValueValuesEnum', 4)
  role = _messages.StringField(5)
  rolePermission = _messages.EnumField('RolePermissionValueValuesEnum', 6)
  rolePermissionRelevance = _messages.EnumField('RolePermissionRelevanceValueValuesEnum', 7)


class GoogleCloudPolicytroubleshooterV1BindingExplanationAnnotatedMembership(_messages.Message):
  r"""Details about whether the binding includes the member.

  Enums:
    MembershipValueValuesEnum: Indicates whether the binding includes the
      member.
    RelevanceValueValuesEnum: The relevance of the member's status to the
      overall determination for the binding.

  Fields:
    membership: Indicates whether the binding includes the member.
    relevance: The relevance of the member's status to the overall
      determination for the binding.
  """

  class MembershipValueValuesEnum(_messages.Enum):
    r"""Indicates whether the binding includes the member.

    Values:
      MEMBERSHIP_UNSPECIFIED: Reserved for future use.
      MEMBERSHIP_INCLUDED: The binding includes the member. The member can be
        included directly or indirectly. For example:  * A member is included
        directly if that member is listed in the binding. * A member is
        included indirectly if that member is in a Google group or   G Suite
        domain that is listed in the binding.
      MEMBERSHIP_NOT_INCLUDED: The binding does not include the member.
      MEMBERSHIP_UNKNOWN_INFO_DENIED: The sender of the request is not allowed
        to access the binding.
      MEMBERSHIP_UNKNOWN_UNSUPPORTED: The member is an unsupported type. Only
        Google Accounts and service accounts are supported.
    """
    MEMBERSHIP_UNSPECIFIED = 0
    MEMBERSHIP_INCLUDED = 1
    MEMBERSHIP_NOT_INCLUDED = 2
    MEMBERSHIP_UNKNOWN_INFO_DENIED = 3
    MEMBERSHIP_UNKNOWN_UNSUPPORTED = 4

  class RelevanceValueValuesEnum(_messages.Enum):
    r"""The relevance of the member's status to the overall determination for
    the binding.

    Values:
      HEURISTIC_RELEVANCE_UNSPECIFIED: Reserved for future use.
      NORMAL: The data point has a limited effect on the result. Changing the
        data point is unlikely to affect the overall determination.
      HIGH: The data point has a strong effect on the result. Changing the
        data point is likely to affect the overall determination.
    """
    HEURISTIC_RELEVANCE_UNSPECIFIED = 0
    NORMAL = 1
    HIGH = 2

  membership = _messages.EnumField('MembershipValueValuesEnum', 1)
  relevance = _messages.EnumField('RelevanceValueValuesEnum', 2)


class GoogleCloudPolicytroubleshooterV1ExplainedPolicy(_messages.Message):
  r"""Details about how a specific IAM Policy contributed to the access check.

  Enums:
    AccessValueValuesEnum: Indicates whether _this policy_ provides the
      specified permission to the specified member for the specified resource.
      This field does _not_ indicate whether the member actually has the
      permission for the resource. There might be another policy that
      overrides this policy. To determine whether the member actually has the
      permission, use the `access` field in the TroubleshootIamPolicyResponse.
    RelevanceValueValuesEnum: The relevance of this policy to the overall
      determination in the TroubleshootIamPolicyResponse.  If the sender of
      the request does not have access to the policy, this field is omitted.

  Fields:
    access: Indicates whether _this policy_ provides the specified permission
      to the specified member for the specified resource.  This field does
      _not_ indicate whether the member actually has the permission for the
      resource. There might be another policy that overrides this policy. To
      determine whether the member actually has the permission, use the
      `access` field in the TroubleshootIamPolicyResponse.
    bindingExplanations: Details about how each binding in the policy affects
      the member's ability, or inability, to use the permission for the
      resource.  If the sender of the request does not have access to the
      policy, this field is omitted.
    fullResourceName: The full resource name that identifies the resource. For
      example, `//compute.googleapis.com/projects/my-project/zones/us-
      central1-a/instances/my-instance`.  If the sender of the request does
      not have access to the policy, this field is omitted.  For examples of
      full resource names for Google Cloud services, see
      https://cloud.google.com/iam/help/troubleshooter/full-resource-names.
    policy: The IAM policy attached to the resource.  If the sender of the
      request does not have access to the policy, this field is empty.
    relevance: The relevance of this policy to the overall determination in
      the TroubleshootIamPolicyResponse.  If the sender of the request does
      not have access to the policy, this field is omitted.
  """

  class AccessValueValuesEnum(_messages.Enum):
    r"""Indicates whether _this policy_ provides the specified permission to
    the specified member for the specified resource.  This field does _not_
    indicate whether the member actually has the permission for the resource.
    There might be another policy that overrides this policy. To determine
    whether the member actually has the permission, use the `access` field in
    the TroubleshootIamPolicyResponse.

    Values:
      ACCESS_STATE_UNSPECIFIED: Reserved for future use.
      GRANTED: The member has the permission.
      NOT_GRANTED: The member does not have the permission.
      UNKNOWN_CONDITIONAL: The member has the permission only if a condition
        expression evaluates to `true`.
      UNKNOWN_INFO_DENIED: The sender of the request does not have access to
        all of the policies that Policy Troubleshooter needs to evaluate.
    """
    ACCESS_STATE_UNSPECIFIED = 0
    GRANTED = 1
    NOT_GRANTED = 2
    UNKNOWN_CONDITIONAL = 3
    UNKNOWN_INFO_DENIED = 4

  class RelevanceValueValuesEnum(_messages.Enum):
    r"""The relevance of this policy to the overall determination in the
    TroubleshootIamPolicyResponse.  If the sender of the request does not have
    access to the policy, this field is omitted.

    Values:
      HEURISTIC_RELEVANCE_UNSPECIFIED: Reserved for future use.
      NORMAL: The data point has a limited effect on the result. Changing the
        data point is unlikely to affect the overall determination.
      HIGH: The data point has a strong effect on the result. Changing the
        data point is likely to affect the overall determination.
    """
    HEURISTIC_RELEVANCE_UNSPECIFIED = 0
    NORMAL = 1
    HIGH = 2

  access = _messages.EnumField('AccessValueValuesEnum', 1)
  bindingExplanations = _messages.MessageField('GoogleCloudPolicytroubleshooterV1BindingExplanation', 2, repeated=True)
  fullResourceName = _messages.StringField(3)
  policy = _messages.MessageField('GoogleIamV1Policy', 4)
  relevance = _messages.EnumField('RelevanceValueValuesEnum', 5)


class GoogleCloudPolicytroubleshooterV1TroubleshootIamPolicyRequest(_messages.Message):
  r"""Request for TroubleshootIamPolicy.

  Fields:
    accessTuple: The information to use for checking whether a member has a
      permission for a resource.
  """

  accessTuple = _messages.MessageField('GoogleCloudPolicytroubleshooterV1AccessTuple', 1)


class GoogleCloudPolicytroubleshooterV1TroubleshootIamPolicyResponse(_messages.Message):
  r"""Response for TroubleshootIamPolicy.

  Enums:
    AccessValueValuesEnum: Indicates whether the member has the specified
      permission for the specified resource, based on evaluating all of the
      applicable IAM policies.

  Fields:
    access: Indicates whether the member has the specified permission for the
      specified resource, based on evaluating all of the applicable IAM
      policies.
    explainedPolicies: List of IAM policies that were evaluated to check the
      member's permissions, with annotations to indicate how each policy
      contributed to the final result.  The list of policies can include the
      policy for the resource itself. It can also include policies that are
      inherited from higher levels of the resource hierarchy, including the
      organization, the folder, and the project.  To learn more about the
      resource hierarchy, see https://cloud.google.com/iam/help/resource-
      hierarchy.
  """

  class AccessValueValuesEnum(_messages.Enum):
    r"""Indicates whether the member has the specified permission for the
    specified resource, based on evaluating all of the applicable IAM
    policies.

    Values:
      ACCESS_STATE_UNSPECIFIED: Reserved for future use.
      GRANTED: The member has the permission.
      NOT_GRANTED: The member does not have the permission.
      UNKNOWN_CONDITIONAL: The member has the permission only if a condition
        expression evaluates to `true`.
      UNKNOWN_INFO_DENIED: The sender of the request does not have access to
        all of the policies that Policy Troubleshooter needs to evaluate.
    """
    ACCESS_STATE_UNSPECIFIED = 0
    GRANTED = 1
    NOT_GRANTED = 2
    UNKNOWN_CONDITIONAL = 3
    UNKNOWN_INFO_DENIED = 4

  access = _messages.EnumField('AccessValueValuesEnum', 1)
  explainedPolicies = _messages.MessageField('GoogleCloudPolicytroubleshooterV1ExplainedPolicy', 2, repeated=True)


class GoogleIamV1AuditConfig(_messages.Message):
  r"""Specifies the audit configuration for a service. The configuration
  determines which permission types are logged, and what identities, if any,
  are exempted from logging. An AuditConfig must have one or more
  AuditLogConfigs.  If there are AuditConfigs for both `allServices` and a
  specific service, the union of the two AuditConfigs is used for that
  service: the log_types specified in each AuditConfig are enabled, and the
  exempted_members in each AuditLogConfig are exempted.  Example Policy with
  multiple AuditConfigs:      {       "audit_configs": [         {
  "service": "allServices"           "audit_log_configs": [             {
  "log_type": "DATA_READ",               "exempted_members": [
  "user:jose@example.com"               ]             },             {
  "log_type": "DATA_WRITE",             },             {
  "log_type": "ADMIN_READ",             }           ]         },         {
  "service": "sampleservice.googleapis.com"           "audit_log_configs": [
  {               "log_type": "DATA_READ",             },             {
  "log_type": "DATA_WRITE",               "exempted_members": [
  "user:aliya@example.com"               ]             }           ]         }
  ]     }  For sampleservice, this policy enables DATA_READ, DATA_WRITE and
  ADMIN_READ logging. It also exempts jose@example.com from DATA_READ logging,
  and aliya@example.com from DATA_WRITE logging.

  Fields:
    auditLogConfigs: The configuration for logging of each type of permission.
    service: Specifies a service that will be enabled for audit logging. For
      example, `storage.googleapis.com`, `cloudsql.googleapis.com`.
      `allServices` is a special value that covers all services.
  """

  auditLogConfigs = _messages.MessageField('GoogleIamV1AuditLogConfig', 1, repeated=True)
  service = _messages.StringField(2)


class GoogleIamV1AuditLogConfig(_messages.Message):
  r"""Provides the configuration for logging a type of permissions. Example:
  {       "audit_log_configs": [         {           "log_type": "DATA_READ",
  "exempted_members": [             "user:jose@example.com"           ]
  },         {           "log_type": "DATA_WRITE",         }       ]     }
  This enables 'DATA_READ' and 'DATA_WRITE' logging, while exempting
  jose@example.com from DATA_READ logging.

  Enums:
    LogTypeValueValuesEnum: The log type that this config enables.

  Fields:
    exemptedMembers: Specifies the identities that do not cause logging for
      this type of permission. Follows the same format of Binding.members.
    logType: The log type that this config enables.
  """

  class LogTypeValueValuesEnum(_messages.Enum):
    r"""The log type that this config enables.

    Values:
      LOG_TYPE_UNSPECIFIED: Default case. Should never be this.
      ADMIN_READ: Admin reads. Example: CloudIAM getIamPolicy
      DATA_WRITE: Data writes. Example: CloudSQL Users create
      DATA_READ: Data reads. Example: CloudSQL Users list
    """
    LOG_TYPE_UNSPECIFIED = 0
    ADMIN_READ = 1
    DATA_WRITE = 2
    DATA_READ = 3

  exemptedMembers = _messages.StringField(1, repeated=True)
  logType = _messages.EnumField('LogTypeValueValuesEnum', 2)


class GoogleIamV1Binding(_messages.Message):
  r"""Associates `members` with a `role`.

  Fields:
    condition: The condition that is associated with this binding. NOTE: An
      unsatisfied condition will not allow user access via current binding.
      Different bindings, including their conditions, are examined
      independently.
    members: Specifies the identities requesting access for a Cloud Platform
      resource. `members` can have the following values:  * `allUsers`: A
      special identifier that represents anyone who is    on the internet;
      with or without a Google account.  * `allAuthenticatedUsers`: A special
      identifier that represents anyone    who is authenticated with a Google
      account or a service account.  * `user:{emailid}`: An email address that
      represents a specific Google    account. For example,
      `alice@example.com` .   * `serviceAccount:{emailid}`: An email address
      that represents a service    account. For example, `my-other-
      app@appspot.gserviceaccount.com`.  * `group:{emailid}`: An email address
      that represents a Google group.    For example, `admins@example.com`.  *
      `deleted:user:{emailid}?uid={uniqueid}`: An email address (plus unique
      identifier) representing a user that has been recently deleted. For
      example, `alice@example.com?uid=123456789012345678901`. If the user is
      recovered, this value reverts to `user:{emailid}` and the recovered user
      retains the role in the binding.  *
      `deleted:serviceAccount:{emailid}?uid={uniqueid}`: An email address
      (plus    unique identifier) representing a service account that has been
      recently    deleted. For example,    `my-other-
      app@appspot.gserviceaccount.com?uid=123456789012345678901`.    If the
      service account is undeleted, this value reverts to
      `serviceAccount:{emailid}` and the undeleted service account retains the
      role in the binding.  * `deleted:group:{emailid}?uid={uniqueid}`: An
      email address (plus unique    identifier) representing a Google group
      that has been recently    deleted. For example,
      `admins@example.com?uid=123456789012345678901`. If    the group is
      recovered, this value reverts to `group:{emailid}` and the    recovered
      group retains the role in the binding.   * `domain:{domain}`: The G
      Suite domain (primary) that represents all the    users of that domain.
      For example, `google.com` or `example.com`.
    role: Role that is assigned to `members`. For example, `roles/viewer`,
      `roles/editor`, or `roles/owner`.
  """

  condition = _messages.MessageField('GoogleTypeExpr', 1)
  members = _messages.StringField(2, repeated=True)
  role = _messages.StringField(3)


class GoogleIamV1Policy(_messages.Message):
  r"""An Identity and Access Management (IAM) policy, which specifies access
  controls for Google Cloud resources.   A `Policy` is a collection of
  `bindings`. A `binding` binds one or more `members` to a single `role`.
  Members can be user accounts, service accounts, Google groups, and domains
  (such as G Suite). A `role` is a named list of permissions; each `role` can
  be an IAM predefined role or a user-created custom role.  Optionally, a
  `binding` can specify a `condition`, which is a logical expression that
  allows access to a resource only if the expression evaluates to `true`. A
  condition can add constraints based on attributes of the request, the
  resource, or both.  **JSON example:**      {       "bindings": [         {
  "role": "roles/resourcemanager.organizationAdmin",           "members": [
  "user:mike@example.com",             "group:admins@example.com",
  "domain:google.com",             "serviceAccount:my-project-
  id@appspot.gserviceaccount.com"           ]         },         {
  "role": "roles/resourcemanager.organizationViewer",           "members":
  ["user:eve@example.com"],           "condition": {             "title":
  "expirable access",             "description": "Does not grant access after
  Sep 2020",             "expression": "request.time <
  timestamp('2020-10-01T00:00:00.000Z')",           }         }       ],
  "etag": "BwWWja0YfJA=",       "version": 3     }  **YAML example:**
  bindings:     - members:       - user:mike@example.com       -
  group:admins@example.com       - domain:google.com       - serviceAccount
  :my-project-id@appspot.gserviceaccount.com       role:
  roles/resourcemanager.organizationAdmin     - members:       -
  user:eve@example.com       role: roles/resourcemanager.organizationViewer
  condition:         title: expirable access         description: Does not
  grant access after Sep 2020         expression: request.time <
  timestamp('2020-10-01T00:00:00.000Z')     - etag: BwWWja0YfJA=     -
  version: 3  For a description of IAM and its features, see the [IAM
  documentation](https://cloud.google.com/iam/docs/).

  Fields:
    auditConfigs: Specifies cloud audit logging configuration for this policy.
    bindings: Associates a list of `members` to a `role`. Optionally, may
      specify a `condition` that determines how and when the `bindings` are
      applied. Each of the `bindings` must contain at least one member.
    etag: `etag` is used for optimistic concurrency control as a way to help
      prevent simultaneous updates of a policy from overwriting each other. It
      is strongly suggested that systems make use of the `etag` in the read-
      modify-write cycle to perform policy updates in order to avoid race
      conditions: An `etag` is returned in the response to `getIamPolicy`, and
      systems are expected to put that etag in the request to `setIamPolicy`
      to ensure that their change will be applied to the same version of the
      policy.  **Important:** If you use IAM Conditions, you must include the
      `etag` field whenever you call `setIamPolicy`. If you omit this field,
      then IAM allows you to overwrite a version `3` policy with a version `1`
      policy, and all of the conditions in the version `3` policy are lost.
    version: Specifies the format of the policy.  Valid values are `0`, `1`,
      and `3`. Requests that specify an invalid value are rejected.  Any
      operation that affects conditional role bindings must specify version
      `3`. This requirement applies to the following operations:  * Getting a
      policy that includes a conditional role binding * Adding a conditional
      role binding to a policy * Changing a conditional role binding in a
      policy * Removing any role binding, with or without a condition, from a
      policy   that includes conditions  **Important:** If you use IAM
      Conditions, you must include the `etag` field whenever you call
      `setIamPolicy`. If you omit this field, then IAM allows you to overwrite
      a version `3` policy with a version `1` policy, and all of the
      conditions in the version `3` policy are lost.  If a policy does not
      include any conditions, operations on that policy may specify any valid
      version or leave the field unset.
  """

  auditConfigs = _messages.MessageField('GoogleIamV1AuditConfig', 1, repeated=True)
  bindings = _messages.MessageField('GoogleIamV1Binding', 2, repeated=True)
  etag = _messages.BytesField(3)
  version = _messages.IntegerField(4, variant=_messages.Variant.INT32)


class GoogleTypeExpr(_messages.Message):
  r"""Represents a textual expression in the Common Expression Language (CEL)
  syntax. CEL is a C-like expression language. The syntax and semantics of CEL
  are documented at https://github.com/google/cel-spec.  Example (Comparison):
  title: "Summary size limit"     description: "Determines if a summary is
  less than 100 chars"     expression: "document.summary.size() < 100"
  Example (Equality):      title: "Requestor is owner"     description:
  "Determines if requestor is the document owner"     expression:
  "document.owner == request.auth.claims.email"  Example (Logic):      title:
  "Public documents"     description: "Determine whether the document should
  be publicly visible"     expression: "document.type != 'private' &&
  document.type != 'internal'"  Example (Data Manipulation):      title:
  "Notification string"     description: "Create a notification string with a
  timestamp."     expression: "'New message received at ' +
  string(document.create_time)"  The exact variables and functions that may be
  referenced within an expression are determined by the service that evaluates
  it. See the service documentation for additional information.

  Fields:
    description: Optional. Description of the expression. This is a longer
      text which describes the expression, e.g. when hovered over it in a UI.
    expression: Textual representation of an expression in Common Expression
      Language syntax.
    location: Optional. String indicating the location of the expression for
      error reporting, e.g. a file name and a position in the file.
    title: Optional. Title for the expression, i.e. a short string describing
      its purpose. This can be used e.g. in UIs which allow to enter the
      expression.
  """

  description = _messages.StringField(1)
  expression = _messages.StringField(2)
  location = _messages.StringField(3)
  title = _messages.StringField(4)


class StandardQueryParameters(_messages.Message):
  r"""Query parameters accepted by all methods.

  Enums:
    FXgafvValueValuesEnum: V1 error format.
    AltValueValuesEnum: Data format for response.

  Fields:
    f__xgafv: V1 error format.
    access_token: OAuth access token.
    alt: Data format for response.
    callback: JSONP
    fields: Selector specifying which fields to include in a partial response.
    key: API key. Your API key identifies your project and provides you with
      API access, quota, and reports. Required unless you provide an OAuth 2.0
      token.
    oauth_token: OAuth 2.0 token for the current user.
    prettyPrint: Returns response with indentations and line breaks.
    quotaUser: Available to use for quota purposes for server-side
      applications. Can be any arbitrary string assigned to a user, but should
      not exceed 40 characters.
    trace: A tracing token of the form "token:<tokenid>" to include in api
      requests.
    uploadType: Legacy upload protocol for media (e.g. "media", "multipart").
    upload_protocol: Upload protocol for media (e.g. "raw", "multipart").
  """

  class AltValueValuesEnum(_messages.Enum):
    r"""Data format for response.

    Values:
      json: Responses with Content-Type of application/json
      media: Media download with context-dependent Content-Type
      proto: Responses with Content-Type of application/x-protobuf
    """
    json = 0
    media = 1
    proto = 2

  class FXgafvValueValuesEnum(_messages.Enum):
    r"""V1 error format.

    Values:
      _1: v1 error format
      _2: v2 error format
    """
    _1 = 0
    _2 = 1

  f__xgafv = _messages.EnumField('FXgafvValueValuesEnum', 1)
  access_token = _messages.StringField(2)
  alt = _messages.EnumField('AltValueValuesEnum', 3, default=u'json')
  callback = _messages.StringField(4)
  fields = _messages.StringField(5)
  key = _messages.StringField(6)
  oauth_token = _messages.StringField(7)
  prettyPrint = _messages.BooleanField(8, default=True)
  quotaUser = _messages.StringField(9)
  trace = _messages.StringField(10)
  uploadType = _messages.StringField(11)
  upload_protocol = _messages.StringField(12)


encoding.AddCustomJsonFieldMapping(
    StandardQueryParameters, 'f__xgafv', '$.xgafv')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_1', '1')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_2', '2')
