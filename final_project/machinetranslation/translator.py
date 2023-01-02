import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

def english_to_french(english_text):
    """ Translate English to French """

    french_text = ""

    if english_text is None:
        return french_text

    authenticator = IAMAuthenticator(apikey)
    translator = LanguageTranslatorV3(
        version=version,
        authenticator=authenticator
    )

    try:
        translator.set_service_url(url)
        translation = translator.translate(
            text=[english_text],
            model_id='en-fr').get_result()
        french_text: str = translation['translations'][0]['translation']
    except ApiException as ex:
        print("Method failed with status code " + str(ex.code) + ": " + ex.message)

    return french_text


def french_to_english(french_text):
    """ Translate French to English """

    english_text = ""

    if french_text is None:
        return english_text

    authenticator = IAMAuthenticator(apikey)
    translator = LanguageTranslatorV3(
        version=version,
        authenticator=authenticator
    )

    try:
        translator.set_service_url(url)
        translation = translator.translate(
            text=[french_text],
            model_id='fr-en').get_result()
        english_text: str = translation['translations'][0]['translation']
    except ApiException as ex:
        print("Method failed with status code " + str(ex.code) + ": " + ex.message)

    return english_text