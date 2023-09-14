# Copyright (c) HashiCorp, Inc.
# SPDX-License-Identifier: MPL-2.0

# Input variable definitions

variable "region" {
  description = "AWS region for all resources."
  type    = string
  default = "us-east-1"
}
variable "account_id"{
  type        = string
  description = "The account ID in which to create/manage resources"
  sensitive   = true
}