import numpy as np
x = "The Foundr Podcast with Nathan Chan on Acasthttps://play.acast.com › foundr 285: The Art of Mind-Blowing Open Rates, Email Flows, and Authentic Email Marketing, With Boundless Labs' Chase Dimond. At 27, Chase Dimond is already"
x = x.lower().replace(','," ").replace('.', " ").replace("-", " ").split(" ")
print(np.array(x))