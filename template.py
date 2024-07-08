#Steps
'''
1_ Create a function to create ticket
2_ Call the API: https://desk.zoho.com/DeskAPIDocument#Tickets#Tickets_Createaticket

$ curl -X POST https://desk.zoho.com/api/v1/tickets
  -H "orgId:2389290"
  -H "Authorization:Zoho-oauthtoken 1000.3d0a155402dbb59f776fd63adb1e67c0.a41ea557a6a8d7e402690098b2056f60s"

  -d'{
  "entitySkills" : [ "18921000000379001", "18921000000364001", "18921000000379055", "18921000000379031" ],
  "subCategory" : "Sub General",
  "cf" : {
    "cf_permanentaddress" : null,
    "cf_dateofpurchase" : null,
    "cf_phone" : null,
    "cf_numberofitems" : null,
    "cf_url" : null,
    "cf_secondaryemail" : null,
    "cf_severitypercentage" : "0.0",
    "cf_modelname" : "F3 2017"
  },
  "productId" : "",
  "contactId" : "1892000000042032",
  "subject" : "Real Time analysis Requirement",
  "dueDate" : "2016-06-21T16:16:16.000Z",
  "departmentId" : "1892000000006907",
  "channel" : "Email",
  "description" : "Hai This is Description",
  "language" : "English",
  "priority" : "High",
  "classification" : "",
  "assigneeId" : "1892000000056007",
  "phone" : "1 888 900 9646",
  "category" : "general",
  "email" : "carol@zylker.com",       // A Query that needs to run to fetch the MID corresponding merchants in an CSV
  "status" : "Open"
}'

3_ Pass a CSV file for the MID<>webhooks

'''
