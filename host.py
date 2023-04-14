import requests

cookies = {
    '_ga': 'GA1.1.1681851052.1681481731',
    '__cf_bm': 'e1o7Msdm6NdnnoWl86psYp8dJJuv9ydlAcb4awU6.cc-1681481730-0-AbPSduf0MhbesIdtFWxEQlqA6cs2BYiYKuyRuz7/M2ZSQYTOB5b39WJKgJbwNrv02Djzii8wzypbvEAm5QzuCh6cCXDydVxxenlhTt/hp/SVO4vpxKx5d5JvWDrbT5y9jg==',
    '_ga_XCLTX4ZEX8': 'GS1.1.1681481730.1.1.1681481933.49.0.0',
}

headers = {
    'authority': 'www.phind.com',
    'accept': '*/*',
    'accept-language': 'nl-NL,nl;q=0.9,en;q=0.8',
    'baggage': 'sentry-environment=vercel-production,sentry-release=e9fcff83a52fa198e6ad6db45aa829378e1f2897,sentry-transaction=%2Fsearch,sentry-public_key=ea29c13458134fd3bc88a8bb4ba668cb,sentry-trace_id=d97162e1100e45d6a7ae486fff17220f,sentry-sample_rate=0.002',
    'content-type': 'application/json',
    # 'cookie': '_ga=GA1.1.1681851052.1681481731; __cf_bm=e1o7Msdm6NdnnoWl86psYp8dJJuv9ydlAcb4awU6.cc-1681481730-0-AbPSduf0MhbesIdtFWxEQlqA6cs2BYiYKuyRuz7/M2ZSQYTOB5b39WJKgJbwNrv02Djzii8wzypbvEAm5QzuCh6cCXDydVxxenlhTt/hp/SVO4vpxKx5d5JvWDrbT5y9jg==; _ga_XCLTX4ZEX8=GS1.1.1681481730.1.1.1681481933.49.0.0',
    'dnt': '1',
    'origin': 'https://www.phind.com',
    'referer': 'https://www.phind.com/search?q=what+is+the+time&c=&source=searchbox&init=true',
    'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sentry-trace': 'd97162e1100e45d6a7ae486fff17220f-bf6fd9c592b18ae0-0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
}

json_data = {
    'question': 'what is the time',
    'bingResults': {
        '_type': 'SearchResponse',
        'queryContext': {
            'originalQuery': 'what is the time',
        },
        'webPages': {
            'webSearchUrl': 'https://www.bing.com/search?q=what+is+the+time',
            'totalEstimatedMatches': 883000000,
            'value': [
                {
                    'id': 'https://api.bing.microsoft.com/api/v7/#WebPages.0',
                    'name': 'Time.is - exact time, any time zone',
                    'url': 'https://time.is/',
                    'isFamilyFriendly': True,
                    'displayUrl': 'https://time.is',
                    'snippet': 'Time.is - exact time, any time zone (Forbidden) Time in New York, United States now: 06:06:38am.',
                    'deepLinks': [
                        {
                            'name': 'Calendar',
                            'url': 'https://time.is/calendar',
                            'snippet': "From 5 November 2023: UTC -8 / Pacific Standard Time (PST) The time in Calendar is normally 3 hours behind the time in New York, but because these time zones don't share the same start and end times for daylight saving time, the time in Calendar can for a short while be 2 or 4 hours behind the time in New York.",
                        },
                        {
                            'name': 'Unix Time Converter',
                            'url': 'https://time.is/Unix_time_converter',
                            'snippet': 'Unix Time Converter - Time.is - exact time, any time zone',
                        },
                        {
                            'name': 'GMT',
                            'url': 'https://time.is/GMT',
                            'snippet': 'Greenwich Mean Time can be either 4 or 5 hours ahead of the time in New York, depending on the time of the year. No daylight saving time, same UTC offset all year The IANA time zone identifier for Greenwich Mean Time is GMT.',
                        },
                        {
                            'name': 'Time Zones',
                            'url': 'https://time.is/time_zones',
                            'snippet': "Time zones List of countries grouped by current UTC offset. This page lists all countries of the world, plus major regions and cities, grouped by their current UTC offset. UTC is practically the same as GMT. A UTC offset is the difference in time between UTC time and a location's observed time.",
                        },
                        {
                            'name': 'Bangkok',
                            'url': 'https://time.is/Bangkok',
                            'snippet': 'The time in Bangkok can be either 11 or 12 hours ahead of the time in New York, depending on the time of the year. No daylight saving time, same UTC offset all year The IANA time zone identifier for Bangkok is Asia/Bangkok.',
                        },
                        {
                            'name': 'Berlin',
                            'url': 'https://time.is/Berlin',
                            'snippet': "The time in Berlin is normally 6 hours ahead of the time in New York, but because these time zones don't share the same start and end times for daylight saving time, the time in Berlin can for a short while be 5 hours ahead of the time in New York. The IANA time zone identifier for Berlin is Europe/Berlin.",
                        },
                        {
                            'name': 'How to Use Time.Is',
                            'url': 'https://time.is/howto',
                            'snippet': 'Example: time.is/CA redirects to time.is/California. Countries can be addressed by top-level domain names. Example: If you type time.is/.us, you will be redirected to time.is/United_States. You can use underscores or spaces in URLs. The URLs are case insensitive. Example: If you go to time.is/new york, you will be redirected to time.is/New_York.',
                        },
                        {
                            'name': 'Newsletter',
                            'url': 'https://time.is/mailing_list',
                            'snippet': 'Join the Time.is mailing list to be the first to hear about new features on Time.is. Your email address will not be shared with anyone, and you can unsubscribe at any time. Your email address (will not be shared) 10:34:53 PM. Thursday, April 13, 2023. Sun: ↑ 06:20AM ...',
                        },
                    ],
                    'dateLastCrawled': '2023-04-13T10:28:00.0000000Z',
                    'language': 'en',
                    'isNavigational': True,
                },
                {
                    'id': 'https://api.bing.microsoft.com/api/v7/#WebPages.1',
                    'name': 'Time in the United States - TimeAndDate',
                    'url': 'https://www.timeanddate.com/worldclock/usa',
                    'thumbnailUrl': 'https://www.bing.com/th?id=OIP.LzYi_beq1KaeTUc84GhabQHaEA&w=80&h=80&c=1&pid=5.1',
                    'isFamilyFriendly': True,
                    'displayUrl': 'https://www.timeanddate.com/worldclock/usa',
                    'snippet': 'Current Local Time in the United States Multiple Time Zones See map below for details Time Zones in USA 11:15 pm Honolulu HST UTC -10 1:15 am Anchorage AKDT UTC -8 2:15 am Los Angeles PDT Phoenix MST UTC -7 3:15 am Salt Lake City MDT UTC -6 4:15 am Chicago CDT UTC -5 5:15 am New York EDT UTC -4 See all Time Zones in United States',
                    'dateLastCrawled': '2023-04-13T11:23:00.0000000Z',
                    'language': 'en',
                    'isNavigational': False,
                },
                {
                    'id': 'https://api.bing.microsoft.com/api/v7/#WebPages.2',
                    'name': 'Current Local Time in London, England, United Kingdom - TimeAndDate',
                    'url': 'https://www.timeanddate.com/worldclock/uk/london',
                    'thumbnailUrl': 'https://www.bing.com/th?id=OIP.wet3Evv0MYhrknAQY-btRwHaHa&w=80&h=80&c=1&pid=5.1',
                    'isFamilyFriendly': True,
                    'displayUrl': 'https://www.timeanddate.com/worldclock/uk/london',
                    'snippet': 'Time Zone BST (British Summer Time) UTC/GMT +1 hour DST started Mar 26, 2023 Forward 1 hour DST ends Oct 29, 2023 Back 1 hour Difference 5 hours ahead of Roanoke Rapids About BST — British Summer Time Set your location Sunrise 6:14 am ↑ 76° East Sunset 7:49 pm ↑ 285° West Day length 13 hours, 36 minutes +3m 52s longer Moon 72.0% Rise – 1:40 am',
                    'dateLastCrawled': '2023-04-13T11:13:00.0000000Z',
                    'language': 'en',
                    'isNavigational': False,
                },
                {
                    'id': 'https://api.bing.microsoft.com/api/v7/#WebPages.3',
                    'name': 'Central Time - exact time now',
                    'url': 'https://time.is/CT',
                    'isFamilyFriendly': True,
                    'displayUrl': 'https://time.is/CT',
                    'snippet': 'Central Time - exact time now Central Time now 05:19:50am Tuesday, April 11, 2023 Make Central Time time default - Add to favorite locations Tokyo 07:19pm Beijing 06:19pm Kyiv 01:19pm Paris 12:19pm London 11:19am New York 06:19am Los Angeles 03:19am Time zone: Central Time (CT) UTC -5 now 1 hour behind New York',
                    'dateLastCrawled': '2023-04-13T12:16:00.0000000Z',
                    'language': 'en',
                    'isNavigational': False,
                },
                {
                    'id': 'https://api.bing.microsoft.com/api/v7/#WebPages.4',
                    'name': 'Time in New York, United States now',
                    'url': 'https://time.is/New_York',
                    'thumbnailUrl': 'https://www.bing.com/th?id=OIP.8lQFKEtPb2VFK5bZcqYRhwAAAA&w=80&h=80&c=1&pid=5.1',
                    'isFamilyFriendly': True,
                    'displayUrl': 'https://time.is/New_York',
                    'snippet': 'Time in New York, United States now Time in New York, United States now 12:27:46pm Tuesday, April 11, 2023 Sun: ↑ 06:23AM ↓ 07:31PM (13h 8m) - More info - Make New York time default - Remove from favorite locations Tokyo 01:27am Beijing 12:27am Kyiv 07:27pm Paris 06:27pm London 05:27pm New York 12:27pm Los Angeles 09:27am',
                    'dateLastCrawled': '2023-04-13T18:26:00.0000000Z',
                    'language': 'en',
                    'isNavigational': False,
                },
                {
                    'id': 'https://api.bing.microsoft.com/api/v7/#WebPages.5',
                    'name': 'What Is Time? A Simple Explanation - ThoughtCo',
                    'url': 'https://www.thoughtco.com/what-is-time-4156799',
                    'thumbnailUrl': 'https://www.bing.com/th?id=OIP.lNjY3j9vglRA5I8E2jPqAQHaE8&w=80&h=80&c=1&pid=5.1',
                    'isFamilyFriendly': True,
                    'displayUrl': 'https://www.thoughtco.com/what-is-time-4156799',
                    'snippet': "Time is the progression of events from the past into the future. Time moves only in one direction. It's possible to move forward in time, but not backward. Scientists believe memory formation is the basis for human perception of time. Sources Carter, Rita. The Human Brain Book. Dorling Kindersley Publishing, 2009, London.",
                    'dateLastCrawled': '2023-04-12T23:42:00.0000000Z',
                    'language': 'en',
                    'isNavigational': False,
                },
                {
                    'id': 'https://api.bing.microsoft.com/api/v7/#WebPages.6',
                    'name': 'Time in the United Kingdom - TimeAndDate',
                    'url': 'https://www.timeanddate.com/worldclock/uk',
                    'thumbnailUrl': 'https://www.bing.com/th?id=OIP.QgcODZ4sXjlTvX6At2cSnQHaDa&w=80&h=80&c=1&pid=5.1',
                    'isFamilyFriendly': True,
                    'displayUrl': 'https://www.timeanddate.com/worldclock/uk',
                    'snippet': 'Time Zone in United Kingdom 10:04 am Belfast BST UTC +1 10:04 am Glasgow BST UTC +1 10:04 am Edinburgh BST UTC +1 10:04 am Cardiff BST UTC +1 10:04 am Birmingham BST UTC +1 10:04 am London BST UTC +1 See all Time Zones in United Kingdom See Holidays in United Kingdom Create a Calendar for United Kingdom * Adjusted for Daylight Saving Time',
                    'dateLastCrawled': '2023-04-13T15:43:00.0000000Z',
                    'language': 'en',
                    'isNavigational': False,
                },
                {
                    'id': 'https://api.bing.microsoft.com/api/v7/#WebPages.7',
                    'name': 'What is time? | Live Science',
                    'url': 'https://www.livescience.com/what-is-time',
                    'isFamilyFriendly': True,
                    'displayUrl': 'https://www.livescience.com/what-is-time',
                    'snippet': "Time is the apparent progression of events from past to future. While it's impossible to completely define the nature of time, we all share many common experiences bound by time: Causes lead ...",
                    'dateLastCrawled': '2023-04-13T11:41:00.0000000Z',
                    'language': 'en',
                    'isNavigational': False,
                },
                {
                    'id': 'https://api.bing.microsoft.com/api/v7/#WebPages.8',
                    'name': "Does Time Exist? A Physicist's Perspective - ThoughtCo",
                    'url': 'https://www.thoughtco.com/does-time-really-exist-2699430',
                    'thumbnailUrl': 'https://www.bing.com/th?id=OIP.AB2z5JPva6uOb1HUYuZX8wHaE8&w=80&h=80&c=1&pid=5.1',
                    'isFamilyFriendly': True,
                    'displayUrl': 'https://www.thoughtco.com/does-time-really-exist-2699430',
                    'snippet': 'Time is actually an integral part of the universe. As mentioned earlier, the very linear concept of time is tied into the concept of the Second Law of Thermodynamics, which is seen by many physicists as one of the most important laws in all of physics! Without time as a real property of the universe, the Second Law becomes meaningless.',
                    'dateLastCrawled': '2023-04-13T19:36:00.0000000Z',
                    'language': 'en',
                    'isNavigational': False,
                },
                {
                    'id': 'https://api.bing.microsoft.com/api/v7/#WebPages.9',
                    'name': 'Time Definition & Meaning - Merriam-Webster',
                    'url': 'https://www.merriam-webster.com/dictionary/time',
                    'isFamilyFriendly': True,
                    'displayUrl': 'https://www.merriam-webster.com/dictionary/time',
                    'snippet': '1. a. : the measured or measurable period during which an action, process, or condition exists or continues : duration. b. : a nonspatial continuum that is measured in terms of events which succeed one another from past through present to future. c. : leisure. time for reading.',
                    'dateLastCrawled': '2023-04-13T10:11:00.0000000Z',
                    'language': 'en',
                    'isNavigational': False,
                },
                {
                    'id': 'https://api.bing.microsoft.com/api/v7/#WebPages.10',
                    'name': 'The Time Now: What Time Is It',
                    'url': 'https://www.thetimenow.com/',
                    'isFamilyFriendly': True,
                    'displayUrl': 'https://www.thetimenow.com',
                    'snippet': 'The Time Now is an accurate tool providing multiple time-related services, various in-depth articles, and more. You can find out what the current local time is, in more than a hundred thousand cities around the world, as well as the UTC/GMT offset, the time zone full name and abbreviation.',
                    'dateLastCrawled': '2023-04-13T07:16:00.0000000Z',
                    'language': 'en',
                    'isNavigational': False,
                },
                {
                    'id': 'https://api.bing.microsoft.com/api/v7/#WebPages.11',
                    'name': 'Time in United States now',
                    'url': 'https://time.is/United_States',
                    'isFamilyFriendly': True,
                    'displayUrl': 'https://time.is/United_States',
                    'snippet': 'United States (incl. dependent territories) has 11 time zones. The time zone for the capital Washington, D.C. is used here. Sun: ↑ 06:34AM ↓ 07:43PM (13h 9m) - More info - Make United States time default - Add to favorite locations',
                    'dateLastCrawled': '2023-04-13T14:36:00.0000000Z',
                    'language': 'en',
                    'isNavigational': False,
                },
                {
                    'id': 'https://api.bing.microsoft.com/api/v7/#WebPages.12',
                    'name': 'expressions - "What time is it" versus "what is the time" - English ...',
                    'url': 'https://ell.stackexchange.com/questions/48175/what-time-is-it-versus-what-is-the-time',
                    'isFamilyFriendly': True,
                    'displayUrl': 'https://ell.stackexchange.com/questions/48175/what-time-is-it-versus-what-is-the-time',
                    'snippet': '"What\'s the time?" is also correct, but maybe slightly less common. ("What is the time?" sounds slightly stilted and foreign to native speakers.) Other idiomatic phrases might be "Hey, Steve, what time do you have?" or "Hey, Steve, do you have the time?" or "Hey, Steve, do you know the time?"',
                    'dateLastCrawled': '2023-04-12T17:11:00.0000000Z',
                    'language': 'en',
                    'isNavigational': False,
                },
                {
                    'id': 'https://api.bing.microsoft.com/api/v7/#WebPages.13',
                    'name': 'What is Time? Definition, Uses, Conversion, Measurement, Example',
                    'url': 'https://www.splashlearn.com/math-vocabulary/time/time',
                    'isFamilyFriendly': True,
                    'displayUrl': 'https://www.splashlearn.com/math-vocabulary/time/time',
                    'snippet': 'What Is Time? In math, time can be defined as an ongoing and continuous sequence of events that occur in succession, from past through the present, and to the future. Time is used to quantify, measure, or compare the duration of events or the intervals between them, and even, sequence events. Times of the Day',
                    'dateLastCrawled': '2023-04-13T11:12:00.0000000Z',
                    'language': 'en',
                    'isNavigational': False,
                },
                {
                    'id': 'https://api.bing.microsoft.com/api/v7/#WebPages.14',
                    'name': 'Time in the United Kingdom (UK) - Greenwich Mean Time',
                    'url': 'https://greenwichmeantime.com/uk/time/',
                    'isFamilyFriendly': True,
                    'displayUrl': 'https://greenwichmeantime.com/uk/time',
                    'snippet': 'Current local time in UK (England, Wales, Scotland and Northern Ireland) The UK is in the Western European Time Zone. It currently abides by EU Daylight (Summer) Saving Time rules. When Daylight Saving Time rules are not in use, UK is on GMT (Greenwich Mean Time), which is the Standard Time.',
                    'dateLastCrawled': '2023-04-13T18:26:00.0000000Z',
                    'language': 'en',
                    'isNavigational': False,
                },
            ],
        },
        'rankingResponse': {
            'mainline': {
                'items': [
                    {
                        'answerType': 'WebPages',
                        'resultIndex': 0,
                        'value': {
                            'id': 'https://api.bing.microsoft.com/api/v7/#WebPages.0',
                        },
                    },
                    {
                        'answerType': 'WebPages',
                        'resultIndex': 1,
                        'value': {
                            'id': 'https://api.bing.microsoft.com/api/v7/#WebPages.1',
                        },
                    },
                    {
                        'answerType': 'WebPages',
                        'resultIndex': 2,
                        'value': {
                            'id': 'https://api.bing.microsoft.com/api/v7/#WebPages.2',
                        },
                    },
                    {
                        'answerType': 'WebPages',
                        'resultIndex': 3,
                        'value': {
                            'id': 'https://api.bing.microsoft.com/api/v7/#WebPages.3',
                        },
                    },
                    {
                        'answerType': 'WebPages',
                        'resultIndex': 4,
                        'value': {
                            'id': 'https://api.bing.microsoft.com/api/v7/#WebPages.4',
                        },
                    },
                    {
                        'answerType': 'WebPages',
                        'resultIndex': 5,
                        'value': {
                            'id': 'https://api.bing.microsoft.com/api/v7/#WebPages.5',
                        },
                    },
                    {
                        'answerType': 'WebPages',
                        'resultIndex': 6,
                        'value': {
                            'id': 'https://api.bing.microsoft.com/api/v7/#WebPages.6',
                        },
                    },
                    {
                        'answerType': 'WebPages',
                        'resultIndex': 7,
                        'value': {
                            'id': 'https://api.bing.microsoft.com/api/v7/#WebPages.7',
                        },
                    },
                    {
                        'answerType': 'WebPages',
                        'resultIndex': 8,
                        'value': {
                            'id': 'https://api.bing.microsoft.com/api/v7/#WebPages.8',
                        },
                    },
                    {
                        'answerType': 'WebPages',
                        'resultIndex': 9,
                        'value': {
                            'id': 'https://api.bing.microsoft.com/api/v7/#WebPages.9',
                        },
                    },
                    {
                        'answerType': 'WebPages',
                        'resultIndex': 10,
                        'value': {
                            'id': 'https://api.bing.microsoft.com/api/v7/#WebPages.10',
                        },
                    },
                    {
                        'answerType': 'WebPages',
                        'resultIndex': 11,
                        'value': {
                            'id': 'https://api.bing.microsoft.com/api/v7/#WebPages.11',
                        },
                    },
                    {
                        'answerType': 'WebPages',
                        'resultIndex': 12,
                        'value': {
                            'id': 'https://api.bing.microsoft.com/api/v7/#WebPages.12',
                        },
                    },
                    {
                        'answerType': 'WebPages',
                        'resultIndex': 13,
                        'value': {
                            'id': 'https://api.bing.microsoft.com/api/v7/#WebPages.13',
                        },
                    },
                    {
                        'answerType': 'WebPages',
                        'resultIndex': 14,
                        'value': {
                            'id': 'https://api.bing.microsoft.com/api/v7/#WebPages.14',
                        },
                    },
                    {
                        'answerType': 'WebPages',
                        'resultIndex': 15,
                        'value': {
                            'id': 'https://api.bing.microsoft.com/api/v7/#WebPages.15',
                        },
                    },
                    {
                        'answerType': 'WebPages',
                        'resultIndex': 16,
                        'value': {
                            'id': 'https://api.bing.microsoft.com/api/v7/#WebPages.16',
                        },
                    },
                    {
                        'answerType': 'WebPages',
                        'resultIndex': 17,
                        'value': {
                            'id': 'https://api.bing.microsoft.com/api/v7/#WebPages.17',
                        },
                    },
                    {
                        'answerType': 'WebPages',
                        'resultIndex': 18,
                        'value': {
                            'id': 'https://api.bing.microsoft.com/api/v7/#WebPages.18',
                        },
                    },
                    {
                        'answerType': 'WebPages',
                        'resultIndex': 19,
                        'value': {
                            'id': 'https://api.bing.microsoft.com/api/v7/#WebPages.19',
                        },
                    },
                ],
            },
        },
    },
    'codeContext': '',
    'options': {
        'skill': 'intermediate',
        'date': '14-4-2023',
        'language': 'nl-NL',
        'detailed': True,
        'creative': False,
    },
}

response = requests.post('https://www.phind.com/api/infer/answer', cookies=cookies, headers=headers, json=json_data)

print(response.text)