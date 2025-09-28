from datetime import datetime

kata = (2019, 9, 25, 3, 30)
date = datetime(*kata)
print (date.strftime('%m/%d/%Y %H:%M'))
