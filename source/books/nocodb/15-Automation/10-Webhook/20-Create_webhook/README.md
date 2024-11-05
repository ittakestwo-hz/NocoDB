# Create webhook

## Create Webhook[](https://docs.nocodb.com/views/views-overview/#create-webhook "Direct link to Create Webhook")

### Accessing webhook page[](https://docs.nocodb.com/views/views-overview/#accessing-webhook-page "Direct link to Accessing webhook page")

1.  Click on table for which webhook needs to be configured on the left sidebar
2.  Open `Details` tab in topbar,
3.  Click on `Webhooks` tab
4.  Click `Add New Webhook`

![Accessing webhook](https://docs.nocodb.com/assets/images/create-webhook-1-be523f2a91b6829cd8d82915d07e92e4.png)

### Configuring webhook[](https://docs.nocodb.com/views/views-overview/#configuring-webhook "Direct link to Configuring webhook")

1.  Name of the webhook
2.  Select the event for which webhook needs to be triggered

| Trigger | Details |
| --- | --- |
| After Record Insert | After a single record is inserted |
| After Record Update | After a single record is updated |
| After Record Delete | After a single record is deleted |
| After Multiple Record Insert | After bulk records are inserted |
| After Multiple Record Update | After bulk records are updated |
| After Multiple Record Delete | After bulk records are deleted |
| Manual Trigger | Manually trigger webhook using button field |

3.  Method & URL: Configure the endpoint to which webhook needs to be triggered. Supported methods are GET, POST, DELETE, PUT, HEAD, PATCH
4.  Headers & Parameters: Configure Request headers & parameters (optional)
5.  Condition: Only records meeting the configured criteria will trigger webhook (optional)
6.  Test webhook (with sample payload) to verify if parameter are configured appropriately (optional)
7.  Save the webhook

![Configuring webhook](https://docs.nocodb.com/assets/images/create-webhook-2-bfee41aaeb94b884024cd5e874f290c1.png)

For more information on **Manual Trigger** webhook & its use with **Button** field, refer [here](https://docs.nocodb.com/fields/field-types/custom-types/button)

### Webhook with conditions[](https://docs.nocodb.com/views/views-overview/#webhook-with-conditions "Direct link to Webhook with conditions")

In case of webhook with conditions, only records meeting the configured criteria will trigger webhook. For example, trigger webhook only when `Status` is `Complete`. You can also configure multiple conditions using `AND` or `OR` operators. For example, trigger webhook only when `Status` is `Complete` and `Priority` is `High`.

Webhook will be triggered only when the configured condition wasn't met before the record was updated. For example, if you have configured webhook with condition `Status` `is` `Complete` and `Priority` `is` `High` and you update the record with `Status` `Complete` and `Priority` `Low` to `High`, webhook will be triggered. However, if you update any other fields of the record with `Status` `Complete` and `Priority` `High`, webhook won't be triggered.

In summary, webhook will be triggered only when `Condition(old-record) = false` and `Condition(new-record) = true`.

note

**Note:** Conditions are not applicable for Manual Trigger webhook.

### Webhook response sample[](https://docs.nocodb.com/views/views-overview/#webhook-response-sample "Direct link to Webhook response sample")

-   After Insert
-   After Update
-   After Delete
-   After Bulk Insert
-   After Bulk Update
-   After Bulk Delete
-   Manual Trigger

```
{  "type": "records.after.insert",  "id": "9dac1c54-b3be-49a1-a676-af388145fa8c",  "data": {    "table_id": "md_xzru7dcqrecc60",    "table_name": "Film",    "view_id": "vw_736wrpoas7tr0c",    "view_name": "Film",    "records": [      {        "FilmId": 1011,        "Title": "FOO",        "Language": {          "LanguageId": 1,          "Name": "English"        },      }    ]  }}
```

### Webhook with custom payload ☁[](https://docs.nocodb.com/views/views-overview/#webhook-with-custom-payload- "Direct link to Webhook with custom payload ☁")

info

This feature is only available in the paid plans, in both cloud & self-hosted.

In the enterprise edition, you can set up a personalized payload for your webhook. Just head to the `Body` tab to make the necessary configurations. Users can utilize [handlebar syntax](https://handlebarsjs.com/guide/#simple-expressions), which allows them to access and manipulate the data easily.

Use `{{ json event }}` to access the event data. Sample response is as follows

```
{  "type": "records.after.insert",  "id": "0698517a-d83a-4e72-bf7a-75f46b704ad1",  "data": {    "table_id": "m969t01blwprpef",    "table_name": "Table-2",    "view_id": "vwib3bvfxdqgymun",    "view_name": "Table-2",    "rows": [      {        "Id": 1,        "Tags": "Sample Text",        "CreatedAt": "2024-04-11T10:40:20.998Z",        "UpdatedAt": "2024-04-11T10:40:20.998Z"      }    ]  }}
```

info

**Note:** The custom payload feature is only available in the enterprise edition.

#### Discord Webhook[](https://docs.nocodb.com/views/views-overview/#discord-webhook "Direct link to Discord Webhook")

Discord webhook can be configured to send messages to a Discord channel. Discord request body should contain content, embeds or attachments, otherwise request will fail. Below is an example of Discord webhook payload. More details can be found [here](https://birdie0.github.io/discord-webhooks-guide/discord_webhook.html)

```
{  "content": "Hello, this is a webhook message",  "embeds": [    {      "title": "Webhook",      "description": "This is a webhook message",      "color": 16711680    }  ]}
```

To send complete event data to Discord, use below payload

```
{  "content" : {{ json ( json event ) }}}
```

One can also customize the payload as per the requirement. For example, to send only the `Title` field to Discord, use below payload. Note that, the value of `content` is what that will get displayed in the Discord channel.

```
{   "content": "{{ event.data.rows.[0].Title }}"}
```

## Environment Variables[](https://docs.nocodb.com/views/views-overview/#environment-variables "Direct link to Environment Variables")

In self-hosted version, you can configure the following environment variables to customize the webhook behavior.

-   NC\_ALLOW\_LOCAL\_HOOKS: Allow localhost based links to be triggered. Default: false

Find more about environment variables [here](https://docs.nocodb.com/getting-started/self-hosted/environment-variables)