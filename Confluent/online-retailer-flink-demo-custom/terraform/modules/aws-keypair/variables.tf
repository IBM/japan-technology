# ===============================
# AWS Key Pair Module Variables
# ===============================

variable "prefix" {
  description = "Prefix for resource names"
  type        = string
}

variable "resource_suffix" {
  description = "Suffix for unique resource naming"
  type        = string
}

variable "output_path" {
  description = "Path to output the private key file"
  type        = string
  default     = "."
}

variable "common_tags" {
  description = "Common tags to apply to all resources"
  type        = map(string)
  default     = {}
}
