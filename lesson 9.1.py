phone_book = {"+380568591425": "Bank", "+12054581022": "Ann",

              "+74052153665": "Alex", "+43056203658": "Tony",

              "+12568254053": "Nick", "+54145251233": "Razor"}

contact_list = list(phone_book.keys())

blocked_1 = contact_list[0]

blocked_2 = contact_list[-1]

block_list = {blocked_1: phone_book[blocked_1], "+19295894824": 0,

              blocked_2: phone_book[blocked_2]}

phones = {"+380568591425", "+53145551433", "+330568597598", "+68952125478",

          "+410500291443", "+13145547853", "+12054581022", "+54145251233",

          "+43056203658", "+19295894824", "+200568591425", "+57632143519",

          "+380568591425", "+53145551433"}

incoming_call = phones.pop()

if incoming_call in contact_list:

    if incoming_call in block_list.keys():
        print("Sorry,", block_list[incoming_call], "not today")

    else:

        print("You call from", phone_book[incoming_call])

else:

    if incoming_call in block_list.keys():

        print("Sorry,", incoming_call, "not today")

    else:

        print("You call from", incoming_call)
