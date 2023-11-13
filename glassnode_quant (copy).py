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
headers = {"cookie":"_gcl_au=1.1.389967978.1694372349; _gid=GA1.2.960455209.1694372356; ajs_anonymous_id=0a76beee-c3ca-47c6-9eb3-97064666c18c; _hjSessionUser_1425107=eyJpZCI6IjAzODcxZjIxLTVmNmItNTkyNS04Nzg1LTIxNjE1MmZiNmQyMiIsImNyZWF0ZWQiOjE2OTQzNzIzNjg0MTEsImV4aXN0aW5nIjp0cnVlfQ==; ajs_user_id=cus_04ylpB81VvKxQANw; _hjSessionUser_3114558=eyJpZCI6ImRlMjExMjQwLTkxMjEtNWFhYS04YWIxLTM1MzJjNjQ2ZjAxNSIsImNyZWF0ZWQiOjE2OTQzNzM2NDIyMTksImV4aXN0aW5nIjpmYWxzZX0=; _ga_8MGXPNL6MF=GS1.1.1694373641.1.0.1694373659.42.0.0; __cuid=b1ba78e6329d4959bf509aa89182b1ce; amp_fef1e8=8bca9985-84ab-4095-9db6-a89644dbf4bbR...1ha0en2du.1ha0fpjn5.h.4.l; _ga_L7S640PB78=GS1.1.1694419669.2.0.1694419669.60.0.0; _ga_YYWW6JR31S=GS1.1.1694418712.4.1.1694420558.0.0.0; _ga_WKCPXFMMLV=GS1.1.1694419672.2.1.1694420578.0.0.0; analytics_session_id=1694502280414; _hjIncludedInSessionSample_1425107=1; _hjSession_1425107=eyJpZCI6IjliZjQ5Zjc5LTM5MWQtNDRiMC04NWY3LTM4ZDg0ZmY0MjM1YiIsImNyZWF0ZWQiOjE2OTQ1MDIyODA3NjMsImluU2FtcGxlIjp0cnVlfQ==; _gat_UA-129287447-1=1; _ga=GA1.1.658618689.1694372356; _ga_M9YVRZCN8G=GS1.1.1694502265.3.1.1694502807.0.0.0; _ga_MT5MWT6847=GS1.1.1694502265.3.1.1694502807.59.0.0; _s=MTY5NDUwMjgxMnxEWUxKcWtSY2dDZEpWZm1PYl9XdTZZOHJpdjhFYkNSdzJMeHpIaHNnc2F0MlptYVByNEZmbEdMMHo3WFBZX0U9fLVzSlSKd0S9awDveMBJ4eXud-WT94NaWKAb-_v64exp; analytics_session_id.last_access=1694502815490"}
# headers = {"X-Api-Key":quant_var['uuid']}
# url = "https://api.glassnode.com/v1/metrics/indicators/sopr?a=btc"
# url = "https://api.glassnode.com"
# url = "https://cms.glassnode.com/api/metrics/derivatives.FuturesAnnualizedBasis3M?populate=*"
# url = "https://api.glassnode.com/v1/metrics/derivatives/options_open_interest_put_call_ratio"
# url = "https://api.glassnode.com/v1/metrics/derivatives/options_open_interest_put_call_ratio?a=BTC&c=native&e=aggregated&i=24h&referer=charts"
# url = "https://api.glassnode.com/v1/metrics/derivatives/futures_annualized_basis_3m?a=BTC&c=native&e=aggregated&i=24h"
# url = "https://cms.glassnode.com/api/metrics?fields[0]=group&fields[1]=metricCode&fields[2]=path&fields[3]=shortName&fields[4]=tier&fields[5]=isNew&fields[6]=resolutions&pagination[page]=3"
# url = "https://api.glassnode.com/v1/metrics/derivatives/futures_funding_rate_perpetual?a=BTC&c=native&e=aggregated&i=24h&referer=charts"
# url = "https://api.glassnode.com/v1/metrics/addresses/active_count?a=BTC&c=native&i=24h&referer=charts"
# url = "https://api.glassnode.com/v1/metrics/supply/supply_by_txout_type?a=BTC&c=native&i=24h&referer=charts"
# url = "https://cms.glassnode.com/api/metrics?fields[0]=group&fields[1]=metricCode&fields[2]=path&fields[3]=shortName&fields[4]=tier&fields[5]=isNew&fields[6]=resolutions"
# url = "https://cms.glassnode.com/api/metrics/derivatives.Options25DeltaSkew1Week?populate=*"
url = "https://api.glassnode.com/v1/metrics/supply/provably_lost?a=BTC&c=native&i=24h&referer=charts"
# url = "https://api.glassnode.com/v1/metrics/derivatives/futures_open_interest_latest?a=BTC&c=usd&i=24h&referer=charts"
# url = "https://api.glassnode.com/v2/metrics/endpoints"
res = requests.get(url,headers=headers)
#params={ 'api_key':"M5sT98VT4FUrQNn1p96VeTnR2iTr6qou"}
# convert to pandas dataframe
print(res.text)
import json 

with open("demo6.json","w") as fl:
    fl.write(res.text)
# df = pd.read_json(res.text, convert_dates=['t'])