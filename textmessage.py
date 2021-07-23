Import http.client as ht
url = ht.HTTPConnection(“api.sms-magic.com”)
payload = {
 “sms_text” : “Hi, Lorem ipsum dolor sit amet”,
 “sender_id” : “ anjali”,
 “mobile_number” : “9800112345”,
 “country” : “INDIA”,
}
{
 “sms_text” : “Hi, Lorem ipsum dolor sit amet”,
 “sender_id” : “ anjali”,
 “mobile_number” : “4442124678”,
 “country” : “USA”,
}
{
 “status” : “successful”,
 “message” : “queued”,
}
{
 “message” : “REQ_API_KEY”
}
Header = {July 22, 2021 Page 2
 ‘apikey’ : “sm8229d1f346e464d04810fxxxx”,
 ‘Content-Type’ : “application/json”,
}
conn.request(“POST”, url, data= payload, header = header)
Response = conn.get response()
Data = response.read()
Print(data.decode(“utf-8”))
 
 
