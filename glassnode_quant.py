null =None
true = True
false=False
quant_var={"uuid":"cus_04ylpB81VvKxQANw","firstName":"Papasani","lastName":"Mohansrinivas","email":"papasani.mohansrinivas@gmail.com","plan":"advanced","planName":"Advanced","searchAPIKey":"ZDY1Nzc1ODQxNjNhYWVmNjQ1ZTA3NmM5OTJmNTE0NTNhNTJmMzZkM2U1MjllOGQzYzRiOWQ5ZjgzZGVmYjJkNWZpbHRlcnM9dmlzaWJsZV9ieSUzQTc0NDE2NCtPUit2aXNpYmxlX2J5JTNBcHVibGlj","features":[],"surveyAssets":["Bitcoin","Ethereum","DeFi","Derivatives","Stablecoins","NFTs"],"trial":true,"trialAvailable":false,"trialExpiry":1695513600,"countryCode":"IN","packages":null}

print(quant_var["searchAPIKey"])

import json
import requests
import pandas as pd


# insert your API key here
# API_KEY = 'c9fe6db32ac8edafc400d4a0df0139d9'
# API_KEY = "M5sT98VT4FUrQNn1p96VeTnR2iTr6qou"
# API_KEY = "de5efc7c458842948af3f9b3c6cd3b9b"
API_KEY = "75c4100b7fcc4d63a2dd28ea1030a61a"
# make API request

# headers = {"cookie":"_gcl_au=1.1.389967978.1694372349; _gid=GA1.2.960455209.1694372356; ajs_anonymous_id=0a76beee-c3ca-47c6-9eb3-97064666c18c; _hjIncludedInSessionSample_1425107=1; _hjSessionUser_1425107=eyJpZCI6IjAzODcxZjIxLTVmNmItNTkyNS04Nzg1LTIxNjE1MmZiNmQyMiIsImNyZWF0ZWQiOjE2OTQzNzIzNjg0MTEsImV4aXN0aW5nIjp0cnVlfQ==; ajs_user_id=cus_04ylpB81VvKxQANw; _hjSessionUser_3114558=eyJpZCI6ImRlMjExMjQwLTkxMjEtNWFhYS04YWIxLTM1MzJjNjQ2ZjAxNSIsImNyZWF0ZWQiOjE2OTQzNzM2NDIyMTksImV4aXN0aW5nIjpmYWxzZX0=; _ga_8MGXPNL6MF=GS1.1.1694373641.1.0.1694373659.42.0.0; __cuid=b1ba78e6329d4959bf509aa89182b1ce; _ga_YYWW6JR31S=GS1.1.1694377029.2.0.1694377029.0.0.0; analytics_session_id=1694377036864; _hjSession_1425107=eyJpZCI6IjUxOGMxMmRkLTY1YmQtNDY1Ni1hMGM4LTgwZDQ1OGY0MjRlMyIsImNyZWF0ZWQiOjE2OTQzNzcwMzcwNzUsImluU2FtcGxlIjp0cnVlfQ==; amp_fef1e8=8bca9985-84ab-4095-9db6-a89644dbf4bbR...1ha0bra5g.1ha0cie3b.d.4.h; _gat_UA-129287447-1=1; _ga=GA1.2.658618689.1694372356; analytics_session_id.last_access=1694378674766; _s=MTY5NDM3ODY3NHxUOFh4Y1BaNEcwNVRHY0dici1jOTM2NTc2RTh1dWxJSTltNW5mWjRPZmFlamdreFZNVkQ5N05vTjB3eHJERWc9fN9eBNJGW4PPzVm-bjQyaQcav6nRABzFmQtmL08X8mU_; _ga_M9YVRZCN8G=GS1.1.1694377037.2.1.1694378675.0.0.0; _ga_MT5MWT6847=GS1.1.1694377037.2.1.1694378675.15.0.0"}
# headers = {"X-Api-Key":API_KEY}
# headers = {"cookie":"_gcl_au=1.1.389967978.1694372349; _gid=GA1.2.960455209.1694372356; ajs_anonymous_id=0a76beee-c3ca-47c6-9eb3-97064666c18c; _hjIncludedInSessionSample_1425107=1; _hjSessionUser_1425107=eyJpZCI6IjAzODcxZjIxLTVmNmItNTkyNS04Nzg1LTIxNjE1MmZiNmQyMiIsImNyZWF0ZWQiOjE2OTQzNzIzNjg0MTEsImV4aXN0aW5nIjp0cnVlfQ==; ajs_user_id=cus_04ylpB81VvKxQANw; _hjSessionUser_3114558=eyJpZCI6ImRlMjExMjQwLTkxMjEtNWFhYS04YWIxLTM1MzJjNjQ2ZjAxNSIsImNyZWF0ZWQiOjE2OTQzNzM2NDIyMTksImV4aXN0aW5nIjpmYWxzZX0=; _ga_8MGXPNL6MF=GS1.1.1694373641.1.0.1694373659.42.0.0; analytics_session_id=1694377036864; _hjSession_1425107=eyJpZCI6IjUxOGMxMmRkLTY1YmQtNDY1Ni1hMGM4LTgwZDQ1OGY0MjRlMyIsImNyZWF0ZWQiOjE2OTQzNzcwMzcwNzUsImluU2FtcGxlIjp0cnVlfQ==; __cuid=b1ba78e6329d4959bf509aa89182b1ce; amp_fef1e8=8bca9985-84ab-4095-9db6-a89644dbf4bbR...1ha0en2du.1ha0fpjn5.h.4.l; _ga_YYWW6JR31S=GS1.1.1694381173.3.0.1694381173.0.0.0; _ga_L7S640PB78=GS1.1.1694381185.1.0.1694381185.60.0.0; _ga_WKCPXFMMLV=GS1.1.1694381183.1.1.1694381294.0.0.0; _ga=GA1.2.658618689.1694372356; _gat_UA-129287447-1=1; _ga_M9YVRZCN8G=GS1.1.1694377037.2.1.1694383140.0.0.0; _ga_MT5MWT6847=GS1.1.1694377037.2.1.1694383140.5.0.0; _s=MTY5NDM4MzE0MHxyeXphLVRncjduZjdkMTZpUEhQN3dQTXJ4OTJHU2NVeWFkNFVwQ0tjdU1kQUx6X0pRSllzbllNN2lwSWZWamc9fKWGePDQXYcyg1W29v8VWRS6mHaliWkLNPZLCCglR39h; analytics_session_id.last_access=1694383146758"}
# headers = {"cookie":"_gcl_au=1.1.389967978.1694372349; _gid=GA1.2.960455209.1694372356; ajs_anonymous_id=0a76beee-c3ca-47c6-9eb3-97064666c18c; _hjSessionUser_1425107=eyJpZCI6IjAzODcxZjIxLTVmNmItNTkyNS04Nzg1LTIxNjE1MmZiNmQyMiIsImNyZWF0ZWQiOjE2OTQzNzIzNjg0MTEsImV4aXN0aW5nIjp0cnVlfQ==; ajs_user_id=cus_04ylpB81VvKxQANw; _hjSessionUser_3114558=eyJpZCI6ImRlMjExMjQwLTkxMjEtNWFhYS04YWIxLTM1MzJjNjQ2ZjAxNSIsImNyZWF0ZWQiOjE2OTQzNzM2NDIyMTksImV4aXN0aW5nIjpmYWxzZX0=; _ga_8MGXPNL6MF=GS1.1.1694373641.1.0.1694373659.42.0.0; __cuid=b1ba78e6329d4959bf509aa89182b1ce; amp_fef1e8=8bca9985-84ab-4095-9db6-a89644dbf4bbR...1ha0en2du.1ha0fpjn5.h.4.l; _ga_L7S640PB78=GS1.1.1694419669.2.0.1694419669.60.0.0; _ga_YYWW6JR31S=GS1.1.1694418712.4.1.1694420558.0.0.0; _ga_WKCPXFMMLV=GS1.1.1694419672.2.1.1694420578.0.0.0; _gat_UA-129287447-1=1; _ga_M9YVRZCN8G=GS1.1.1694502265.3.0.1694502266.0.0.0; _ga_MT5MWT6847=GS1.1.1694502265.3.0.1694502266.59.0.0; _ga=GA1.2.658618689.1694372356; analytics_session_id=1694502280414; analytics_session_id.last_access=1694502280437; _hjIncludedInSessionSample_1425107=1; _hjSession_1425107=eyJpZCI6IjliZjQ5Zjc5LTM5MWQtNDRiMC04NWY3LTM4ZDg0ZmY0MjM1YiIsImNyZWF0ZWQiOjE2OTQ1MDIyODA3NjMsImluU2FtcGxlIjp0cnVlfQ==; ln_or=eyI0NzM5NDYiOiJkIn0=; _s=MTY5NDUwMjI5NHxzeW5jdGRfal9weDhjd2kwR0pKZGhNZzNDRjB6eWRHTHRwdWRrSVRIaHNOcXlUTHpIWWRYbnJNZmwtSk02U1k9fEnkqP-iJd_8JzlZbgjwPWdJYi3kjzpN5KR4_CULF6MT"}                                                                                                                                                                                                                                                                                                                    
# headers = {"cookie":"_gcl_au=1.1.389967978.1694372349; _gid=GA1.2.960455209.1694372356; ajs_anonymous_id=0a76beee-c3ca-47c6-9eb3-97064666c18c; _hjSessionUser_1425107=eyJpZCI6IjAzODcxZjIxLTVmNmItNTkyNS04Nzg1LTIxNjE1MmZiNmQyMiIsImNyZWF0ZWQiOjE2OTQzNzIzNjg0MTEsImV4aXN0aW5nIjp0cnVlfQ==; ajs_user_id=cus_04ylpB81VvKxQANw; _hjSessionUser_3114558=eyJpZCI6ImRlMjExMjQwLTkxMjEtNWFhYS04YWIxLTM1MzJjNjQ2ZjAxNSIsImNyZWF0ZWQiOjE2OTQzNzM2NDIyMTksImV4aXN0aW5nIjpmYWxzZX0=; _ga_8MGXPNL6MF=GS1.1.1694373641.1.0.1694373659.42.0.0; __cuid=b1ba78e6329d4959bf509aa89182b1ce; amp_fef1e8=8bca9985-84ab-4095-9db6-a89644dbf4bbR...1ha0en2du.1ha0fpjn5.h.4.l; _ga_L7S640PB78=GS1.1.1694419669.2.0.1694419669.60.0.0; _ga_YYWW6JR31S=GS1.1.1694418712.4.1.1694420558.0.0.0; _ga_WKCPXFMMLV=GS1.1.1694419672.2.1.1694420578.0.0.0; analytics_session_id=1694502280414; _hjIncludedInSessionSample_1425107=1; _hjSession_1425107=eyJpZCI6IjliZjQ5Zjc5LTM5MWQtNDRiMC04NWY3LTM4ZDg0ZmY0MjM1YiIsImNyZWF0ZWQiOjE2OTQ1MDIyODA3NjMsImluU2FtcGxlIjp0cnVlfQ==; _gat_UA-129287447-1=1; _ga=GA1.1.658618689.1694372356; _ga_M9YVRZCN8G=GS1.1.1694502265.3.1.1694502807.0.0.0; _ga_MT5MWT6847=GS1.1.1694502265.3.1.1694502807.59.0.0; _s=MTY5NDUwMjgxMnxEWUxKcWtSY2dDZEpWZm1PYl9XdTZZOHJpdjhFYkNSdzJMeHpIaHNnc2F0MlptYVByNEZmbEdMMHo3WFBZX0U9fLVzSlSKd0S9awDveMBJ4eXud-WT94NaWKAb-_v64exp; analytics_session_id.last_access=1694502815490"}
# headers = {"X-Api-Key":quant_var['uuid']}
# headers = {}
headers = {"cookie":"_gcl_au=1.1.389967978.1694372349; ajs_anonymous_id=0a76beee-c3ca-47c6-9eb3-97064666c18c; _hjSessionUser_1425107=eyJpZCI6IjAzODcxZjIxLTVmNmItNTkyNS04Nzg1LTIxNjE1MmZiNmQyMiIsImNyZWF0ZWQiOjE2OTQzNzIzNjg0MTEsImV4aXN0aW5nIjp0cnVlfQ==; ajs_user_id=cus_04ylpB81VvKxQANw; _ga_L7S640PB78=GS1.1.1694419669.2.0.1694419669.60.0.0; _ga_WKCPXFMMLV=GS1.1.1694419672.2.1.1694420578.0.0.0; __cuid=b1ba78e6329d4959bf509aa89182b1ce; amp_fef1e8=8bca9985-84ab-4095-9db6-a89644dbf4bbR...1ha8ovv9p.1ha8ovvaf.12.b.1d; _ga_YYWW6JR31S=GS1.1.1694659250.6.0.1694659250.0.0.0; _hjSessionUser_3114558=eyJpZCI6ImRlMjExMjQwLTkxMjEtNWFhYS04YWIxLTM1MzJjNjQ2ZjAxNSIsImNyZWF0ZWQiOjE2OTQzNzM2NDIyMTksImV4aXN0aW5nIjp0cnVlfQ==; _ga_8MGXPNL6MF=GS1.1.1694954994.3.0.1694954996.58.0.0; _gid=GA1.2.1911853280.1694955026; analytics_session_id=1694955032208; _hjSession_1425107=eyJpZCI6Ijg2YmViNzFhLWVmNDYtNGQxZS05YTI5LWE5ZWU4NDE0ZDlhZSIsImNyZWF0ZWQiOjE2OTQ5NTUwMzI3ODEsImluU2FtcGxlIjp0cnVlfQ==; _ga=GA1.2.658618689.1694372356; analytics_session_id.last_access=1694955561153; _gat_UA-129287447-1=1; _ga_M9YVRZCN8G=GS1.1.1694955027.5.1.1694956781.0.0.0; _ga_MT5MWT6847=GS1.1.1694955027.5.1.1694956781.55.0.0; _s=MTY5NDk1Njc5NHx5dDlBWlFZQ29UaFpOV2xHUnBUb3FZMzFvaUtXSjF2RDlMb2ZUcnhCeFU4dmlYOGhLQy1BOUF4Tk90bFp5U2s9fNGyglASNEKRr0UzXcq9ojtivhSPTp3PKQYQPok6JaHN"}
headers = {"cookie":"_gcl_au=1.1.389967978.1694372349; ajs_anonymous_id=0a76beee-c3ca-47c6-9eb3-97064666c18c; _hjSessionUser_1425107=eyJpZCI6IjAzODcxZjIxLTVmNmItNTkyNS04Nzg1LTIxNjE1MmZiNmQyMiIsImNyZWF0ZWQiOjE2OTQzNzIzNjg0MTEsImV4aXN0aW5nIjp0cnVlfQ==; ajs_user_id=cus_04ylpB81VvKxQANw; _ga_L7S640PB78=GS1.1.1694419669.2.0.1694419669.60.0.0; _ga_WKCPXFMMLV=GS1.1.1694419672.2.1.1694420578.0.0.0; __cuid=b1ba78e6329d4959bf509aa89182b1ce; amp_fef1e8=8bca9985-84ab-4095-9db6-a89644dbf4bbR...1ha8ovv9p.1ha8ovvaf.12.b.1d; _ga_YYWW6JR31S=GS1.1.1694659250.6.0.1694659250.0.0.0; _hjSessionUser_3114558=eyJpZCI6ImRlMjExMjQwLTkxMjEtNWFhYS04YWIxLTM1MzJjNjQ2ZjAxNSIsImNyZWF0ZWQiOjE2OTQzNzM2NDIyMTksImV4aXN0aW5nIjp0cnVlfQ==; _ga_8MGXPNL6MF=GS1.1.1694954994.3.0.1694954996.58.0.0; _gid=GA1.2.1911853280.1694955026; _gat_UA-129287447-1=1; analytics_session_id=1694955032208; _hjIncludedInSessionSample_1425107=1; _hjSession_1425107=eyJpZCI6Ijg2YmViNzFhLWVmNDYtNGQxZS05YTI5LWE5ZWU4NDE0ZDlhZSIsImNyZWF0ZWQiOjE2OTQ5NTUwMzI3ODEsImluU2FtcGxlIjp0cnVlfQ==; _ga=GA1.2.658618689.1694372356; _s=MTY5NDk1NTA1NHxTWXdfWnEtcm1LaFoxN2p1T1lod0hpN2RjandUVXdXaEs4Y3FkMkxPWUUtV25seFkxTExULVM1ZjJnTklsczQ9fN-JJ0vP76LfbNo4V0qmnDoi44C47DP0a4Qt5w54ADJi; analytics_session_id.last_access=1694955069527; _ga_M9YVRZCN8G=GS1.1.1694955027.5.1.1694955070.0.0.0; _ga_MT5MWT6847=GS1.1.1694955027.5.1.1694955070.17.0.0"}
headers = {"cookie":"_gcl_au=1.1.389967978.1694372349; ajs_anonymous_id=0a76beee-c3ca-47c6-9eb3-97064666c18c; _hjSessionUser_1425107=eyJpZCI6IjAzODcxZjIxLTVmNmItNTkyNS04Nzg1LTIxNjE1MmZiNmQyMiIsImNyZWF0ZWQiOjE2OTQzNzIzNjg0MTEsImV4aXN0aW5nIjp0cnVlfQ==; ajs_user_id=cus_04ylpB81VvKxQANw; _ga_L7S640PB78=GS1.1.1694419669.2.0.1694419669.60.0.0; _ga_WKCPXFMMLV=GS1.1.1694419672.2.1.1694420578.0.0.0; __cuid=b1ba78e6329d4959bf509aa89182b1ce; amp_fef1e8=8bca9985-84ab-4095-9db6-a89644dbf4bbR...1ha8ovv9p.1ha8ovvaf.12.b.1d; _ga_YYWW6JR31S=GS1.1.1694659250.6.0.1694659250.0.0.0; _hjSessionUser_3114558=eyJpZCI6ImRlMjExMjQwLTkxMjEtNWFhYS04YWIxLTM1MzJjNjQ2ZjAxNSIsImNyZWF0ZWQiOjE2OTQzNzM2NDIyMTksImV4aXN0aW5nIjp0cnVlfQ==; _hjSession_3114558=eyJpZCI6ImRiZTQ1NDEzLTQzYTUtNGYzNy04NGNiLTBiYWRmNGFmNzA5NyIsImNyZWF0ZWQiOjE2OTU3NDI2MDA3NzYsImluU2FtcGxlIjpmYWxzZSwic2Vzc2lvbml6ZXJCZXRhRW5hYmxlZCI6ZmFsc2V9; _ga_8MGXPNL6MF=GS1.1.1695742598.4.1.1695742653.5.0.0; _gid=GA1.2.1836961310.1695742704; analytics_session_id=1695742707552; _hjSession_1425107=eyJpZCI6ImIyYmQxYjQwLTg0NWItNDgyMy05ZGQ2LTFhZDBlYmU3ZTJiNyIsImNyZWF0ZWQiOjE2OTU3NDI3MDg2NTgsImluU2FtcGxlIjp0cnVlLCJzZXNzaW9uaXplckJldGFFbmFibGVkIjpmYWxzZX0=; _ga=GA1.2.658618689.1694372356; _gat_UA-129287447-1=1; analytics_session_id.last_access=1695743743467; _ga_M9YVRZCN8G=GS1.1.1695742704.10.1.1695743744.0.0.0; _ga_MT5MWT6847=GS1.1.1695742704.10.1.1695743744.60.0.0; _s=MTY5NTc0Mzc0OHx6bmxCRnpqTXBBeEFkaW0zLVNXdVB0QXZHNk9JYzF5c0hERFFMTUNXTHNzbUJhX3pfZ0thcGdYdTlqWEM1Tk09fE22TGkLlvs54SrddierWGSUwlgvrAKKVldUaZoZQBCw"}
null = None
# headers = "cookie":"_s=MTY5NTc0NTI1MXxzdGlnNlVTRDh2enhEYVd3NFdzcDdzWTFoQU5hUm9oMFdyNDNEdU9ZSG5DVk5HXzFUZC1TQURzdm1zNTJ1TU09fNvaPcsZbnGpCzn8CjFPX7hJCMHa01FcYaoB9hzG2hJb; amp_fef1e8=f417fb01-e16e-4232-9272-81a3239f36d6R...1hb945h84.1hb946sb3.9.0.9; __cuid=d09d01d4ac504ff2a0ec140335cd16c0"
headers = {"cookie":"_gcl_au=1.1.68520543.1695746209; _gid=GA1.2.1468857504.1695746213; ajs_anonymous_id=bb6ca20d-dbf3-4e80-bc32-6617f6abb245; analytics_session_id=1695746283197; _hjFirstSeen=1; _hjSession_1425107=eyJpZCI6IjUyNDhjZjdjLTMxZWUtNGViMS04NzhiLWE2ZDE0YjU5NDhmZiIsImNyZWF0ZWQiOjE2OTU3NDYyODM1NTgsImluU2FtcGxlIjp0cnVlLCJzZXNzaW9uaXplckJldGFFbmFibGVkIjpmYWxzZX0=; _hjSessionUser_1425107=eyJpZCI6ImIwZjcyOGU0LTBhOTgtNTk5NS1hNGMwLTcxZjMwNzE5YzY0NSIsImNyZWF0ZWQiOjE2OTU3NDYyODM1NTEsImV4aXN0aW5nIjp0cnVlfQ==; ajs_user_id=cus_MP54LxloNzZB61kq; _ga=GA1.2.1322330777.1695746213; _gat_UA-129287447-1=1; _ga_M9YVRZCN8G=GS1.1.1695746213.1.1.1695746452.0.0.0; _ga_MT5MWT6847=GS1.1.1695746213.1.1.1695746452.33.0.0; _s=MTY5NTc0NjQ1NXx5ZW14ek1od2t3VHN6OWlyRXVvcFM0UVdVYlJuVkV6N2N0eEZoT0NUNU9LOHdIeDdqbV9tZjVlWGFXNnlQYTg9fMyraLL_-gmaaJcOvmv4JBw7IS5f4_p4KjbiE4o49jcd; analytics_session_id.last_access=1695746459477"}

# data = {"categoryUuid":null,"data":{"configs":[{"meta":{"date":1695600000000,"asset":"BTC","since":1230940800000,"until":1695600000000,"currency":"native","metricCode":"addresses.ActiveCount","resolution":"1w","movingAverage":0,"movingMedian":0},"uuid":"1ed2005a-0d82-475d-a346-0f1f1a01b639","extra":{"price":true,"scale":"lin","lineColor":"#f7931a","chartStyle":"line"},"configType":"metric"},{"meta":{"date":1695600000000,"asset":"LTC","since":1230940800000,"until":1695600000000,"currency":"native","metricCode":"addresses.ActiveCount","resolution":"24h"},"uuid":"02277cc5-a2ea-4a24-a12e-330aad5e2f56","extra":{"price":true,"scale":"lin","lineColor":"#bfbbbb","chartStyle":"line"},"configType":"metric"}],"layouts":[{"h":3,"i":"1ed2005a-0d82-475d-a346-0f1f1a01b639","w":6,"x":6,"y":0,"minH":1,"minW":3},{"h":3,"i":"02277cc5-a2ea-4a24-a12e-330aad5e2f56","w":6,"x":0,"y":0,"minH":1,"minW":3}],"meta":{"name":"BoleBalma"}}}

data = {
	"categoryUuid": null,
	"data": {
		"configs": [
			{
				"configType": "metric",
				"extra": {
					"chartStyle": "line",
					"lineColor": "#f7931a",
					"price": true,
					"scale": "lin"
				},
				"meta": {
					"asset": "BTC",
					"currency": "native",
					"date": 1695600000000,
					"metricCode": "addresses.SendingCount",
					"resolution": "24h",
					"since": 1230940800000,
					"until": 1695600000000
				},
				"uuid": "1196910a-088a-46de-be88-48030ed20a54"
			}
		],
		"layouts": [
			{
				"h": 3,
				"i": "1196910a-088a-46de-be88-48030ed20a54",
				"minH": 1,
				"minW": 3,
				"w": 6,
				"x": 0,
				"y": 0
			}
		],
		"meta": {
			"name": "desilala"
		}
	}
}
headers = {"cookie":"_gcl_au=1.1.389967978.1694372349; ajs_anonymous_id=0a76beee-c3ca-47c6-9eb3-97064666c18c; _hjSessionUser_1425107=eyJpZCI6IjAzODcxZjIxLTVmNmItNTkyNS04Nzg1LTIxNjE1MmZiNmQyMiIsImNyZWF0ZWQiOjE2OTQzNzIzNjg0MTEsImV4aXN0aW5nIjp0cnVlfQ==; ajs_user_id=cus_04ylpB81VvKxQANw; _ga_L7S640PB78=GS1.1.1694419669.2.0.1694419669.60.0.0; _ga_WKCPXFMMLV=GS1.1.1694419672.2.1.1694420578.0.0.0; __cuid=b1ba78e6329d4959bf509aa89182b1ce; amp_fef1e8=8bca9985-84ab-4095-9db6-a89644dbf4bbR...1ha8ovv9p.1ha8ovvaf.12.b.1d; _ga_YYWW6JR31S=GS1.1.1694659250.6.0.1694659250.0.0.0; _hjSessionUser_3114558=eyJpZCI6ImRlMjExMjQwLTkxMjEtNWFhYS04YWIxLTM1MzJjNjQ2ZjAxNSIsImNyZWF0ZWQiOjE2OTQzNzM2NDIyMTksImV4aXN0aW5nIjp0cnVlfQ==; _ga_8MGXPNL6MF=GS1.1.1695742598.4.1.1695742653.5.0.0; _legacy_auth0.M5sT98VT4FUrQNn1p96VeTnR2iTr6qou.is.authenticated=true; auth0.M5sT98VT4FUrQNn1p96VeTnR2iTr6qou.is.authenticated=true; _gid=GA1.2.1836961310.1695742704; _hjSession_1425107=eyJpZCI6ImIyYmQxYjQwLTg0NWItNDgyMy05ZGQ2LTFhZDBlYmU3ZTJiNyIsImNyZWF0ZWQiOjE2OTU3NDI3MDg2NTgsImluU2FtcGxlIjp0cnVlLCJzZXNzaW9uaXplckJldGFFbmFibGVkIjpmYWxzZX0=; ln_or=eyI0NzM5NDYiOiJkIn0=; _ga=GA1.2.658618689.1694372356; analytics_session_id=1695748195207; _gat_UA-129287447-1=1; analytics_session_id.last_access=1695748656535; _ga_M9YVRZCN8G=GS1.1.1695748195.12.1.1695748657.0.0.0; _ga_MT5MWT6847=GS1.1.1695748195.12.1.1695748657.60.0.0; _s=MTY5NTc0ODY3MHx5N1BIUTRWZXVab0JZRi1HcnNPclowdFpJTWEwZDEyMGMyRGpzMWx0M1ZKUmNPWE9rZE9pcnZVNFk2V1ZYWGc9fF8hiKWd5g7kOgAvr2qWuglfHlhU5mnxNKSNcmK34FWz"}
# headers = {"cookie":"_gcl_au=1.1.389967978.1694372349; ajs_anonymous_id=0a76beee-c3ca-47c6-9eb3-97064666c18c; _hjSessionUser_1425107=eyJpZCI6IjAzODcxZjIxLTVmNmItNTkyNS04Nzg1LTIxNjE1MmZiNmQyMiIsImNyZWF0ZWQiOjE2OTQzNzIzNjg0MTEsImV4aXN0aW5nIjp0cnVlfQ==; ajs_user_id=cus_04ylpB81VvKxQANw; _hjSessionUser_3114558=eyJpZCI6ImRlMjExMjQwLTkxMjEtNWFhYS04YWIxLTM1MzJjNjQ2ZjAxNSIsImNyZWF0ZWQiOjE2OTQzNzM2NDIyMTksImV4aXN0aW5nIjpmYWxzZX0=; _ga_8MGXPNL6MF=GS1.1.1694373641.1.0.1694373659.42.0.0; _ga_L7S640PB78=GS1.1.1694419669.2.0.1694419669.60.0.0; _ga_WKCPXFMMLV=GS1.1.1694419672.2.1.1694420578.0.0.0; _gid=GA1.2.1609045842.1694659155; analytics_session_id=1694659157262; _hjIncludedInSessionSample_1425107=1; _hjSession_1425107=eyJpZCI6ImE2NThlNTgwLTU1YTEtNGUyMy1iNzM0LTM5YmRhNGZlODI4MiIsImNyZWF0ZWQiOjE2OTQ2NTkxNTc5NzEsImluU2FtcGxlIjp0cnVlfQ==; _gat_UA-129287447-1=1; _ga_M9YVRZCN8G=GS1.1.1694659155.4.1.1694659233.0.0.0; _ga_MT5MWT6847=GS1.1.1694659155.4.1.1694659233.52.0.0; analytics_session_id.last_access=1694659236303; __cuid=b1ba78e6329d4959bf509aa89182b1ce; amp_fef1e8=8bca9985-84ab-4095-9db6-a89644dbf4bbR...1ha8ovv9p.1ha8ovvaf.12.b.1d; _gat_gtag_UA_129287447_3=1; _ga_YYWW6JR31S=GS1.1.1694659250.6.0.1694659250.0.0.0; _s=MTY5NDY1OTI1NXxKWFhROUJGOC0zREF4UWRFbm1QWmZrTUhmR0paNmpKcWxqS09MbFNudGhibUMwbjJteDFMSTVwTkZiS2xOTkk9fDgqBDZZ9wZ3mLNlza1S3GS8QKWGblWUymZvSi3wVdoc; _ga=GA1.2.658618689.1694372356"}
# url = "https://api.glassnode.com/v1/metrics/indicators/sopr?a=btc"
# url = "https://api.glassnode.com"
# url = "https://cms.glassnode.com/api/metrics/derivatives.FuturesAnnualizedBasis3M?populate=*"
# url = "https://api.glassnode.com/v1/metrics/derivatives/options_open_interest_put_call_ratio"
# url = "https://api.glassnode.com/v1/metrics/derivatives/options_open_interest_put_call_ratio?a=BTC&c=native&e=aggregated&i=1h&referer=charts"
# url = "https://api.glassnode.com/v1/metrics/derivatives/futures_annualized_basis_3m?a=BTC&c=native&e=aggregated&i=24h"
# url = "https://cms.glassnode.com/api/metrics?fields[0]=group&fields[1]=metricCode&fields[2]=path&fields[3]=shortName&fields[4]=tier&fields[5]=isNew&fields[6]=resolutions&pagination[page]=3"
# url = "https://api.glassnode.com/v1/metrics/derivatives/futures_funding_rate_perpetual?a=BTC&c=native&e=aggregated&i=24h&referer=charts"
# url = "https://api.glassnode.com/v1/metrics/addresses/active_count?a=BTC&c=native&i=24h&referer=charts"
# url = "https://api.glassnode.com/v1/metrics/supply/supply_by_txout_type?a=BTC&c=native&i=24h&referer=charts"
# url = "https://cms.glassnode.com/api/metrics?fields[0]=group&fields[1]=metricCode&fields[2]=path&fields[3]=shortName&fields[4]=tier&fields[5]=isNew&fields[6]=resolutions"
# url = "https://cms.glassnode.com/api/metrics/derivatives.Options25DeltaSkew1Week?populate=*"
# url = "https://api.glassnode.com/v1/metrics/supply/provably_lost?a=BTC&c=native&i=24h&referer=charts"
# url = "https://api.glassnode.com/v1/metrics/derivatives/futures_open_interest_latest?a=BTC&c=usd&i=24h&referer=charts"
# url = "https://api.glassnode.com/v2/metrics/endpoints"
data = {
	"_account_id": "62c6ed5ef7956500111dbbb4",
	"_if_none_match": "W/46a3b254d2f4929696d93b8361b1ebfa2cb5fe13",
	"_mode": "user",
	"_profile_id": "651308a9d52f9b002d070f72",
	"_ratelimit_delay": 15
}
url = "https://fast.chameleon.io/observe/v2/profiles/651308a9d52f9b002d070f72"
# url = "https://api.glassnode.com/v1/metrics/addresses/active_count?a=BTC&c=native&i=24h&referer=charts"
# res = requests.put(url,data=data)
payload = {
	"items": [
		{
			"configType": "metric",
			"extra": {
				"lineColor": "#87999f",
				"name": "BTC: Price",
				"ref": 1,
				"scale": "log",
				"yAxis": 0
			},
			"meta": {
				"asset": "BTC",
				"currency": "native",
				"metricCode": "market.PriceUsdClose"
			},
			"uuid": "4f3600f5-5df6-4cf6-bc75-71b78d9265e8"
		}
	],
	"name": "olalala2"
}
# payload  = {"items":[{"configType":"metric","extra":{"lineColor":"#87999f","name":"BTC: Price","ref":1,"scale":"log","yAxis":0},"meta":{"asset":"BTC","currency":"native","metricCode":"market.PriceUsdClose"},"uuid":"4f3600f5-5df6-4cf6-bc75-71b78d9265e8"}],"name":"some2"}
# url_to_create = "{"items":[{"configType":"metric","extra":{"lineColor":"#87999f","name":"BTC: Price","ref":1,"scale":"log","yAxis":0},"meta":{"asset":"BTC","currency":"native","metricCode":"market.PriceUsdClose"},"uuid":"d9ee9655-64a0-4407-b8c7-6d787610a506"}],"name":"hutes4"}"
navaneet_workbench = "009d82d6-7dc0-41da-4085-eb5e08519073"
url_to_workbench = "https://studio.glassnode.com/workbench/{}".format(navaneet_workbench)
# headers = {"cookie":"_gcl_au=1.1.389967978.1694372349; ajs_anonymous_id=0a76beee-c3ca-47c6-9eb3-97064666c18c; _hjSessionUser_1425107=eyJpZCI6IjAzODcxZjIxLTVmNmItNTkyNS04Nzg1LTIxNjE1MmZiNmQyMiIsImNyZWF0ZWQiOjE2OTQzNzIzNjg0MTEsImV4aXN0aW5nIjp0cnVlfQ==; ajs_user_id=cus_04ylpB81VvKxQANw; _ga_L7S640PB78=GS1.1.1694419669.2.0.1694419669.60.0.0; _ga_WKCPXFMMLV=GS1.1.1694419672.2.1.1694420578.0.0.0; __cuid=b1ba78e6329d4959bf509aa89182b1ce; amp_fef1e8=8bca9985-84ab-4095-9db6-a89644dbf4bbR...1ha8ovv9p.1ha8ovvaf.12.b.1d; _ga_YYWW6JR31S=GS1.1.1694659250.6.0.1694659250.0.0.0; _hjSessionUser_3114558=eyJpZCI6ImRlMjExMjQwLTkxMjEtNWFhYS04YWIxLTM1MzJjNjQ2ZjAxNSIsImNyZWF0ZWQiOjE2OTQzNzM2NDIyMTksImV4aXN0aW5nIjp0cnVlfQ==; _ga_8MGXPNL6MF=GS1.1.1695742598.4.1.1695742653.5.0.0; _legacy_auth0.M5sT98VT4FUrQNn1p96VeTnR2iTr6qou.is.authenticated=true; auth0.M5sT98VT4FUrQNn1p96VeTnR2iTr6qou.is.authenticated=true; _gid=GA1.2.1836961310.1695742704; _hjSession_1425107=eyJpZCI6ImIyYmQxYjQwLTg0NWItNDgyMy05ZGQ2LTFhZDBlYmU3ZTJiNyIsImNyZWF0ZWQiOjE2OTU3NDI3MDg2NTgsImluU2FtcGxlIjp0cnVlLCJzZXNzaW9uaXplckJldGFFbmFibGVkIjpmYWxzZX0=; ln_or=eyI0NzM5NDYiOiJkIn0=; _ga=GA1.2.658618689.1694372356; analytics_session_id=1695748195207; _s=MTY5NTc0ODY3MnxfMTVqZVZxdlRQWTZJc09LRDBPYW5WQ2JsSHB4WWJMMzAyaFd2MktqREJCNjc1c282dV91ZURhWmNfYmpjOVk9fL6DOiZNYsgh1OVYCHr2weOdnvtN0Pu8xkqP0pHkMGXn; _ga_M9YVRZCN8G=GS1.1.1695748195.12.1.1695748692.0.0.0; _ga_MT5MWT6847=GS1.1.1695748195.12.1.1695748693.24.0.0; analytics_session_id.last_access=1695749694248"}
headers = {"cookie":"_s=MTY5NTc1MDk0NnwyNmdVdEVGYThudXdIbkgyNzNhb0NoQkJ0X2ZFME5yMUZSRGlTZDRmTVpxcm8xZ2o0RmNPaHBUN3FxbzlpVEU9fHYsyx0-hPUkxqK0srhVVvMNYnjBuoO5C82CS4kGgvEI; _gcl_au=1.1.351402891.1695750480; _ga_M9YVRZCN8G=GS1.1.1695750482.1.1.1695750918.0.0.0; _ga=GA1.2.204424854.1695750483; _ga_MT5MWT6847=GS1.1.1695750482.1.1.1695750918.59.0.0; _gid=GA1.2.17625442.1695750484; ajs_anonymous_id=17350786-b4a0-473c-8b0e-345eedca260a; _legacy_auth0.M5sT98VT4FUrQNn1p96VeTnR2iTr6qou.is.authenticated=true; auth0.M5sT98VT4FUrQNn1p96VeTnR2iTr6qou.is.authenticated=true; analytics_session_id=1695750594140; analytics_session_id.last_access=1695750941603; ajs_user_id=cus_04ylpB81VvKxQANw; _hjSessionUser_1425107=eyJpZCI6Ijc1N2EwYzM0LWRhOTItNTk3OC05NDc5LTYzZTAwNTZjZmVlMiIsImNyZWF0ZWQiOjE2OTU3NTA1OTY1OTEsImV4aXN0aW5nIjp0cnVlfQ==; _hjFirstSeen=1; _hjIncludedInSessionSample_1425107=1; _hjSession_1425107=eyJpZCI6IjIxYTM1MmMxLTg3MjctNDQ5NC1hZmQzLWE2YjFiMmM4NzgyMyIsImNyZWF0ZWQiOjE2OTU3NTA1OTY1OTQsImluU2FtcGxlIjp0cnVlLCJzZXNzaW9uaXplckJldGFFbmFibGVkIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; _hjHasCachedUserAttributes=true; _hjUserAttributesHash=b738f34fdc478bd6cbabb86b53d5bafa; ln_or=eyI0NzM5NDYiOiJkIn0%3D"}

cookies = {
		"_ga": "GA1.2.204424854.1695750483",
		"_ga_M9YVRZCN8G": "GS1.1.1695750482.1.1.1695750701.0.0.0",
		"_ga_MT5MWT6847": "GS1.1.1695750482.1.1.1695750701.10.0.0",
		"_gcl_au": "1.1.351402891.1695750480",
		"_gid": "GA1.2.17625442.1695750484",
		"_hjAbsoluteSessionInProgress": "0",
		"_hjFirstSeen": "1",
		"_hjHasCachedUserAttributes": "true",
		"_hjIncludedInSessionSample_1425107": "1",
		"_hjSession_1425107": "eyJpZCI6IjIxYTM1MmMxLTg3MjctNDQ5NC1hZmQzLWE2YjFiMmM4NzgyMyIsImNyZWF0ZWQiOjE2OTU3NTA1OTY1OTQsImluU2FtcGxlIjp0cnVlLCJzZXNzaW9uaXplckJldGFFbmFibGVkIjpmYWxzZX0=",
		"_hjSessionUser_1425107": "eyJpZCI6Ijc1N2EwYzM0LWRhOTItNTk3OC05NDc5LTYzZTAwNTZjZmVlMiIsImNyZWF0ZWQiOjE2OTU3NTA1OTY1OTEsImV4aXN0aW5nIjp0cnVlfQ==",
		"_hjUserAttributesHash": "b738f34fdc478bd6cbabb86b53d5bafa",
		"_legacy_auth0.M5sT98VT4FUrQNn1p96VeTnR2iTr6qou.is.authenticated": "true",
		"_s": "MTY5NTc1MDYxNHxYUkZDbE0xUlBnRlhSckx2M3RKZVVKNDBLUkc1Z05NRDhNaFVVMnBlYWtEQXhlLUxqQ1FDSnU4ZEgyeUE2R0E9fKoY7-tRhPBrDMDXBv3-2aGAFch9mW0fhM-6FYaiHyQl",
		"ajs_anonymous_id": "17350786-b4a0-473c-8b0e-345eedca260a",
		"ajs_user_id": "cus_04ylpB81VvKxQANw",
		"analytics_session_id": "1695750594140",
		"analytics_session_id.last_access": "1695750700679",
		"auth0.M5sT98VT4FUrQNn1p96VeTnR2iTr6qou.is.authenticated": "true",
		"ln_or": "eyI0NzM5NDYiOiJkIn0="
	
}
cookies = {
		"_ga": "GA1.2.204424854.1695750483",
		"_ga_M9YVRZCN8G": "GS1.1.1695750482.1.1.1695750918.0.0.0",
		"_ga_MT5MWT6847": "GS1.1.1695750482.1.1.1695750918.59.0.0",
		"_gcl_au": "1.1.351402891.1695750480",
		"_gid": "GA1.2.17625442.1695750484",
		"_hjAbsoluteSessionInProgress": "0",
		"_hjFirstSeen": "1",
		"_hjIncludedInSessionSample_1425107": "1",
		"_hjSession_1425107": "eyJpZCI6IjIxYTM1MmMxLTg3MjctNDQ5NC1hZmQzLWE2YjFiMmM4NzgyMyIsImNyZWF0ZWQiOjE2OTU3NTA1OTY1OTQsImluU2FtcGxlIjp0cnVlLCJzZXNzaW9uaXplckJldGFFbmFibGVkIjpmYWxzZX0=",
		"_hjSessionUser_1425107": "eyJpZCI6Ijc1N2EwYzM0LWRhOTItNTk3OC05NDc5LTYzZTAwNTZjZmVlMiIsImNyZWF0ZWQiOjE2OTU3NTA1OTY1OTEsImV4aXN0aW5nIjp0cnVlfQ==",
		"_s": "MTY5NTc1MjAyMXxTMmlYdml0YzNwX3pXTWg1SVdIQ3MtQklXblNkM3NadWxxd2dmRHktTlNJeFdka0xxTE5KUVBsVTdIbUtmSWs9fA8FxLFgW6BsGXhmh0D7ktiUBarqhBjecEo7ypV-ufot",
		"ajs_anonymous_id": "17350786-b4a0-473c-8b0e-345eedca260a",
		"ajs_user_id": "cus_04ylpB81VvKxQANw",
		"analytics_session_id": "1695750594140",
		"analytics_session_id.last_access": "1695750941603"
	
}
# data=payload
# res = requests.get(url_to_workbench,cookies=cookies)
# url_to_workbench2 = "https://studio.glassnode.com/workbench/aeaa60d3-f651-4cb6-7a9f-47f67c6374f8"
# res2 = requests.get(url_to_workbench2)
key = "e25c8690-3887-4c16-aff8-672f7ae19ab1"
payload = {"description":"","items":[{"configType":"metric","extra":{"ref":1,"name":"BTC: Price","scale":"log","yAxis":0,"lineColor":"#87999f"},"meta":{"asset":"BTC","currency":"native","metricCode":"market.PriceUsdClose"},"uuid":"e25c8690-3887-4c16-aff8-672f7ae19ab1"}],"name":"oppp6"}
payload = {"description":"","items":[{"configType":"metric","extra":{"ref":1,"name":"BTC: Price","scale":"log","yAxis":0,"lineColor":"#87999f"},"meta":{"asset":"BTC","currency":"native","metricCode":"market.PriceUsdClose"},"uuid":"9f5243bb-3c12-4568-9142-c24ce2487923"}],"name":"opp"}
navaneet_workbench_id2 = "2ae5e9d6-a4e5-40eb-6ba3-86fee0a5d503"
navaneet_workbench_id3 = "9f5243bb-3c12-4568-9142-c24ce2487923"


# payload = {"items":[{"configType":"metric","extra":{"lineColor":"#87999f","name":"BTC: Price","ref":1,"scale":"log","yAxis":0},"meta":{"asset":"BTC","currency":"native","metricCode":"market.PriceUsdClose"},"uuid":"d9ee9655-64a0-4407-b8c7-6d787610a506"}],"name":"hutes6"}
# headers = {"Cookie":"_s=MTY5NTc1MjAyMXxTMmlYdml0YzNwX3pXTWg1SVdIQ3MtQklXblNkM3NadWxxd2dmRHktTlNJeFdka0xxTE5KUVBsVTdIbUtmSWs9fA8FxLFgW6BsGXhmh0D7ktiUBarqhBjecEo7ypV-ufot; _gcl_au=1.1.351402891.1695750480; _ga_M9YVRZCN8G=GS1.1.1695750482.1.1.1695750918.0.0.0; _ga=GA1.2.204424854.1695750483; _ga_MT5MWT6847=GS1.1.1695750482.1.1.1695750918.59.0.0; _gid=GA1.2.17625442.1695750484; ajs_anonymous_id=17350786-b4a0-473c-8b0e-345eedca260a; analytics_session_id=1695750594140; analytics_session_id.last_access=1695750941603; ajs_user_id=cus_04ylpB81VvKxQANw; _hjSessionUser_1425107=eyJpZCI6Ijc1N2EwYzM0LWRhOTItNTk3OC05NDc5LTYzZTAwNTZjZmVlMiIsImNyZWF0ZWQiOjE2OTU3NTA1OTY1OTEsImV4aXN0aW5nIjp0cnVlfQ==; _hjFirstSeen=1; _hjIncludedInSessionSample_1425107=1; _hjSession_1425107=eyJpZCI6IjIxYTM1MmMxLTg3MjctNDQ5NC1hZmQzLWE2YjFiMmM4NzgyMyIsImNyZWF0ZWQiOjE2OTU3NTA1OTY1OTQsImluU2FtcGxlIjp0cnVlLCJzZXNzaW9uaXplckJldGFFbmFibGVkIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0"}
headers = {"Cookie":"_s=MTY5NTc2Mjk0OHxhemZ5V0g3YjR4SlJQOVQwZHJvM3hYeTJPSVlzU0cyT2NtN3loaDBYNzc2UVF6WFF5WEY1TkFXb2t0c0dOd2c9fFkK7E5PF9UzBuEP0K-oXaqQtD7sBUWK1H-EENi74lsg; _gcl_au=1.1.351402891.1695750480; _ga_M9YVRZCN8G=GS1.1.1695762933.3.0.1695762933.0.0.0; _ga=GA1.2.204424854.1695750483; _ga_MT5MWT6847=GS1.1.1695762933.3.0.1695762933.60.0.0; _gid=GA1.2.17625442.1695750484; ajs_anonymous_id=17350786-b4a0-473c-8b0e-345eedca260a; analytics_session_id=1695762917305; analytics_session_id.last_access=1695762948773; ajs_user_id=cus_04ylpB81VvKxQANw; _hjSessionUser_1425107=eyJpZCI6Ijc1N2EwYzM0LWRhOTItNTk3OC05NDc5LTYzZTAwNTZjZmVlMiIsImNyZWF0ZWQiOjE2OTU3NTA1OTY1OTEsImV4aXN0aW5nIjp0cnVlfQ==; _hjSession_1425107=eyJpZCI6ImJhYzkyNDNkLTc4YzAtNDNkMy1iNDQ4LWFiMjQyNDFiNjdkMiIsImNyZWF0ZWQiOjE2OTU3NjI5MTI2MDEsImluU2FtcGxlIjp0cnVlLCJzZXNzaW9uaXplckJldGFFbmFibGVkIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=1"}
cookies={
	
		"_ga": "GA1.2.204424854.1695750483",
		"_ga_M9YVRZCN8G": "GS1.1.1695762933.3.0.1695762933.0.0.0",
		"_ga_MT5MWT6847": "GS1.1.1695762933.3.0.1695762933.60.0.0",
		"_gcl_au": "1.1.351402891.1695750480",
		"_gid": "GA1.2.17625442.1695750484",
		"_hjAbsoluteSessionInProgress": "1",
		"_hjSession_1425107": "eyJpZCI6ImJhYzkyNDNkLTc4YzAtNDNkMy1iNDQ4LWFiMjQyNDFiNjdkMiIsImNyZWF0ZWQiOjE2OTU3NjI5MTI2MDEsImluU2FtcGxlIjp0cnVlLCJzZXNzaW9uaXplckJldGFFbmFibGVkIjpmYWxzZX0=",
		"_hjSessionUser_1425107": "eyJpZCI6Ijc1N2EwYzM0LWRhOTItNTk3OC05NDc5LTYzZTAwNTZjZmVlMiIsImNyZWF0ZWQiOjE2OTU3NTA1OTY1OTEsImV4aXN0aW5nIjp0cnVlfQ==",
		"_s": "MTY5NTc2Mjk0OHxhemZ5V0g3YjR4SlJQOVQwZHJvM3hYeTJPSVlzU0cyT2NtN3loaDBYNzc2UVF6WFF5WEY1TkFXb2t0c0dOd2c9fFkK7E5PF9UzBuEP0K-oXaqQtD7sBUWK1H-EENi74lsg",
		"ajs_anonymous_id": "17350786-b4a0-473c-8b0e-345eedca260a",
		"ajs_user_id": "cus_04ylpB81VvKxQANw",
		"analytics_session_id": "1695762917305",
		"analytics_session_id.last_access": "1695762948773"
	
}
cookies = {
		"__cuid": "1cc8489544c6474e9b20eda9548bf64e",
		"_ga": "GA1.2.204424854.1695750483",
		"_ga_M9YVRZCN8G": "GS1.1.1695791898.4.1.1695792201.0.0.0",
		"_ga_MT5MWT6847": "GS1.1.1695791898.4.1.1695792201.59.0.0",
		"_ga_YYWW6JR31S": "GS1.1.1695763879.1.0.1695764213.0.0.0",
		"_gcl_au": "1.1.351402891.1695750480",
		"_gid": "GA1.2.17625442.1695750484",
		"_hjAbsoluteSessionInProgress": "1",
		"_hjIncludedInSessionSample_1425107": "1",
		"_hjSession_1425107": "eyJpZCI6IjA0MjE5NDQzLTg1YWUtNDA4NS1iZjMwLTYxNGY5Yzk1MWNmYSIsImNyZWF0ZWQiOjE2OTU3OTE5MDM4MjEsImluU2FtcGxlIjp0cnVlLCJzZXNzaW9uaXplckJldGFFbmFibGVkIjpmYWxzZX0=",
		"_hjSessionUser_1425107": "eyJpZCI6Ijc1N2EwYzM0LWRhOTItNTk3OC05NDc5LTYzZTAwNTZjZmVlMiIsImNyZWF0ZWQiOjE2OTU3NTA1OTY1OTEsImV4aXN0aW5nIjp0cnVlfQ==",
		"_s": "MTY5NTc5MjIxMnw5a3lBWGJ2NnRTTEw0bEZtYlktT2hFQ3FTN3NHRFU0N1dNdTcyQlZwOGFrSGRYNmx1X1kxSFdHVDJmMnJZa0E9fKQUXUSRehnybT38UfC6Jp3gmli1OOvAxY7hKX1dvkY-",
		"ajs_anonymous_id": "17350786-b4a0-473c-8b0e-345eedca260a",
		"ajs_user_id": "cus_04ylpB81VvKxQANw",
		"amp_fef1e8": "d63fa0e6-8ffa-45d0-a4fe-0de39a4e5763R...1hb9melen.1hb9melet.1.0.1",
		"analytics_session_id": "1695791902053",
		"analytics_session_id.last_access": "1695792213900"
	
}
cookies = {
		"ajs_user_id": "cus_DklWaeBODxJ24P7Y"
	
}
headers = {"Cookie":"_gcl_au=1.1.351402891.1695750480; _ga_M9YVRZCN8G=GS1.1.1695791898.4.1.1695792201.0.0.0; _ga=GA1.2.204424854.1695750483; _ga_MT5MWT6847=GS1.1.1695791898.4.1.1695792201.59.0.0; _gid=GA1.2.17625442.1695750484; ajs_anonymous_id=17350786-b4a0-473c-8b0e-345eedca260a; analytics_session_id=1695791902053; analytics_session_id.last_access=1695792213900; ajs_user_id=cus_04ylpB81VvKxQANw; _hjSessionUser_1425107=eyJpZCI6Ijc1N2EwYzM0LWRhOTItNTk3OC05NDc5LTYzZTAwNTZjZmVlMiIsImNyZWF0ZWQiOjE2OTU3NTA1OTY1OTEsImV4aXN0aW5nIjp0cnVlfQ==; _ga_YYWW6JR31S=GS1.1.1695763879.1.0.1695764213.0.0.0; amp_fef1e8=d63fa0e6-8ffa-45d0-a4fe-0de39a4e5763R...1hb9melen.1hb9melet.1.0.1; __cuid=1cc8489544c6474e9b20eda9548bf64e; _s=MTY5NTc5MjIxMnw5a3lBWGJ2NnRTTEw0bEZtYlktT2hFQ3FTN3NHRFU0N1dNdTcyQlZwOGFrSGRYNmx1X1kxSFdHVDJmMnJZa0E9fKQUXUSRehnybT38UfC6Jp3gmli1OOvAxY7hKX1dvkY-; _hjSession_1425107=eyJpZCI6IjA0MjE5NDQzLTg1YWUtNDA4NS1iZjMwLTYxNGY5Yzk1MWNmYSIsImNyZWF0ZWQiOjE2OTU3OTE5MDM4MjEsImluU2FtcGxlIjp0cnVlLCJzZXNzaW9uaXplckJldGFFbmFibGVkIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=1; _hjIncludedInSessionSample_1425107=1"}
headers = {
	"Cookie":"_gcl_au=1.1.351402891.1695750480; _ga_M9YVRZCN8G=GS1.1.1695834538.9.1.1695836229.0.0.0; _ga=GA1.1.204424854.1695750483; _ga_MT5MWT6847=GS1.1.1695834538.9.1.1695836230.58.0.0; _gid=GA1.2.17625442.1695750484; ajs_anonymous_id=17350786-b4a0-473c-8b0e-345eedca260a; analytics_session_id=1695834544647; analytics_session_id.last_access=1695836196196; ajs_user_id=cus_04ylpB81VvKxQANw; _hjSessionUser_1425107=eyJpZCI6Ijc1N2EwYzM0LWRhOTItNTk3OC05NDc5LTYzZTAwNTZjZmVlMiIsImNyZWF0ZWQiOjE2OTU3NTA1OTY1OTEsImV4aXN0aW5nIjp0cnVlfQ==; _ga_YYWW6JR31S=GS1.1.1695763879.1.0.1695764213.0.0.0; amp_fef1e8=d63fa0e6-8ffa-45d0-a4fe-0de39a4e5763R...1hb9melen.1hb9melet.1.0.1; __cuid=1cc8489544c6474e9b20eda9548bf64e; _s=MTY5NTgzNjI2NXxJY2Z2LWM0cHB5cDE1Wm9zVW4xQmdqNXZZaVB3YktzbnlLRVU1RHotSi1sT0N6YWd5ZnVEd3JMVlI4YzhOSzQ9fA4PWExvvVMECI-4DFzjnTBkuUb7q18f1fAjK1MwXcMH; _hjSession_1425107=eyJpZCI6IjM5Yzk5YjMwLWQ1ODUtNDllYi04NzE1LTQ4MTcwMWQ5OWU1YSIsImNyZWF0ZWQiOjE2OTU4MzQ1NDgzNTIsImluU2FtcGxlIjp0cnVlLCJzZXNzaW9uaXplckJldGFFbmFibGVkIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0"
}
url_to_workbench4 = "https://api.glassnode.com/v1/udm/c66acc99-268a-49b0-5d97-4b1489ce2685?"
payload2 = {"timestamp":"2023-09-27T05:53:01.834Z","integrations":{"Actions Amplitude":{"session_id":1695791902053}},"userId":"cus_04ylpB81VvKxQANw","anonymousId":"17350786-b4a0-473c-8b0e-345eedca260a","event":"Workbench Updated","type":"track","properties":{"name":"p56","uuid":"2ae5e9d6-a4e5-40eb-6ba3-86fee0a5d503"},"context":{"page":{"path":"/workbench/2ae5e9d6-a4e5-40eb-6ba3-86fee0a5d503","referrer":"","search":"","title":"Glassnode Studio - On-Chain Market Intelligence","url":"https://studio.glassnode.com/workbench/2ae5e9d6-a4e5-40eb-6ba3-86fee0a5d503?"},"userAgent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/117.0","locale":"en-US","library":{"name":"analytics.js","version":"next-1.55.0"}},"messageId":"ajs-next-5eed66cd379bc520508f5782fc90cc15","writeKey":"npuIBmJlhWHVAzEprvuac51oGJFMJAr9","sentAt":"2023-09-27T05:53:03.193Z","_metadata":{"bundled":["Chameleon","Hotjar","LinkedIn Insight Tag","ProfitWell","Segment.io"],"unbundled":[],"bundledIds":["62f13aeb4be02d4098692616","6360d613e316f787f2b85f9e","64020c0c54ac58d5ec5c355f","62bc673a764c6a2bed67e0a1"]}}
url_clone = "https://events.eu1.segmentapis.com/v1/t"
url_clone2 = "https://fast.chameleon.io/observe/batches"
url_clone3 = "https://fast.chameleon.io/observe/v2/profiles/2ae5e9d6-a4e5-40eb-6ba3-86fee0a5d503"
payload3= {"events":[{"name":"Workbench Updated","uuid":"2ae5e9d6-a4e5-40eb-6ba3-86fee0a5d503","_id":"6513c4cab921baab2999cf58","library":"chmln","revision":"v9","kind":"event","url_group_id":"62c6ed5eb9bd960900000000"}],"_mode":"user","_account_id":"62c6ed5ef7956500111dbbb4","_profile_id":"64fe14306d8f1d002ed73222"}
probe_url ="https://fast.chameleon.io/v3/edit/profiles/forget?email=dtechnoguy.navneet@gmail.com"
# probe_url2 = "https://fast.chameleon.io/observe/v2/profiles/64fe14306d8f1d002ed73222"

with open("../v1_uuids.txt","r") as fl:
	# headers = {"Cookie":"_gcl_au=1.1.351402891.1695750480; _ga_M9YVRZCN8G=GS1.1.1695983538.11.1.1695984753.0.0.0; _ga=GA1.2.204424854.1695750483; _ga_MT5MWT6847=GS1.1.1695983538.11.1.1695984753.59.0.0; ajs_anonymous_id=17350786-b4a0-473c-8b0e-345eedca260a; analytics_session_id=1696001403350; analytics_session_id.last_access=1696001403350; ajs_user_id=cus_04ylpB81VvKxQANw; _hjSessionUser_1425107=eyJpZCI6Ijc1N2EwYzM0LWRhOTItNTk3OC05NDc5LTYzZTAwNTZjZmVlMiIsImNyZWF0ZWQiOjE2OTU3NTA1OTY1OTEsImV4aXN0aW5nIjp0cnVlfQ==; _ga_YYWW6JR31S=GS1.1.1695763879.1.0.1695764213.0.0.0; amp_fef1e8=d63fa0e6-8ffa-45d0-a4fe-0de39a4e5763R...1hb9melen.1hb9melet.1.0.1; __cuid=1cc8489544c6474e9b20eda9548bf64e; _s=MTY5NTk4NDc5NXxqOTM0LVBQVHFZNFJYYVhCMjVuY0d0WGFXLTM4OWpzandfV21mUnJUVFJQRHBEeXR0NjZGTnVNeER4UHRCRFU9fK8USpiyEIeqJ7w7H6caxCFU7uzQXtN-oD9wqSL1jHoA; _gid=GA1.2.331329626.1695983539; ln_or=eyI0NzM5NDYiOiJkIn0%3D; _hjIncludedInSessionSample_1425107=1; _hjUserAttributesHash=420faa1fd6ca14d278fb29ba6a1d4575; _legacy_auth0.M5sT98VT4FUrQNn1p96VeTnR2iTr6qou.is.authenticated=true; auth0.M5sT98VT4FUrQNn1p96VeTnR2iTr6qou.is.authenticated=true; _hjSession_1425107=eyJpZCI6ImU0NGNjYTcxLTMzNGUtNDRjYy05MmI5LWRmMTZiYTFiMjgwNiIsImNyZWF0ZWQiOjE2OTYwMDEzOTM2OTgsImluU2FtcGxlIjp0cnVlLCJzZXNzaW9uaXplckJldGFFbmFibGVkIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0"}
	co = 0
	# headers = {"Cookie":"_gcl_au=1.1.351402891.1695750480; _ga_M9YVRZCN8G=GS1.1.1696003442.13.1.1696003714.0.0.0; _ga=GA1.2.204424854.1695750483; _ga_MT5MWT6847=GS1.1.1696003443.13.1.1696003714.60.0.0; ajs_anonymous_id=17350786-b4a0-473c-8b0e-345eedca260a; analytics_session_id=1696003504362; analytics_session_id.last_access=1696003509028; ajs_user_id=cus_04ylpB81VvKxQANw; _hjSessionUser_1425107=eyJpZCI6Ijc1N2EwYzM0LWRhOTItNTk3OC05NDc5LTYzZTAwNTZjZmVlMiIsImNyZWF0ZWQiOjE2OTU3NTA1OTY1OTEsImV4aXN0aW5nIjp0cnVlfQ==; _ga_YYWW6JR31S=GS1.1.1695763879.1.0.1695764213.0.0.0; amp_fef1e8=d63fa0e6-8ffa-45d0-a4fe-0de39a4e5763R...1hb9melen.1hb9melet.1.0.1; __cuid=1cc8489544c6474e9b20eda9548bf64e; _s=MTY5NjAwMzcyMXxiZmp2b0RsbTIxNjFETTJSM2FMRzdnVFFaLUJjOUJ5cUtTdGZtb2Z2VHZiaXozTWRlX081TTRTM0NEenVQNnM9fLA6w_fZYgNaO8psCfKo4VP2JTSoM0IKh4ppBsbCK3gO; _gid=GA1.2.331329626.1695983539; ln_or=eyI0NzM5NDYiOiJkIn0%3D; _hjIncludedInSessionSample_1425107=1; _hjUserAttributesHash=420faa1fd6ca14d278fb29ba6a1d4575; _legacy_auth0.M5sT98VT4FUrQNn1p96VeTnR2iTr6qou.is.authenticated=true; auth0.M5sT98VT4FUrQNn1p96VeTnR2iTr6qou.is.authenticated=true; _hjSession_1425107=eyJpZCI6ImU0NGNjYTcxLTMzNGUtNDRjYy05MmI5LWRmMTZiYTFiMjgwNiIsImNyZWF0ZWQiOjE2OTYwMDEzOTM2OTgsImluU2FtcGxlIjp0cnVlLCJzZXNzaW9uaXplckJldGFFbmFibGVkIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; _hjHasCachedUserAttributes=true; _gat_UA-129287447-1=1"}
	# headers = {"Cookie":"_gcl_au=1.1.389967978.1694372349; ajs_anonymous_id=0a76beee-c3ca-47c6-9eb3-97064666c18c; _hjSessionUser_1425107=eyJpZCI6IjAzODcxZjIxLTVmNmItNTkyNS04Nzg1LTIxNjE1MmZiNmQyMiIsImNyZWF0ZWQiOjE2OTQzNzIzNjg0MTEsImV4aXN0aW5nIjp0cnVlfQ==; ajs_user_id=cus_04ylpB81VvKxQANw; _ga_L7S640PB78=GS1.1.1694419669.2.0.1694419669.60.0.0; _ga_WKCPXFMMLV=GS1.1.1694419672.2.1.1694420578.0.0.0; _hjSessionUser_3114558=eyJpZCI6ImRlMjExMjQwLTkxMjEtNWFhYS04YWIxLTM1MzJjNjQ2ZjAxNSIsImNyZWF0ZWQiOjE2OTQzNzM2NDIyMTksImV4aXN0aW5nIjp0cnVlfQ==; _ga_8MGXPNL6MF=GS1.1.1695742598.4.1.1695742653.5.0.0; __cuid=b1ba78e6329d4959bf509aa89182b1ce; amp_fef1e8=8bca9985-84ab-4095-9db6-a89644dbf4bbR...1hbbrmn8u.1hbbrunih.1i.f.21; _ga_YYWW6JR31S=GS1.1.1695843212.8.1.1695843213.0.0.0; _gid=GA1.2.2064275538.1696025502; analytics_session_id=1696025503772; _hjIncludedInSessionSample_1425107=1; _hjSession_1425107=eyJpZCI6IjI4ZjNhNGUzLTQ3MTMtNGJhNS04ZmEwLTY1ZGIyZmZlMTc1MyIsImNyZWF0ZWQiOjE2OTYwMjU1MDQ0MzMsImluU2FtcGxlIjp0cnVlLCJzZXNzaW9uaXplckJldGFFbmFibGVkIjpmYWxzZX0=; _ga=GA1.2.658618689.1694372356; _gat_UA-129287447-1=1; _ga_M9YVRZCN8G=GS1.1.1696025502.16.1.1696025604.0.0.0; _ga_MT5MWT6847=GS1.1.1696025502.16.1.1696025604.29.0.0; _s=MTY5NjAyNTYwNnxCMy0weDZkYW1xa2VHUmJOQlFsc2ZVdU9GWkxWdDZ6T2p4NHZncVNueTEwZlNqX1dpYmlQQjV1VVNia1dBY0E9fD0Ny1MI7lGVRs1I1hwb2yAbJy3Bb7IO_vD_fSnXNpVL; analytics_session_id.last_access=1696025610296"}
	headers = {"Cookie":"_gcl_au=1.1.389967978.1694372349; ajs_anonymous_id=0a76beee-c3ca-47c6-9eb3-97064666c18c; _hjSessionUser_1425107=eyJpZCI6IjAzODcxZjIxLTVmNmItNTkyNS04Nzg1LTIxNjE1MmZiNmQyMiIsImNyZWF0ZWQiOjE2OTQzNzIzNjg0MTEsImV4aXN0aW5nIjp0cnVlfQ==; ajs_user_id=cus_04ylpB81VvKxQANw; _ga_L7S640PB78=GS1.1.1694419669.2.0.1694419669.60.0.0; _ga_WKCPXFMMLV=GS1.1.1694419672.2.1.1694420578.0.0.0; _hjSessionUser_3114558=eyJpZCI6ImRlMjExMjQwLTkxMjEtNWFhYS04YWIxLTM1MzJjNjQ2ZjAxNSIsImNyZWF0ZWQiOjE2OTQzNzM2NDIyMTksImV4aXN0aW5nIjp0cnVlfQ==; _ga_8MGXPNL6MF=GS1.1.1695742598.4.1.1695742653.5.0.0; __cuid=b1ba78e6329d4959bf509aa89182b1ce; amp_fef1e8=8bca9985-84ab-4095-9db6-a89644dbf4bbR...1hbbrmn8u.1hbbrunih.1i.f.21; _ga_YYWW6JR31S=GS1.1.1695843212.8.1.1695843213.0.0.0; _gid=GA1.2.2112573371.1696517610; _gat_UA-129287447-1=1; _ga=GA1.2.658618689.1694372356; analytics_session_id=1696517623550; _hjIncludedInSessionSample_1425107=1; _hjSession_1425107=eyJpZCI6ImU2YTdiMjY2LWZlNGItNGE0MS1hMTMwLWE2NThkM2Q1ZjA0OCIsImNyZWF0ZWQiOjE2OTY1MTc2MjQwMjMsImluU2FtcGxlIjp0cnVlLCJzZXNzaW9uaXplckJldGFFbmFibGVkIjpmYWxzZX0=; _s=MTY5NjUxNzY0NnxQNVZQak9PTG16NDBzS0FtcEkteEVqT0pzX24yRkVjVDNyb1B6WE9WazRpZ0o5cThjUERqbVRMQzNGMkYzdTQ9fA9UU3BoFeZ6RSlmY7OMLmQgR7A_mf3GiuvGMX_vhQWH; _ga_M9YVRZCN8G=GS1.1.1696517610.30.1.1696517653.0.0.0; _ga_MT5MWT6847=GS1.1.1696517610.30.1.1696517653.17.0.0; analytics_session_id.last_access=1696517654056"}
	import time 
	t1 = time.time()

	with open("results_v4_variant0_2.txt","a+") as fl2 :
		for txt in fl.readlines():
			if 1:
				url_to_workbench3 = "https://api.glassnode.com/v1/udm/{}".format(txt)
				print("sample_generated url  {} :".format(co),url_to_workbench3)
				res = requests.get(url_to_workbench3,headers=headers)
				# res = requests.get(url_to_workbench3,cookies=cookies,headers=headers)
				#params={ 'api_key':"M5sT98VT4FUrQNn1p96VeTnR2iTr6qou"}
				# convert to pandas dataframe
				print(res,res.text)
				fl2.write("sample_generated url  {} : ".format(co)+url_to_workbench3  +" "+res.text)


			co+=1
			# print((co)/(time.time()-t1))
			# import json 

# with open("demo6.json","w") as fl:
#     fl.write(res.text)
# # df = pd.read_json(res.text, convert_dates=['t'])
