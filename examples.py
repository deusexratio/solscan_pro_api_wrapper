from client import APIV2, PublicAPI

your_pro_api_key = ''
your_free_api_key = your_pro_api_key

api = APIV2(your_pro_api_key)
public_api = PublicAPI(your_free_api_key)

# print(api.account.transfer_export(address='HiP1svfH24XdX8MyxmJzpAf3ZjsgEPcURr8fgNqg1FUo',
#                    activity_type=['ACTIVITY_SPL_TRANSFER'], exclude_amount_zero=True))

# print(api.token.markets(token=['DezXAZ8z7PnrnRJjz3wXBoRgixCa6xjnB7YaB1pPB263'], program=['BSwp6bEBihVLdqJRKGgzjcGLHkcTuzmSo1TQkHepzH8p']))

# print(api.monitoring.usage())

# print(api.nft.news())

print(public_api.chain_info())
