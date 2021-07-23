from typing import List

from smart_energy.common.security.providers.base_provider import BaseAuthenticationProvider
from smart_energy.common.security.providers.jwt_cognito_provider import CognitoAuthenticationProvider
from smart_energy.common.security.providers.jwt_secret_provider import JWTSecretAuthenticationProvider
from smart_energy.properties.cognito import CognitoConfig
from smart_energy.properties.jwt import JWTProperties


# Todo add auth builder/manager
def jwt_secret_provider() -> JWTSecretAuthenticationProvider:
    secret_provider = JWTSecretAuthenticationProvider(
        secret_key=JWTProperties.secret_key
    )

    return secret_provider


def get_cognito_provider() -> CognitoAuthenticationProvider:
    cognito_provider = CognitoAuthenticationProvider(
        key_url=CognitoConfig.keys_url
    )

    return cognito_provider


def get_available_providers() -> List[BaseAuthenticationProvider]:
    providers = [
        get_cognito_provider(),
        jwt_secret_provider(),
    ]

    return providers
