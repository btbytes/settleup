# Settle up

- a cloudflare hosted poker buy-in and final settlment app
- uses only cloudflare native tech, maybe just plain HTML and Javascript.
- Make the app visually attractive
- does not need any authentication to use
- stores information in browser session for use next time
- should start with a place to enter Date (autoselect current day), and place
- enter details for the following -- Player Name, Buy-in Count, Cash-out Count
- can add/delete rows as needed

- Buy-in Count should be in whole numbers - 1 to 50
- Cash-out count can be 0 - 5000

- Each buy-in represents 100 chips
- Each buy-in is $20

- Once calculate button is hit, the app should show:

Game summary:

Buy-in Total: $xxx.xx
Cash-out Total: $xxx.xx

Cash-out Difference: $xxx.xx

AND

Final Transactions
Payer, Pays, Receiver
Name, $xx.xx, Name



Adjustment Rules:

- Round down anything less than $1 to Zero
- When there is a difference, the adjustment should be fair to all participants.
- Distribute the missing money among all the winners equally.

Explain how the final adjustment was done.
