from tap_chargebee.streams.base import BaseChargebeeStream


class PaymentSourcesStream(BaseChargebeeStream):
    TABLE = 'payment_sources'
    ENTITY = 'payment_source'
    REPLICATION_METHOD = 'INCREMENTAL'
    REPLICATION_KEY = 'updated_at'
    KEY_PROPERTIES = ['id']
    BOOKMARK_PROPERTIES = ['updated_at']
    SELECTED_BY_DEFAULT = True
    VALID_REPLICATION_KEYS = ['updated_at']
    INCLUSION = 'available'
    API_METHOD = 'GET'
    SCHEMA = 'common/payment_sources'

    def get_url(self):
        return 'https://{}.chargebee.com/api/v2/payment_sources'.format(self.config.get('site'))
