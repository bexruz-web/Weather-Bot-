from get_weather import get_weather_data, get_all_regions, get_three_weather_data

from buttons import region_back, region_inline_buttons, three_back

def inline_handler(update, context):
    query = update.callback_query

    if "https" in query.data:
        # Set
        context.user_data['region_url'] = query.data
        weather_data = get_weather_data(region_url=query.data)

        # Set region
        context.user_data['region_name'] = weather_data['region_name']

        weather_string = f"<b>{weather_data['region_name']}</b>\n\n"

        weather_string += (f"📅 {weather_data['current_day']}\n"
                           f"🌅 <b>Kunduzi:</b> {weather_data['high_temp']}, 🌃 <b>Kechasi:</b> {weather_data['low_temp']}\n"
                           f"🏞 <b>Havo Holati:</b> {weather_data['current_forecast_desc']}\n\n"
                           f"📌 <b>Qo'shimcha Malumotlar:</b>\n"
                           f"🌇 <b>Quyosh chiqishi:</b> {weather_data['sunrise']}\n"
                           f"🏙 <b>Quyosh botishi:</b> {weather_data['sunset']}\n"
                           f"🌤 <b>Tong:</b> {weather_data['morning']}\n"
                           f"☀️ <b>Kun:</b> {weather_data['during_day']}\n"
                           f"☁️ <b>Oqshom:</b> {weather_data['evening']}\n"
                           )
        query.edit_message_text(text=weather_string, reply_markup=region_back(), parse_mode='HTML')
    elif query.data == "close":
        msg = query.edit_message_text(text="⏳", reply_markup=None)
        context.bot.delete_message(chat_id=query.message.chat_id, message_id=msg.message_id)

    elif query.data == "region_back":
        query.edit_message_text(text="📍 <b>Marhamat kerakli viloyatni tanlang:</b>", parse_mode='HTML')
        query.edit_message_reply_markup(reply_markup=region_inline_buttons(get_all_regions()))
    elif query.data == "three_back":
        weather_data = get_weather_data(region_url=context.user_data['region_url'])

        # Set region
        context.user_data['region_name'] = weather_data['region_name']

        weather_string = f"<b>{weather_data['region_name']}</b>\n\n"

        weather_string += (f"📅 {weather_data['current_day']}\n"
                           f"🌅 <b>Kunduzi:</b> {weather_data['high_temp']}, 🌃 <b>Kechasi:</b> {weather_data['low_temp']}\n"
                           f"🏞 <b>Havo Holati:</b> {weather_data['current_forecast_desc']}\n\n"
                           f"📌 <b>Qo'shimcha Malumotlar:</b>\n"
                           f"🌇 <b>Quyosh chiqishi:</b> {weather_data['sunrise']}\n"
                           f"🏙 <b>Quyosh botishi:</b> {weather_data['sunset']}\n"
                           f"🌤 <b>Tong:</b> {weather_data['morning']}\n"
                           f"☀️ <b>Kun:</b> {weather_data['during_day']}\n"
                           f"☁️ <b>Oqshom:</b> {weather_data['evening']}\n"
                           )
        query.edit_message_text(text=weather_string, parse_mode='HTML')
        query.edit_message_reply_markup(reply_markup=region_back())

    elif query.data == "three_weather":
        if context.user_data.get('region_url'):
            three_weather = get_three_weather_data(context.user_data.get('region_url'))

            three_string = f"<b>{context.user_data['region_name']}</b> dagi 3 kunlik ob havo malumotlari:\n\n"

            for day in three_weather[:3]:
                description = day['description'].capitalize()

                three_string += (f"{day['week_day']}, {day['month_day']}\n"
                                f"<b>Yuqori daraja:</b> {day['forecast_day']}, <b>Past daraja:</b> {day['forecast_night']}\n"
                                f"{description}\n"
                                f"<b>Yog'ingarchilik ehtimoli:</b> {day['precipitation']}\n\n")

            query.edit_message_text(text=three_string, parse_mode='HTML')
            query.edit_message_reply_markup(reply_markup=three_back())