# Copyright (c) HashiCorp, Inc.
# SPDX-License-Identifier: MPL-2.0

# Input variable definitions

variable "region" {
  description = "AWS region for all resources."

  type    = string
  default = "us-east-1"
}
#variable "account_id"{
#  type        = string
#  description = "The account ID in which to create/manage resources"
#  default     = "AWS_ACCOUNT_TO_DEPLOY_TO" //target account for deployment if running this terraform locally
#}