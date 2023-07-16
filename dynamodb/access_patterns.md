## Access Patterns

* The only users are building owners
* Building owner wants to see their buildings, and from there, their units and tenants
* Building owners wants to see all units with rent due today.
* Proper owner wants to see all their tenants with arrears
* Property owner wants to see all tenants with rent due yesterday
* when a payment is received, we want to update the last_payment_timestamp and arrears for a tenants
* at midnight we want to fetch all tenants with rent_due_day is yesterday, and set the arrears
