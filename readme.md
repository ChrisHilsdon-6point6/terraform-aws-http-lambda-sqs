# Terraform AWS HTTP Lambda SQS
A terraform configuration to provision Lambda function with Function URL that submits post data to SQS queue for processing.

Once the terraform configuration has been applied, you will see a curl command in the output to send some data to the function url. Check the SQS queue message to see if it worked.


## Resources used

 - https://docs.aws.amazon.com/lambda/latest/dg/lambda-urls.html
 - https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/lambda_function
 - https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/lambda_function_url
 - https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/sqs_queue