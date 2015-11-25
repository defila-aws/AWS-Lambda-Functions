# API Gateway Binary Data Passthrough to S3

* Developed in collaboration with ODP.

This function has the ability to passthrough binary data to S3 using the AWS API Gateway service, as base64 encoded strings.  It is configured to ingest a JSON blob (includes the base64 encoded file body, and file/S3 metadata), decode the base64 encoded string, and upload the file to S3.

## An Example JSON Blob for Uploading Two Files

```json
{
  "putfile": [
    {
      "region": "us-west-2",
      "bucketname": "your-bucket",
      "key": "lambdatest.txt",
      "contenttype": "text/plain",
      "acl": "public-read",
      "body": "SGVsbG8gV29ybGQK"
    },
    {
      "region": "us-east-1",
      "bucketname": "your-bucket-useast1",
      "key": "lambdatest.txt",
      "contenttype": "text/plain",
      "acl": "public-read",
      "body": "SGVsbG8gV29ybGQK"
    }
  ]
}
```
