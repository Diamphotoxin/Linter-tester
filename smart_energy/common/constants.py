from datetime import timedelta
from enum import Enum

import pytz


class ApplicationConstants(object):
    OCTOPUS_SUPPORT_EMAIL = 'agile@octopus.energy'
    VOLTAWARE_SUPPORT_EMAIL = 'octopus@voltaware.com'


class OAuth2Constants:
    GRANT_TYPE_CODE = 'authorization_code'
    GRANT_TYPE_CREDENTIALS = 'client_credentials'
    GRANT_TYPE_REFRESH_TOKEN = 'refresh_token'


class DeviceAttributesConstants(object):
    OPTIMIZATION = 'optimization_type'
    DASHBOARD_ATTACHED = 'dashboard_attached'
    DEVICE_CONSUMPTION = 'device_consumption'
    NOT_OPTIMIZATION = None
    OCTOPUS_OPTIMIZATION = 'octopus'
    CARBON_OPTIMIZATION = 'carbon'
    OPTIMIZATION_TYPES = [NOT_OPTIMIZATION, OCTOPUS_OPTIMIZATION, CARBON_OPTIMIZATION]
    ALGORITHMS_WITH_SUBTYPES = [OCTOPUS_OPTIMIZATION, CARBON_OPTIMIZATION]


class DeviceModes(object):
    ON = 'ON'
    OFF = 'OFF'


class AttributesTypesConstants(object):
    STRING_TYPE = "string"
    NUMBER_TYPE = "number"
    BOOLEAN_TYPE = "boolean"
    AVAILABLE_TYPES = [STRING_TYPE, NUMBER_TYPE, BOOLEAN_TYPE]


class DashboardConstants(object):
    HOT_WATER = "hot_water"
    HEATING = "heating"
    SOLAR = "solar"
    HOME_BATTERY = "home_battery"
    EV = "ev_v2g"
    AVAILABLE_SECTION = [None, HOT_WATER, HEATING, SOLAR, HOME_BATTERY, EV]


class EnvironmentVariables(object):
    AWS_REGION = 'AWS_REGION'
    AWS_COGNITO_USER_POOL = 'AWS_COGNITO_USER_POOL'
    AWS_COGNITO_CLIENT_ID = 'AWS_COGNITO_CLIENT_ID'

    PROTOCOL = 'PROTOCOL'
    HOST = 'APPLICATION_HOST'
    SCHEMA = 'APPLICATION_SCHEMA'
    LOGGING_LEVEL = 'APPLICATION_LOGGING_LEVEL'
    BUG_SNAG_API_KEY = 'BUG_SNAG_API_KEY'

    DATABASE_HOST = 'DATABASE_HOST'
    DATABASE_PORT = 'DATABASE_PORT'
    DATABASE_NAME = 'DATABASE_NAME'
    DATABASE_USER = 'DATABASE_USER'
    DATABASE_PASS = 'DATABASE_PASS'

    OAUTH_ENDPOINT_CALLBACK = 'OAUTH_ENDPOINT_CALLBACK'

    NIBE_AUTH_BASE_URL = 'NIBE_AUTH_BASE_URL'
    NIBE_ENDPOINT_AUTH = 'NIBE_ENDPOINT_AUTH'
    NIBE_ENDPOINT_TOKEN = 'NIBE_ENDPOINT_TOKEN'
    NIBE_CLIENT_ID = 'NIBE_CLIENT_ID'
    NIBE_CLIENT_SECRET = 'NIBE_CLIENT_SECRET'
    NIBE_SCOPE = 'NIBE_SCOPE'

    TADO_AUTH_BASE_URL = 'TADO_AUTH_BASE_URL'
    TADO_ENDPOINT_AUTH = 'TADO_ENDPOINT_AUTH'
    TADO_ENDPOINT_TOKEN = 'TADO_ENDPOINT_TOKEN'
    TADO_CLIENT_ID = 'TADO_CLIENT_ID'
    TADO_CLIENT_SECRET = 'TADO_CLIENT_SECRET'
    TADO_SCOPE = 'TADO_SCOPE'

    NETATMO_AUTH_BASE_URL = 'NETATMO_AUTH_BASE_URL'
    NETATMO_ENDPOINT_AUTH = 'NETATMO_ENDPOINT_AUTH'
    NETATMO_ENDPOINT_TOKEN = 'NETATMO_ENDPOINT_TOKEN'
    NETATMO_CLIENT_ID = 'NETATMO_CLIENT_ID'
    NETATMO_CLIENT_SECRET = 'NETATMO_CLIENT_SECRET'
    NETATMO_SCOPE = 'NETATMO_SCOPE'

    CIPHER_SECRET_KEY = 'CIPHER_SECRET_KEY'

    AIREX_BASE_URL = 'AIREX_BASE_URL'
    AIREX_AUTH_BASE_URL = 'AIREX_AUTH_BASE_URL'
    AIREX_ENDPOINT_AUTH = 'AIREX_ENDPOINT_AUTH'
    AIREX_ENDPOINT_TOKEN = 'AIREX_ENDPOINT_TOKEN'
    AIREX_CLIENT_ID = 'AIREX_CLIENT_ID'
    AIREX_CLIENT_SECRET = 'AIREX_CLIENT_SECRET'
    AIREX_SCOPE = 'AIREX_SCOPE'

    POWERLOOP_LOGIN = 'POWERLOOP_LOGIN'
    POWERLOOP_PASSWORD = 'POWERLOOP_PASSWORD'

    SMTP_HOST = 'SMTP_HOST'
    SMTP_PORT = 'SMTP_PORT'
    SMTP_SLL = 'SMTP_SLL'
    SMTP_USERNAME = 'SMTP_USERNAME'
    SMTP_PASSWORD = 'SMTP_PASSWORD'
    SMTP_SENDER = 'SMTP_SENDER'

    SNS_SMS_TOPIC = 'SNS_SMS_TOPIC'

    VOLTAWARE_BASE_AUTH = 'VOLTAWARE_BASE_AUTH'
    VOLTAWARE_ENDPOINT_AUTH = 'VOLTAWARE_ENDPOINT_AUTH'
    VOLTAWARE_ENDPOINT_TOKEN = 'VOLTAWARE_ENDPOINT_TOKEN'
    VOLTAWARE_CLIENT_ID = 'VOLTAWARE_CLIENT_ID'
    VOLTAWARE_CLIENT_SECRET = 'VOLTAWARE_CLIENT_SECRET'
    VOLTAWARE_SCOPE = 'VOLTAWARE_SCOPE'

    PRIME_HYBRID_ENERGY_API_TOKEN = 'PRIME_HYBRID_ENERGY_API_TOKEN'

    CLIMOTE_API_KEY = 'CLIMOTE_API_KEY'
    GIVENERGY_API_KEY = 'GIVENERGY_API_KEY'

    JWT_SECRET_KEY = 'JWT_SECRET_KEY'

    TIMEOUT_TOTAL = 'TIMEOUT_TOTAL'
    TIMEOUT_CONNECT = 'TIMEOUT_CONNECT'

    FAN_CLUB_URL = 'FAN_CLUB_URL'
    IFTTT_URL = 'IFTTT_URL'


class SupportedBrands:
    TADO = 'tado'
    NIBE = 'nibe_uplink'
    NETATMO = 'netatmo'
    GIVENERGY = 'givenergy'
    GIVENERGY_API = 'givenergy_v2'
    LUX_POWER = 'luxpower'
    NCUBE = 'ncube'
    CLIMOTE = 'climote'
    MIXERGY = 'mixergy'
    EOCHARGING = 'eocharging'
    POWERVAULT = 'powervault'
    HILDEBRAND = 'hildebrand_cad'
    PRIME_HYBRID_ENERGY = 'prime_hybrid_energy'
    PRIME_HYBRID_ENERGY_PORTAL = 'prime_hybrid_energy_portal'
    SOLAR_EDGE = 'solar_edge'
    POWERLOOP = 'powerloop'
    WALLBOX = 'wallbox'
    AIREX = 'airex'
    VOLTAWARE = 'voltaware'
    FAN_CLUB = 'fan_club'


class SupportedBrandsTitles:
    TADO = 'Tado'
    NIBE = 'Nibe Uplink'
    NETATMO = 'Netatmo'
    GIVENERGY = 'GivEnergy'
    LUX_POWER = 'LuxPower'
    NCUBE = 'nCube'
    CLIMOTE = 'Climote'
    MIXERGY = 'MixEnergy'
    EOCHARGING = 'EOCharging'
    POWERVAULT = 'Powervault'
    HILDEBRAND = 'Hildebrand CAD'
    PRIME_HYBRID_ENERGY = 'Prime Hybrid Energy'
    SOLAR_EDGE = 'Solar Edge'
    WALLBOX = 'Wallbox'
    POWERLOOP_OPEN_ENERGY = 'PowerLoop Open Energy'
    AIREX = 'Airex'


class DeviceTypes:
    THERMOSTAT = 'thermostat'
    BOILER = 'boiler'
    SMART_MODULE = 'smart_module'
    INVERTER = 'inverter'
    HUE_LAMP = 'hue_lamp'
    NOTIFICATION_SENSOR = 'notification_sensor'
    ROUTING_MULTILEVEL_SWITCH = 'routing_multilevel_switch'
    BINARY_POWER_SWITCH = 'binary_power_switch'
    METER = 'meter'
    SENSOR = 'sensor'
    GATEWAY = 'gateway'
    BATTERY = 'battery'
    HEAT_PUMP = 'heat_pump'
    ELECTRICITY_VEHICLE = 'electricity_vehicle'
    VENTILATION = 'ventilation'
    CAR_CHARGER = 'car_charger'
    HYBRID = "hybrid"
    TURBINE = 'turbine'


class DecodeConstants(object):
    UTF8 = 'utf-8'


class ContentType(object):
    ALL = '*/*'
    APPLICATION_XLS = 'application/vnd.ms-excel'
    APPLICATION_ATOM_XML = 'application/atom+xml'
    APPLICATION_FORM_URLENCODED = 'application/x-www-form-urlencoded'
    APPLICATION_JSON = 'application/json'
    APPLICATION_JSON_UTF8 = 'application/json;charset=UTF-8'
    APPLICATION_OCTET_STREAM = 'application/octet-stream'
    APPLICATION_PDF = 'application/pdf'
    APPLICATION_PROBLEM_JSON = 'application/problem+json'
    APPLICATION_PROBLEM_JSON_UTF8 = 'application/problem+json;charset=UTF-8'
    APPLICATION_PROBLEM_XML = 'application/problem+xml'
    APPLICATION_RSS_XML = 'application/rss+xml'
    APPLICATION_STREAM_JSON = 'application/stream+json'
    APPLICATION_XHTML_XML = 'application/xhtml+xml'
    APPLICATION_XML = 'application/xml'
    IMAGE_GIF = 'image/gif'
    IMAGE_JPEG = 'image/jpeg'
    IMAGE_PNG = 'image/png'
    MULTIPART_FORM_DATA = 'multipart/form-data'
    TEXT_EVENT_STREAM = 'text/event-stream'
    TEXT_HTML = 'text/html'
    TEXT_MARKDOWN = 'text/markdown'
    TEXT_PLAIN = 'text/plain'
    TEXT_XML = 'text/xml'
    TEXT_CSV = 'text/csv'


class HttpHeaders(object):
    ACCEPT = "Accept"
    ACCEPT_CHARSET = "Accept-Charset"
    ACCEPT_ENCODING = "Accept-Encoding"
    ACCEPT_LANGUAGE = "Accept-Language"
    ACCEPT_RANGES = "Accept-Ranges"
    ACCESS_CONTROL_ALLOW_CREDENTIALS = "Access-Control-Allow-Credentials"
    ACCESS_CONTROL_ALLOW_HEADERS = "Access-Control-Allow-Headers"
    ACCESS_CONTROL_ALLOW_METHODS = "Access-Control-Allow-Methods"
    ACCESS_CONTROL_ALLOW_ORIGIN = "Access-Control-Allow-Origin"
    ACCESS_CONTROL_EXPOSE_HEADERS = "Access-Control-Expose-Headers"
    ACCESS_CONTROL_MAX_AGE = "Access-Control-Max-Age"
    ACCESS_CONTROL_REQUEST_HEADERS = "Access-Control-Request-Headers"
    ACCESS_CONTROL_REQUEST_METHOD = "Access-Control-Request-Method"
    AGE = "Age"
    ALLOW = "Allow"
    AUTHORIZATION = "Authorization"
    CACHE_CONTROL = "Cache-Control"
    CONNECTION = "Connection"
    CONTENT_ENCODING = "Content-Encoding"
    CONTENT_DISPOSITION = "Content-Disposition"
    CONTENT_LANGUAGE = "Content-Language"
    CONTENT_LENGTH = "Content-Length"
    CONTENT_LOCATION = "Content-Location"
    CONTENT_RANGE = "Content-Range"
    CONTENT_TYPE = "Content-Type"
    COOKIE = "Cookie"
    DATE = "Date"
    ETAG = "ETag"
    EXPECT = "Expect"
    EXPIRES = "Expires"
    FROM = "From"
    HOST = "Host"
    IF_MATCH = "If-Match"
    IF_MODIFIED_SINCE = "If-Modified-Since"
    IF_NONE_MATCH = "If-None-Match"
    IF_RANGE = "If-Range"
    IF_UNMODIFIED_SINCE = "If-Unmodified-Since"
    LAST_MODIFIED = "Last-Modified"
    LINK = "Link"
    LOCATION = "Location"
    MAX_FORWARDS = "Max-Forwards"
    ORIGIN = "Origin"
    PRAGMA = "Pragma"
    PROXY_AUTHENTICATE = "Proxy-Authenticate"
    PROXY_AUTHORIZATION = "Proxy-Authorization"
    RANGE = "Range"
    REFERER = "Referer"
    RETRY_AFTER = "Retry-After"
    SERVER = "Server"
    SET_COOKIE = "Set-Cookie"
    SET_COOKIE2 = "Set-Cookie2"
    TE = "TE"
    TRAILER = "Trailer"
    TRANSFER_ENCODING = "Transfer-Encoding"
    UPGRADE = "Upgrade"
    USER_AGENT = "User-Agent"
    VARY = "Vary"
    VIA = "Via"
    WARNING = "Warning"
    WWW_AUTHENTICATE = "WWW-Authenticate"


class HttpStatus:
    OK = 200
    CREATED = 201
    FOUND = 302
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404
    TOO_MANY_REQUESTS = 429
    INTERNAL_SERVER_ERROR = 500
    BAD_GATEWAY = 502
    SERVICE_UNAVAILABLE = 503
    GATEWAY_TIMEOUT = 504

    CLIENT_ERRORS = range(400, 500)
    SERVER_ERRORS = range(500, 600)


class SchedulerStatus(object):
    WAITING = 'Waiting'
    EXECUTING = 'Executing'
    CREATED = 'Created'
    PAUSED = 'Paused'
    FAILED = 'Failed'
    REMOVED = 'Removed'
    UPDATED = 'Updated'


class OctopusTariffs:
    AGILE = 'AGILE'
    FIXED = 'FIXED'
    DAY_NIGHT = 'DAY_NIGHT'
    GO = 'GO'
    UNKNOWN = 'UNKNOWN'


class OctopusTariffTypes:
    GAS = 'G'
    ELECTRICITY = 'E'


class OctopusRegistersTypes:
    SINGLE = 1
    DUAL = 2


class OctopusTariffRatesInterval:
    AGILE = timedelta(minutes=30)

    GO_MIN = timedelta(hours=4)
    GO_MAX = timedelta(hours=20)
    GO_INTERVALS = [GO_MIN, GO_MAX]


class TimeInSeconds:
    MINUTE = 60
    FIVE_MINUTE = 300


class TimeZone:
    LONDON = pytz.timezone('Europe/London')


class Octopus:
    ACCOUNT_ID = 'account_id'
    API_KEY = 'api_key'


class LuxPowerSettings(object):
    GRID_BASE = 'GRID_BASE'
    GRID_ADVANCED = 'GRID_ADVANCED'
    CHARGE = 'CHARGE'
    DISCHARGE = 'DISCHARGE'

    START_REGISTER = 'start_register'
    POINT_NUMBER = 'point_number'


class SortDirection(Enum):
    ASC = 'asc'
    DESC = 'desc'


class BaseInverterRegister:
    ENABLE_MID_METER = 7
    ENABLE_WINTER_MODE = 20
    SET_MCU_TYPE = 23
    SET_REGISTER_VALUE = 24
    READ_REGISTER_VALUE = 25
    POWER_EXPORT_TO_GRID_LIMIT = 26
    BAT_DISCHARGE_MODEL = 27
    BAT_SOC_CORRECTION = 29

    CHARGE_2_START_TIME = 31
    CHARGE_2_STOP_TIME = 32

    CT_CORRECTION = 42
    DC_DISCHARGE_2_START_TIME = 44
    DC_DISCHARGE_2_END_TIME = 45
    ENABLE_METER_TYPE = 47
    SET_METER_115_DIRECTION = 48
    SET_METER_418_DIRECTION = 49

    INV_POWER_LIMIT = 50
    BATTERY_TYPE = 54
    BATTERY_CAPACITY = 55
    DC_DISCHARGE_1_START_TIME = 56
    DC_DISCHARGE_1_END_TIME = 57
    DC_DISCHARGE = 59

    UVP_LIMIT = 71
    OVP_LIMIT = 72
    UFP_LIMIT = 73
    OFP_LIMIT = 74

    ARP_PWR = 92
    ARP_PF = 93
    AC_CHARGE_START_TIME = 94
    AC_CHARGE_END_TIME = 95
    AC_CHARGE_ON_OFF = 96
    BATTERY_DISCHARGE_LOWER_LIMIT = 97
    BATTERY_CHARGE_UPPER_LIMIT = 98

    BMS_TYPE = 109
    SET_SHALLOW_CHARGE_DISCHARGE = 110
    SET_DISCHARGE_CUT_OFF_SOC = 114
    SET_WINTER_MODE = 116

    SECOND_PHASE_OF_CHARGE = 117
    SECOND_STAGE_OF_DISCHARGE_CUTOFF_SOC = 118
    FIRST_STAGE_OF_DISCHARGE_CUTOFF_SOC = 120

    RESTART = 163
    ACTIVATE_BATTERY = 175


class EventColors:
    ORANGE_500 = '#ff9800'
    LIGHT_GREEN_500 = '#8bc34a'
    PURPLE_500 = '#9c27b0'
    RED_500 = '#f44336'
    INDIGO_500 = '#3f51b5'
    PINK_500 = '#e91e63'
    CYAN_500 = '#00bcd4'


class PowerLoop:
    MAX_LIMIT = 200000


class Cache:
    MINUTE_TTL = 60
    HOUR_TTL = 3600
    DAY_TTL = 86400


class Carbon:
    FORWARD_48_HOURS = 'fw48h'
    FORWARD_24_HOURS = 'fw24h'
    PAST_24_HOURS = 'pt24h'


class FileFormats:
    CSV = 'csv'
    XLS = 'xls'
    XLSX = 'xlsx'


class LuxPowerRegister:
    CHARGE_LIMIT = 'HOLD_AC_CHARGE_SOC_LIMIT'
    DISCHARGE_LIMIT = 'HOLD_FORCED_DISCHG_SOC_LIMIT'

    ENABLE_AC_CHARGE = 'FUNC_AC_CHARGE'
    ENABLE_FORCED_DISCHARGE = 'FUNC_FORCED_DISCHG_EN'

    CHARGE_START_TIME = 'HOLD_AC_CHARGE_START_TIME'
    CHARGE_END_TIME = 'HOLD_AC_CHARGE_END_TIME'

    DISCHARGE_START_TIME = 'HOLD_FORCED_DISCHARGE_START_TIME'
    DISCHARGE_END_TIME = 'HOLD_FORCED_DISCHARGE_END_TIME'

    CHARGE_START_TIME_1 = 'HOLD_AC_CHARGE_START_TIME_1'
    CHARGE_END_TIME_1 = 'HOLD_AC_CHARGE_END_TIME_1'

    DISCHARGE_START_TIME_1 = 'HOLD_FORCED_DISCHARGE_START_TIME_1'
    DISCHARGE_END_TIME_1 = 'HOLD_FORCED_DISCHARGE_END_TIME_1'

    CHARGE_START_TIME_2 = 'HOLD_AC_CHARGE_START_TIME_2'
    CHARGE_END_TIME_2 = 'HOLD_AC_CHARGE_END_TIME_2'

    DISCHARGE_START_TIME_2 = 'HOLD_FORCED_DISCHARGE_START_TIME_2'
    DISCHARGE_END_TIME_2 = 'HOLD_FORCED_DISCHARGE_END_TIME_2'


class AuthorizationData:
    AUTHORIZATION_HEADER = 'Authorization'
    AUTHORIZATION_METHOD = 'Bearer '
    BEARER_AUTHORIZATION_KEY_LEN = 7
    INVALID_HEADER_MESSAGE = 'Invalid authorization header structure!'
    MISSING_AUTHORIZATION_KEY = 'Missing authorization header!'
    AUTHORIZATION_ERROR_MESSAGE = 'Authorization error'


class ClientTimeout:
    """Default timeout for connection and response in seconds"""

    TOTAL: int = 5 * 60
    CONNECT: int = 30


class OptimizationsType:
    STANDARD = 'standard'
    HALVES = 'halves'

    ALL = [STANDARD, HALVES]


class CognitoAuthFlowConstants(object):
    CUSTOM: str = 'CUSTOM_AUTH'
    USER_SRP: str = 'USER_SRP_AUTH'
    USER_PASSWORD: str = 'USER_PASSWORD_AUTH'
    REFRESH_TOKEN: str = 'REFRESH_TOKEN_AUTH'


class SchedulersIntervals:
    NEVER = 'never'
    DAILY = 'days'
    WEEKLY = 'weeks'
    MONTHLY = 'months'
    REPEATING_INTERVALS = [DAILY, WEEKLY, MONTHLY]


class CurrencyConstants(object):
    ZERO_VALUE: float = 0.0
    PENCE_IN_ONE_POUND: float = 100.0
    TWO_DECIMALS: int = 2


class SchedulerConstants:
    SCHEDULER_DATE = 'date'
    SCHEDULER_CRON = 'cron'
    SCHEDULER_INTERVAL = 'interval'
    SCHEDULER_MAX_INSTANCES = 20

    EVENT_SCHEDULER_HOUR = 18
    EVENT_SCHEDULER_MINUTES = 30

    SCHEDULER_START_HOUR = '18'
    SCHEDULER_START_MINUTES = '30'

    AGILE_RATES_HOUR = '18'
    AGILE_RATES_MINUTES = '00-29/5'

    ZERO_MINUTES = 0
    FULL_DAY_EVENT_HOURS = 23
    FULL_DAY_EVENT_MINUTES = 59


class EventStatuses:
    SUCCESS = 'SUCCESS'
    ERROR = 'ERROR'
    SKIPPED = 'SKIPPED'
    UNKNOWN = 'UNKNOWN'
    STARTED = 'STARTED'
    STOPPED = 'STOPPED'

    ALL = [
        SUCCESS,
        ERROR,
        SKIPPED,
        UNKNOWN,
        STARTED,
        STOPPED
    ]


class EventInitiator:
    USER = 'USER'
    SCHEDULER = 'SCHEDULER'
    UNKNOWN = 'UNKNOWN'


class OctopusRates:
    VALUE_INC_VAT: str = 'value_inc_vat'
    VALUE_EXC_VAT: str = 'value_exc_vat'
    VALID_FROM: str = 'valid_from'
    VALID_TO: str = 'valid_to'


class PossibleInverterCharts:
    BATTERY_SOC = 'batPercent'
    IMPORT_EXPORT = 'pac'
    BATTERY_VOLTAGE = 'batVoltage'
    BATTERY_TEMPERATURE = 'batTemperature'
    PV_GENERATION = 'ppv'
    PV1_VOLTAGE = 'vpv1'
    PV2_VOLTAGE = 'vpv2'
    PV1_CURRENT = 'ipv1'
    PV2_CURRENT = 'ipv2'
    AC_GRID_VOLTAGE = 'vacr'
    AC_OUTPUT_VOLTAGE = 'iacr'
    DEMANDED_POWER = 'loadPower'
    HYBRID_TEMPERATURE = 'temperature'
    FREQUENCY_AC = 'fac'
    PINV = 'meter1ActivePower'
    BMS_VOLTAGE = 'moduleVoltage'


class PrimeHybridCharts(PossibleInverterCharts):
    ALL = [
        PossibleInverterCharts.BATTERY_SOC,
        PossibleInverterCharts.IMPORT_EXPORT,
        PossibleInverterCharts.BATTERY_VOLTAGE,
        PossibleInverterCharts.BATTERY_TEMPERATURE,
        PossibleInverterCharts.PV_GENERATION,
        PossibleInverterCharts.PV1_VOLTAGE,
        PossibleInverterCharts.PV2_VOLTAGE,
        PossibleInverterCharts.PV1_CURRENT,
        PossibleInverterCharts.PV2_CURRENT,
        PossibleInverterCharts.AC_GRID_VOLTAGE,
        PossibleInverterCharts.AC_OUTPUT_VOLTAGE,
        PossibleInverterCharts.DEMANDED_POWER,
        PossibleInverterCharts.HYBRID_TEMPERATURE,
        PossibleInverterCharts.FREQUENCY_AC
    ]


class GivEnergyCharts(PossibleInverterCharts):
    ALL = [
        PossibleInverterCharts.BATTERY_SOC,
        PossibleInverterCharts.IMPORT_EXPORT,
        PossibleInverterCharts.BATTERY_VOLTAGE,
        PossibleInverterCharts.BATTERY_TEMPERATURE,
        PossibleInverterCharts.PV_GENERATION,
        PossibleInverterCharts.PV1_VOLTAGE,
        PossibleInverterCharts.PV2_VOLTAGE,
        PossibleInverterCharts.PV1_CURRENT,
        PossibleInverterCharts.PV2_CURRENT,
        PossibleInverterCharts.AC_GRID_VOLTAGE,
        PossibleInverterCharts.AC_OUTPUT_VOLTAGE,
        PossibleInverterCharts.DEMANDED_POWER,
        PossibleInverterCharts.HYBRID_TEMPERATURE,
        PossibleInverterCharts.FREQUENCY_AC,
        PossibleInverterCharts.PINV,
        PossibleInverterCharts.BMS_VOLTAGE
    ]


class PossibleNibeSmartHomeModes:
    DEFAULT_OPERATION = "DEFAULT_OPERATION"
    AWAY_FROM_HOME = "AWAY_FROM_HOME"
    VACATION = "VACATION"


class NibeSmartHomeModes(PossibleNibeSmartHomeModes):
    ALL = [
        PossibleNibeSmartHomeModes.DEFAULT_OPERATION,
        PossibleNibeSmartHomeModes.AWAY_FROM_HOME,
        PossibleNibeSmartHomeModes.VACATION
    ]


class LuxPowerCharts:
    PPV1 = 'ppv1'
    SOC = 'soc'
    VBAT = 'vBat'
    PCHARGE = 'pCharge'
    PDISCHARGE = 'pDisCharge'
    VACR = 'vacr'
    QAC = 'qac'
    PTOGRID = 'pToGrid'
    VEPSR = 'vepsr'
    FEPS = 'feps'
    PEPS = 'peps'
    SEPS = 'seps'

    ALL = [
        PPV1,
        SOC,
        VBAT,
        PCHARGE,
        PDISCHARGE,
        VACR,
        QAC,
        PTOGRID,
        VEPSR,
        FEPS,
        PEPS,
        SEPS
    ]


class ConsumptionConstants:
    ZERO_VALUE = 0.0
    DAYS_OF_WEEK = 7
    WATTS_IN_KILOWATT = 1000.0
    SECONDS_IN_AN_HOUR = 3600


class DashboardDeviceModes:
    SOLAR = 'solar'

    EXPORT = 'export'
    IMPORT = 'import'

    CHARGING = 'charging'
    DISCHARGING = 'discharging'

    HEATING = 'heating'
    HOT_WATER = 'hot_water'

    ALL = [SOLAR, EXPORT, IMPORT, CHARGING, DISCHARGING, HEATING, HOT_WATER]


class ContextVariables:
    USER = 'authentication'
    REQUEST_ID = 'request_id'
    SESSION = 'session'
    APP = 'application'
    ALL = [USER, REQUEST_ID, SESSION, APP]


class NibeErrorCodes:
    NO_CHANGE = -2
    NO_ERROR = -1
    UNKNOWN_ERROR = 0
    FORMAT_ERROR = 1
    UNKNOWN_SYSTEM = 2
    ALREADY_CONNECTED = 3
    NOT_ALLOWED_AS_SERVICE_USER = 4
    NEEDS_RECONNECT = 5
    NOT_ALLOWED_TO_RECONNECT = 6
    NOT_FOUND = 7
    NOT_POSSIBLE = 8
    UNKNOWN_SYSTEM_UNIT = 9
    UNKNOWN_HEAT_SYSTEM = 10
    NOT_ALLOWED_ON_SYSTEM = 11
    NO_PREMIUM_ON_SYSTEM = 12
    TOO_MANY = 13
    INVALID = 14
    OUT_OF_RANGE = 15
    NOT_SETABLE = 16
    NO_METADATA = 17
    UNKNOWN_PARAMETER = 18
    OAUTH_AUTHORIZATION_FAILED = 19
    OAUTH_INVALID_SCOPE = 20
    OAUTH_INVALID_ROLES = 21
    OAUTH_NOT_ALLOWED_CLIENT = 22
    UNKNOWN_CLIENT = 23
    INVALID_CLIENT_GROUP = 24
    NOT_ALLOWED_AS_DEMO_USER = 25
    SYSTEM_OFFLINE = 26
    INVALID_VOUCHER_TYPE = 27
    RATE_LIMIT = 28
    NOT_AVAILABLE = 29
    INVALID_VOUCHER_SERIAL_NUMBER = 30
    CANT_BE_REGISTERED = 31
    REGISTRATION_UNAVAILABLE = 32


class DateRange:
    MAX_CALENDAR_DAYS = 31


class GivEnergyRegisterNames:
    DISCHARGE = 'dischargeFlag'
    DISCHARGE_DOWN_TO = 'dischargeDownTo'
    DISCHARGE_START = 'dischargeStart'
    DISCHARGE_END = 'dischargeEnd'
    CHARGE = 'chargeFlag'
    CHARGE_UP_TO = 'chargeUpTo'
    CHARGE_START = 'chargeStart'
    CHARGE_END = 'chargeEnd'
    CONSUMPTION = 'selfConsumption'
    SHALLOW = 'shallowValue'

    ALL = [
        DISCHARGE,
        DISCHARGE_DOWN_TO,
        DISCHARGE_START,
        DISCHARGE_END,
        CHARGE,
        CHARGE_UP_TO,
        CHARGE_START,
        CHARGE_END,
        CONSUMPTION,
        SHALLOW
    ]


class EventErrorMessage:
    DEFAULT = ''
    AUTHORIZATION_ERROR = 'Failed to authorize to a remote server'
    TOO_MANY_REQUESTS = 'Too many requests to a remote server in a given amount of time'
    UNAVAILABLE_ERROR = 'Remote service is temporary unavailable'
    CLIENT_ERROR = 'Error occurred while communicating with a remote server'
    SERVER_ERROR = 'Remote server responded with an error'
    GATEWAY_TIMEOUT = 'Could not get remote server response in time.'


class BugSnagConstants:
    IGNORE_STATUS_CODES = [
        HttpStatus.BAD_REQUEST,
        HttpStatus.UNAUTHORIZED,
    ]
