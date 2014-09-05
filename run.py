
from twisted.internet import reactor
from gerrit_bot import GerritBot

MINNIE="minnie.acer.com.tw"
MICKEY="mickey.acer.com.tw"
MINNIE_WHITE_LIST=["acer/dandelion", "acer/conga", "acer/timbero", "acer/bongo", "acer/bolero", "acer/asf", "acer/partyshot"]
MICKEY_WHITE_LIST=[]
HIPCHAT_AUTH_TOKEN=""
HIPCHAT_ROOM_ID=""
REDMINE_API_KEY=""

gb_minnie = GerritBot(MINNIE, MINNIE_WHITE_LIST, HIPCHAT_AUTH_TOKEN, HIPCHAT_ROOM_ID, REDMINE_API_KEY)
gb_mickey = GerritBot(MICKEY, MICKEY_WHITE_LIST, HIPCHAT_AUTH_TOKEN, HIPCHAT_ROOM_ID, REDMINE_API_KEY)
ctrl_minnie = reactor.spawnProcess(gb_minnie, "ssh", args= ["ssh", "-p", "29418", MINNIE, "gerrit", "stream-events"])
ctrl_mickey = reactor.spawnProcess(gb_mickey, "ssh", args= ["ssh", "-p", "29418", MICKEY, "gerrit", "stream-events"])
reactor.run()