WORKDIR=~/repos/rm2/TLD-workflow
TARGETDIR=$WORKDIR/today
rm -rf $TARGETDIR
mkdir $TARGETDIR
cp -r $WORKDIR/template-day/* $TARGETDIR
TODAY=$(date +"%B %d, %Y")

generate_hex() {
    local length=$1
    od -An -N$((length/2)) -tx1 /dev/urandom | tr -d ' '
}

generate_tag() {
  hex1=$(generate_hex 8)
  hex2=$(generate_hex 4)
  hex3=$(generate_hex 4)
  hex4=$(generate_hex 4)
  hex5=$(generate_hex 12)

  echo "$hex1-$hex2-$hex3-$hex4-$hex5"
}

NB_TAG=$(generate_tag)
echo $NB_TAG
P1_TAG=$(generate_tag)
P2_TAG=$(generate_tag)
echo $P1_TAG
echo $P2_TAG

TODAY=$(date +"%B %d, %Y")
NOW=$(date +"%s000")

cat > $TARGETDIR/templatenotebook.metadata<< EOF
{
    "createdTime": "$NOW",
    "lastModified": "$NOW",
    "lastOpened": "$NOW",
    "lastOpenedPage": 1,
    "parent": "",
    "pinned": false,
    "type": "DocumentType",
    "visibleName": "$TODAY"
}
EOF

rename templatenotebook $NB_TAG $TARGETDIR/*
rename page1 $P1_TAG $TARGETDIR/$NB_TAG*/*
rename page2 $P2_TAG $TARGETDIR/$NB_TAG*/*

mv $TARGETDIR/** $WORKDIR/xochitl 
rmdir $TARGETDIR 

