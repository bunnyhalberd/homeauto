# HomeKit Backups

I made these repos as a backup of the HomeKit settings I've had. I made them by setting each one in HomeKit, and then running this:

`curl -vks https://192.168.7.39/api/<apiKey>/lights | jq . > normalEvening.json`

It's just a way for me to keep track of what I've had. There's lots of data in each one that's not good for the scene, but it's what I've gotta do at this point. :)
