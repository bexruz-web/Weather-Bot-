from telegram import InlineKeyboardMarkup, InlineKeyboardButton

def region_inline_buttons(regions):
    buttons = []
    temp_row = []

    for region in regions:
        for region_name, region_link in region.items():
            button = InlineKeyboardButton(text=region_name, callback_data=region_link)
            temp_row.append(button)

            if len(temp_row) == 2:
                buttons.append(temp_row)
                temp_row = []
    if temp_row:
        buttons.append(temp_row)

    button = InlineKeyboardButton(text="🔚 Yopish", callback_data="close")
    buttons.append([button])

    return InlineKeyboardMarkup(buttons)

def region_back():
    three_button = [InlineKeyboardButton(text="📆 3 Kunlik ob-havo malumoti", callback_data="three_weather")]
    back_button = [InlineKeyboardButton(text="🔙 Orqaga", callback_data="region_back")]
    return InlineKeyboardMarkup([three_button, back_button])

def three_back():
        back_button = [InlineKeyboardButton(text="🔙 Orqaga", callback_data="three_back")]
        return InlineKeyboardMarkup([back_button])

# print(region_inline_buttons("Samarqand"))



