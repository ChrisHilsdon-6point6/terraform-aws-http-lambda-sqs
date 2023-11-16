output "http_latest_url" {
  value = aws_lambda_function_url.http_latest.function_url
}


output "curl_command" {
  value = "curl -d '{\"key1\":\"value1\", \"key2\":\"value2\"}' -H 'Content-Type: application/json' -X POST ${aws_lambda_function_url.http_latest.function_url}"
}
