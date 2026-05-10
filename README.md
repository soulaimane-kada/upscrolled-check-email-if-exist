# UpScrolled Check Email If Exist

Check any email if exist in upscrolled (Social Media app)

## Features

- **isExist** → if True → email already registred exist
- **isNotConfirmed** → if True → user exist but he still didn't confirm his email

## How to Use This API

### Input Parameters

The input for this scraper should be a JSON object containing the email of the target user you want to check. Check the input tab for a detailed list of parameters.

```json
{
  "email": "Donald_Truck_666@gmail.com"
}
```

## UpScrolled Output Format

After a successful request, the API will return the data.

```json
{
  "success": true,
  "results": {
    "statusCode": 200,
    "isExist": False,
    "checker": "Donald_Truck_666@gmail.com",
    "isNotConfirmed": False
  }
}
```

### Your feedback
We’re always working on improving the performance of our Actors. So if you’ve got any technical feedback for upscrolled post scraper or simply found a bug, please create an issue on the Actor’s Issues tab in Apify Console.

