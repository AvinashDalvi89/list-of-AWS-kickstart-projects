# Business Card Organiser using Amazon Textract and S3 bucket
This project allows you to experiment with Textract's capabilities and gain practical experience with uploading files and processing data in the AWS cloud environment.

## How to Build:

- Set Up S3 Bucket: Create a bucket in S3 to store uploaded business card images.
- Develop Upload Functionality: Build a simple web interface where users can upload business card images.
  - This can be done with HTML, CSS, and Javascript (or a web framework like React).
- Integrate Textract: Use the AWS SDK to call Textract and process the uploaded image. Textract will return the extracted text data.
- Data Processing & Storage: Parse the extracted text to identify relevant information like name, title, company, etc. (Regular expressions can be helpful here).
- Store the Data: Save the extracted contact information in a user-friendly format. This can be:
  - A database on another AWS service (like DynamoDB)
  - A downloadable spreadsheet (CSV format)

 
