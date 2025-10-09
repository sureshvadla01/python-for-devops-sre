accesslog="/Users/sureshvadla/toyota/suresh/suresh-code/access.log"
http_count="/Users/sureshvadla/toyota/suresh/suresh-code/count.log"

with open(accesslog,"r") as inputfile, open(http_count,"w") as outputfile:
    for read in inputfile:
        if "login" in read:
            outputfile.write(read)