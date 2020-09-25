#run these (with the correct values) before running this script

#export API_KEY=

export EVENT_ID=5573

echo "--------- getting data from Hey Summit for event $EVENT_ID"

curl  "https://api.heysummit.com/api/talks/?event=$EVENT_ID"         -H "Authorization: Token $API_KEY" > ../../data/hey_summit/talks_page_1.json
curl  "https://api.heysummit.com/api/talks/?event=$EVENT_ID&page=2"  -H "Authorization: Token $API_KEY" > ../../data/hey_summit/talks_page_2.json
curl  "https://api.heysummit.com/api/talks/?event=$EVENT_ID&page=3"  -H "Authorization: Token $API_KEY" > ../../data/hey_summit/talks_page_3.json
curl  "https://api.heysummit.com/api/talks/?event=$EVENT_ID&page=4"  -H "Authorization: Token $API_KEY" > ../../data/hey_summit/talks_page_4.json
curl  "https://api.heysummit.com/api/talks/?event=$EVENT_ID&page=5"  -H "Authorization: Token $API_KEY" > ../../data/hey_summit/talks_page_5.json
curl  "https://api.heysummit.com/api/talks/?event=$EVENT_ID&page=6"  -H "Authorization: Token $API_KEY" > ../../data/hey_summit/talks_page_6.json
curl  "https://api.heysummit.com/api/talks/?event=$EVENT_ID&page=7"  -H "Authorization: Token $API_KEY" > ../../data/hey_summit/talks_page_7.json
curl  "https://api.heysummit.com/api/talks/?event=$EVENT_ID&page=8"  -H "Authorization: Token $API_KEY" > ../../data/hey_summit/talks_page_8.json
curl  "https://api.heysummit.com/api/talks/?event=$EVENT_ID&page=9"  -H "Authorization: Token $API_KEY" > ../../data/hey_summit/talks_page_9.json
curl  "https://api.heysummit.com/api/talks/?event=$EVENT_ID&page=10" -H "Authorization: Token $API_KEY" > ../../data/hey_summit/talks_page_10.json

#curl  "https://api.heysummit.com/api/talks/"   \
#  -H "Authorization: Token $API_KEY" > talks-all.json