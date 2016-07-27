import settings
import auth
from niantic import Niantic
from radar import Radar

token = auth.login(('google', 'tatyana.volkunovich@gmail.com', 'ijrjkflyjt xelj'))
auth.tokens[token.value] = token
niantic = Niantic()
radar = Radar(niantic)
niantic.connect()
location = (55.7538723, 37.6200955)
radar.locate(location)
