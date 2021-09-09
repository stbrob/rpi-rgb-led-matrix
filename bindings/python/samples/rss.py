
#!/usr/bin/env python
# Display a runtext with double-buffering.
from samplebase import SampleBase
from rgbmatrix import graphics
import time
import feedparser
# Iterate over the allheadlines list and print each headline
Marque=""
WAITTIME = 600


def parseRSS( rss_url ):
    return feedparser.parse( rss_url ) 
    
# Function grabs the rss feed headlines (titles) and returns them as a list
def getHeadlines( rss_url ):
    headlines = []
    feed = parseRSS( rss_url )
    for newsitem in feed['items']:
        headlines.append(newsitem['title']) 
    return headlines




class RunText(SampleBase):
    def __init__(self, *args, **kwargs):
        super(RunText, self).__init__(*args, **kwargs)
        self.parser.add_argument("-t", "--text", help="The text to scroll on the RGB LED panel", default="Hello world!")

    def run(self):
        print ('Test')
        offscreen_canvas = self.matrix.CreateFrameCanvas()
        font = graphics.Font()
        font.LoadFont("../../../fonts/7x13.bdf")
        textColor = graphics.Color(255, 255, 0)
        pos = offscreen_canvas.width
        my_text = Marque
        print ("Marque"+Marque)
        valid = True
        secondCount = 0

        while valid:
            offscreen_canvas.Clear()
            len = graphics.DrawText(offscreen_canvas, font, pos, 12, textColor, my_text)
            pos -= 1
            if (pos + len < 0):
                pos = offscreen_canvas.width

            time.sleep(0.025)
            secondCount=secondCount+0.025
            offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)
            if secondCount > WAITTIME:
                valid = False

# Main function
if __name__ == "__main__":
    # A list to hold all headlines
    while True:
        allheadlines = []
        allheadlines.extend( getHeadlines('https://www.abc.net.au/news/feed/51120/rss.xml') )
        # Iterate over the allheadlines list and print each headline
        for hl in allheadlines:    
                Marque=Marque+" -ABCNews- "+hl 
        #print(Marque)
        run_text = RunText()
        if (not run_text.process()):
            run_text.print_help()

