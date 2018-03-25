Homework by: Ravinder Lambadi and Orly Esteban

# Amazon Kinesis Data streams
This tutorial provides high level overview on Amazon Kinesis and details setting up Amazon Kinesis data stream.
Amazon kinesis is used to collect and process large streams of data records in a real time. Amazon kinesis data streams application reads data from a Kinesis data stream as records. Kinesis applications can use the kinesis client libraries and they can run on Amazon EC2 instances.
## Components of Kinesis Data Streams
- Kinesis Data Streams
- Data Records
- Producers
- Consumers

## High Level Components Description
The Producers continually push data to Kinesis data streams and the consumers process the data in real time. Consumers are any applications running on Amazon EC2, can store their results on AWS service such as Amazon dynamo DB, Amazon Redshift, Amazon S3.

## Limits of Amazon Kinesis
Following are certain limits that should be kept in mind while using Amazon Kinesis Streams 
- Records of a stream can be accessible up to 24 hours by default and can be extended up to 7 days by enabling extended data retention.
- The maximum size of a data blob (the data payload before Base64-encoding) in one record is 1 megabyte (MB).
- One shard supports up to 1000 PUT records per second.
## Setting up for Amazon kinesis Data Streams
- Setup the AWS account
- Download libraries and tools
  - Amazon Kinesis API reference is the basic set of operations that kinesis data streams supports
  - The AWS SDKs based on your preference language of development like Java, .NET , Python and etc.
  - The Kinesis client library provides easy-to-use programing model for processing data.
  - The AWS command line interface supports kinesis data streams. The AWS CLI enables you to control multiple AWS services from command the command line and automate them through the scripts

## Create Kinesis

Step1 - Login to AWS and create the Kinesis data streams
A Kinesis stream is an ordered sequence of data records. To add data to a Kinesis stream, configure producers using the Streams PUT API or the Amazon Kinesis Producer Library (KPL).

Step2 – Click the create stream and fill the required fields such as stream name and number of shared and then click on create button.
 
![AWS CreateKenesisStream](https://github.com/cloudmesh-community/hid-sp18-506/blob/master/tutorial/images/CreateKinesisStream.png?raw=true)

![AWS DataStreamDetails](https://github.com/cloudmesh-community/hid-sp18-506/blob/master/tutorial/images/DataStreamDetails.png?raw=true)
 

Step3 – Set up users on kinesis stream. Create new users and assign a policy to each user.

Step4 – Connect your application to Amazon kinesis

## Features of Amazon Kinesis
- Real-time processing − It allows to collect and analyze information in real-time.
- Easy to use − Using Amazon Kinesis, we can create a new stream, set its requirements, and start streaming data quickly.
- High throughput, elastic − It allows to collect and analyze information in real-time like stock trade prices otherwise we need to wait for data-out report.
- Integrate with other Amazon services − It can be integrated with Amazon Redshift, Amazon S3 and Amazon DynamoDB.
- Build kinesis applications − Amazon Kinesis provides the developers with client libraries that enable the design and operation of real-time data processing applications. Add the Amazon Kinesis Client Library to Java application and it will notify when new data is available for processing.
- Cost-efficient − Amazon Kinesis is cost-efficient for workloads of any scale. Pay as we go for the resources used and pay hourly for the throughput required.
