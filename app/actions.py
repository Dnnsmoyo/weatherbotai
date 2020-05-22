# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message("Hello World!")
#
#         return []


from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import requests

class ActionWeather(Action):
	def name(self):
		return 'action_weather'
		
	def run(self, dispatcher, tracker, domain):
		api_key = 'cc24cc7c42f06680e1bec75abb70ca0c' #your apixu key
		
		loc = tracker.get_slot('location')
		current = requests.get('http://api.openweathermap.org/data/2.5/weather?q={}&appid=cc24cc7c42f06680e1bec75abb70ca0c'.format(loc)).json()
		country = current['sys']['country']
		city = current['name']
		condition = current['weather'][0]['main']
		temperature_c = current['main']['temp']
		humidity = current['main']['humidity']
		wind_mph = current['wind']['speed']

		response = """It is currently {} in {} at the moment. The temperature is {} degrees, the humidity is {} and the wind speed is {} mph.""".format(condition, city, round(temperature_c - 273.15,2), humidity, wind_mph)
			
		dispatcher.utter_message(response)
		return []