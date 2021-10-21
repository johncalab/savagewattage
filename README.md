# savagewattage

Simple web app to calculate power zones given an FTP. It also estimates FTP given a ramp test.
Deployed via heroku at: https://savagewattage.herokuapp.com/

---
Reminder how to use the heroku cli
```bash
heroku login
heroku stack:set container -a savagewattage
heroku logs --tail -a savagewattage
heroku apps:open -a savagewattage
```
