#!/usr/bin/env python3

from twython import Twython
from random import shuffle

from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

#offense votes
playerOff=['\n#ProBowlVote @JimmyG_10 ', '\n#ProBowlVote Tevin Coleman ', '\n#ProBowlVote Weston Richburg ', '\n#ProBowlVote @gkittle46 ', '\n#ProBowlVote Joe Staley ', '\n#ProBowlVote Mike Mcglinchey ', '\n#ProBowlVote Deebo Samuel ', '\n#ProBowlVote @ESanders_10 ', '\n#ProBowlVote @JuiceCheck44 ']

copyPlayers = playerOff[:]
shuffle(copyPlayers)
message = copyPlayers
twitter.update_status(status=message)

print("Tweeted: %s" % message)

#defense votes

playerDef = ['\n#ProBowlVote K\'Waun Williams ', '\n#ProBowlVote @RSherman_25 ', '\n#ProBowlVote Jimmie Ward ', '\n#ProBowlVote @Quaski29', '\n#ProBowlVote @fred_warner ', '\n#ProBowlVote @DreGreenlaw ', '\n#ProBowlVote @DeforestBuckner ', '\n#ProBowlVote @arikarmstead ', '\n#ProBowlVote @nbsmallerbear', '\n#ProBowlVote @IamDeeFord ']
copyPlayers = playerDef[:]
shuffle(copyPlayers)
message = copyPlayers
twitter.update_status(status=message)

print("Tweeted: %s" % message)

#Special teams and others

playerMoar = ['\n#ProBowlVote @MattBreida ','\n#ProBowlVote Mike Person ', '\n#ProBowlVote Laken Tomlinson ', '\n#ProBowlVote Azeez Al-Shaair ', '\n#ProBowlVote Robbie Gould ', '\n#ProBowlVote Richie James ', '\n#ProBowlVote Mitch Wishnowsky ', '\n#ProBowlVote @RMos_8ball ']
copyPlayers = playerMoar[:]
shuffle(copyPlayers)
message = copyPlayers
twitter.update_status(status=message)

print("Tweeted: %s" % message)




