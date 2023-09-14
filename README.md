## API integration with Lambda

# Objective
As an engineer, I want a solution that will accept a json request consisting of two key/value pairs in the following form:
{"id": "1234", "message": "Hello World"}

The endpoint should return a value "count" which is the total number of words contained in the message received. 
Subsequent messages will add to this count. A total of all words sent should be returned. 

# Overview
This solution consists of an API Gateway integrated with a Lambda function and Dynamodb table. Requests to the endpoint 
will trigger the Lambda function which will perform the following operations:
 - Fetch the current count value in the dynamodb table
 - Calculate the new count of words in the message
 - Add the counts together
 - Update the dynamodb table and respond with the total count

# Build and Deploy
*This project is using Terraform Cloud integration with GitHub Actions. You will need a Terraform Cloud account to utilize the workflows
 or modify your cloned repo to run without.*

To build this solution in your AWS environment follow the steps below:
- clone the repo https://github.com/jdgarrison1898/api-lambda-integration-terraform.git
- modify the terraform-apply.yml with your organization and workspace
- modify the terraform-plan.yml with your organization and workspace
- set an Terraform API (TF_API_TOKEN) token variable in your cloned repo under "Settings", "Secrets", "Actions"
  https://github.com/YOUR-USER/api-lambda-integration-terraform/settings/secrets/actions
- create a PR and merge your changes

**If running this locally without Terraform Cloud/GitHub Actions, modify the variables.tf in the root with your AWS details**

# Post-Deployment Validation
After successfully deploying, the URL of your API endpoint will appear in your Terraform Cloud workspace runs or terminal output
if running local.

Use this URL to send a request with json ex. (curl YOUR_ENDPOINT_URL \
-d '{"id": "1234", "message": "Hello World"}')