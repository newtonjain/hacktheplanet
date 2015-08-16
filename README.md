# Getting Started
##### Modules
- [FrontEnd](https://github.com/newtonjain/hacktheplanet/tree/master/FrontEnd): UX Design
- [docs](https://github.com/newtonjain/hacktheplanet/tree/master/docs): *you're reading them*
- [requirements](https://github.com/newtonjain/hacktheplanet/tree/master/requirements): *lolwut?*
- [utsu-bulletinboard](https://github.com/newtonjain/hacktheplanet/tree/master/utsu-bulletinboard): Django Infrastructure

# Timeline
* customer/rider experience
  * customer
    * inputs point a to b [POST TO /trip]
      * scenic or economically
      * scenic computation has to happen right here [IN REQUEST CALLBACK, SCENIC ROADMAP IS GIVEN BACK TO FRONT END]
    * inputs 3 top profiles he would like to ride with [in request body and stuff]
  * rider
    * text message from twilio to riders phone
    * checks app
    * sees new requests
    * accepts one of them
  * customer
    * text sms arrives to customer when he confirms
  * rider
    * *drives to destination*
    * presses arrived on the app
  * customer
    * text sms arrives to customer when driver arrives
  * rider
    * desination arrived, hits button
  * customer
    * checks app and in the ticker pane, he has a transaction report
