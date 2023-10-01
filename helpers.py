from flask import render_template


def inputs_validation(email, password, html,  rePassword=None):
     # checking for proper inputs
      if email == "" or "@" not in email:
          return render_template(html, emailErr = "Email is required and it needs to be an email"), 400
      if password == "" or len(password) < 4 or len(password) > 15:
          return render_template(html, passErr = True, email=email), 400
      if rePassword != None and rePassword != password:
          return render_template(html, rePassErr = "Password do not match.", email=email), 400
      return None

def condition_emoji(condition):
        if condition == "clear":
            return "☀️"
        elif condition == "partly-cloudy":
            return "🌥️"
        elif condition == "cloudy-with-sunny-intervals":
            return "🌥️"
        elif condition == "cloudy":
            return "☁️"
        elif condition == "thunder":
            return "🌩️"
        elif condition == "isolated-thunderstorms":
            return "🌩️"
        elif condition == "thunderstorms":
            return "🌩️"
        elif condition == "heavy-rain-with-thunderstorms":
            return "⛈️"
        elif condition == "light-rain":
            return "🌦️"
        elif condition == "rain":
            return "🌧️"
        elif condition == "heavy-rain":
            return "🌧️"
        elif condition == "light-sleet":
            return "☔"
        elif condition == "freezing-rain":
            return "☔"
        elif condition == "hail":
            return "☔"
        elif condition == "light-snow":
            return "🌨️"
        elif condition == "snow":
            return "🌨️"
        elif condition == "heavy-snow":
            return "🌨️"
        elif condition == "fog":
            return "🌫️"
        else:
            return "⁉️"

def recommendation(airTemp, condition, temp_ranges):
    if condition == "heavy-rain-with-thunderstorms" or condition == "rain" or condition == "heavy-rain":
        return "blue"

    if airTemp <= temp_ranges["low"]:
        return "red"
    elif airTemp <= temp_ranges["mid"]:
        return "yellow"
    elif airTemp <= temp_ranges["high"]:
        return "green"
    else:
        return "red"

def more_info(temp, temp_ranges):
    if temp <= temp_ranges["low"]:
        return "Layering is crucial to retain warmth. Consider wearing a thermal base layer, insulating mid-layer, and a windproof outer layer. Don't forget gloves, a hat, and thermal socks to protect extremities."
    elif temp <= temp_ranges["mid"]:
        return "Layering may be necessary. Opt for a light jacket or vest that can be easily added or removed as needed. Long-sleeved jerseys or arm warmers can provide flexibility in regulating body temperature."
    elif temp <= temp_ranges["high"]:
        return "Make sure to stay hydrated and use sunscreen to protect your skin from sun exposure. Wear lightweight and breathable clothing to stay cool. Consider sunglasses and a cycling cap to shield your eyes and face."
    else:
        return "Opt for breathable and moisture-wicking fabrics to stay cool. Wear shorts and short-sleeved jerseys to maximize airflow. Carry extra water and electrolytes, especially on longer rides. Plan routes with shaded areas or consider riding during cooler parts of the day."