from utils import _make_get_request


class PublicAPI:
    def __init__(self, api_key):
        self.url = 'https://public-api.solscan.io/'
        self.headers = {"token": api_key}

    def chain_info(self):
        method_url = self.url + 'chaininfo'
        return _make_get_request(method_url, self.headers)


class APIV2:
    def __init__(self, api_key):
        self.url = 'https://pro-api.solscan.io/v2.0/'
        self.headers = {"token": api_key}
        self._api_key = api_key

    @property
    def token(self) -> "TokenAPIV2":
        """Возвращает объект TokenAPIV2."""
        if not hasattr(self, "_token"):
            self._token = TokenAPIV2(self._api_key)
        return self._token

    @property
    def account(self) -> "AccountAPIV2":
        """Возвращает объект AccountAPIV2."""
        if not hasattr(self, "_account"):
            self._account = AccountAPIV2(self._api_key)
        return self._account

    @property
    def nft(self) -> "NFTAPIV2":
        """Возвращает объект NFTAPIV2."""
        if not hasattr(self, "_nft"):
            self._nft = NFTAPIV2(self._api_key)
        return self._nft

    @property
    def transaction(self) -> "TransactionAPIV2":
        """Возвращает объект TransactionAPIV2."""
        if not hasattr(self, "_transaction"):
            self._transaction = TransactionAPIV2(self._api_key)
        return self._transaction

    @property
    def block(self) -> "BlockAPIV2":
        """Возвращает объект BlockAPIV2."""
        if not hasattr(self, "_block"):
            self._block = BlockAPIV2(self._api_key)
        return self._block

    @property
    def monitoring(self) -> "MonitoringAPIV2":
        """Возвращает объект MonitoringAPIV2."""
        if not hasattr(self, "_monitoring"):
            self._monitoring = MonitoringAPIV2(self._api_key)
        return self._monitoring


class AccountAPIV2(APIV2):
    def __init__(self, api_key):
        super().__init__(api_key)
        self.url_module = self.url + 'account/'

    def defi_activities(self, address: str, activity_type: list[str] | None = None, from_: str | None = None,
                        platform: list[str] | None = None, source: list[str] | None = None, token: str | None = None,
                        block_time: list[int] | None = None, page: int | None = None, page_size: int | None = None,
                        sort_by: str | None = None, sort_order: str | None = None):
        """
        Get defi activities involving an account

        Args:
            address (str): address of an account (required).

            activity_type (list[str] | None): ACTIVITY_TOKEN_SWAP, ACTIVITY_AGG_TOKEN_SWAP, ACTIVITY_TOKEN_ADD_LIQ,
            ACTIVITY_TOKEN_REMOVE_LIQ, ACTIVITY_SPL_TOKEN_STAKE, ACTIVITY_SPL_TOKEN_UNSTAKE,
            ACTIVITY_SPL_TOKEN_WITHDRAW_STAKE, ACTIVITY_SPL_INIT_MINT

            from_ (str | None): Filter activities from an address

            platform (list[str] | None): Filter by list platform addresses. Maximum 5 addresses

            source (list[str] | None): Filter by list source addresses. Maximum 5 addresses

            token (str | None): Filter activities data by token address

            block_time (list[int] | None): Used when you want to filter data by block time.
            Format time: UnixTime in seconds. [timestamp_start, timestamp_stop]

            page (int | None): Page number for pagination

            page_size (int | None): Number items per page. Possible values: (10, 20, 30, 40, 60, 100)

            sort_by (str | None): The parameter allows you to specify the field by which the returned list will be sorted.
            Now only 'block_time' is supported.

            sort_order (str | None): The parameter allows you to specify the sort order. Possible values: (asc, desc)

        """
        method_url = self.url_module + 'defi/activities?address=' + address
        if isinstance(activity_type, list):
            for i in range(0, len(activity_type)):
                method_url = method_url + '&activity_type[]=' + activity_type[i]
        elif activity_type is not None:
            raise TypeError('Wrong type for input args')

        if isinstance(from_, str):
            method_url = method_url + '&from=' + from_
        elif from_ is not None:
            raise TypeError('Wrong type for input args')

        if isinstance(platform, list):
            for i in range(0, len(platform)):
                method_url = method_url + '&platform[]=' + platform[i]
        elif platform is not None:
            raise TypeError('Wrong type for input args')

        if isinstance(source, list):
            for i in range(0, len(source)):
                method_url = method_url + '&source[]=' + source[i]
        elif source is not None:
            raise TypeError('Wrong type for input args')

        if isinstance(token, str):
            method_url = method_url + '&token=' + token
        elif token is not None:
            raise TypeError('Wrong type for input args')

        if isinstance(block_time, list):
            for i in range(0, len(block_time)):
                method_url = method_url + '&block_time[]=' + str(block_time[i])
        elif block_time is not None:
            raise TypeError('Wrong type for input args')

        if isinstance(page, int):
            method_url = method_url + '&page=' + str(page)
        elif page is not None:
            raise TypeError('Wrong type for input args')

        if isinstance(page_size, int):
            method_url = method_url + '&page_size=' + str(page_size)
        elif page_size is not None:
            raise TypeError('Wrong type for input args')

        if isinstance(sort_by, str):
            method_url = method_url + '&sort_by=' + sort_by
        elif sort_by is not None:
            raise TypeError('Wrong type for input args')

        if isinstance(sort_order, str):
            method_url = method_url + '&sort_order=' + sort_order
        elif sort_order is not None:
            raise TypeError('Wrong type for input args')

        return _make_get_request(method_url, self.headers)

    def transfer(self, address: str, activity_type: list[str] | None = None, token_account: str | None = None,
                 from_: str | None = None, to_: str | None = None, token: str | None = None,
                 amount: list[int] | None = None, exclude_amount_zero: bool | None = None, flow: str | None = None,
                 block_time: list[int] | None = None, page: int | None = None,
                 page_size: int | None = None, sort_by: str | None = None, sort_order: str | None = None):
        """
        Get transfer data of an account

        Args:
            address (str): address of an account (required).

            activity_type (list[str] | None): ACTIVITY_TOKEN_SWAP, ACTIVITY_AGG_TOKEN_SWAP, ACTIVITY_TOKEN_ADD_LIQ,
            ACTIVITY_TOKEN_REMOVE_LIQ, ACTIVITY_SPL_TOKEN_STAKE, ACTIVITY_SPL_TOKEN_UNSTAKE,
            ACTIVITY_SPL_TOKEN_WITHDRAW_STAKE, ACTIVITY_SPL_INIT_MINT

            from_ (str | None): Filter transfer data with direction is from an address

            to_ (str | None): Filter transfers from a specific address

            flow (str | None): Filter by transfer direction: in or out. Enum: in, out

            amount (list[int] | None): Filter by amount range for a specific token. Example: ?amount[]=1&amount[]=2&token=So11111111111111111111111111111111111111112

            token_account (str | None): Filter transfers for a specific token account in the wallet

            token (str | None): Filter by token address. For native SOL transfers, use So11111111111111111111111111111111111111111

            exclude_amount_zero (bool | None): Exclude transfers with zero amount

            block_time (list[int] | None): Used when you want to filter data by block time.
            Format time: UnixTime in seconds. [timestamp_start, timestamp_stop]

            page (int | None): Page number for pagination

            page_size (int | None): Number items per page. Possible values: (10, 20, 30, 40, 60, 100)

            sort_by (str | None): The parameter allows you to specify the field by which the returned list will be sorted.
            Now only 'block_time' is supported.

            sort_order (str | None): The parameter allows you to specify the sort order. Possible values: (asc, desc)
        """
        method_url = self.url_module + 'transfer?address=' + address
        if isinstance(activity_type, list):
            for i in range(0, len(activity_type)):
                method_url = method_url + '&activity_type[]=' + activity_type[i]
        elif activity_type is not None:
            raise TypeError('Wrong type for input args')

        if isinstance(token_account, str):
            method_url = method_url + '&token_account=' + token_account
        elif token_account is not None:
            raise TypeError('Wrong type for input args')

        if isinstance(from_, str):
            method_url = method_url + '&from=' + from_
        elif from_ is not None:
            raise TypeError('Wrong type for input args')

        if isinstance(to_, str):
            method_url = method_url + '&from=' + to_
        elif to_ is not None:
            raise TypeError('Wrong type for input args')

        if isinstance(token, str):
            method_url = method_url + '&token=' + token
        elif token is not None:
            raise TypeError('Wrong type for input args')

        if isinstance(amount, list):
            for i in range(0, len(amount)):
                method_url = method_url + '&amount[]=' + str(amount[i])
        elif amount is not None:
            raise TypeError('Wrong type for input args')

        if isinstance(flow, str):
            method_url = method_url + '&flow=' + flow
        elif flow is not None:
            raise TypeError('Wrong type for input args')

        if isinstance(exclude_amount_zero, bool):
            method_url = method_url + '&exclude_amount_zero=' + str(exclude_amount_zero).lower()
        elif exclude_amount_zero is not None:
            raise TypeError('Wrong type for input args')

        if isinstance(block_time, list):
            for i in range(0, len(block_time)):
                method_url = method_url + '&block_time[]=' + str(block_time[i])
        elif block_time is not None:
            raise TypeError('Wrong type for input args')

        if isinstance(page, int):
            method_url = method_url + '&page=' + str(page)
        elif page is not None:
            raise TypeError('Wrong type for input args')

        if isinstance(page_size, int):
            method_url = method_url + '&page_size=' + str(page_size)
        elif page_size is not None:
            raise TypeError('Wrong type for input args')

        if isinstance(sort_by, str):
            method_url = method_url + '&sort_by=' + sort_by
        elif sort_by is not None:
            raise TypeError('Wrong type for input args')

        if isinstance(sort_order, str):
            method_url = method_url + '&sort_order=' + sort_order
        elif sort_order is not None:
            raise TypeError('Wrong type for input args')

        return _make_get_request(method_url, self.headers)

    def token_accounts(self, address: str, type: str, hide_zero: bool | None = None,
                  page: int | None = None, page_size: int | None = None):
        """
        Get token accounts of an account

        Args:
            address (str): address of an account (required).

            type (str): Type of token. Enum: token, nft

            hide_zero (bool | None): Filter tokens that have amount is zero

            page (int | None): Page number for pagination

            page_size (int | None): Number items per page. Possible values: (10, 20, 30, 40, 60, 100)
        """
        method_url = self.url_module + 'token-accounts?address=' + address + '&type=' + type

        if isinstance(hide_zero, bool):
            method_url = method_url + '&hide_zero=' + str(hide_zero).lower()
        elif hide_zero is not None:
            raise TypeError('Wrong type for input args')

        if isinstance(page, int):
            method_url = method_url + '&page=' + str(page)
        elif page is not None:
            raise TypeError('Wrong type for input args')

        if isinstance(page_size, int):
            method_url = method_url + '&page_size=' + str(page_size)
        elif page_size is not None:
            raise TypeError('Wrong type for input args')

        return _make_get_request(method_url, self.headers)

    def balance_change_activities(self, address: str, token: str | None = None, remove_spam: bool | None = None,
                 amount: list[int] | None = None, flow: str | None = None,
                 block_time: list[int] | None = None, page: int | None = None,
                 page_size: int | None = None, sort_by: str | None = None, sort_order: str | None = None):
        """
        Get balance change activities involving an account

        Args:
            address (str): address of an account (required).

            flow (str | None): Filter by transfer direction: in or out. Enum: in, out

            amount (list[int] | None): Filter by amount range for a specific token. Example: ?amount[]=1&amount[]=2&token=So11111111111111111111111111111111111111112

            token (str | None): Filter by token address. For native SOL transfers, use So11111111111111111111111111111111111111111

            remove_spam (bool | None): The query parameter to determine if spam activities have been removed or not

            block_time (list[int] | None): Used when you want to filter data by block time.
            Format time: UnixTime in seconds. [timestamp_start, timestamp_stop]

            page (int | None): Page number for pagination

            page_size (int | None): Number items per page. Possible values: (10, 20, 30, 40, 60, 100)

            sort_by (str | None): The parameter allows you to specify the field by which the returned list will be sorted.
            Now only 'block_time' is supported.

            sort_order (str | None): The parameter allows you to specify the sort order. Possible values: (asc, desc)
        """
        method_url = self.url_module + 'balance_change?address=' + address

        if isinstance(token, str):
            method_url = method_url + '&token=' + token
        elif token is not None:
            raise TypeError('Wrong type for input args')

        if isinstance(amount, list):
            for i in range(0, len(amount)):
                method_url = method_url + '&amount[]=' + str(amount[i])
        elif amount is not None:
            raise TypeError('Wrong type for input args')

        if isinstance(flow, str):
            method_url = method_url + '&flow=' + flow
        elif flow is not None:
            raise TypeError('Wrong type for input args')

        if isinstance(remove_spam, bool):
            method_url = method_url + '&remove_spam=' + str(remove_spam).lower()
        elif remove_spam is not None:
            raise TypeError('Wrong type for input args')

        if isinstance(block_time, list):
            for i in range(0, len(block_time)):
                method_url = method_url + '&block_time[]=' + str(block_time[i])
        elif block_time is not None:
            raise TypeError('Wrong type for input args')

        if isinstance(page, int):
            method_url = method_url + '&page=' + str(page)
        elif page is not None:
            raise TypeError('Wrong type for input args')

        if isinstance(page_size, int):
            method_url = method_url + '&page_size=' + str(page_size)
        elif page_size is not None:
            raise TypeError('Wrong type for input args')

        if isinstance(sort_by, str):
            method_url = method_url + '&sort_by=' + sort_by
        elif sort_by is not None:
            raise TypeError('Wrong type for input args')

        if isinstance(sort_order, str):
            method_url = method_url + '&sort_order=' + sort_order
        elif sort_order is not None:
            raise TypeError('Wrong type for input args')

        return _make_get_request(method_url, self.headers)

    def transactions(self, address: str, before: str | None = None, limit: int | None = None):
        """
        Get the list of transactions of an account

        Args:
            address (str): address of an account (required).

            before (str): The signature of the latest transaction of previous page

            limit (int): The number of transactions should be returned. Enum: 10, 20, 30, 40
        """
        method_url = self.url_module + 'transactions?address=' + address

        if isinstance(before, str):
            method_url = method_url + '&before=' + before
        elif before is not None:
            raise TypeError('Wrong type for input args')

        if isinstance(limit, int):
            method_url = method_url + '&limit=' + str(limit)
        elif limit is not None:
            raise TypeError('Wrong type for input args')

        return _make_get_request(method_url, self.headers)

    def stake(self, address: str, page: int | None = None, page_size: int | None = None):
        """
        Get the list of stake accounts of an account

        Args:
            address (str): address of an account (required).

            page (int | None): Page number for pagination

            page_size (int | None): Number items per page. Enum: 10, 20, 30, 40
        """
        method_url = self.url_module + 'stake?address=' + address

        if isinstance(page, int):
            method_url = method_url + '&page=' + str(page)
        elif page is not None:
            raise TypeError('Wrong type for input args')

        if isinstance(page_size, int):
            method_url = method_url + '&page_size=' + str(page_size)
        elif page_size is not None:
            raise TypeError('Wrong type for input args')

        return _make_get_request(method_url, self.headers)

    def detail(self, address: str):
        """
        Get the details of an account

        Args:
            address (str): address of an account (required).
        """
        method_url = self.url_module + 'detail?address=' + address
        return _make_get_request(method_url, self.headers)

    def rewards_export(self, address: str, time_from: int, time_to: int):
        """
        Export the rewards for an account. Maximum items: 5000

        Args:
            address (str): address of an account (required).

            time_from (int): The start time for the export. Format: Unix time in seconds

            time_to (int): The end time for the export. Format: Unix time in seconds
        """
        method_url = (self.url_module + 'reward/export?address=' + address +
                      '&time_from=' + str(time_from) + '&time_to=' + str(time_to))
        return _make_get_request(method_url, self.headers)

    def transfer_export(self, address: str, activity_type: list[str] | None = None, token_account: str | None = None,
                 from_: str | None = None, to_: str | None = None, token: str | None = None,
                 amount: list[int] | None = None, exclude_amount_zero: bool | None = None, flow: str | None = None,
                 block_time: list[int] | None = None):
        """
        Export transfer data of an account

        Args:
            address (str): address of an account (required).

            activity_type (list[str] | None): ACTIVITY_SPL_TRANSFER, ACTIVITY_SPL_BURN, ACTIVITY_SPL_MINT, ACTIVITY_SPL_CREATE_ACCOUNT

            from_ (str | None): Filter transfer data with direction is from an address

            to_ (str | None): Filter transfers from a specific address

            flow (str | None): Filter by transfer direction: in or out. Enum: in, out

            amount (list[int] | None): Filter by amount range for a specific token. Example: ?amount[]=1&amount[]=2&token=So11111111111111111111111111111111111111112

            token_account (str | None): Filter transfers for a specific token account in the wallet

            token (str | None): Filter by token address. For native SOL transfers, use So11111111111111111111111111111111111111111

            exclude_amount_zero (bool | None): Exclude transfers with zero amount

            block_time (list[int] | None): Used when you want to filter data by block time.
            Format time: UnixTime in seconds. [timestamp_start, timestamp_stop]
        """
        method_url = self.url_module + 'transfer?address=' + address
        if isinstance(activity_type, list):
            for i in range(0, len(activity_type)):
                method_url = method_url + '&activity_type[]=' + activity_type[i]
        elif activity_type is not None:
            raise TypeError('Wrong type for input args')

        if isinstance(token_account, str):
            method_url = method_url + '&token_account=' + token_account
        elif token_account is not None:
            raise TypeError('Wrong type for input args')

        if isinstance(from_, str):
            method_url = method_url + '&from=' + from_
        elif from_ is not None:
            raise TypeError('Wrong type for input args')

        if isinstance(to_, str):
            method_url = method_url + '&from=' + to_
        elif to_ is not None:
            raise TypeError('Wrong type for input args')

        if isinstance(token, str):
            method_url = method_url + '&token=' + token
        elif token is not None:
            raise TypeError('Wrong type for input args')

        if isinstance(amount, list):
            for i in range(0, len(amount)):
                method_url = method_url + '&amount[]=' + str(amount[i])
        elif amount is not None:
            raise TypeError('Wrong type for input args')

        if isinstance(flow, str):
            method_url = method_url + '&flow=' + flow
        elif flow is not None:
            raise TypeError('Wrong type for input args')

        if isinstance(exclude_amount_zero, bool):
            method_url = method_url + '&exclude_amount_zero=' + str(exclude_amount_zero).lower()
        elif exclude_amount_zero is not None:
            raise TypeError('Wrong type for input args')

        if isinstance(block_time, list):
            for i in range(0, len(block_time)):
                method_url = method_url + '&block_time[]=' + str(block_time[i])
        elif block_time is not None:
            raise TypeError('Wrong type for input args')

        return _make_get_request(method_url, self.headers)


class TokenAPIV2(APIV2):
    def __init__(self, api_key):
        super().__init__(api_key)
        self.url_module = self.url + 'token/'

    def meta(self, address: str):
        """
        Get the metadata of a token

        Args:
            address (str): address of an account (required).
        """
        method_url = self.url_module + 'meta?address=' + address
        return _make_get_request(method_url, self.headers)

    def markets(self, token: list[str], sort_by: str | None = None, program: list[str] | None = None,
                page: int | None = None, page_size: int | None = 100):
        """
        Get token markets

        Args:
            token (list[str]): Token pair addresses

            program (list[str]): Filter by list program addresses. Maximum 5 addresses

            page (int | None): Page number for pagination

            page_size (int | None): Number items per page. Possible values: (10, 20, 30, 40, 60, 100)

            sort_by (str | None): The parameter allows you to specify the field by which the returned list will be sorted.
            Now only 'block_time' is supported.
        """
        method_url = self.url_module + 'markets?token[]='

        if isinstance(token, list):
            method_url = method_url + token[0]
            for i in range(1, len(token)):
                method_url = method_url + '&token[]=' + token[i]
        elif token is not None:
            raise TypeError('Wrong type for input args')

        if isinstance(sort_by, str):
            method_url = method_url + '&sort_by=' + sort_by
        elif sort_by is not None:
            raise TypeError('Wrong type for input args')

        if isinstance(program, list):
            for i in range(0, len(program)):
                method_url = method_url + '&program[]=' + program[i]
        elif program is not None:
            raise TypeError('Wrong type for input args')

        if isinstance(page, int):
            method_url = method_url + '&page=' + str(page)
        elif page is not None:
            raise TypeError('Wrong type for input args')

        if isinstance(page_size, int):
            method_url = method_url + '&page_size=' + str(page_size)
        elif page_size is not None:
            raise TypeError('Wrong type for input args')

        return _make_get_request(method_url, self.headers)

    def market_info(self, address: str):
        """
        Get token market info

        Args:
            address (str): address of an account (required).
        """
        method_url = self.url_module + 'market/info?address=' + address
        return _make_get_request(method_url, self.headers)

    def transfer(self, address: str, activity_type: list[str] | None = None, token_account: str | None = None,
                 from_: str | None = None, to_: str | None = None, token: str | None = None,
                 amount: list[int] | None = None, exclude_amount_zero: bool | None = None, flow: str | None = None,
                 block_time: list[int] | None = None, sort_by: str | None = None, sort_order: str | None = None):
        """
        Get transfer data of a token

        Args:
            address (str): A token address on solana blockchain

            activity_type (list[str] | None): ACTIVITY_SPL_TRANSFER, ACTIVITY_SPL_BURN, ACTIVITY_SPL_MINT, ACTIVITY_SPL_CREATE_ACCOUNT

            from_ (str | None): Filter transfer data with direction is from an address

            to_ (str | None): Filter transfers from a specific address

            flow (str | None): Filter by transfer direction: in or out. Enum: in, out

            amount (list[int] | None): Filter by amount range for a specific token. Example: ?amount[]=1&amount[]=2&token=So11111111111111111111111111111111111111112

            token_account (str | None): Filter transfers for a specific token account in the wallet

            token (str | None): Filter by token address. For native SOL transfers, use So11111111111111111111111111111111111111111

            exclude_amount_zero (bool | None): Exclude transfers with zero amount

            block_time (list[int] | None): Used when you want to filter data by block time.
            Format time: UnixTime in seconds. [timestamp_start, timestamp_stop]

            sort_by (str | None): The parameter allows you to specify the field by which the returned list will be sorted.
            Now only 'block_time' is supported.

            sort_order (str | None): The parameter allows you to specify the sort order. Possible values: (asc, desc)
        """
        method_url = self.url_module + 'transfer?address=' + address
        if isinstance(activity_type, list):
            for i in range(0, len(activity_type)):
                method_url = method_url + '&activity_type[]=' + activity_type[i]
        elif activity_type is not None:
            raise TypeError('Wrong type for input args')

        if isinstance(token_account, str):
            method_url = method_url + '&token_account=' + token_account
        elif token_account is not None:
            raise TypeError('Wrong type for input args')

        if isinstance(from_, str):
            method_url = method_url + '&from=' + from_
        elif from_ is not None:
            raise TypeError('Wrong type for input args')

        if isinstance(to_, str):
            method_url = method_url + '&from=' + to_
        elif to_ is not None:
            raise TypeError('Wrong type for input args')

        if isinstance(token, str):
            method_url = method_url + '&token=' + token
        elif token is not None:
            raise TypeError('Wrong type for input args')

        if isinstance(amount, list):
            for i in range(0, len(amount)):
                method_url = method_url + '&amount[]=' + str(amount[i])
        elif amount is not None:
            raise TypeError('Wrong type for input args')

        if isinstance(flow, str):
            method_url = method_url + '&flow=' + flow
        elif flow is not None:
            raise TypeError('Wrong type for input args')

        if isinstance(exclude_amount_zero, bool):
            method_url = method_url + '&exclude_amount_zero=' + str(exclude_amount_zero).lower()
        elif exclude_amount_zero is not None:
            raise TypeError('Wrong type for input args')

        if isinstance(block_time, list):
            for i in range(0, len(block_time)):
                method_url = method_url + '&block_time[]=' + str(block_time[i])
        elif block_time is not None:
            raise TypeError('Wrong type for input args')

        if isinstance(sort_by, str):
            method_url = method_url + '&sort_by=' + sort_by
        elif sort_by is not None:
            raise TypeError('Wrong type for input args')

        if isinstance(sort_order, str):
            method_url = method_url + '&sort_order=' + sort_order
        elif sort_order is not None:
            raise TypeError('Wrong type for input args')

        return _make_get_request(method_url, self.headers)

    def defi_activities(self, address: str, activity_type: list[str] | None = None, from_: str | None = None,
                        platform: list[str] | None = None, source: list[str] | None = None, token: str | None = None,
                        block_time: list[int] | None = None, page: int | None = None, page_size: int | None = None,
                        sort_by: str | None = None, sort_order: str | None = None):
        """
        Get defi activities involving a token

        Args:
            address (str): A token address on solana blockchain

            from_ (str): Filter activities from an address

            activity_type (list[str] | None): ACTIVITY_TOKEN_SWAP, ACTIVITY_AGG_TOKEN_SWAP, ACTIVITY_TOKEN_ADD_LIQ,
            ACTIVITY_TOKEN_REMOVE_LIQ, ACTIVITY_SPL_TOKEN_STAKE, ACTIVITY_SPL_TOKEN_UNSTAKE,
            ACTIVITY_SPL_TOKEN_WITHDRAW_STAKE, ACTIVITY_SPL_INIT_MINT

            platform (list[str] | None): Filter by list platform addresses. Maximum 5 addresses

            source (list[str] | None): Filter by list source addresses. Maximum 5 addresses

            token (str | None): Filter activities data by token address

            block_time (list[int] | None): Used when you want to filter data by block time.
            Format time: UnixTime in seconds. [timestamp_start, timestamp_stop]

            page (int | None): Page number for pagination

            page_size (int | None): Number items per page. Possible values: (10, 20, 30, 40, 60, 100)

            sort_by (str | None): The parameter allows you to specify the field by which the returned list will be sorted.
            Now only 'block_time' is supported.

            sort_order (str | None): The parameter allows you to specify the sort order. Possible values: (asc, desc)
        """
        method_url = self.url_module + 'defi/activities?address=' + address
        if isinstance(activity_type, list):
            for i in range(0, len(activity_type)):
                method_url = method_url + '&activity_type[]=' + activity_type[i]
        elif activity_type is not None:
            raise TypeError('Wrong type for input args')

        if isinstance(from_, str):
            method_url = method_url + '&from=' + from_
        elif from_ is not None:
            raise TypeError('Wrong type for input args')

        if isinstance(platform, list):
            for i in range(0, len(platform)):
                method_url = method_url + '&platform[]=' + platform[i]
        elif platform is not None:
            raise TypeError('Wrong type for input args')

        if isinstance(source, list):
            for i in range(0, len(source)):
                method_url = method_url + '&source[]=' + source[i]
        elif source is not None:
            raise TypeError('Wrong type for input args')

        if isinstance(token, str):
            method_url = method_url + '&token=' + token
        elif token is not None:
            raise TypeError('Wrong type for input args')

        if isinstance(block_time, list):
            for i in range(0, len(block_time)):
                method_url = method_url + '&block_time[]=' + str(block_time[i])
        elif block_time is not None:
            raise TypeError('Wrong type for input args')

        if isinstance(page, int):
            method_url = method_url + '&page=' + str(page)
        elif page is not None:
            raise TypeError('Wrong type for input args')

        if isinstance(page_size, int):
            method_url = method_url + '&page_size=' + str(page_size)
        elif page_size is not None:
            raise TypeError('Wrong type for input args')

        if isinstance(sort_by, str):
            method_url = method_url + '&sort_by=' + sort_by
        elif sort_by is not None:
            raise TypeError('Wrong type for input args')

        if isinstance(sort_order, str):
            method_url = method_url + '&sort_order=' + sort_order
        elif sort_order is not None:
            raise TypeError('Wrong type for input args')

        return _make_get_request(method_url, self.headers)

    def token_list(self, page: int = 1, page_size: int | None = None,
                        sort_by: str | None = None, sort_order: str | None = None):
        """
        Get the list of tokens

        Args:
            page (int | None): Page number for pagination

            page_size (int | None): Number items per page. Enum: 10, 20, 30, 40, 60, 100

            sort_by (str | None): The parameter allows you to specify the field by which the returned list will be sorted.
            Now only 'block_time' is supported.

            sort_order (str | None): The parameter allows you to specify the sort order. Possible values: (asc, desc)
        """
        method_url = self.url_module + 'list?page=' + str(page)

        if isinstance(page_size, int):
            method_url = method_url + '&page_size=' + str(page_size)
        elif page_size is not None:
            raise TypeError('Wrong type for input args')

        if isinstance(sort_by, str):
            method_url = method_url + '&sort_by=' + sort_by
        elif sort_by is not None:
            raise TypeError('Wrong type for input args')

        if isinstance(sort_order, str):
            method_url = method_url + '&sort_order=' + sort_order
        elif sort_order is not None:
            raise TypeError('Wrong type for input args')

        return _make_get_request(method_url, self.headers)

    def market_volume(self, address: str, time: list[int] | None = None):
        """
        Get token market info

        Args:
            address (str): A token address on solana blockchain

            time (list[int]): Used when you want to filter data by time. Format time: YYYYMMDD. You need to pass array into http query to filter by start and end time. Example: ?time[]=20240701&time[]=20240715
        """
        method_url = self.url_module + 'market/volume?address=' + address

        if isinstance(time, list):
            for i in range(0, len(time)):
                method_url = method_url + '&time[]=' + str(time[i])
        elif time is not None:
            raise TypeError('Wrong type for input args')

        return _make_get_request(method_url, self.headers)

    def trending(self, limit: int = 10):
        """
        Get the list of trending tokens

        Args:
            limit(int): Number items should be returned
        """
        method_url = self.url_module + 'trending?limit=' + str(limit)
        return _make_get_request(method_url, self.headers)

    def token_price(self, address: str, time: list[int] | None = None):
        """
        Get price of a token

        Args:
            address (str): A token address on solana blockchain

            time (list[int]): Used when you want to filter data by time. Format time: YYYYMMDD. You need to pass array into http query to filter by start and end time. Example: ?time[]=20240701&time[]=20240715
        """
        method_url = self.url_module + 'price?address=' + address

        if isinstance(time, list):
            for i in range(0, len(time)):
                method_url = method_url + '&time[]=' + str(time[i])
        elif time is not None:
            raise TypeError('Wrong type for input args')

        return _make_get_request(method_url, self.headers)

    def holders(self, address: str, page: int = 1, page_size: int | None = None,
                        from_amount: int | None = None, to_amount: int | None = None):
        """
        Get the list of tokens

        Args:
            address (str): A token address on solana blockchain

            page (int | None): Page number for pagination

            page_size (int | None): Number items per page. Enum: 10, 20, 30, 40

            from_amount (int | None): Filter holders by minimum token holding amount. The number should be in string format

            to_amount (int | None): Filter holders by maximum token holding amount. The number should be in string format
        """
        method_url = self.url_module + 'list?page=' + str(page)

        if isinstance(page_size, int):
            method_url = method_url + '&page_size=' + str(page_size)
        elif page_size is not None:
            raise TypeError('Wrong type for input args')

        if isinstance(from_amount, int):
            method_url = method_url + '&from_amount=' + str(from_amount)
        elif from_amount is not None:
            raise TypeError('Wrong type for input args')

        if isinstance(to_amount, int):
            method_url = method_url + '&to_amount=' + str(to_amount)
        elif to_amount is not None:
            raise TypeError('Wrong type for input args')

        return _make_get_request(method_url, self.headers)

    def top(self):
        """
        Get the list of top tokens
        """
        method_url = self.url_module + 'top'
        return _make_get_request(method_url, self.headers)


class NFTAPIV2(APIV2):
    def __init__(self, api_key):
        super().__init__(api_key)
        self.url_module = self.url + 'nft/'

    def news(self, filter_: str = 'created_time', page: int = 1, page_size: int | None = None):
        """
        Get the list of tokens

        Args:
            filter_ (str): Filter ('created_time'). Enum: created_time

            page (int | None): Page number for pagination

            page_size (int | None): Number items per page. Enum: 12, 24, 36
        """
        method_url = self.url_module + 'news?filter=' + filter_

        if isinstance(page_size, int):
            method_url = method_url + '&page_size=' + str(page_size)
        elif page_size is not None:
            raise TypeError('Wrong type for input args')

        if isinstance(page, int):
            method_url = method_url + '&page=' + str(page)
        elif page is not None:
            raise TypeError('Wrong type for input args')

        return _make_get_request(method_url, self.headers)

    def activities(self, activity_type: list[str] | None = None, from_: str | None = None, to_: str | None = None,
                        currency_token: str | None = None, collection: str | None = None,
                        price: list[int] | None = None, source: list[str] | None = None, token: str | None = None,
                        block_time: list[int] | None = None, page: int | None = 1, page_size: int | None = None):
        """
        Get defi activities involving a token

        Args:
            from_ (str): from

            to_ (str): to

            activity_type (list[str] | None): ACTIVITY_NFT_SOLD, ACTIVITY_NFT_LISTING, ACTIVITY_NFT_BIDDING,
            ACTIVITY_NFT_CANCEL_BID, ACTIVITY_NFT_CANCEL_LIST, ACTIVITY_NFT_REJECT_BID, ACTIVITY_NFT_UPDATE_PRICE,
            ACTIVITY_NFT_LIST_AUCTION.

            currency_token (str | None): currency_token

            price (list[int] | None): Filter transfer data by amount. But you need to pass token address in
            field currency_token first because price filter will belong to one currency token address. Ex: Filter price from 1 to 2 SOL ?price[]=1&price[]=2&currency_token=So11111111111111111111111111111111111111112

            source (list[str] | None): Filter by list source addresses. Maximum 5 addresses

            token (str | None): Filter activities data by token address

            collection (str | None): Collection ID, if not provided, will return all collections

            block_time (list[int] | None): Used when you want to filter data by block time.
            Format time: UnixTime in seconds. [timestamp_start, timestamp_stop]

            page (int | None): Page number for pagination

            page_size (int | None): Number items per page. Enum: 10, 20, 30, 40, 60, 100
        """
        method_url = self.url_module + 'activities?page=' + str(page)
        if isinstance(activity_type, list):
            for i in range(0, len(activity_type)):
                method_url = method_url + '&activity_type[]=' + activity_type[i]
        elif activity_type is not None:
            raise TypeError('Wrong type for input args')

        if isinstance(from_, str):
            method_url = method_url + '&from=' + from_
        elif from_ is not None:
            raise TypeError('Wrong type for input args')

        if isinstance(to_, str):
            method_url = method_url + '&to_=' + to_
        elif to_ is not None:
            raise TypeError('Wrong type for input args')

        if isinstance(currency_token, str):
            method_url = method_url + '&currency_token=' + currency_token
        elif currency_token is not None:
            raise TypeError('Wrong type for input args')

        if isinstance(price, list):
            if not currency_token:
                raise ValueError('Specify currency_token first before price')
            for i in range(0, len(price)):
                method_url = method_url + '&platform[]=' + str(price[i])
        elif price is not None:
            raise TypeError('Wrong type for input args')

        if isinstance(source, list):
            for i in range(0, len(source)):
                method_url = method_url + '&source[]=' + source[i]
        elif source is not None:
            raise TypeError('Wrong type for input args')

        if isinstance(collection, str):
            method_url = method_url + '&collection=' + collection
        elif collection is not None:
            raise TypeError('Wrong type for input args')

        if isinstance(token, str):
            method_url = method_url + '&token=' + token
        elif token is not None:
            raise TypeError('Wrong type for input args')

        if isinstance(block_time, list):
            for i in range(0, len(block_time)):
                method_url = method_url + '&block_time[]=' + str(block_time[i])
        elif block_time is not None:
            raise TypeError('Wrong type for input args')

        if isinstance(page_size, int):
            method_url = method_url + '&page_size=' + str(page_size)
        elif page_size is not None:
            raise TypeError('Wrong type for input args')

        return _make_get_request(method_url, self.headers)

    def collection_lists(self, range_: int | None = 1, collection: str | None = None, page: int | None = 1,
                         page_size: int | None = None, sort_by: str | None = None, sort_order: str | None = None):
        """
        Get the list of NFT collections

        Args:
            range_ (int | None): Days range. Enum: 1, 7, 30

            collection (str | None): Collection ID, if not provided, will return all collections

            page (int | None): Page number for pagination

            page_size (int | None): Number items per page. Enum: 10, 18, 20, 30, 40

            sort_by (str | None): The parameter allows you to specify the field by which the returned list will be sorted. Enum: items, floor_price, volumes

            sort_order (str | None): The parameter allows you to specify the sort order. Possible values: (asc, desc)
        """
        method_url = self.url_module + 'collection/lists?range=' + str(range_)

        if isinstance(collection, str):
            method_url = method_url + '&collection=' + collection
        elif collection is not None:
            raise TypeError('Wrong type for input args')

        if isinstance(page, int):
            method_url = method_url + '&page=' + str(page)
        elif page is not None:
            raise TypeError('Wrong type for input args')

        if isinstance(page_size, int):
            method_url = method_url + '&page_size=' + str(page_size)
        elif page_size is not None:
            raise TypeError('Wrong type for input args')

        if isinstance(sort_by, str):
            method_url = method_url + '&sort_by=' + sort_by
        elif sort_by is not None:
            raise TypeError('Wrong type for input args')

        if isinstance(sort_order, str):
            method_url = method_url + '&sort_order=' + sort_order
        elif sort_order is not None:
            raise TypeError('Wrong type for input args')

        return _make_get_request(method_url, self.headers)

    def collection_items(self, collection: str, page: int | None = 1, page_size: int | None = None,
                         sort_by: str | None = None):
        """
        Get the list of items of a NFT collection

        Args:
            collection (str | None): Collection ID, if not provided, will return all collections

            page (int | None): Page number for pagination

            page_size (int | None): Number items per page. Enum: 10, 18, 20, 30, 40

            sort_by (str | None): The parameter allows you to specify the field by which the returned list will be sorted. Enum: last_trade, listing_price
        """
        method_url = self.url_module + 'collection/items?collection=' + collection

        if isinstance(page, int):
            method_url = method_url + '&page=' + str(page)
        elif page is not None:
            raise TypeError('Wrong type for input args')

        if isinstance(page_size, int):
            method_url = method_url + '&page_size=' + str(page_size)
        elif page_size is not None:
            raise TypeError('Wrong type for input args')

        if isinstance(sort_by, str):
            method_url = method_url + '&sort_by=' + sort_by
        elif sort_by is not None:
            raise TypeError('Wrong type for input args')

        return _make_get_request(method_url, self.headers)


class TransactionAPIV2(APIV2):
    def __init__(self, api_key):
        super().__init__(api_key)
        self.url_module = self.url + 'transaction/'

    def last(self, limit: int | None = 100, filter_: str | None = 'exceptVote'):
        """
        Get the list of the latest transactions

        Args:
        limit (int): The number of transactions should be returned. Enum: 10, 20, 30, 40, 60, 100

        filter_ (str): The filter parameter for excluding vote transactions. Enum: exceptVote, all
        """
        method_url = self.url_module + 'last?filter=' + filter_

        if isinstance(limit, int):
            method_url = method_url + '&limit=' + str(limit)
        elif limit is not None:
            raise TypeError('Wrong type for input args')

        return _make_get_request(method_url, self.headers)

    def detail(self, tx: str):
        """
        Get the detail of a transaction. Return transaction data after parsed by Solscan Parser. Data will include very helpful data such as: token and sol balance changes, IDL data, defi or transfer activities of each instructions

        Args:
        tx (str): Transaction Address
        """
        method_url = self.url_module + 'detail?tx=' + tx

        return _make_get_request(method_url, self.headers)

    def actions(self, tx: str):
        """
        Get the actions of a transaction. Return the actions like: transfers, swap activities, nft activities...

        Args:
        tx (str): Transaction Address
        """
        method_url = self.url_module + 'actions?tx=' + tx

        return _make_get_request(method_url, self.headers)


class BlockAPIV2(APIV2):
    def __init__(self, api_key):
        super().__init__(api_key)
        self.url_module = self.url + 'block/'

    def last(self, limit: int | None = 100):
        """
        Get the list of the latest transactions

        Args:
        limit (int): The number of transactions should be returned. Enum: 10, 20, 30, 40, 60, 100
        """
        method_url = self.url_module + 'last?limit=' + str(limit)

        return _make_get_request(method_url, self.headers)

    def transactions(self, block: int, page: int | None = None, page_size: int | None = None):
        """
        Get the list of transactions of a block

        Args:
        block (int): The slot index of a block

        page (int | None): Page number for pagination

        page_size (int | None): Number items per page. Enum: 10, 20, 30, 40, 60, 100
        """
        method_url = self.url_module + 'transactions?block=' + str(block)

        if isinstance(page, int):
            method_url = method_url + '&page=' + str(page)
        elif page is not None:
            raise TypeError('Wrong type for input args')

        if isinstance(page_size, int):
            method_url = method_url + '&page_size=' + str(page_size)
        elif page_size is not None:
            raise TypeError('Wrong type for input args')

        return _make_get_request(method_url, self.headers)

    def detail(self, block: int):
        """
        Get the details of a block

        Args:
        block (int): The slot index of a block
        """
        method_url = self.url_module + 'detail?block=' + str(block)

        return _make_get_request(method_url, self.headers)


class MonitoringAPIV2(APIV2):
    def __init__(self, api_key):
        super().__init__(api_key)
        self.url_module = self.url + 'monitor/'

    def usage(self):
        """
        Get the used Compute Units of a subscriber
        """
        method_url = self.url_module + 'usage'
        return _make_get_request(method_url, self.headers)
