#!/usr/bin/bash
## FOR FILES.MUSICPLACE.VIP: -----------------------------------------

DIR=`pwd`
USER1=chunk
USER2=www-data

sudo chown -R $USER1:$USER2 $DIR
sudo find $DIR -type f -exec chmod 660 {} \;
sudo find $DIR -type d -exec chmod 770 {} \;
sudo find $DIR/public -type f -exec chmod 664 {} \;
sudo find $DIR/public -type d -exec chmod 775 {} \;

echo ""
echo "Success!"
echo ""

## =============================================================
