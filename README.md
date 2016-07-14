# What is this?

This is template for upload file to s3 in python.
You can upload file to s3, but canot delete, copy, read.

# What you have to do

Create role like below.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "FirstStatement",
      "Effect":"Allow",
      "Action":["s3:PutObject","s3:PutObjectAcl"],
      "Resource":["arn:aws:s3:::*"]
    },
    {
      "Sid": "SecondStatement", 
      "Effect": "Allow",
      "Action": [
        "logs:CreateLogGroup",
        "logs:CreateLogStream",
        "logs:PutLogEvents"
      ],
      "Resource": "arn:aws:logs:*:*:*"
    }
  ]
}
```
